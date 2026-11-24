---
tipo: resolucion
---
# Resoluciones detalladas — Ejercicios de finales

> [!abstract] Cómo usar esta nota
> Compilado de ejercicios extraídos de finales, parciales y modelos revisados. Cada ejercicio incluye, según corresponda: **contexto**, **teoría mínima**, **pasos/método**, **caso resuelto**, **respuesta modelo corta** y **trampas típicas**. Los enunciados están en [[01 Enunciados]].

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
| E12 | Multiprogramación y spooling (teoría y uso de CPU) | Parcial 2025 T1 y T2, 2T Feb 2025 | [[fuente_uso_cpu_vs_multiprogramacion.png]] |
| E13 | LRU, NRU y Aging (matriz y contadores) | PP30, RS, Modelos | — |
| E14 | Casos trampa de bits (5 KB, 9 bits, 52 bits) | Parcial 2024 T2, Final 11-12-2024, Recu 2024 | — |
| E15 | Traducción de dirección con tabla (20500) | Final 27-11-2024, TP3-3 | — |
| E16 | Gantt 60% y 90% (sin redondear) | 1T Feb 2024, Recu 2024 T1 | — |
| E17 | LRU por hardware: costo de memoria | Recu 2025 T2, Modelos | — |
| E18 | Seg+pag: ¿cabe el proceso? (1 KB) | Recu 2025 T2, Junio 2026 | — |
| E19 | Multinivel 2×14 bits, páginas 64 B, 32 GB | Recu 2025 T2 | — |

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

**Caso resuelto (1T Feb 2025 — tabla de 8 bits, reconstruido desde OCR).**
- **Enunciado típico:** direccionamiento de 8 bits; tabla con 8 filas (páginas 0–7), cada fila con 2 bits de marco y 1 bit de presencia/ausencia.
- **Memoria direccionable:** 8 bits → $2^8 = 256$ bytes.
- **Bits para página / cantidad de páginas:** 8 filas = 8 páginas → 3 bits de página, 5 bits de desplazamiento → páginas de $2^5 = 32$ bytes.
- **Marcos y memoria física:** 2 bits de marco → $2^2 = 4$ marcos. Si la memoria física está totalmente ocupada: $4 	imes 32 = 128$ bytes.
- **Cómo usar la tabla:** página = bits altos; desplazamiento = bits bajos; si presencia = 0 → fallo de página; si presencia = 1 → físico = marco × tamaño de página + desplazamiento.
- **Trampa OCR:** el original escaneado puede tener valores puntuales distintos en la tabla; verificá con la imagen/fuente si te dan una tabla concreta.

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
- Si los procesos tienen **p distinto**, la CPU queda ociosa solo cuando **todos** esperan: U = 1 − ∏pᵢ. Ejemplo: p₁ = 0,5 y p₂ = 0,9 ⇒ U = 1 − 0,5 × 0,9 = **55 %**.

![[utilizacion_cpu_1_menos_p_n.svg]]

> [!note] Extracto de la cátedra (uso de CPU vs. grado de multiprogramación)
> ![[fuente_uso_cpu_vs_multiprogramacion.png]]
> La curva muestra que agregar procesos mejora mucho al principio y después rinde cada vez menos. Con 80 % de espera de E/S hacen falta muchos más procesos para alcanzar la misma utilización que con 20 %.

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

**Caso resuelto (Resumen SAE — p = 0,8, 4 trabajos, llegadas escalonadas).** Este es el ejemplo canónico que la cátedra usa para explicar el reparto round robin con multiprogramación.

| Trabajo | Llega | CPU requerida |
|---|---:|---:|
| 1 | 10:00 | 4 min |
| 2 | 10:10 | 4 min |
| 3 | 10:15 | 4 min |
| 4 | 10:20 | 4 min |

