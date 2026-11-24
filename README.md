# Introducción a los Sistemas Operativos — Bóveda Obsidian

Repositorio/bóveda de estudio para la materia **Introducción a los Sistemas Operativos** (Ingeniería/UCASAL). Contiene teoría organizada por unidades, material de finales, ejercicios, resoluciones y recursos gráficos.

## Estructura del repositorio

```text
.
├── Introducción a los Sistemas Operativos/
│   ├── 00 Inicio.md                  # Portada de la bóveda
│   ├── MATERIA-COMPLETA/             # Teoría completa (guía de estudio)
│   │   ├── 00 Índice de la materia.md
│   │   ├── Materia completa (las 4 unidades en un archivo).md
│   │   ├── Unidad 1 — Introducción al sistema operativo/
│   │   ├── Unidad 2 — Procesos y planificación/
│   │   ├── Unidad 3 — Administración de memoria (asignación contigua)/
│   │   └── Unidad 4 — Memoria virtual/
│   └── FINALES/                      # Preparación de final
│       ├── Índice del final.md
│       ├── 00-05 ...                 # Plan, temas, preguntas, ejercicios, mapa
│       ├── 06-08 ...                 # Modelos, ejercicios resueltos, paso a paso
│       ├── 09 Ejercicios de finales (solo enunciados).md
│       ├── 10 Ejercicios de finales (resoluciones).md
│       ├── Gráficos/                 # Diagramas, figuras y capturas de diapositivas
│       └── OCR/                      # Textos extraídos por OCR de exámenes escaneados
└── scripts/
    ├── extract_scanned_content.py    # Extracción de texto/OCR para PDFs e imágenes
    └── README.md
```

## Cómo usar

1. Abrí la carpeta `Introducción a los Sistemas Operativos/` como bóveda en **Obsidian**.
2. Empezá por `00 Inicio.md`.
3. Para teoría completa: `MATERIA-COMPLETA/00 Índice de la materia.md`.
4. Para preparar final: `FINALES/Índice del final.md`.
5. Para practicar: `FINALES/09 Ejercicios de finales (solo enunciados).md` y luego `FINALES/10 Ejercicios de finales (resoluciones).md`.

## Convenciones

- **Wikilinks Obsidian**: `[[Nombre de nota]]`.
- **MATERIA-COMPLETA**: organizada por **Unidad → Tema → Subtema**. Cada subtema busca incluir definición, desarrollo, ejemplo, trampas y gráficos cuando aportan.
- **FINALES**: materiales orientados a examen; los ejercicios incluyen contexto, teoría mínima, pasos, caso resuelto y trampas cuando corresponde.
- **OCR**: los textos en `FINALES/OCR/` fueron extraídos automáticamente y pueden contener errores; conviene contrastar con el original ante dudas.

## Scripts

Ver [`scripts/README.md`](scripts/README.md) para el extractor OCR de PDFs/imágenes.