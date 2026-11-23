---
tipo: resolucion
---
# Ejercicios frecuentes: resolución paso a paso

> [!abstract] Para qué es esta nota
> Acá están los **ejercicios que más se repiten** en los finales y parciales revisados (incluye los de 2T Feb 2025, Parcial 2025 Tema 1 y 2, Final de julio 2024). Para cada uno: **contexto**, **teoría mínima**, **método paso a paso** y **un caso resuelto**. Si te alcanza el tiempo, estudiá en el orden de la tabla.

## Mapa rápido

| # | Ejercicio | Dónde apareció | Gráfico |
|---|---|---|---|
| E1 | Bits, páginas y marcos | casi todos | [[traduccion_direccion.svg]] |
| E2 | Tamaño óptimo de página √(2PE) | Parcial 2025 T1 y T2, 2T Feb 2025 | — |
| E3 | Multiprogramación: U = 1 − pⁿ | Parcial 2025 T1 y T2, Final julio 2024, Modelos | [[utilizacion_cpu_1_menos_p_n.svg]] |
| E4 | Gantt con E/S del 50 % | Parcial 2025 T1 y T2 | [[gantt_parcial_2025_t1.svg]] · [[gantt_parcial_2025_t2.svg]] |
| E5 | Tabla de páginas invertida | Final julio 2024, 2T Feb 2025, Parcial 2025 T1 y T2, Diciembre 2025 | [[tabla_invertida.svg]] |
| E6 | Tabla multinivel | Final julio 2024, 1T Feb 2024 y 2025 | [[tabla_multinivel_32_bits.svg]] |
| E7 | Fallo de página: pasos y reemplazo | Final julio 2024, Parcial 2025 T1 y T2 | [[fallo_pagina_pasos.svg]] |
| E8 | FIFO y su problema (con bit R) | Parcial 2025 T1 y T2, Recuperatorio 2024 | [[fuente_fifo_segunda_oportunidad.png]] |
| E9 | Asignación de memoria: first, best, worst, next fit | TP2-4, Final 2024 | [[fuente_tabla_algoritmos.png]] |
| E10 | Fragmentación interna y externa | 2T Feb 2025, Final 2024, Parcial 2022 | [[fragmentacion_interna_externa.svg]] |
| E11 | Mapa de bits vs. listas enlazadas | Final julio 2024, 1T/2T Feb 2025 | [[fuente_particiones_colas.png]] |
| E12 | Multiprogramación y spooling (teoría y uso de CPU) | Parcial 2025 T1 y T2, 2T Feb 2025 | `fuente_uso_cpu_vs_multiprogramacion.png` |

---

## E1. Bits, páginas y marcos

**Contexto.** La dirección virtual se parte en dos: el número de página (bits altos) y el desplazamiento dentro de la página (bits bajos). La memoria física se parte en marcos del mismo tamaño que las páginas.

**Teoría mínima.**
- Desplazamiento = log₂(tamaño de página).
- Bits de página = bits de la dirección − desplazamiento.
- Páginas virtuales = 2^(bits de página).
- Marcos = memoria física ÷ tamaño de página.
- **Memoria que el sistema puede usar = la menor** entre la direccionable (2^bits) y la física.

![[traduccion_direccion.svg]]

**Pasos.**
1. Escribí los datos: bits de la dirección, tamaño de página, memoria física.
2. Pasá el tamaño de página a potencia de 2 (si no lo es, el desplazamiento no es entero: es un error del enunciado o una trampa).
3. Calculá el desplazamiento y los bits de página.
4. Calculá páginas y marcos.
5. Respondé lo que piden (bits para tabla, bits para desplazamiento, memoria direccionable).

**Caso resuelto (Parcial 2025 T2, inciso 5 — 64 bits, páginas de 8 KB, memoria de 32 GB).**
- Desplazamiento: 2¹³ = 8 KB → **13 bits**.
- Bits de página: 64 − 13 = **51 bits**.
- Páginas: 2⁵¹.
- Marcos: 32 GB ÷ 8 KB = 2³⁵ ÷ 2¹³ = **2²² marcos**.
- Memoria direccionable: 2⁶⁴ bytes (16 EB), pero solo hay 32 GB físicos.

