---
tipo: mapa
---
# Mapa: pregunta → subtema

> [!abstract] Para qué sirve
> Cada pregunta de los parciales (PP) y de los TP apunta al subtema que la resuelve. Si una pregunta te suena, buscala acá y andá directo a la nota. La columna **Frecuencia** indica si es de las que se repiten.

## Preguntas posibles de parciales (PP)
| PP | Pregunta (resumen) | Subtema | Frecuencia |
|---|---|---|---|
| 1 | Qué es un SO y sus funciones | [[1.1.1 Definición y funciones]] | Alta |
| 2 | Kernel vs. shell | [[1.1.2 Kernel, shell y programas del sistema]] | Alta |
| 3 | Llamadas al sistema y ejemplos | [[1.2.2 Llamadas al sistema]] | Alta |
| 4 | Programa vs. proceso; IPC | [[2.1.1 Programa vs. proceso]] · [[2.6.1 Comunicación entre procesos (IPC)]] | Alta |
| 5 | Multiprogramación y ventajas | [[2.5.1 Multiprogramación — concepto y beneficios]] | **Muy alta** |
| 6 | Spooling | [[1.3.2 Multiprogramación, spooling y tiempo compartido]] | Alta |
| 7 | Modos kernel y usuario | [[1.2.1 Modo usuario y modo kernel]] | Alta |
| 8 | Máquina virtual y JVM | [[1.4.4 Máquinas virtuales, hipervisor, JVM y CLR]] | Media |
| 9 | Fragmentación interna y externa | [[3.3.3 Fragmentación interna y externa]] | **Muy alta** |
| 10 | Paginación y ventajas | [[4.1.2 Paginación y la MMU]] | Alta |
| 11 | Segmentación | [[4.6.1 Segmentación]] | Media-alta |
| 12 | Tamaño de página óptimo | [[4.5.1 Tamaño de página óptimo — s = √(2PE)]] | Alta |
| 13 | 64 bits, 8 KB, 32 GB | [[4.1.3 Cálculo de bits, páginas y marcos]] | **Muy alta** |
| 14 | 64 bits, 16 KB, 65 GB | [[4.1.3 Cálculo de bits, páginas y marcos]] | Alta |
| 15 | Memoria virtual y paginación por demanda | [[4.1.1 Memoria virtual y overlays]] | Media |
| 16 | Estados y transiciones | [[2.2.1 Estados de un proceso y transiciones]] | Media |
| 17 | Contenido del PCB | [[2.1.2 El PCB (Process Control Block)]] | Alta |
| 18 | Proceso vs. hilo | [[2.3.1 Proceso vs. hilo]] | Media-baja |
| 19 | Mecanismos de IPC | [[2.6.1 Comunicación entre procesos (IPC)]] | Media |
| 20 | Sincronización | [[2.6.2 Sincronización y condiciones de carrera]] | Baja |
| 21 | Objetivos de la planificación | [[2.4.1 Objetivos de la planificación]] | Media |
| 22 | FIFO, SJF, RR y prioridades | [[2.4.2 FIFO, SJF y Round Robin (quantum)]] · [[2.4.3 Prioridades, hambre y aging]] | Media |
| 23 | Quantum y rendimiento en RR | [[2.4.2 FIFO, SJF y Round Robin (quantum)]] | Media |
| 24 | Utilización con 50 % de E/S | [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] | **Muy alta** |
| 25 | Parámetros de la planificación | [[2.4.1 Objetivos de la planificación]] | Baja |
| 26 | Fallo de página y pasos | [[4.3.1 Pasos de un fallo de página]] | **Muy alta** |
| 27 | FIFO | [[4.4.1 Óptimo, FIFO y anomalía de Belady]] | **Muy alta** |
| 28 | Problema de FIFO y Belady | [[4.4.1 Óptimo, FIFO y anomalía de Belady]] | Alta |
| 29 | FIFO con bit R; reloj | [[4.4.2 Segunda oportunidad y algoritmo del reloj]] | Alta |
| 30 | LRU, NRU y segunda oportunidad | [[4.4.3 NRU, LRU y aging]] · [[4.4.2 Segunda oportunidad y algoritmo del reloj]] | **Muy alta** |
| 31 | 50 % de E/S: calcular n para 90 % | [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] | Alta |
| 32 | 64 bits, 8 KB, 32 GB (recap) | [[4.1.3 Cálculo de bits, páginas y marcos]] | Alta |
| 33 | 64 bits, 16 KB, 65 GB (recap) | [[4.1.3 Cálculo de bits, páginas y marcos]] | Media |
| 34 | Tamaño óptimo con 8 KB y 4 bytes | [[4.5.1 Tamaño de página óptimo — s = √(2PE)]] | Alta |
| 35 | U para distintos n y p | [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] | Alta |

