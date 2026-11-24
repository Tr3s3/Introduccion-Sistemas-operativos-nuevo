---
tipo: modelos
---
# Modelos de final revisados (2022 a 2025)

> [!abstract] Qué contiene esta nota
> Cada examen real que revisamos, qué temas trae y **qué se repite**. Sirve para saber con qué te puede tocar cada bloque. La resolución numérica está en [[07 Ejercicios de los modelos (resueltos)]].

> [!warning] Nombres y fechas
> Los nombres de archivo no siempre coinciden con la fecha impresa en la hoja. Acá se usa la **fecha impresa** cuando la hay, y si no, una descripción por contenido.

## Inventario

> [!note] Criterio
> Cuando hay foto/PDF del examen, se toma lo que se lee en la hoja. Si el nombre de archivo no coincide con la fecha impresa, se indica. Esta lista mezcla exámenes ya cargados en el vault y los adjuntos en la última revisión.

| Examen | Qué trae (resumen) |
|---|---|
| **Recuperatorio 2024 – Tema 1** (foto) | Llamada al sistema y `time` · Gantt 90% (2 procesos, 1,38 min) · 52 bits, páginas 2 KB (problema/solución) · FIFO (defecto, solución, reloj) · 25 bits con 3 niveles (4+5+5) |
| **Recuperatorio 2025 – Tema 2** (foto) | Multinivel 2 niveles de 14 bits, páginas 64 B, 32 GB · modelo probabilístico multiprogramación (CPU total e individual) · 16 bits, 1 KB, segmentación con paginación (código 30145, datos 18834, pila 14870) · LRU por HW (problema, solución, memoria en 32 bits/4 KB) · spooling en impresión |
| **1T Febrero 2024** (foto) | Llamada al sistema y `time` · Gantt 60% (3 procesos: 13:00/2,32; 13:05/2,32; 13:12/4,00) · segmentación vs. paginación vs. seg+pag · 36 bits, 16 KB, 128 GB · NRU (problema y solución) |
| **Final 11-12-2024** (foto) | Gantt 50% (12:00/2; 12:01/5; 12:09/2,5) · TLB (qué es, beneficio, por qué no en tabla convencional y sí en TLB indicar página virtual) · 52 bits, 2 KB (problema) · FIFO (defecto, solución, algoritmo más eficiente) · 9 bits, páginas 8 bytes, 2 GB física |
| **Junio 2026** (foto) | Multiprogramación (3ª gen, spooling, relación, importancia actual) · 16 bits, 2 KB, seg+pag SO+programa (¿entra? ¿y con 1 KB?) · fallo de página con todos los marcos ocupados (graficar/explicar) · tabla invertida 64 bits, 16 GB, 8 KB, factor 2 |
| **Final 29-11-2023** (foto) | Multiprogramación (por qué se agrega, problema) · fragmentación interna/externa con ejemplo · máquina virtual (JVM, CLR, ejemplos) · 32 bits, 4 KB, PC 4 MB, entrada 4 bytes (problema/solución) · 25 bits, 13 de desplazamiento, 1 GB, entradas 32 bits |
| **Final 27-11-2024** (foto) | Llamada al sistema y `time` · tabla invertida (ejemplo numérico) · TLB · NRU (problema/solución) · 16 bits, 4 KB, tabla dada: dirección virtual 20500 (página, marco, desplazamiento, dirección física) |
| **Parcial 2022** (foto) | Spooling (3ª gen, importancia) · 32 bits, 4 KB, 4 MB, entradas 4 bytes (problema) · fragmentación interna y externa · 22 bits, 2 K, 16 M · NRU |
| **Parcial 2023 – Tema 1** (foto) | Multiprogramación (qué permite, generación, importancia) · mapa de bits vs. listas enlazadas · modelo probabilístico 50%, 3 procesos (E/S, CPU total, CPU por proceso, 2 procesos 50%/90%) · 42 bits, 8 KB, 8 GB · LRU (problema/solución) |
| **Parcial 2024 – Tema 2** (foto) | Gantt 50% (12:00/2, 12:01/5, 12:20/2,5) · 36 bits, páginas **5 KB**, 16 GB (trampa: página no potencia de 2) · fragmentación externa · multiprogramación y spooling · segunda oportunidad |
| **1T Febrero 2025** | Llamada al sistema · modelo probabilístico · mapa de bits · tabla de 8 bits · 32 bits, 16 K, 3 niveles |
| **2T Febrero 2024** | Máquina virtual · LRU (ventaja y problema) · fallo de página · tabla de 16 bits · 56 bits, 16 K, 16 GB |
| **2T Febrero 2025** (26/02/2025) | Multiprogramación · fragmentación · máquina virtual · tabla invertida 32 bits · 31 bits con páginas de 8 K |
| **Final julio 2024** (03/07/2024) | Multiprogramación y spooling · tabla multinivel 10+10+12 · listas enlazadas · fallo de página · tabla invertida 64 bits, 16 GB, factor 2 |
| **Parcial 2025 Tema 1 y 2** | Gantt 50 % con llegadas · tamaño óptimo de página · 64 bits con páginas de 16 K (64 GB) u 8 K (32 GB) · FIFO con bit R |
| **Modelos resueltos** (13 págs.) | Semáforos, TSL, Peterson, aging, RR, multiprogramación 75 %, estados con swapping, condiciones de competencia, bits, tablas multinivel, relocación, spooling, LRU |