1. **10:00–10:10** (n = 1): U = 1 − 0,8 = 0,2. T1 avanza 0,2 × 10 = **2,0 min**. Le quedan 2,0.
2. **10:10–10:15** (n = 2): U = 1 − 0,8² = 0,36. Velocidad por proceso = 0,36 / 2 = 0,18. En 5 min cada uno avanza 0,9. T1 queda en 1,1; T2 queda en 3,1.
3. **10:15–10:20** (n = 3): U = 1 − 0,8³ = 0,488. Velocidad = 0,488 / 3 ≈ 0,1627. En 5 min cada uno avanza ≈ 0,8133. T1 queda en ≈ 0,2867; T2 en ≈ 2,2867; T3 en ≈ 3,1867.
4. **10:20 en adelante** (n = 4): U = 1 − 0,8⁴ = 0,5904. Velocidad = 0,5904 / 4 = 0,1476. T1 termina primero: 0,2867 ÷ 0,1476 ≈ 1,94 min → **10:21:56** aprox. Después se recalcula con n = 3, etc.

![[fuente_gantt_trabajos_sae.png]]

> [!success] Convención verificada
> El reparto U/n por proceso sale del ejemplo de la página 4-4 del resumen SAE: con 2 trabajos, U = 0,36 y cada uno recibe 0,36 / 2 = 0,18 min de CPU por minuto de reloj. Cuando un trabajo termina, **recalculá n y U** para el intervalo siguiente. Solo cambia el cálculo si el enunciado da la duración como tiempo de reloj y no como tiempo de CPU: en ese caso, preguntá en el final.

---

## E16. Gantt 60% y 90% (sin redondear)

**Contexto.** Son los mismos pasos que E4, pero cambian `p` y los tiempos. La clave es no redondear y recalcular en cada evento.

### Caso A — 1T Febrero 2024 (p = 0,6)

| Proceso | Llega | CPU |
|---|---:|---:|
| P1 | 13:00 | 2,32 min |
| P2 | 13:05 | 2,32 min |
| P3 | 13:12 | 4,00 min |

1. **13:00–13:05** (n=1): `U = 1 − 0,6 = 0,4`. Velocidad = 0,4. En 5 min, P1 avanza `0,4 × 5 = 2,0`. Le quedan **0,32**.
2. **13:05–13:06** (n=2, llega P2): `U = 1 − 0,6² = 0,64`. Velocidad por proceso = `0,64/2 = 0,32`. P1 necesita `0,32 / 0,32 = 1 min` → **P1 termina 13:06**. En ese minuto, P2 avanza 0,32; le quedan **2,0**.
3. **13:06–13:12** (n=1): `U = 0,4`. P2 necesita `2,0 / 0,4 = 5 min` → **P2 termina 13:11**. De 13:11 a 13:12 la CPU queda ociosa.
4. **13:12 en adelante** (n=1, llega P3): `U = 0,4`. P3 necesita `4,0 / 0,4 = 10 min` → **P3 termina 13:22**.

**Resultado:** P1 = 13:06, P2 = 13:11, P3 = 13:22.

### Caso B — Recu 2024 Tema 1 (p = 0,9)

| Proceso | Llega | CPU |
|---|---:|---:|
| A | 15:00 | 1,38 min |
| B | 15:10 | 1,38 min |

1. **15:00–15:10** (n=1): `U = 1 − 0,9 = 0,1`. En 10 min, A avanza `0,1 × 10 = 1,0`. Le quedan **0,38**.
2. **15:10–15:14** (n=2, llega B): `U = 1 − 0,9² = 1 − 0,81 = 0,19`. Velocidad por proceso = `0,19/2 = 0,095`. A necesita `0,38 / 0,095 = 4 min` → **A termina 15:14**. B avanza `0,095 × 4 = 0,38`; le quedan **1,0**.
3. **15:14 en adelante** (n=1): `U = 0,1`. B necesita `1,0 / 0,1 = 10 min` → **B termina 15:24**.

**Resultado:** A = 15:14, B = 15:24.

> [!warning] Trampas
> - Con p alto (0,9) la CPU rinde muy poco con 1 proceso (10%), pero mejora al haber 2. Mostrá ese salto.
> - No redondees en el medio: arrastrá decimales.
---

## E5. Tabla de páginas invertida

**Contexto.** Con direcciones de 64 bits, una tabla normal tiene una entrada por página virtual: 2⁵¹ entradas, imposible de guardar. La **invertida** tiene una entrada por **marco** físico y la búsqueda se hace por hash.

