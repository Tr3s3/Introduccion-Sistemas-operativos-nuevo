---
tipo: indice
unidad: 4
---
# Unidad 4 — Memoria virtual

> [!abstract] Qué pide la unidad
> Cómo el SO permite ejecutar procesos más grandes que la memoria física: paginación, MMU, TLB, fallos de página, reemplazo, tamaño de página, working set/thrashing, segmentación y segmentación paginada.

> [!tip] Fuente principal
> Desarrollada con base en las **diapositivas de cátedra** “Administración de Memoria Virtual” (66 diapositivas; ver [[00 Fuente - Temario de diapositivas]] y `_slides/Unidad 4/`). Se complementa con explicación, ejemplos, trampas de examen y libro (Tanenbaum).

> [!tip] Para leer toda la unidad de corrido
> [[Unidad 4 — completa (lectura de corrido)]].

## Temas y subtemas

### Tema 4.1 — Concepto y paginación
- [[4.1.1 Memoria virtual y overlays]]
- [[4.1.2 Paginación y la MMU]]
- [[4.1.3 Cálculo de bits, páginas y marcos]]

### Tema 4.2 — Traducción rápida y tablas de páginas
- [[4.2.1 TLB (memoria asociativa)]]
- [[4.2.2 Tablas multinivel e invertidas]]

### Tema 4.3 — Fallo de página
- [[4.3.1 Pasos de un fallo de página]]
- [[4.3.2 Reinicio de la instrucción y páginas compartidas]]

### Tema 4.4 — Algoritmos de reemplazo de páginas
- [[4.4.1 Óptimo, FIFO y anomalía de Belady]]
- [[4.4.2 Segunda oportunidad y algoritmo del reloj]]
- [[4.4.3 NRU, LRU y aging]]

### Tema 4.5 — Tamaño de página y rendimiento
- [[4.5.1 Tamaño de página óptimo — s = √(2PE)]]
- [[4.5.2 Conjunto de trabajo y thrashing]]

### Tema 4.6 — Segmentación y esquemas combinados
- [[4.6.1 Segmentación]]
- [[4.6.2 Segmentación con paginación y su combinación]]

---
[[00 Índice de la materia]] · [[Unidad 4 — completa (lectura de corrido)]]