**Caso resuelto (2T Feb 2025, inciso 5 — 31 bits, 13 de desplazamiento).**
- Tamaño de página: 2¹³ = **8 KB**.
- Cantidad de páginas: 2^(31 − 13) = 2¹⁸ = **262 144**.
- Marcos con 512 MB: 2²⁹ ÷ 2¹³ = 2¹⁶ = **65 536 marcos**.
- Tabla de páginas tradicional con entradas de 4 bytes: 2¹⁸ × 4 B = **1 MB**.

**Caso resuelto (1T Feb 2024 — tabla de 8 bits).** Ver [[07 Ejercicios de los modelos (resueltos)]].

---

## E2. Tamaño óptimo de página: s = √(2 · P · E)

**Contexto.** Una página grande desperdicia memoria en la última página de cada proceso (fragmentación interna). Una página chica necesita una tabla grande. El tamaño óptimo equilibra las dos cosas.

**Teoría mínima.**
- P = tamaño promedio de un proceso.
- E = tamaño de cada entrada de la tabla de páginas.
- Fragmentación interna promedio ≈ s/2 por proceso. Tamaño de la tabla ≈ (P/s) · E.
- Minimizando s/2 + PE/s da **s = √(2PE)**.

**Pasos.**
1. Pasá P y E a la misma unidad (bytes).
2. Calculá 2 · P · E.
3. Sacá la raíz cuadrada.
4. Si el enunciado pide potencia de 2, redondeá al valor más cercano.

**Caso resuelto (Parcial 2025 T1, inciso 2 — P = 8 KB, E = 4 B).**
- 2 · 8192 · 4 = 65 536. √65 536 = **256 bytes**.

**Caso resuelto (Parcial 2025 T2, inciso 2 — P = 1 KB, E = 8 B).**
- 2 · 1024 · 8 = 16 384. √16 384 = **128 bytes**.

> [!note] Respuesta de teoría
> Factores: fragmentación interna (página grande), tamaño de la tabla (página chica), velocidad de E/S (las páginas grandes leen más datos de una vez). Esto es lo que suele pedir la pregunta "¿qué factores inciden?".

---

## E3. Multiprogramación: U = 1 − pⁿ

**Contexto.** Un proceso pasa parte de su tiempo esperando E/S. Si la fracción de espera es p, la probabilidad de que los n procesos estén esperando todos a la vez es pⁿ, así que la CPU queda ociosa con probabilidad pⁿ.

**Teoría mínima.**
- U = 1 − pⁿ (utilización de la CPU).
- Para un objetivo U_obj: pⁿ ≤ 1 − U_obj ⇒ **n ≥ log(1 − U_obj) ÷ log(p)**.
- Con p = 0,5: n = 1 → 50 %, n = 2 → 75 %, n = 3 → 87,5 %, n = 4 → 93,75 %.

![[utilizacion_cpu_1_menos_p_n.svg]]

**Pasos.**
1. Identificá p (fracción de E/S).
2. Calculá U para cada n, o despejá n del objetivo.
3. Si pide "cuántos procesos", tomá el **menor n** que alcanza el objetivo.

**Caso resuelto (Modelos — p = 0,75 y U = 90 %).** 0,75ⁿ ≤ 0,1 ⇒ n ≥ log 0,1 ÷ log 0,75 = 7,96 ⇒ **n = 8**.

**Caso resuelto (Parcial 2025 — p = 0,5 y 3 procesos).** U = 1 − 0,5³ = **87,5 %**.

---

## E4. Gantt de procesos que llegan (E/S del 50 %)

**Contexto.** Los procesos llegan en distintos momentos y comparten la CPU. Cuando hay n procesos, la CPU da U = 1 − pⁿ de su capacidad, repartida en partes iguales (round robin).

**Convención que usa la cátedra (resumen SAE).**
- Con n procesos en memoria, **cada proceso avanza U/n de CPU por minuto de reloj**.
- Si un proceso necesita d minutos de CPU, tarda d ÷ (U/n) minutos de reloj **mientras sea n el grado de multiprogramación**.
- Cada vez que llega o termina un proceso, **recalculá n y U** y seguí desde ese momento.
- No redondees: usá los decimales completos.

**Pasos.**
1. Armá una tabla con llegadas, duraciones (CPU) y hora de inicio.
2. Entre dos eventos (llegada o fin), n es constante: U = 1 − pⁿ, velocidad por proceso = U/n.
3. Calculá cuánto CPU avanza cada proceso en el intervalo, restale a su duración y mirá quién termina primero.
4. Dibujá el Gantt y anotá los momentos de fin.