**Revisados en la segunda pasada (antes pendientes):**
- **2T Febrero 2025** (26/02/2025 según la hoja): multiprogramación, fragmentación, máquina virtual, tabla invertida de 32 bits con PC de 4 MB, 31 bits con páginas de 8 KB.
- **Final julio 2024** (03/07/2024, archivo `junio2024`): multiprogramación y spooling, tabla multinivel 32 bits (10+10+12), listas enlazadas, fallo de página, tabla invertida de 64 bits con 16 GB y factor 2.
- **Parcial 2025 Tema 1 y Tema 2**: Gantt con E/S del 50 % y llegadas escalonadas, tamaño óptimo de página, 64 bits con páginas de 16 KB o 8 KB, FIFO con bit R.

## Material adicional integrado

**Primera tanda (PDFs de repaso):**
- **PreguntasPosibles_Parciales.pdf**: verificación de cobertura de las 35 preguntas y respuestas modelo.
- **RepasoISO.pdf**: mapa de bits vs. listas (velocidad/espacio), LRU con matriz, Aging/NFU, NRU con limpieza de bit R, estados con suspensión, spooling.
- **ResumenISOSAE1.pdf**: definiciones base, monolítico vs. microkernel, creación/fin de procesos, Buddy System y Quick Fit, TLB/MMU, tabla comparativa de algoritmos de reemplazo, y el Gantt canónico de 4 trabajos con 80 % de E/S.

**Segunda tanda (diapositivas, TPs y Tanenbaum):**
- **Diapositivas de cátedra** (Introducción, Procesos y Memoria, Administración de Memoria Virtual): se extrajeron diagramas clave y se embebieron en `08 Ejercicios frecuentes paso a paso.md` (`slide_tlb.png`, `slide_reloj.png`, `slide_lru.png`, `slide_aging_nru.png`, `slide_bitmap_vs_listas.png`, `slide_tabla_multinivel.png`, `slide_working_set_thrashing.png`, `slide_estados_proceso.png`).
- **TP1 2022, TP2 2022, TP3 2018**: verificados contra el mapa de preguntas/ejercicios; la cobertura en `03`, `05`, `07` y `08` se mantiene alineada.
- **Tanenbaum (cap. Introducción, Procesos, Memoria, Memoria Virtual) + libro completo**: usados como referencia de respaldo para definiciones y terminología; se priorizó el contenido que aparece en parciales/finales.