## Preguntas de los TP (1, 2 y 3)
| TP | Pregunta (resumen) | Subtema |
|---|---|---|
| TP1-1 | Funciones principales del SO | [[1.1.1 Definición y funciones]] |
| TP1-2 | Lenguaje de máquina, microprogramación, assembler y procesos | [[1.1.1 Definición y funciones]] · [[2.1.1 Programa vs. proceso]] |
| TP1-3 | Modo usuario y kernel; código del SO mínimo | [[1.2.1 Modo usuario y modo kernel]] |
| TP1-4 | Por qué el shell no es SO | [[1.1.2 Kernel, shell y programas del sistema]] |
| TP1-5, 6 | Fecha y hora desde el shell y desde un programa | [[1.4.5 Práctica — consultar fecha y hora del sistema (TP1, preguntas 5 y 6)]] |
| TP1-7 | Instrucciones privilegiadas | [[1.2.1 Modo usuario y modo kernel]] |
| TP1-8 | Multiprogramación y sus razones | [[1.3.2 Multiprogramación, spooling y tiempo compartido]] |
| TP1-9, 10 | Spooling; procedimiento 1401/7094 | [[1.3.2 Multiprogramación, spooling y tiempo compartido]] · [[1.3.1 Generaciones de computadoras y su SO]] |
| TP1-11 | Tiempo compartido | [[1.3.2 Multiprogramación, spooling y tiempo compartido]] |
| TP1-12, 13 | Llamadas al sistema; shell de código | [[1.2.2 Llamadas al sistema]] · [[1.1.2 Kernel, shell y programas del sistema]] |
| TP1-14 | Proceso y programa | [[2.1.1 Programa vs. proceso]] |
| TP1-15, 16, 21 | Raíz; archivos de bloque y de caracteres; sistema de archivos | [[1.4.1 Sistema de archivos y directorios]] · [[1.4.2 Archivos especiales de bloque y de caracteres]] |
| TP1-17 | Multiprogramación sin DMA | [[1.4.3 E-S programada, interrupciones, DMA]] |
| TP1-18 | Dos CPU con hiperhilos | [[03 Ejercicios tipo con resultado]] |
| TP1-19 | Tiempo medio de acceso con caché y disco | [[03 Ejercicios tipo con resultado]] |
| TP1-20 | Syscall vs. función de biblioteca | [[1.2.2 Llamadas al sistema]] |
| TP1-22 | VM, hipervisor, JVM y CLR | [[1.4.4 Máquinas virtuales, hipervisor, JVM y CLR]] |
| TP1-23 | Conversiones de unidades | [[02 Preguntas destacadas (aparecieron una vez)]] |
| TP2-1, 2, 3 | Fragmentación; listas enlazadas; asignación con 1 GB | [[3.3.3 Fragmentación interna y externa]] · [[3.4.2 Listas enlazadas]] · [[3.3.1 Particiones fijas]] |
| TP2-4 | Cuatro algoritmos de asignación | [[3.5.1 Primer ajuste, próximo ajuste, mejor ajuste y peor ajuste]] |
| TP2-5 | Costo de compactación | [[3.3.2 Particiones variables, swapping y compactación]] |
| TP2-6, 7 | Desperdicio de CPU y mejora con más memoria | [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] |
| TP2-8, 9 | Simulación de multiprogramación | [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] |
| TP3-1 | Pasos para acceder a un dato con tabla de páginas | [[4.1.2 Paginación y la MMU]] |
| TP3-2 | Tamaño de página con dos niveles | [[4.2.2 Tablas multinivel e invertidas]] |
| TP3-3 | Direcciones físicas | [[4.1.2 Paginación y la MMU]] |
| TP3-4 | Pasos del fallo de página | [[4.3.1 Pasos de un fallo de página]] |
| TP3-5, 6, 7 | Bits de direcciones y tablas | [[4.1.3 Cálculo de bits, páginas y marcos]] |
| TP3-8 | Reemplazo con tabla de tiempos | [[4.4.3 NRU, LRU y aging]] · [[03 Ejercicios tipo con resultado]] |
| TP3-9 | Programa de 16 bits: 4 KB vs. 256 bytes | [[4.6.2 Segmentación con paginación y su combinación]] |
| TP3-10 | Segmentación | [[4.6.1 Segmentación]] |
| TP3-11 | Tamaño óptimo de página | [[4.5.1 Tamaño de página óptimo — s = √(2PE)]] |