**Caso resuelto (Parcial 2025 T1 — p = 0,5).**

| Proceso | Inicia | CPU |
|---|---|---|
| P1 | 12:00 | 2 min |
| P2 | 12:01 | 5 min |
| P3 | 12:15 | 3,5 min |

- 12:00–12:01 (n = 1, U = 0,5, velocidad 0,5): P1 avanza 0,5 → le quedan **1,5**.
- 12:01–12:05 (n = 2, U = 0,75, velocidad 0,375): P1 necesita 1,5 ÷ 0,375 = 4 min → **termina 12:05**. P2 avanzó 1,5 → le quedan **3,5**.
- 12:05–12:15 (n = 1, velocidad 0,5): P2 necesita 3,5 ÷ 0,5 = 7 min → **termina 12:12**. Entre 12:12 y 12:15 la CPU queda ociosa.
- 12:15–12:22 (n = 1): P3 necesita 3,5 ÷ 0,5 = 7 min → **termina 12:22**.

![[gantt_parcial_2025_t1.svg]]

**Caso resuelto (Parcial 2025 T2 — p = 0,5).**

| Proceso | Inicia | CPU |
|---|---|---|
| P1 | 17:00 | 9 min |
| P2 | 17:15 | 2,5 min |
| P3 | 17:23 | 2 min |

- 17:00–17:15 (n = 1, velocidad 0,5): P1 avanza 7,5 → le quedan **1,5**.
- 17:15–17:19 (n = 2, velocidad 0,375): P1 necesita 1,5 ÷ 0,375 = 4 min → **termina 17:19**. P2 avanzó 1,5 → le quedan **1,0**.
- 17:19–17:21 (n = 1, velocidad 0,5): P2 necesita 1 ÷ 0,5 = 2 min → **termina 17:21**.
- 17:23–17:27 (n = 1): P3 necesita 2 ÷ 0,5 = 4 min → **termina 17:27**.

![[gantt_parcial_2025_t2.svg]]

> [!warning] Convención a confirmar
> Esta es la interpretación de la cátedra (round robin con reparto U/n). Si el enunciado da "duración" como tiempo de reloj y no de CPU, cambiá el cálculo. Preguntá cuál es la convención en el final.

---

## E5. Tabla de páginas invertida

**Contexto.** Con direcciones de 64 bits, una tabla normal tiene una entrada por página virtual: 2⁵¹ entradas, imposible de guardar. La **invertida** tiene una entrada por **marco** físico y la búsqueda se hace por hash.

**Teoría mínima.**
- Entradas = cantidad de marcos (memoria física ÷ tamaño de página).
- Bits para acceder a la tabla = bits necesarios para indicar un marco.
- Si el enunciado pide "factor 2": la tabla tiene el doble de entradas que marcos.

![[tabla_invertida.svg]]

**Pasos.**
1. Calculá el desplazamiento y los bits de página (E1).
2. Calculá los marcos: memoria física ÷ tamaño de página.
3. Si preguntan la tabla normal: páginas virtuales (2^(bits de página)).
4. Si preguntan la invertida: entradas = marcos (o marcos × factor).
5. Bits para acceder a la tabla = log₂(marcos).

**Caso resuelto (Final julio 2024 — 64 bits, páginas de 8 KB, memoria física de 16 GB, factor 2).**
- Sin tabla invertida: 2⁶⁴ ÷ 2¹³ = **2⁵¹ páginas** (entradas) → tabla enorme.
- Con tabla invertida: memoria con factor 2 = 32 GB = 2³⁵ bytes → marcos = 2³⁵ ÷ 2¹³ = **2²² entradas**.

**Caso resuelto (Parcial 2025 T1 — 64 bits, páginas de 16 KB, memoria física de 64 GB).**
- Desplazamiento: 14 bits.
- Marcos: 2³⁶ ÷ 2¹⁴ = **2²² marcos** → **22 bits** para acceder a la tabla invertida.
- Bits de página: 64 − 14 = 50 → **2⁵⁰ páginas virtuales**.
- Memoria direccionable: 2⁶⁴ bytes; memoria usable: 64 GB.

---

## E6. Tabla multinivel

**Contexto.** Una tabla de un nivel con 2²⁰ entradas de 4 bytes ocupa 4 MB, es decir, **toda** la memoria física. La tabla de dos niveles divide la dirección y crea subtablas solo donde hacen falta.

