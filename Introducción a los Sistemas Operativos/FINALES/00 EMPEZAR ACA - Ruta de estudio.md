---
tipo: ruta
---

# Empezar acá — Ruta de estudio para el final (escrito)

> [!abstract] Objetivo
> Esta es la guía única para estudiar el final en orden. Seguí la ruta de arriba hacia abajo. No hace falta leer todo el material complementario: enfocáte en esta secuencia.

## Cómo usar esta ruta

1. **Leé la teoría mínima** del bloque.
2. **Hacé la práctica** indicada (primero intentá vos, después mirá la resolución).
3. **Marcá lo que te costó** y volvé a ese punto antes del simulacro.
4. Si necesitás profundizar teoría: usá `Complementario/MATERIA-COMPLETA/`.

---

## Plan recomendado (7 días)

| Día | Bloque | Estudiar | Practicar |
|---:|---|---|---|
| 1 | Fundamentos de SO | [[01 Temas que más se repiten]] (sección SO/procesos) + [[05 Mapa pregunta a subtema]] (filas 1,2,3,7) | Preguntas núcleo 7,8,9 de [[00 Cómo atacar el final (plan)]]; explicalas por escrito |
| 2 | Procesos y multiprogramación | Núcleo 1 y 9: modelo `U=1-p^n`, estados, PCB | [[09 Ejercicios de finales (solo enunciados)]] E3,E4,E16 → corregir en [[10 Ejercicios de finales (resoluciones)]] |
| 3 | Memoria contigua | Núcleo 2 y 10: fragmentación, asignación, bitmap/listas | [[09 Ejercicios de finales (solo enunciados)]] E9,E10,E11 → corregir en [[10 Ejercicios de finales (resoluciones)]] |
| 4 | Paginación y direcciones | Núcleo 3: bits, páginas, marcos, traducción, tamaño óptimo | [[09 Ejercicios de finales (solo enunciados)]] E1,E2,E14,E15 → corregir en [[10 Ejercicios de finales (resoluciones)]] |
| 5 | Fallos y reemplazo | Núcleo 4 y 5: fallo de página, FIFO, reloj, NRU, LRU, aging | [[09 Ejercicios de finales (solo enunciados)]] E7,E8,E13,E17 → corregir en [[10 Ejercicios de finales (resoluciones)]] |
| 6 | Tablas avanzadas y segmentación | Núcleo 6 + tablas multinivel/invertida + segmentación paginada | [[09 Ejercicios de finales (solo enunciados)]] E5,E6,E18,E19,E20,E21,E22 → corregir en [[10 Ejercicios de finales (resoluciones)]] |
| 7 | Simulacro escrito | Repaso de trampas y preguntas destacadas | [[02 Preguntas destacadas (aparecieron una vez)]] + hacer 5 ejercicios al azar de 09 y corregir con 10 |

## Plan corto (3 días)

| Día | Foco | Hacer |
|---:|---|---|
| 1 | Núcleo | Las 10 preguntas núcleo de [[00 Cómo atacar el final (plan)]] + [[01 Temas que más se repiten]] |
| 2 | Cálculos | E1,E2,E3,E4,E5,E6,E14,E15,E16 de [[09 Ejercicios de finales (solo enunciados)]] → corregir con [[10 Ejercicios de finales (resoluciones)]] |
| 3 | Algoritmos y simulacro | E7,E8,E9,E10,E13,E18 + [[02 Preguntas destacadas (aparecieron una vez)]] + simulacro escrito cronometrado |

---

## Secuencia estricta de estudio (orden sugerido)

### Fase 1 — Orientación (30-45 min)
1. [[00 Cómo atacar el final (plan)]] — entendé el formato, las 10 preguntas núcleo y los errores típicos.
2. [[01 Temas que más se repiten]] — priorizá lo que más cae.
3. [[04 Plan de estudio (cronograma)]] — elegí plan 7 días o 3 días.

### Fase 2 — Teoría mínima que hay que saber explicar por escrito
4. **Syscalls, kernel/usuario, shell**: núcleo 7 y 8 del plan. Apoyo: [[05 Mapa pregunta a subtema]].
5. **Procesos, PCB, estados, transiciones**: núcleo 9.
6. **Multiprogramación y `U=1-p^n`**: núcleo 1.
7. **Memoria contigua, fragmentación, asignación, bitmap/listas**: núcleos 2 y 10.
8. **Paginación, bits, dirección física, fallo de página**: núcleos 3 y 4.
9. **Reemplazo de páginas**: núcleo 5.
10. **Tamaño óptimo de página**: núcleo 6.
11. **Tablas multinivel/invertida, segmentación paginada**: temas de alta frecuencia en modelos.

> [!note] Dónde profundizar
> Si un tema no te cierra, buscá el subtema correspondiente en `Complementario/MATERIA-COMPLETA/00 Índice de la materia.md`. No hace falta leer toda la materia completa de corrido.

### Fase 3 — Práctica obligatoria (hacer en este orden)
12. [[09 Ejercicios de finales (solo enunciados)]] — **intentá primero sin mirar**.
13. [[10 Ejercicios de finales (resoluciones)]] — corregí con pasos, resultado y trampa.
14. [[08 Ejercicios frecuentes paso a paso]] — para ver el desarrollo detallado de los ejercicios más comunes.
15. [[07 Ejercicios de los modelos (resueltos)]] — casos extraídos de modelos.
16. [[03 Ejercicios tipo con resultado]] — verificación rápida.

### Fase 4 — Cierre y simulacro
17. [[02 Preguntas destacadas (aparecieron una vez)]] — cubrir sorpresas.
18. [[06 Modelos de final revisados]] — ver qué trae cada modelo real.
19. **Simulacro escrito**: elegí 5 ejercicios de 09 + 3 preguntas teóricas, resolvé en 60–90 min, corregí con 10.

---

## Checklist antes del final

- [ ] Sé calcular bits de página, desplazamiento, marcos y dirección física.
- [ ] Sé aplicar `U = 1 - p^n` y resolver Gantt con llegadas.
- [ ] Sé explicar fallo de página en orden.
- [ ] Sé comparar FIFO, reloj/segunda oportunidad, NRU, LRU, Aging.
- [ ] Sé calcular tamaño óptimo `s = sqrt(2PE)`.
- [ ] Sé resolver tabla multinivel e invertida.
- [ ] Sé detectar trampas: página no potencia de 2, usar toda la RAM física, tabla lineal inviable.
- [ ] Sé explicar fragmentación interna/externa, bitmap/listas, asignación contigua.

## Material de respaldo (solo si lo necesitás)

- [[00 Índice de la materia]] — teoría completa por subtema.
- [[Materia completa (las 4 unidades en un archivo)]] — lectura de corrido.
- `Complementario/OCR/` — textos OCR de exámenes (pueden tener errores).
- `FINALES/Gráficos/` — diagramas y figuras.
