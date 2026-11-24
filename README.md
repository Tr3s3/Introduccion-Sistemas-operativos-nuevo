# Introducción a los Sistemas Operativos — Bóveda Obsidian

Repositorio/bóveda de estudio para la materia **Introducción a los Sistemas Operativos** (Ingeniería/UCASAL). Contiene teoría organizada por unidades, material de finales, ejercicios, resoluciones y recursos gráficos.

## Estructura del repositorio

```text
.
├── Introducción a los Sistemas Operativos/
│   ├── 00 Inicio.md                  # Portada de la bóveda
│   ├── FINALES/                      # LO PRINCIPAL PARA ESTUDIAR EL FINAL
│   │   ├── Índice del final.md
│   │   ├── 00-05 ...                 # Plan, temas, preguntas, cronograma, mapa
│   │   ├── 06-08 ...                 # Modelos, ejercicios resueltos, paso a paso
│   │   ├── 09 Ejercicios de finales (solo enunciados).md
│   │   ├── 10 Ejercicios de finales (resoluciones).md
│   │   └── Gráficos/                 # Diagramas y figuras de apoyo
│   └── Complementario/               # Material de apoyo (no necesario para ir directo al final)
│       ├── MATERIA-COMPLETA/         # Teoría completa por Unidad → Tema → Subtema
│       └── OCR/                      # Textos OCR de exámenes escaneados/fotos
└── scripts/
    ├── extract_scanned_content.py    # Extracción de texto/OCR para PDFs e imágenes
    └── README.md
```

## Cómo usar

1. Abrí la carpeta `Introducción a los Sistemas Operativos/` como bóveda en **Obsidian**.
2. Empezá por `00 Inicio.md`.
3. Para preparar final: `FINALES/Índice del final.md`.
4. Para practicar: `FINALES/09 Ejercicios de finales (solo enunciados).md` y luego `FINALES/10 Ejercicios de finales (resoluciones).md`.
5. Para teoría completa: `Complementario/MATERIA-COMPLETA/00 Índice de la materia.md`.

## Convenciones

- **Wikilinks Obsidian**: `[[Nombre de nota]]`.
- **FINALES**: materiales orientados a examen; los ejercicios incluyen contexto, teoría mínima, pasos, caso resuelto y trampas cuando corresponde.
- **MATERIA-COMPLETA**: organizada por **Unidad → Tema → Subtema**. Cada subtema busca incluir definición, desarrollo, ejemplo, trampas y gráficos cuando aportan.
- **OCR**: los textos en `Complementario/OCR/` fueron extraídos automáticamente y pueden contener errores; conviene contrastar con el original ante dudas.

## Scripts

Ver [`scripts/README.md`](scripts/README.md) para el extractor OCR de PDFs/imágenes.
