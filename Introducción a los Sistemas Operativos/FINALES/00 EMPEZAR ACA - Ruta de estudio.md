---
tipo: ruta
---

# Empezar acá — Ruta de estudio para el final (escrito)

> [!important] Cómo usar esta guía
> Esta es la ruta única para preparar el final. **No hay parte oral: el final es todo escrito.** Seguí el orden de abajo: primero entendés el formato, después teoría mínima, después práctica, y al final simulacro.

## Regla de uso

- **Teoría:** leé primero [[01 Preguntas de teoria|Preguntas de teoría]] e intentá responder por escrito; corregí con [[02 Respuestas detalladas]].
- **Ejercicios:** resolvé primero [[01 Enunciados|Enunciados de ejercicios de finales]]; corregí después con [[02 Resoluciones detalladas]].
- **No saltear el orden:** si un ejercicio te sale mal, volvé a la pregunta/respuesta de teoría correspondiente antes de seguir.

## Dónde está cada cosa

| Necesitás | Carpeta / archivo | Cómo leerlo |
|---|---|---|
| Preguntas de teoría | [[Teoria/01 Preguntas de teoria\|Teoria/01 Preguntas de teoria]] | Leelas y respondelas por escrito |
| Respuestas de teoría | [[Teoria/02 Respuestas detalladas\|Teoria/02 Respuestas detalladas]] | Corrección detallada, en el mismo orden |
| Ejercicios de finales | [[Ejercicios de finales/01 Enunciados\|Ejercicios de finales/01 Enunciados]] | Intentá resolver sin mirar |
| Resoluciones de ejercicios | [[Ejercicios de finales/02 Resoluciones detalladas\|Ejercicios de finales/02 Resoluciones detalladas]] | Corrección paso a paso, en el mismo orden |
| Plan y estrategia | [[00 Cómo atacar el final (plan)]] · [[04 Plan de estudio (cronograma)]] | Contexto y tiempos |
| Mapa de cobertura | [[05 Mapa pregunta a subtema]] | Para ubicar tema ↔ práctica ↔ teoría |
| Modelos revisados | [[06 Modelos de final revisados]] | Qué apareció en exámenes/modelos |

## Planificación propuesta (con lo que hay que estudiar)

### Opción A — Plan 7 días (recomendado)

| Día | Teoría (responder por escrito) | Práctica (enunciado → resolución) | Objetivo |
|---|---|---|---|
| **1** | Sección A: SO, kernel/modo, syscalls, interrupciones, DMA, spooling, VM, monolítico/microkernel | E1, E14 (bits/casos trampa) | Base conceptual + cálculo de bits |
| **2** | Sección B: proceso/PCB/estados, planificación, $U=1-p^n$, sincronización | E3, E4, E16 (multiprogramación y Gantt) | Dominar U=1-p^n y Gantt |
| **3** | Sección C: fragmentación, bitmap/listas, first/next/best/worst, compactación, buddy/quick fit | E9, E10, E11 | Memoria contigua sin confundir criterios |
| **4** | Sección D: paginación, traducción, fallo de página, TLB, tamaño óptimo | E2, E7, E15, E21 | Traducción y fallos de página |
| **5** | Sección D: FIFO/reloj/NRU/LRU/Aging, Belady, working set/thrashing | E8, E13 | Algoritmos de reemplazo con criterio |
| **6** | Sección E: multinivel, invertida, segmentación, seg+pag | E5, E6, E17, E18, E19, E20, E22 | Tablas avanzadas y segmentación |
| **7** | Sección F + repaso de trampas | Simulacro escrito: 2 teoría + 2 ejercicios cronometrados | Detectar huecos y corregir |

### Opción B — Plan 3 días (intensivo)

