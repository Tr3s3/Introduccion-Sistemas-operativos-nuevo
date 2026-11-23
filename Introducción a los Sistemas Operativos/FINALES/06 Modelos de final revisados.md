---
tipo: modelos
---
# Modelos de final revisados (2022 a 2025)

> [!abstract] Qué contiene esta nota
> Cada examen real que revisamos, qué temas trae y **qué se repite**. Sirve para saber con qué te puede tocar cada bloque. La resolución numérica está en [[07 Ejercicios de los modelos (resueltos)]].

> [!warning] Nombres y fechas
> Los nombres de archivo no siempre coinciden con la fecha impresa en la hoja. Acá se usa la **fecha impresa** cuando la hay, y si no, una descripción por contenido.

## Inventario (según el nombre del archivo)

> [!note] Fechas
> Los archivos de febrero y noviembre no traen fecha impresa legible en el texto. Acá se usa el nombre del archivo; las fechas exactas hay que confirmarlas en la hoja original.

| Examen (archivo) | Qué trae (resumen) |
|---|---|
| **Parcial 2022** | Spooling y generación · tabla de 32 bits, páginas 4 KB, PC de 4 MB · fragmentación interna vs. externa · 22 bits, páginas 2 K, 16 M · NRU |
| **Parcial 2023** | Multiprogramación · administración por mapa de bits vs. listas · modelo probabilístico (p = 0,5 con 3 procesos) · 42 bits, 8 KB, 8 GB · LRU |
| **Parcial 2024** | Gantt con 50 % de E/S · 36 bits, páginas de **5 KB**, 16 GB · fragmentación externa · multiprogramación y spooling · segunda oportunidad |
| **Recuperatorio 2024** | Llamada al sistema · modelo probabilístico y grado de multiprogramación · 32 bits, 2 K, 1 MB · multinivel 12+12, 4 K, 96 GB · segmentación vs. paginación |
| **Recuperatorio 2025** | Llamada al sistema y el comando `time` · Gantt con 90 % · 52 bits, 2 KB · FIFO · 25 bits con 3 niveles (4+5+5) |
| **1T Febrero 2024** | Llamada al sistema · modelo probabilístico · mapa de bits · tabla de 8 bits · 32 bits, 16 K, tabla de 3 niveles |
| **2T Febrero 2024** | Máquina virtual · LRU (ventaja y problema) · fallo de página · tabla de 16 bits · 56 bits, 16 K, 16 GB |
| **Noviembre 2023 / Diciembre 2023** | Multiprogramación · fragmentación · máquina virtual · 32 bits, 4 K, PC de 4 MB · 25 bits con 13 de desplazamiento |
| **Noviembre 2024 / Diciembre 2024** | Gantt con 50 % · TLB · 52 bits, 2 KB · FIFO · 9 bits con páginas de 8 bytes · tabla invertida · NRU · llamada al sistema y `time` |
| **1T Febrero 2025** | Llamada al sistema · modelo probabilístico · mapa de bits · tabla de 8 bits · 32 bits, 16 K, 3 niveles |
| **Diciembre 2025** | Multiprogramación, generación y spooling · segmentación con paginación (SO + programa) · fallo de página · tabla invertida de 64 bits |
| **Junio 2026** | Multiprogramación con segmentos de 16 bits y páginas de 2 K · tabla invertida 64 bits, 16 GB, 8 K |
| **Modelos resueltos** (13 págs.) | Semáforos, TSL, Peterson, aging, RR, multiprogramación 75 %, estados con swapping, condiciones de competencia, bits, tablas multinivel, relocación, spooling, LRU |

**Pendiente de revisar en detalle:** 2T Febrero 2025, junio 2024 y Parcial 2025 (PDF escaneados). No los incluimos en las frecuencias.

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
> Si tenés tiempo para una sola cosa: los **cálculos de bits** y el **modelo probabilístico**. Son los que casi siempre tocan y los que más puntos dan en el oral.