**Teoría mínima.**
- Entradas = cantidad de marcos (memoria física ÷ tamaño de página).
- Bits para acceder a la tabla = bits necesarios para indicar un marco.
- Si el enunciado pide "factor 2": la tabla tiene el doble de entradas que marcos.
- La tabla normal crece con el espacio **virtual**; la invertida crece con la memoria **física**. Por eso la invertida es la opción cuando el espacio virtual es enorme.
- **TLB (Translation Lookaside Buffer)**: caché de hardware con las traducciones recientes (página→marco). Si la traducción está en la TLB (*hit*), se evita ir a la tabla en memoria.

![[tabla_invertida.svg]]

> [!note] Extracto del libro (tabla tradicional vs. hash/invertida)
> ![[fuente_reloj.png]]
> A la izquierda: tabla indexada por página virtual (una entrada por cada página virtual, muy grande en 64 bits). A la derecha: tabla indexada por hash sobre la página virtual, con entradas que apuntan al marco físico correspondiente.

> [!note] Diapositiva de cátedra (TLB)
> ![[slide_tlb.png]]
> La TLB guarda entradas recientes: página virtual, marco, bits de validez/protección/modificación. Es la razón por la que el acceso paginado puede ser rápido en el caso común.

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

> [!note] Diapositiva de cátedra (tabla de dos niveles)
> ![[slide_tabla_multinivel.png]]

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

> [!note] Por qué importa tanto el disco
> ![[fuente_tabla_paginas_hash.png]]
> Un acceso a RAM está en el orden de nanosegundos, pero un acceso a disco está en milisegundos. Por eso un fallo de página es carísimo y los algoritmos de reemplazo buscan minimizar la cantidad de fallos.

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

> [!note] Diapositiva de cátedra (algoritmo del reloj)
> ![[slide_reloj.png]]
> El puntero recorre las páginas en círculo. Si R = 0, reemplaza; si R = 1, limpia R y avanza. Es la implementación eficiente de la segunda oportunidad.

**Anomalía de Belady (extracto del libro).** Con FIFO, aumentar la cantidad de marcos puede aumentar los fallos de página. En el ejemplo clásico, con 3 marcos hay 9 fallos y con 4 marcos hay 10 para la misma secuencia de referencias:

![[fuente_lru_matriz.png]]

> [!warning] Qué decir en el final
> FIFO es el único de los algoritmos comunes visto en la materia que sufre la anomalía de Belady. LRU y el algoritmo óptimo **no** la sufren.

**Pasos.**
1. Escribí el problema: FIFO reemplaza páginas importantes porque solo mira la antigüedad.
2. Nombrá la solución: FIFO con bit R (segunda oportunidad) o reloj.
3. Explicá por qué: el bit R indica uso reciente; si está en 1, la página no se reemplaza todavía.
4. Si preguntan por Belady, definila y aclaró que le pasa a FIFO (no a LRU).

**Respuesta modelo (Parcial 2025 T1, inciso 5 y Parcial 2025 T2, inciso 3).** El problema de FIFO es que puede reemplazar una página muy usada. Lo soluciona **FIFO con bit R** (segunda oportunidad): si el bit R de la página más antigua es 1, se pone en 0 y se mueve al final; así se protegen las páginas usadas recientemente.

---

## E13. LRU, NRU y Aging (cómo se eligen en la práctica)

**Contexto.** FIFO solo mira la antigüedad. LRU mira el uso reciente, pero implementarlo exacto es caro. NRU y Aging son aproximaciones prácticas.

### NRU (Not Recently Used)
- Usa los bits **R** (referenciada) y **M** (modificada). Periódicamente el SO pone R = 0.
- Clases (de mejor a peor para reemplazar):

| Clase | R | M | Significado |
|---:|:---:|:---:|---|
| 0 | 0 | 0 | No usada, no modificada |
| 1 | 0 | 1 | No usada, pero modificada (parece raro, pero pasa cuando se limpió R) |
| 2 | 1 | 0 | Usada, no modificada |
| 3 | 1 | 1 | Usada y modificada |

- Se reemplaza una página de la **clase más baja** disponible. Ventaja: simple. Límite: solo 4 clases, puede ser poco preciso.

### LRU (Least Recently Used)
- Reemplaza la página que no se usó hace **más tiempo**.
- Implementación por **matriz n×n** (si hay n marcos): al referenciar la página i, se pone en 1 toda la fila i y en 0 toda la columna i. La página con la **fila de menor valor** (menos 1s) es la menos usada recientemente.
- Problema: mantener la matriz es caro en tiempo y memoria (crece como n²).

