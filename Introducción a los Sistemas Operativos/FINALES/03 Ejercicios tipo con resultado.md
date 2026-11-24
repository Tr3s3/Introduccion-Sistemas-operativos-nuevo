---
tipo: ejercicios
---
# Ejercicios tipo con resultado

> [!abstract] Cómo usar esta nota
> Cada bloque es un **tipo de ejercicio** con su procedimiento y el resultado de los casos de la cátedra. Los resultados están recalculados; cuando hay una ambigüedad en el enunciado, se indica. Para la teoría de cada uno, ver el subtema enlazado.

## 1. Dirección virtual → física (paginación)
**Procedimiento:** (1) desplazamiento = dirección mod tamaño de página; (2) número de página = división entera; (3) si V = 0 → fallo de página; (4) física = marco × tamaño + desplazamiento.
Caso TP3-3 (páginas de 2 KB; página 1 → marco 4; página 2 → marco 7):
- (1, 481) → 4 × 2048 + 481 = **8673**
- (2, 1324) → 7 × 2048 + 1324 = **15660**
- (5, 122), (3, 2051) → **fallo de página** (la página no está en RAM; en (3, 2051) además el desplazamiento supera 2048)
- (9, 21) → **fuera de la tabla**

Teoría: [[4.1.2 Paginación y la MMU]].

## 2. Dirección virtual → física (segmentación)
**Procedimiento:** si desplazamiento < longitud → base + desplazamiento; si no, **trampa**.
Caso TP3-10: (0, 230) → **253** · (1, 2) → **352** · (2, 699) → **2399** · (1, 602), (3, 400), (4, 700) → **fuera del segmento**.

Teoría: [[4.6.1 Segmentación]].

## 3. Bits de una dirección
**Procedimiento:** desplazamiento = log₂(página); bits de página = total − desplazamiento; páginas = 2^(bits de página); marcos = física ÷ página.
- 42 bits, 8 KB, 8 GB → 13 · 29 · 2²⁰ marcos.
- 64 bits, 8 KB, 32 GB → 13 · 51 · 2²² marcos.
- 16 bits, 4 KB → dirección 12 315 está en la **página 3**, desplazamiento **27** (12 315 = 3 × 4096 + 27).

Teoría: [[4.1.3 Cálculo de bits, páginas y marcos]].

## 4. Tamaño óptimo de página
s = √(2PE). Caso: P = 8 KB, E = 4 bytes → **256 bytes**. Caso: P = 2 MB, E = 16 bytes → **8 KB**.
Teoría: [[4.5.1 Tamaño de página óptimo — s = √(2PE)]].

## 5. Reemplazo de páginas (con tabla de tiempos)
**Procedimiento:**
- **FIFO:** la página con **menor tiempo de carga**.
- **LRU:** la página con **menor tiempo de última referencia**.
- **NRU:** la página de **clase más baja** (R, M): 0 = (0,0), 1 = (0,1), 2 = (1,0), 3 = (1,1).
- **Reloj:** puntero circular; si R = 0 reemplaza, si R = 1 pone R = 0 y avanza.

Caso TP3-8 (cuatro páginas en RAM, en marcos 3, 1, 2 y 4):

| Página | Marco | Carga | Última ref. | M | R |
|---|---|---|---|---|---|
| 0 | 3 | 3200 | 5600 | 1 | 1 |
| 1 | 1 | 2400 | 5440 | 1 | 0 |
| 3 | 2 | 2600 | 5200 | 0 | 1 |
| 4 | 4 | 2520 | 5580 | 0 | 0 |

- **NRU → página 4** (clase 0: R = 0, M = 0).
- **FIFO → página 1** (la más antigua, carga 2400).
- **LRU → página 3** (última referencia más vieja, 5200).
- **Reloj → página 1** si el puntero arranca en la más antigua (R = 0). Decilo como supuesto.
- **Inconsistencia a señalar:** hay **5 marcos** pero **4 páginas** en memoria, y el marco 0 no aparece asignado; además, la página 2 figura con tiempos en 0. Confirmalo con la cátedra.

Teoría: [[4.4.1 Óptimo, FIFO y anomalía de Belady]] · [[4.4.2 Segunda oportunidad y algoritmo del reloj]] · [[4.4.3 NRU, LRU y aging]].

