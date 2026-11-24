# Introducción a los Sistemas Operativos — Bóveda Obsidian

Repositorio/bóveda de estudio para la materia **Introducción a los Sistemas Operativos** (Ingeniería/UCASAL). Contiene teoría, preguntas/respuestas, ejercicios de finales con resoluciones detalladas y recursos gráficos.

> [!important]
> **El final es escrito (no oral).** La ruta de estudio está pensada para practicar respuestas escritas y resolución de ejercicios.

## Estructura del repositorio

```text
.
├── Introducción a los Sistemas Operativos/
│   ├── 00 Inicio.md                  # Portada de la bóveda
│   ├── FINALES/                      # LO PRINCIPAL PARA ESTUDIAR EL FINAL
│   │   ├── 00 EMPEZAR ACA - Ruta de estudio.md
│   │   ├── Índice del final.md
│   │   ├── 00-01,04-06 ...           # Plan, temas, cronograma, mapa, modelos
│   │   ├── Teoria/                   # Par teoría: preguntas + respuestas
│   │   │   ├── 01 Preguntas de teoria.md
│   │   │   └── 02 Respuestas detalladas.md
│   │   ├── Ejercicios de finales/    # Par ejercicios: enunciados + resoluciones
│   │   │   ├── 01 Enunciados.md
│   │   │   └── 02 Resoluciones detalladas.md
│   │   └── Gráficos/                 # Diagramas y figuras de apoyo
│   └── Complementario/               # Material de apoyo (consultar si hace falta)
│       ├── MATERIA-COMPLETA/         # Teoría completa por Unidad → Tema → Subtema
│       └── OCR/                      # Textos OCR de exámenes escaneados/fotos
└── scripts/
    ├── extract_scanned_content.py    # Extracción de texto/OCR para PDFs e imágenes
    └── README.md
```

## Cómo usar

1. Abrí la carpeta `Introducción a los Sistemas Operativos/` como bóveda en **Obsidian**.
2. Empezá por `FINALES/00 EMPEZAR ACA - Ruta de estudio.md`.
3. **Teoría:** leé `FINALES/Teoria/01 Preguntas de teoria.md` y corregí con `FINALES/Teoria/02 Respuestas detalladas.md`.
4. **Ejercicios:** resolvé `FINALES/Ejercicios de finales/01 Enunciados.md` y corregí con `FINALES/Ejercicios de finales/02 Resoluciones detalladas.md`.
5. Para teoría completa de respaldo: `Complementario/MATERIA-COMPLETA/00 Índice de la materia.md`.

## Convenciones

- **Wikilinks Obsidian**: `[[Nombre de nota]]`.
- **Pares en carpetas propias**: cada carpeta de estudio tiene un archivo para practicar (preguntas/enunciados) y otro para corregir (respuestas/resoluciones), en orden lógico.
- **FINALES**: material orientado a examen escrito; las resoluciones incluyen contexto, teoría mínima, pasos, caso resuelto y trampas cuando corresponde.
- **MATERIA-COMPLETA**: organizada por **Unidad → Tema → Subtema**. Cada subtema busca incluir definición, desarrollo, ejemplo, trampas y gráficos cuando aportan.
- **OCR**: los textos en `Complementario/OCR/` fueron extraídos automáticamente y pueden contener errores; conviene contrastar con el original ante dudas.

## Scripts

Ver [`scripts/README.md`](scripts/README.md) para el extractor OCR de PDFs/imágenes.