**Teoría mínima.**
- Con dos niveles de 10 bits y desplazamiento de 12: el primer nivel tiene 1024 entradas, cada una apunta a una tabla de 1024 entradas.
- Si una entrada del primer nivel está vacía, **no existe** su subtabla: eso ahorra memoria.

![[tabla_multinivel_32_bits.svg]]

**Pasos.**
1. Desplazamiento = log₂(página).
2. Repartí los bits de página entre los niveles (tabla de 10 + 10 bits, o 6 + 6 + 6, según el enunciado).
3. Cantidad de tablas = 1 (raíz) + entradas del nivel 1 × cantidad de tablas del nivel 2.
4. Si pide solo subtablas, restá la raíz.

**Caso resuelto (Final julio 2024, inciso 2 — 32 bits, páginas de 4 KB, dos niveles de 10 bits).**
- Desplazamiento: 12 bits. Bits de página: 20 (10 + 10).
- Tabla de nivel 1: 2¹⁰ = 1024 entradas.
- Si se usaran todas: 1 + 1024 subtablas, cada una con 1024 entradas: cada página virtual tiene su entrada, pero se crean solo las que se usan.
- Motivo para introducirla: una tabla de 2²⁰ entradas de 4 bytes ocupa 4 MB.

**Caso resuelto (1T Feb 2025 — 32 bits, páginas de 16 KB, 3 niveles de 6 bits).**
- Desplazamiento: 14. Bits de página: 18 (6 + 6 + 6). Páginas: 2¹⁸ = 262 144.
- Tablas: 1 + 2⁶ + 2⁶ × 2⁶ = **4161 tablas en total**, o **4160 subtablas** sin contar la raíz.

---

## E7. Fallo de página: pasos y reemplazo

**Contexto.** El bit de presencia de la página está en 0: la página no está en un marco. El hardware dispara un trap y el SO la trae del disco.

**Teoría mínima (pasos de la cátedra).**
1. Fallo de página (la instrucción referencia una página no presente).
2. TRAP al SO.
3. El SO busca un marco libre. Si no hay, elige una **víctima** según el algoritmo.
4. Si la víctima fue modificada (M = 1), la escribe al disco.
5. Carga la página pedida en el marco y actualiza la tabla.
6. Reinicia la instrucción.

![[fallo_pagina_pasos.svg]]

**Pasos del caso "todos los marcos ocupados".** Mismo procedimiento, pero el paso 3 siempre elige una víctima. Esto es lo que pide el Final julio 2024 (inciso 4).

**Respuesta modelo (Final julio 2024, inciso 4).**
- Se detecta el fallo (bit en 0).
- TRAP al SO.
- El SO elige una víctima con el algoritmo de reemplazo.
- Si la víctima tiene M = 1, la escribe al disco. Si no, la descarta.
- Carga la página nueva en el marco y actualiza la tabla.
- Reinicia la instrucción.

---

## E8. FIFO y su problema

**Contexto.** FIFO reemplaza la página que lleva más tiempo en memoria. Su problema es que puede reemplazar una página **muy usada** solo porque es la más antigua. Además, tiene la **anomalía de Belady** (más marcos pueden producir más fallos).

**Teoría mínima.** La solución es la **segunda oportunidad**: si la página más antigua tiene R = 1, se le da otra oportunidad (R = 0, se mueve al final de la cola). El **reloj** hace lo mismo con una lista circular.

![[fuente_fifo_segunda_oportunidad.png]]

**Pasos.**
1. Escribí el problema: FIFO reemplaza páginas importantes porque solo mira la antigüedad.
2. Nombrá la solución: FIFO con bit R (segunda oportunidad) o reloj.
3. Explicá por qué: el bit R indica uso reciente; si está en 1, la página no se reemplaza todavía.

**Respuesta modelo (Parcial 2025 T1, inciso 5 y Parcial 2025 T2, inciso 3).** El problema de FIFO es que puede reemplazar una página muy usada. Lo soluciona **FIFO con bit R** (segunda oportunidad): si el bit R de la página más antigua es 1, se pone en 0 y se mueve al final; así se protegen las páginas usadas recientemente.

---

## E9. Asignación de memoria: first, next, best y worst fit

**Contexto.** Cuando llega un proceso, hay que elegir un hueco libre para ponerlo. Cada criterio elige distinto.