**Tercera tanda (OCR de escaneados/fotos, 2026-11-23):**
- Se implementó `scripts/extract_scanned_content.py` (PyMuPDF + RapidOCR + `opencv-python-headless`) para extraer texto de PDFs escaneados y JPEG/PNG.
- Se auditaron 33 archivos en `/tmp/arena-coding-uploads`: 15 con texto embebido, 18 requerían OCR.
- Los 18 OCR quedaron en `Complementario/OCR/` y se usaron para integrar preguntas/ejercicios faltantes. **Nota:** el OCR puede tener errores en símbolos, fórmulas y manuscrito; ante duda, contrastar con la imagen/PDF original.
- Modelos extraídos por OCR: `1TFebrero2024`, `1TFebrero2025`, `2TFebrero2024`, `2TFebrero2025`, `Diciembre2023/2024/2025`, `Junio2026`, `Noviembre2023/2024`, `Parcial2022/2023/2024/2025`, `Recu 2024`, `Recu2025`, `junio2024`, `image-1` (captura/listado).

## Lo que más se repite (en los exámenes revisados)

| Tema | Veces que aparece | Dónde estudiarlo |
|---|---|---|
| **Cálculo de bits, páginas y marcos** (desplazamiento, páginas, marcos, memoria direccionable) | **en casi todos** | [[4.1.3 Cálculo de bits, páginas y marcos]] |
| **Llamada al sistema** (concepto, ejemplos, si `time` lo es) | **6 o más** | [[1.2.2 Llamadas al sistema]] |
| **Modelo probabilístico U = 1 − pⁿ** y Gantt de E/S | **6 o más** | [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] |
| **Tablas multinivel** (3 niveles, cantidad de subtablas) y **tabla invertida** | **5 o más** | [[4.2.2 Tablas multinivel e invertidas]] |
| **NRU** (qué es, problema, qué lo soluciona) | **4** | [[4.4.3 NRU, LRU y aging]] |
| **LRU** (ventaja, problema de la matriz, solución) | **3** | [[4.4.3 NRU, LRU y aging]] |
| **FIFO** (defecto, Belady, segunda oportunidad) | **3** | [[4.4.1 Óptimo, FIFO y anomalía de Belady]] · [[4.4.2 Segunda oportunidad y algoritmo del reloj]] |
| **Multiprogramación y spooling** (concepto, generación, relación) | **4** | [[1.3.2 Multiprogramación, spooling y tiempo compartido]] |
| **Fragmentación interna vs. externa** | **3** | [[3.3.3 Fragmentación interna y externa]] |
| **Mapa de bits vs. listas enlazadas** | **3** | [[3.4.1 Mapa de bits]] · [[3.4.2 Listas enlazadas]] |
| **Segmentación vs. paginación vs. combinada** | **2** | [[4.6.2 Segmentación con paginación y su combinación]] |
| **TLB** | **2** | [[4.2.1 TLB (memoria asociativa)]] |
| **Fallo de página, pasos** | **2** | [[4.3.1 Pasos de un fallo de página]] |
| **Máquina virtual** | **2** | [[1.4.4 Máquinas virtuales, hipervisor, JVM y CLR]] |

## Preguntas que aparecieron una sola vez (destacadas)
- **Tabla de páginas de 52 bits con páginas de 2 KB**: aparece en dos exámenes, así que es repetida. Ver la resolución en el archivo 07.
- **Página de 5 KB** (no es potencia de 2): el "problema de la definición del sistema" del Parcial 2024. Es la trampa más fácil.
- **Memoria de 9 bits con páginas de 8 bytes** (Final de Diciembre 2024): tamaño de página muy chico, 64 páginas.
- **Sistema de 56 bits con páginas de 16 K** (2T Febrero 2024): tabla gigante, cada página es un trabajo de traducción.
- **Gantt de E/S del 60 %** (procesos de 2,32 y 4 minutos): pide no redondear.
- **Pila y datos en 16 bits y segmentación con paginación** (Junio 2026): exige sumar páginas por segmento y decidir si entra.

> [!tip] Cómo usar esto
> Si tenés tiempo para una sola cosa: los **cálculos de bits** y el **modelo probabilístico**. Son los que casi siempre tocan y los que más puntos dan en el examen escrito.
