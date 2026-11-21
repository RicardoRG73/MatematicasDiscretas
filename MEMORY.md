# MEMORY.md

Registro persistente del estado, decisiones y convenciones del repositorio **Matemáticas Discretas** (`LISSI0211`).

## Datos de la Asignatura

- **Nombre:** Matemáticas Discretas | **Clave:** `LISSI0211` | **Ciclo:** Segundo Semestre
- **Horas totales:** 96 h (64 h aula + 32 h independientes) | **Unidades:** 6

## Estado Actual del Repositorio

- `README.md`: Temario oficial completo, actividades, criterios de evaluación y bibliografía.
- `GEMINI.md` / `MEMORY.md`: Arnés del repositorio (`MEMORY.md` máx. 50 líneas).
- `LICENSE`: Licencia del repositorio.
- `figuras/`: Directorio con 31 scripts generadores en Python (`.py`), sus 31 figuras (`.png`) y `figuras/logos/`.
- `notas/`: Apuntes completos de las **6 unidades del temario** (`1-0` a `6-0` y todos sus subtemas `1-1` a `6-6`) con desarrollo teórico, figuras ilustrativas, ejemplos de práctica resueltos paso a paso y ejercicios de tarea con solución oculta en comentarios HTML (`<!-- ... -->`), más sus versiones compiladas en `notas/pdf/`.
- `generar_pdfs.py`: Script en Python (Pandoc + filtro Lua + XeLaTeX) para regenerar los PDF de `notas/` manteniendo el tema de color del curso.

## Decisiones y Cambios Clave

- **2026-11-15 — Temario y evaluación:** Se transcribió el temario a `README.md`, se eliminó `Temario scan.pdf` y se fijó evaluación: 10% Asistencia, 50% Prueba de desempeño, 40% Portafolio de evidencias.
- **2026-11-15 — Arnés y estructura:** Se crearon `GEMINI.md`, `MEMORY.md`, `figuras/` y `notas/` con los archivos `X-0-unidad.md` y `X-Y-subtema.md` para las 6 unidades.
- **2026-11-15 — Exclusión de referencias externas:** No versionar ni listar carpetas de referencias externas como contenido del repositorio.
- **2026-11-16 — Desarrollo de las Unidades 1 a 3:** Apuntes completos de Sistemas Numéricos (`1-1` a `1-5`), Conjuntos (`2-1` a `2-4`) y Lógica Matemática (`3-1` a `3-2`), con 17 scripts/figuras en `figuras/`.
- **2026-11-16 — Desarrollo de la Unidad 4 (`4-1` a `4-3`):** Apuntes completos de Álgebra Booleana (`notas/4-0-algebra-booleana.md` y `notas/4-1` a `4-3`) con 5 scripts/figuras en `figuras/`.
- **2026-11-16 — Desarrollo de la Unidad 5 (`5-1` a `5-5`):** Apuntes completos de Relaciones y Funciones (`notas/5-0-relaciones.md` y `notas/5-1` a `5-5`) con ejemplos resueltos, tareas comentadas y 4 scripts/figuras en `figuras/`.
- **2026-11-16 — Desarrollo de la Unidad 6 (`6-1` a `6-6`):** Apuntes completos de Teoría de Grafos, Árboles y Redes (`notas/6-0-teoria-de-grafos.md` y `notas/6-1` a `6-6`) con ejemplos resueltos, tareas comentadas y 5 scripts/figuras en `figuras/`.
- **2026-11-16 — Autoría de commits y PRs:** Se estableció en `GEMINI.md` que los commits y *pull requests* deben llevar exclusivamente autoría humana, excluyendo cualquier autoría o coautoría de IA.
- **2026-11-20 — Script generador de PDFs (`generar_pdfs.py`):** Se creó el script autocontenido en Python usando Pandoc + filtro Lua + XeLaTeX con la paleta original (`#0F172A`, `#1E293B`, `#1E3A8A`, `#2563EB`, `#BE123C`, `#EFF6FF`, `#F1F5F9`, `#F8FAFC`, `#CBD5E1`) e incremento automático por `mtime`.

## Pendientes / Próximos Pasos

- Elaborar instrumentos de evaluación (pruebas de desempeño) y rúbricas para el portafolio de evidencias de las 6 unidades.
