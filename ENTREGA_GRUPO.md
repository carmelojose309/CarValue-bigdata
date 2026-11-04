# Entrega · CarValue AI

**Grupo:** Pablo Díaz, Eduardo Caicedo, Lucas Bravo.

**Repositorio GitHub (privado, con acceso al profesor):** https://github.com/carmelojose309/CarValue-bigdata

| Integrante | Parte implementada | Rama | 2 commits propios | URL del PR | ¿Quién revisó? |
|---|---|---|---|---|---|
| Eduardo Caicedo | Apartado A | Feature/infra-datos | Sí | https://github.com/carmelojose309/CarValue-bigdata/pull/2 | Pablo Díaz |
| Pablo Díaz | Apartado B | Feature/Api-ml | Sí | https://github.com/carmelojose309/CarValue-bigdata/pull/4 | Lucas Bravo |
| Lucas Bravo | Apartado C | Feature/Vision-web | Sí | https://github.com/carmelojose309/CarValue-bigdata/pull/5 | Eduardo Caicedo |

## Pruebas de funcionamiento

- [ ] Docker Compose: 3 servicios activos.
- [ ] `SELECT COUNT(*) FROM anuncios` devuelve 50000.
- [ ] `GET /health` OK.
- [ ] Formulario POST sin JavaScript; fotografía recibida en Flask.
- [ ] Modo `MOCK` integra modelo ML + SQLAlchemy y guarda tasación.
- [ ] `/historial` muestra tasación.
- [ ] Modo real Cohere (`VISION_MOCK=0`): probado / no probado por falta de clave o límite de uso (explicar).
- [ ] `docker compose exec app pytest -q`: ___ tests superados.
- [ ] `.env` no está versionado.
- [ ] Prompt propio escrito en `app/vision.py` (sin usar uno prefabricado).
- [ ] Formulario HTML y página de resultado programados por el equipo.

## Reflexión breve (4 preguntas)

**1. HTTP frente a SQL:** ...

**2. Host `db` frente a `localhost`:** ...

**3. Valor del PR respecto a commits directos en `main`:** ...

**4. Qué hacemos si Cohere devuelve `unknown`:** ...

## Incidencias que no pudimos resolver (si las hay)



## Decisiones de implementación

**Criterio del prompt (cómo definimos las categorías y el caso `unknown`):** ...

**Decisión del HTML (atributos de formulario y envío de foto):** ...