> [!note] Diapositiva de cátedra (matriz LRU)
> ![[slide_lru.png]]

### Aging (NFU con envejecimiento)
- Aproxima LRU con un contador por página.
- En cada interrupción de reloj: se desplaza el contador a la derecha y se inserta el bit R como bit más significativo; luego se limpia R.
- Se reemplaza la página con el **contador más chico**.
- Es más barato que la matriz y captura bien la historia reciente.

> [!note] Diapositiva de cátedra (Aging/NFU)
> ![[slide_aging_nru.png]]

> [!tip] Cómo responder en el final
> Si te piden "¿qué problema tiene LRU y cómo se soluciona?", respondé: el costo de mantener la matriz/estructura exacta; se soluciona con aproximaciones como **Aging (NFU)** o **NRU**. Si te piden NRU, siempre mencioná los bits R y M y las 4 clases.

---

## E9. Asignación de memoria: first, next, best y worst fit

**Contexto.** Cuando llega un proceso, hay que elegir un hueco libre para ponerlo. Cada criterio elige distinto.

**Teoría mínima.**
- **First fit**: el primer hueco que alcanza.
- **Next fit**: como first fit, pero la búsqueda empieza donde quedó la última vez.
- **Best fit**: el hueco que alcanza con menor sobra.
- **Worst fit**: el hueco más grande.

![[fuente_tabla_algoritmos.png]]

**Otros algoritmos (nombralos si preguntan):**
- **Quick Fit**: mantiene listas separadas para tamaños de hueco solicitados con frecuencia. Busca rápido, pero complica la fusión (coalescencia) al liberar.
- **Buddy System**: divide la memoria en bloques de potencia de 2; si un bloque es muy grande, lo parte en dos "buddies" iguales. Facilita mucho la fusión, pero puede generar fragmentación interna.

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

> [!note] Diapositiva de cátedra (mapa de bits vs. listas enlazadas)
> ![[slide_bitmap_vs_listas.png]]

**Respuesta modelo (Final julio 2024, inciso 3).** La administración por listas enlazadas registra, para cada segmento, si está ocupado por un proceso o libre (P o H), su dirección de inicio, su tamaño y un puntero al siguiente. Es **más fácil** encontrar un hueco para un proceso con listas que con mapa de bits, porque en el mapa hay que buscar k ceros seguidos. (Hay criterios que prefieren el mapa de bits por su tamaño fijo: justificá la respuesta.)

---

## E14. Casos trampa de bits (5 KB, 9 bits, 52 bits)

### Caso A — Página no potencia de 2 (Parcial 2024 T2)
**Enunciado tipo:** 36 bits, páginas de **5 KB**, memoria física 16 GB.

1. **Verificación:** 5 KB = 5120 bytes. No es potencia de 2 (2^12=4096, 2^13=8192).
2. **Problema:** el desplazamiento dentro de la página debería ser `log2(5120)`, que no es entero. En paginación, el tamaño de página debe ser potencia de 2 para dividir la dirección en [página | desplazamiento] con bits fijos.
3. **Cómo responder:** “El sistema está mal definido para paginación estándar porque el tamaño de página no es potencia de 2; no se puede obtener un desplazamiento entero en bits. La solución es usar un tamaño de página potencia de 2 (por ejemplo 4 KB u 8 KB).”

> [!warning] No inventes un desplazamiento decimal. Decí claramente el problema de definición.

### Caso B — 9 bits con páginas de 8 bytes (Final 11-12-2024)
**Datos:** dirección virtual de 9 bits, página de 8 bytes, memoria física de 2 GB.

1. **Desplazamiento:** 8 bytes = 2^3 → **3 bits**.
2. **Bits de página:** 9 − 3 = **6 bits**.
3. **Páginas virtuales:** 2^6 = **64 páginas**.
4. **Marcos:** 2 GB / 8 B = 2^31 / 2^3 = **2^28 marcos**.
5. **Memoria direccionable:** 2^9 = **512 bytes**.
6. **¿Se puede usar toda la física?** No. El espacio virtual solo direcciona 512 bytes; aunque haya 2 GB de RAM, el proceso no puede referenciarlos con 9 bits.

