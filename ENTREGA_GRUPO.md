# Entrega · CarValue AI

**Grupo:** Pablo Díaz, Eduardo Caicedo, Lucas Bravo.

**Repositorio GitHub (privado, con acceso al profesor):** https://github.com/carmelojose309/CarValue-bigdata

| Integrante | Parte implementada | Rama | 2 commits propios | URL del PR | ¿Quién revisó? |
|---|---|---|---|---|---|
| Eduardo Caicedo | Apartado A | Feature/infra-datos | Sí | https://github.com/carmelojose309/CarValue-bigdata/pull/2 | Pablo Díaz |
| Pablo Díaz | Apartado B | Feature/Api-ml | Sí | https://github.com/carmelojose309/CarValue-bigdata/pull/4 | Lucas Bravo |
| Lucas Bravo | Apartado C | Feature/Vision-web | Sí | https://github.com/carmelojose309/CarValue-bigdata/pull/5 | Eduardo Caicedo |

## Pruebas de funcionamiento

- [x] Docker Compose: 3 servicios activos.
- [ ] `SELECT COUNT(*) FROM anuncios` devuelve 50000.
- [x] `GET /health` OK.
- [x] Formulario POST sin JavaScript; fotografía recibida en Flask.
- [x] Modo `MOCK` integra modelo ML + SQLAlchemy y guarda tasación.
- [x] `/historial` muestra tasación.
- [ ] Modo real Cohere (`VISION_MOCK=0`): probado / no probado por falta de clave o límite de uso (explicar).
- [x] `docker compose exec app pytest -q`: 6 tests superados.
- [ ] `.env` no está versionado.
- [x] Prompt propio escrito en `app/vision.py` (sin usar uno prefabricado).
- [x] Formulario HTML y página de resultado programados por el equipo.

## Reflexión breve (4 preguntas)

**1. HTTP frente a SQL:** ...
HTTP comunica el navegador del usuario con la aplicación web Flask. SQL comunica el backend (Flask/Jupyter) con la base de datos PostgreSQL.

**2. Host `db` frente a `localhost`:** ...
En la red interna de Docker, db es el nombre del contenedor PostgreSQL; si Flask usara localhost, se buscaría a sí mismo y fallaría. Usamos localhost:5000 en el navegador porque Docker expone el puerto a nuestra máquina física.

**3. Valor del PR respecto a commits directos en `main`:** ...
Permite desarrollar en paralelo sin sobrescribir el trabajo ajeno y hace obligatoria la revisión cruzada antes de integrar el código.

**4. Qué hacemos si Cohere devuelve `unknown`:** ...
Se interrumpe el proceso y se muestra un error. Nunca se debe inventar una categoría, realizar la predicción, ni guardar la tasación.

## Incidencias que no pudimos resolver (si las hay)



## Decisiones de implementación

**Criterio del prompt (cómo definimos las categorías y el caso `unknown`):** ...
Establecimos reglas estrictas para forzar a la IA a elegir solo entre las cuatro etiquetas permitidas, prohibiendo deducir fallos mecánicos. Si la imagen no es nítida, se fuerza a devolver unknown. Exigimos una salida en JSON plano para asegurar un parseo correcto.

**Decisión del HTML (atributos de formulario y envío de foto):** ...
Se utilizó el método POST y el atributo enctype="multipart/form-data" para permitir la subida del archivo y que Flask lo lea en request.files. Sustituimos JavaScript empleando atributos nativos de HTML5 (min, max, required) para validar las entradas.
