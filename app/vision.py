"""Cohere Vision: una foto -> estado exterior + justificación breve."""
import base64
import json
import os
import re
import cohere
from .config import ESTADOS

MODELO_VISION = "command-a-vision-07-2025"

PROMPT = """Actúa como un tasador de vehículos especializado únicamente en el aspecto exterior. 
Analiza la fotografía proporcionada y determina el estado exterior del vehículo.

REGLAS ESTRICTAS:
1. Evalúa SOLO el aspecto exterior visible. No deduzcas el estado del motor, historial de accidentes, kilometraje real, ni funcionamiento mecánico.
2. Debes clasificar el estado utilizando ÚNICAMENTE uno de estos cuatro valores exactos:
   - "like new": Como nuevo, sin defectos apreciables.
   - "excellent": Excelente, con desgaste mínimo.
   - "good": Bueno, con marcas pequeñas de uso normal.
   - "fair": Aceptable, con daños o desgaste clearly visibles.
3. Si la imagen no muestra claramente un coche o faltan evidencias visuales para evaluarlo, el estado debe ser "unknown".
4. Devuelve el resultado ESTRICTAMENTE en formato JSON plano, sin bloques de código Markdown ni texto introductorio.

El JSON debe tener exactamente esta estructura:
{
  "condition": "<una de las 4 etiquetas permitidas o unknown>",
  "reason": "<breve justificación en español basada solo en los detalles visuales>"
}"""

class VisionError(Exception):
    """Error de proveedor o de respuesta no interpretable."""

def parsear_respuesta(texto: str) -> tuple[str, str]:
    """Helper ya implementado: valida el JSON que responde la IA."""
    limpio = re.sub(r"^```(?:json)?\s*|\s*```$", "", texto.strip(), flags=re.I)
    if not limpio.startswith("{"):
        a, b = limpio.find("{"), limpio.rfind("}")
        if a >= 0 and b > a:
            limpio = limpio[a:b+1]
    try:
        obj = json.loads(limpio)
    except (ValueError, TypeError) as exc:
        raise VisionError("Cohere no devolvió un JSON interpretable.") from exc
    estado = str(obj.get("condition", "")).strip().lower()
    razon = str(obj.get("reason", "")).strip()[:350]
    if estado not in (*ESTADOS, "unknown"):
        raise VisionError(f"Cohere devolvió una categoría inesperada: {estado!r}")
    return estado, razon or "Sin justificación visible."

def clasificar_estado(contenido: bytes, mimetype: str) -> tuple[str, str, str]:
    """Devuelve (condition, reason, fuente)."""
    if os.getenv("VISION_MOCK", "0") == "1":
        return "good", "Modo demostración: estado fijo, sin analizar la fotografía.", "MOCK"
    
    token = os.getenv("COHERE_API_KEY", "").strip()
    if not token:
        raise VisionError("Falta COHERE_API_KEY en el archivo .env")
    
    if not PROMPT.strip():
        raise VisionError("Falta redactar el prompt visual: tarea C1-A.")
        
    try:
        foto_b64 = base64.b64encode(contenido).decode('utf-8')
        image_url = f"data:{mimetype};base64,{foto_b64}"
        
        cliente = cohere.ClientV2(api_key=token)
        response = cliente.chat(
            model=MODELO_VISION,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": PROMPT},
                        {"type": "image_url", "image_url": {"url": image_url}}
                    ]
                }
            ]
        )
        
        texto = response.message.content[0].text
        estado, razon = parsear_respuesta(texto)
        return estado, razon, "COHERE"
        
    except Exception as e:
        raise VisionError(f"Error al comunicar con Cohere o procesar la imagen: {str(e)}")