**Resultado:** offset 3, 64 páginas, 2^28 marcos, direccionable 512 B, no se usa toda la RAM.

### Caso C — 52 bits con páginas de 2 KB (Recu 2024 T1 / Final 11-12-2024)
**Datos:** 52 bits de dirección virtual, páginas de 2 KB.

1. **Desplazamiento:** 2 KB = 2^11 → **11 bits**.
2. **Bits de página:** 52 − 11 = **41 bits**.
3. **Páginas virtuales:** 2^41.
4. **Problema:** una tabla de páginas de un solo nivel tendría 2^41 entradas; si cada entrada fuera, por ejemplo, de 4 u 8 bytes, la tabla sería inmanejable.
5. **Solución:** usar **tablas multinivel** (se crean solo las subtablas usadas) o **tabla invertida** (una entrada por marco físico). También TLB para acelerar traducciones, pero la TLB no reemplaza la estructura de la tabla.

**Respuesta corta:** “Hay 2^41 páginas; la tabla lineal es demasiado grande. Se soluciona con paginación multinivel o tabla invertida.”

---

## E15. Traducción de dirección con tabla (20500)

**Contexto.** Te dan la tabla página→marco y una dirección virtual decimal. Tenés que descomponerla y traducirla.

**Caso (Final 27-11-2024 / TP3-3):** sistema de 16 bits, páginas de 4 KB. Dirección virtual = 20500.

1. **Tamaño de página:** 4 KB = 4096 bytes = 2^12 → desplazamiento 12 bits.
2. **Número de página:** `20500 div 4096 = 5`.
3. **Desplazamiento:** `20500 mod 4096 = 20500 − 5×4096 = 20500 − 20480 = 20`.
4. **Verificación:** 5×4096 + 20 = 20500. OK.
5. **Binario (16 bits):** 20500 = `0101 0000 0001 0100`.
   - Bits altos (página 5): `0101`
   - Bits bajos (desplazamiento 20): `0000 0001 0100`
6. **Marco:** según la tabla del examen, la página 5 está en el marco 3.
7. **Dirección física:** `3 × 4096 + 20 = 12308`.
8. **Física en binario:** 12308 = `0011 0000 0001 0100` (marco `0011`, desplazamiento igual).

| Campo | Decimal | Binario |
|---|---:|---|
| Dirección virtual | 20500 | 0101 0000 0001 0100 |
| Página | 5 | 0101 |
| Desplazamiento | 20 | 0000 0001 0100 |
| Marco | 3 | 0011 |
| Dirección física | 12308 | 0011 0000 0001 0100 |

> [!tip] En el examen
> Escribí la división, la verificación, y después el binario. El desplazamiento se copia igual en la dirección física.

---

## E17. LRU por hardware: costo de memoria

**Contexto.** LRU exacto es buen algoritmo, pero implementarlo en hardware es caro porque hay que registrar el orden de uso.

**Caso (Recu 2025 T2):** sistema de 32 bits, páginas de 4 KB. ¿Cuánta memoria necesita LRU por hardware para llevar registro de uso reciente?

1. **Páginas del espacio virtual:** 2^32 / 2^12 = **2^20 páginas**.
2. **Problema de LRU HW:** para saber cuál fue la menos usada recientemente hay que mantener información de orden.
   - **Matriz n×n bits** (para n elementos comparados): crece como n^2. Si se pensara sobre todas las páginas virtuales sería inviable; incluso sobre marcos físicos es costoso.
   - **Contadores/timestamps por entrada:** cada página/marco necesita un contador suficientemente grande; también consume memoria y hardware de actualización.
3. **Cálculo orientativo:** 2^20 páginas × N bits por contador. Por ejemplo, con 20 bits por entrada: 2^20 × 20 bits = 20.971.520 bits ≈ 2,5 MB solo para contadores (y todavía hay que actualizarlos en cada acceso).
4. **Conclusión:** es costoso en memoria y lógica de hardware. Por eso se usan aproximaciones: **NRU** (bits R/M) o **Aging/NFU** (contador con desplazamiento).

> [!warning] Cómo responder sin trabarte
> Indicá el número de páginas (2^20), explicá que LRU exacto requiere registrar orden/tiempo de uso por cada entrada, mostrás que escala mal, y proponés Aging/NRU como solución.

---