| Día | Teoría | Práctica | Objetivo |
|---|---|---|---|
| **1** | Secciones A, B y D (núcleo): syscalls, procesos/estados, U=1-p^n, paginación, fallos, reemplazo | E1, E3, E4, E7, E8 | Cubrir lo más frecuente |
| **2** | Secciones C y E: fragmentación, asignación, bitmap/listas, tamaño óptimo, multinivel/invertida, segmentación | E2, E5, E6, E9, E10, E18 | Completar ejercicios de memoria |
| **3** | Sección F + trampas + mapa de cobertura | Simulacro escrito completo y corrección con resoluciones | Cerrar con método de examen |

## Secuencia estricta de estudio

### Fase 1 — Orientación (30–45 min)
1. [[00 Cómo atacar el final (plan)]] — formato del final escrito y plantilla de respuesta.
2. [[01 Temas que más se repiten]] — priorizá por frecuencia.
3. [[04 Plan de estudio (cronograma)]] — elegí plan 7 días o 3 días.

### Fase 2 — Teoría mínima (en orden)
Estudiá por secciones de [[01 Preguntas de teoria|Preguntas de teoría]] y corregí con [[02 Respuestas detalladas]]:
1. **A. Base del SO:** SO, modo kernel/usuario, syscalls, interrupciones, DMA, spooling, multiprogramación, VM, monolítico/microkernel.
2. **B. Procesos:** programa/proceso, PCB, estados, creación/fin, planificación, $U=1-p^n$, sincronización.
3. **C. Memoria básica:** fragmentación, bitmap/listas, first/next/best/worst, compactación, buddy/quick fit, dirección lógica/física.
4. **D. Paginación:** página/marco/MMU, traducción, bits, fallo de página, TLB, reemplazo, Belady, tamaño óptimo, working set/thrashing.
5. **E. Tablas avanzadas:** multinivel, invertida, segmentación, segmentación paginada.
6. **F. Trampas:** 5 KB, LRU por hardware, DMA/spooling, $p_i$ distintos, checklist numérico.

### Fase 3 — Práctica (obligatoria)
1. **Hacé enunciados primero:** [[01 Enunciados|Ejercicios de finales — Enunciados]].
2. **Corregí en el mismo orden:** [[02 Resoluciones detalladas|Ejercicios de finales — Resoluciones detalladas]].
3. **Si fallás un ejercicio:** volvé a la pregunta de teoría correspondiente (usar [[05 Mapa pregunta a subtema]]).
4. **Revisá modelos reales:** [[06 Modelos de final revisados]] para reconocer cómo preguntan.

### Fase 4 — Cierre (antes del final)
1. Repasá la **Sección F: trampas** en [[02 Respuestas detalladas]].
2. Hacé un **simulacro escrito**: 2 preguntas de teoría + 2 ejercicios, con tiempo.
3. Corregí con método: definición, pasos, resultado, unidad, trampa.

## Checklist antes de rendir

- [ ] Sé explicar kernel/modo usuario/syscall/interrupción/DMA/spooling.
- [ ] Sé explicar proceso, PCB, estados y transiciones (sin bloqueado→ejecución directo).
- [ ] Sé calcular $U=1-p^n$ y hacer Gantt recalculando al llegar/terminar procesos.
- [ ] Sé calcular desplazamiento, bits de página, páginas, marcos y dirección física.
- [ ] Sé resolver fallos de página y elegir víctima por FIFO/reloj/NRU/LRU/Aging.
- [ ] Sé calcular tamaño óptimo $s=\sqrt{2PE}$.
- [ ] Sé distinguir fragmentación interna/externa y first/next/best/worst.
- [ ] Sé explicar/armar tabla multinivel y tabla invertida.
- [ ] Sé explicar segmentación vs paginación vs segmentación paginada.
- [ ] Puedo responder por escrito con: definición, desarrollo, ejemplo/trampa.

## Material de respaldo (solo si hace falta)

- [[00 Índice de la materia]] y `Complementario/MATERIA-COMPLETA/` — teoría completa.
- `Complementario/OCR/` — exámenes escaneados/OCR; pueden tener errores, contrastar con la fuente.