## 6. Asignación contigua (first, next, best, worst)
Caso TP2-4 (huecos 800, 300, 1500, 600, 700, 1000, 1200; procesos 1000, 800, 700):
- First fit: 1500 · 800 · 700
- Next fit: 1500 · 1000 · 1200
- Best fit: 1000 · 800 · 700 (todos exactos)
- Worst fit: 1500 · 1200 · 1000

Teoría: [[3.5.1 Primer ajuste, próximo ajuste, mejor ajuste y peor ajuste]].

## 7. Modelo probabilístico
**U = 1 − pⁿ.** Para saber n mínimo con U ≥ objetivo: pⁿ ≤ 1 − objetivo.
- p = 0,5, objetivo 90 % → n = **4**.
- p = 0,75, n = 4 → U = 68,4 %; desperdicio **31,6 %** (TP2-6).
- p = 0,7, n = 3 → 65,7 %; n = 5 → 83,2 % (aumento de 26,6 % al agregar memoria, TP2-7).
- Si cada proceso tiene **p distinto**, U = 1 − ∏pᵢ. Ejemplo: p = 0,5 y 0,9 → U = 1 − 0,45 = **55 %**.

**Gantt SAE (p = 0,8, 4 trabajos, llegadas 10:00/10:10/10:15/10:20, 4 min de CPU c/u):**
- 10:00–10:10, n=1, U=0,2: T1 avanza 2,0.
- 10:10–10:15, n=2, U=0,36, 0,18 c/u: T1 queda 1,1; T2 queda 3,1.
- 10:15–10:20, n=3, U=0,488, 0,1627 c/u: T1 queda ~0,287; T2 ~2,287; T3 ~3,187.
- 10:20+, n=4, U=0,5904, 0,1476 c/u: T1 termina ~10:21:56; luego recalcular con n=3.

> [!note] Regla del Gantt
> En cada intervalo, velocidad por proceso = U/n minutos de CPU por minuto de reloj. Al terminar o llegar un proceso, se recalcula n y U.

Teoría: [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]]. Pasos detallados: [[08 Ejercicios frecuentes paso a paso]].

## 8. Round Robin: sobrecarga por cambio de contexto
Sobrecarga = cambio / (cambio + quantum). Caso: 6 ms y 25 ms → 6 / 31 ≈ **19,4 %**.
Teoría: [[2.4.2 FIFO, SJF y Round Robin (quantum)]].

## 9. Tiempo medio de acceso con jerarquía de memoria (TP1-19)
t = h₁·t₁ + (1 − h₁)·[h₂·t₂ + (1 − h₂)·t₃]
= 0,93 · 1,5 + 0,07 · [0,97 · 7 + 0,03 · 6 000 000] ns
= 1,395 + 0,07 · [6,79 + 180 000] ns ≈ **12 602 ns ≈ 12,6 µs**.

> [!note] Supuesto
> El cálculo asume que cada nivel se consulta solo si falla el anterior y que los tiempos son de acceso total (no de transferencia). Decilo.

Teoría: [[1.4.3 E-S programada, interrupciones, DMA]] (la jerarquía) y [[4.2.1 TLB (memoria asociativa)]] (la misma fórmula con TLB).

## 10. Hilos y procesos en paralelo (TP1-18)
Dos CPU × dos hilos = 4 hilos para 3 programas de 5, 10 y 20 ms, sin bloqueos ni cambio de CPU: cada uno corre en su hilo y el total es **20 ms** (el más largo). Si el enunciado diera penalidad por compartir núcleo, cambia.

## 11. Fragmentación (TP2-1 y 3)
Caso: huecos de 10, 5 y 12 KB (total 27 KB) y llega un proceso de 20 KB → no entra: **fragmentación externa**. Caso: bloque de 128 KB para 100 KB → **28 KB de fragmentación interna**.
Teoría: [[3.3.3 Fragmentación interna y externa]].

> [!tip] Antes de empezar cualquier cálculo
> Escribí la **fórmula** y los **datos** con unidades. Los errores más comunes son de unidad (KB vs. bytes, palabras vs. bytes) y de bits (total vs. de página).