## E18. Seg+pag: ¿cabe el proceso? (1 KB)

**Contexto.** En segmentación paginada, cada segmento se divide en páginas. Una página no puede contener datos de segmentos distintos; por eso se redondea **hacia arriba por segmento**.

**Caso (Recu 2025 T2):** sistema de 16 bits, páginas de 1 KB. Programa: código 30145 B, datos 18834 B, pila 14870 B. ¿Se puede ejecutar? (se puede asignar todo el direccionamiento de 16 bits al proceso).

1. **Tamaño de página:** 1 KB = 1024 bytes.
2. **Páginas por segmento** (techo):
   - Código: `ceil(30145 / 1024) = ceil(29,438...) = 30` páginas. (29×1024=29696; sobran 449).
   - Datos: `ceil(18834 / 1024) = ceil(18,393...) = 19` páginas. (18×1024=18432; sobran 402).
   - Pila: `ceil(14870 / 1024) = ceil(14,521...) = 15` páginas. (14×1024=14336; sobran 534).
3. **Total:** 30 + 19 + 15 = **64 páginas**.
4. **Espacio direccionable:** 16 bits → 2^16 = 65536 bytes. En páginas de 1 KB: 65536 / 1024 = **64 páginas**.
5. **Comparación:** 64 necesarias ≤ 64 disponibles → **entra justo**.

**Respuesta modelo:** “Sí, se puede ejecutar. Cada segmento se pagina por separado: 30+19+15=64 páginas. El espacio de 16 bits con páginas de 1 KB tiene 64 páginas, por lo tanto entra justo. No sobra espacio, así que cualquier crecimiento requeriría más memoria o swapping.”

> [!warning] Trampa común
> No sumes todos los bytes y después dividas por 1024. Si lo hacés, podés subestimar páginas porque perdés el redondeo por segmento. El redondeo es **por segmento**.

---

## E19. Multinivel 2 niveles de 14 bits, páginas 64 B, 32 GB

**Caso (Recu 2025 T2, Q1).**

**Datos:** 2 niveles de 14 bits cada uno; página de 64 bytes; memoria física de 32 GB.

1. **Offset (acceso interno a la página):** 64 B = 2^6 → **6 bits**.
2. **Bits para tabla de paginación:** 14 + 14 = **28 bits**.
3. **Dirección virtual total:** 28 + 6 = **34 bits**.
4. **Memoria virtual direccionable:** 2^34 = **16 GB**.
5. **Páginas:** 2^28 = **268.435.456 páginas**.
6. **Marcos:** 32 GB / 64 B = 2^35 / 2^6 = **2^29 marcos**.
7. **¿Problema?** Sí: la memoria física (32 GB) es mayor que la memoria direccionable (16 GB). El sistema no puede usar toda la RAM porque le faltan bits de dirección virtual. Además, páginas de 64 B implican muchísimas entradas de tabla.

**Respuesta corta:** “Se usan 28 bits para la tabla y 6 para el offset; se direccionan 16 GB en 2^28 páginas; hay 2^29 marcos, pero no se puede usar toda la memoria física porque la dirección virtual solo cubre 16 GB.”

---

## E20. Caso 64 bits, página 64 B, 32 GB física (tabla lineal inviable)

**Caso (Recu 2025 T2, según OCR; verificar con original).**

**Datos:** dirección virtual 64 bits; página 64 bytes; memoria física 32 GB.

1. **Offset:** 64 B = 2^6 → **6 bits**.
2. **Bits de tabla:** 64 - 6 = **58 bits**.
3. **Páginas virtuales:** 2^58.
4. **Marcos físicos:** 32 GB / 64 B = 2^35 / 2^6 = **2^29 marcos**.
5. **Memoria direccionable:** 2^64 (teórica por arquitectura), pero la tabla lineal tendría 2^58 entradas: inviable.

**Respuesta corta:** “El offset usa 6 bits y la tabla 58; hay 2^58 páginas virtuales y 2^29 marcos. El problema es el tamaño absurdo de la tabla lineal; se resuelve con tabla multinivel o tabla invertida.”

---

## E21. Caso chico: 12 bits, páginas 32 B, 256 B físicos

**Caso (Noviembre 2024, según OCR; verificar con original).**

**Datos:** dirección virtual 12 bits; página 32 bytes; memoria física 256 bytes.