**Teoría mínima.**
- **First fit**: el primer hueco que alcanza.
- **Next fit**: como first fit, pero la búsqueda empieza donde quedó la última vez.
- **Best fit**: el hueco que alcanza con menor sobra.
- **Worst fit**: el hueco más grande.

![[fuente_tabla_algoritmos.png]]

**Caso resuelto (TP2-4).** Huecos: 800, 300, 1500, 600, 700, 1000, 1200. Llegan procesos de 1000, 800 y 700.

| Algoritmo | 1000 | 800 | 700 |
|---|---|---|---|
| First fit | 1500 (queda 500) | 800 | 700 |
| Best fit | 1000 | 800 | 700 |
| Worst fit | 1500 (queda 500) | 1200 (queda 400) | 1000 (queda 300) |
| Next fit | 1500 | 1000 (queda 200) | 1200 (queda 500) |

**Pasos.** Recorré la lista en el orden del algoritmo, marcá el hueco elegido, calculá lo que sobra y actualizá la lista antes del siguiente proceso.

---

## E10. Fragmentación interna y externa

**Contexto.** La fragmentación es memoria que existe pero no se usa.

**Teoría mínima.**
- **Interna**: el bloque asignado es más grande que el proceso. Lo que sobra queda dentro del bloque. Ocurre con particiones fijas y con páginas.
- **Externa**: hay huecos libres, pero ninguno alcanza para el proceso, porque están separados. Ocurre con particiones variables.
- Solución a la externa: **compactación** o paginación.

![[fragmentacion_interna_externa.svg]]

**Respuesta modelo (2T Feb 2025, inciso 2).**
- Externa: cuando hay huecos entre bloques de memoria que no se pueden usar porque son muy chicos para asignar un proceso.
- Interna: cuando se asigna a un proceso un bloque mayor al que necesita; lo que sobra queda sin usar. Ejemplo: un proceso de 200 KB en un bloque de 320 KB deja 120 KB sin usar.

---

## E11. Mapa de bits vs. listas enlazadas

**Contexto.** Son dos formas de registrar qué partes de la memoria están libres.

**Teoría mínima.**
- **Mapa de bits**: un bit por unidad de asignación (0 = libre, 1 = ocupada). Tamaño fijo, pero buscar un hueco de k unidades es lento (hay que contar k ceros seguidos).
- **Listas enlazadas**: un nodo por segmento (P/H, dirección, tamaño, puntero al siguiente). Son más flexibles y se recorren para buscar huecos; ocupan memoria según la cantidad de segmentos.

![[fuente_particiones_colas.png]]

**Respuesta modelo (Final julio 2024, inciso 3).** La administración por listas enlazadas registra, para cada segmento, si está ocupado por un proceso o libre (P o H), su dirección de inicio, su tamaño y un puntero al siguiente. Es **más fácil** encontrar un hueco para un proceso con listas que con mapa de bits, porque en el mapa hay que buscar k ceros seguidos. (Hay criterios que prefieren el mapa de bits por su tamaño fijo: justificá la respuesta.)

---

## Preguntas de teoría que más se repiten (respuesta corta)

- **Programa vs. proceso**: el programa es el archivo ejecutable guardado en disco; el proceso es el programa en ejecución, con su PCB, registros, pila y memoria. El programa se guarda en disco; el proceso vive en memoria. Los datos entre procesos se pasan por **IPC** (memoria compartida, tuberías, mensajes).
- **Multiprogramación**: tener varios procesos en memoria para usar la CPU mientras otro espera E/S. Aparece en la 3.ª generación junto con el **spooling**: los trabajos se guardan en disco para que la CPU no espere a los lectores de tarjetas.
- **Máquina virtual**: software que emula una computadora completa (o un proceso) sobre un sistema operativo anfitrión. Ejemplos: VMware, VirtualBox (hipervisor); JVM (máquina virtual de Java); CLR (.NET); emuladores de consolas.
- **Tablas multinivel**: para no tener una tabla de páginas gigante, que ocupa demasiada memoria si se mantiene completa.
- **Tabla invertida**: una entrada por marco físico, no por página virtual; útil con espacios de 64 bits.

> [!tip] Orden de estudio
> E1 y E3 casi siempre aparecen. Después E4 (Gantt), E5 (invertida), E7 (fallo de página) y E8 (FIFO). Los demás los tenés que saber explicar, pero rara vez son el ejercicio entero.