1. **Offset:** 32 B = 2^5 → **5 bits**.
2. **Número de página:** 12 - 5 = **7 bits** → 2^7 = **128 páginas**.
3. **Marcos:** 256 B / 32 B = **8 marcos** → 3 bits de marco.
4. **Memoria direccionable:** 2^12 = **4096 B = 4 KB**.

**Lectura de examen:** aunque el espacio virtual sea chico, solo 8 marcos físicos pueden estar presentes a la vez; hay alta presión de reemplazo si se usan muchas páginas.

**Respuesta corta:** “7 bits para página, 5 para offset, 128 páginas virtuales, 8 marcos físicos y 4 KB direccionables.”

---

## E22. Tabla invertida 64 bits, 8 KB, 16 GB (factor 2)

**Caso (junio/Julio 2024 y modelos OCR similares).**

**Datos:** 64 bits virtuales; página 8 KB; RAM 16 GB; tabla invertida con factor 2.

1. **Offset:** 8 KB = 2^13 → **13 bits**.
2. **Marco:** 16 GB / 8 KB = 2^34 / 2^13 = **2^21 marcos**.
3. **Entradas tabla invertida:** 2 × 2^21 = **2^22 entradas**.
4. **Páginas virtuales (teóricas):** 2^(64-13) = **2^51**. Una tabla directa por proceso sería inviable; por eso se usa invertida.

**Respuesta corta:** “13 bits de offset, 2^21 marcos, 2^22 entradas con factor 2; una tabla directa tendría 2^51 entradas por proceso, por eso conviene tabla invertida.”

---

## Preguntas de teoría que más se repiten (respuesta corta)

- **Programa vs. proceso**: el programa es el archivo ejecutable guardado en disco; el proceso es el programa en ejecución, con su PCB, registros, pila y memoria. El programa se guarda en disco; el proceso vive en memoria. Los datos entre procesos se pasan por **IPC** (memoria compartida, tuberías, mensajes).
- **Estados de un proceso**: nuevo, listo, ejecución, bloqueado y terminado; con swapping aparecen listo/suspendido y bloqueado/suspendido. Transiciones clave: listo→ejecución (planificador), ejecución→listo (quantum/interrupción), ejecución→bloqueado (E/S), bloqueado→listo (fin de E/S). Nunca bloqueado→ejecución directo.

  ![[fuente_estados_proceso.png]]
- **Multiprogramación**: tener varios procesos en memoria para usar la CPU mientras otro espera E/S. Aparece en la 3.ª generación junto con el **spooling**: los trabajos se guardan en disco para que la CPU no espere a los lectores de tarjetas.
- **Máquina virtual**: software que emula una computadora completa (o un proceso) sobre un sistema operativo anfitrión. Ejemplos: VMware, VirtualBox (hipervisor); JVM (máquina virtual de Java); CLR (.NET); emuladores de consolas.
- **Tablas multinivel**: para no tener una tabla de páginas gigante, que ocupa demasiada memoria si se mantiene completa.
- **Tabla invertida**: una entrada por marco físico, no por página virtual; útil con espacios de 64 bits.
- **Monolítico vs. microkernel**: monolítico = todo el SO en modo kernel (rápido, pero frágil). Microkernel = solo lo esencial en kernel (IPC, interrupciones, planificación básica); drivers y servicios en modo usuario (más robusto, pero más lento por paso de mensajes).
- **Creación/fin de procesos**: creación por arranque del sistema, `fork`, solicitud de usuario o trabajo batch; fin por salida normal, error voluntario, error fatal o terminado por otro proceso/SO.
- **Thrashing y conjunto de trabajo**: thrashing ocurre cuando el sistema pasa más tiempo paginando que ejecutando procesos, porque no hay marcos suficientes para los conjuntos de trabajo activos. El conjunto de trabajo (working set) es el conjunto de páginas que un proceso necesita en un intervalo reciente; el SO intenta mantenerlo en memoria.

  ![[slide_working_set_thrashing.png]]

> [!tip] Orden de estudio
> E1 y E3 casi siempre aparecen. Después E4 (Gantt), E5 (invertida), E7 (fallo de página) y E8 (FIFO). Los demás los tenés que saber explicar, pero rara vez son el ejercicio entero.
