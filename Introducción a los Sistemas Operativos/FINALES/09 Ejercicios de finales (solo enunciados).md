---
tipo: ejercicios
---

# Ejercicios de finales (solo enunciados)

> [!abstract] Para qué es esta nota
> Compilado condensado de ejercicios obtenidos de finales/parciales/modelos revisados. Acá están **solo los enunciados**; las resoluciones paso a paso están en [[10 Ejercicios de finales (resoluciones)]].

## Índice

- E1. Bits, páginas y marcos
- E2. Tamaño óptimo de página `s = √(2PE)`
- E3. Multiprogramación: `U = 1 − p^n`
- E4. Gantt con E/S del 50%
- E5. Tabla de páginas invertida
- E6. Tabla multinivel
- E7. Fallo de página
- E8. FIFO, segunda oportunidad y anomalía de Belady
- E9. Asignación de memoria: first/next/best/worst fit
- E10. Fragmentación interna y externa
- E11. Mapa de bits vs. listas enlazadas
- E12. Multiprogramación y spooling (teoría)
- E13. NRU, LRU y Aging
- E14. Casos trampa de bits
- E15. Traducción de dirección con tabla
- E16. Gantt con E/S del 60% y 90%
- E17. LRU por hardware: costo de memoria
- E18. Segmentación con paginación: ¿cabe el proceso?
- E19. Multinivel 2×14 bits, páginas 64 B, 32 GB
- E20. 64 bits, página 64 B, 32 GB física
- E21. 12 bits, páginas 32 B, 256 B físicos
- E22. Tabla invertida 64 bits, 8 KB, 16 GB (factor 2)

---

## E1. Bits, páginas y marcos

**Caso A (Parcial 2025 T2).** Sistema de 64 bits, páginas de 8 KB, memoria física de 32 GB. Calcular: bits de desplazamiento, bits de página, cantidad de páginas virtuales, cantidad de marcos físicos y memoria direccionable.

**Caso B (2T Feb 2025).** Sistema de 31 bits, 13 bits de desplazamiento. Calcular: tamaño de página, cantidad de páginas, cantidad de marcos con 512 MB de RAM, tamaño de la tabla de páginas tradicional con entradas de 4 bytes.

**Caso C (1T Feb 2024).** Dada una tabla de páginas de 8 bits (según el modelo), determinar memoria direccionable, bits para acceso a página, cantidad de páginas, tamaño de memoria física si está llena y cantidad de marcos.

---

## E2. Tamaño óptimo de página

**Fórmula:** `s = √(2PE)`, donde `P` es el tamaño promedio del proceso y `E` el tamaño de cada entrada de la tabla de páginas.

**Caso A (Parcial 2025 T1).** `P = 8 KB`, `E = 4 B`. Calcular el tamaño óptimo de página.

**Caso B (Parcial 2025 T2).** `P = 1 KB`, `E = 8 B`. Calcular el tamaño óptimo de página.

**Pregunta teórica.** ¿Qué factores inciden en la decisión del tamaño de página? ¿Cómo se modela matemáticamente y cómo se obtiene la fórmula?

---

## E3. Multiprogramación: `U = 1 − p^n`

**Caso A (Modelos).** Fracción de espera de E/S `p = 0,75`. ¿Cuántos procesos se necesitan para alcanzar una utilización de CPU del 90%?

**Caso B (Parcial 2025).** `p = 0,5` y 3 procesos en memoria. Calcular la utilización de CPU.

**Caso C.** Si los procesos tienen esperas distintas, por ejemplo `p1 = 0,5` y `p2 = 0,9`, calcular la utilización de CPU del sistema.

---

## E4. Gantt con E/S del 50%

Usar la convención: con `n` procesos, `U = 1 − p^n` y cada proceso avanza `U/n` de CPU por minuto de reloj mientras `n` no cambie. Recalcular en cada llegada o finalización.

**Caso A (Parcial 2025 T1, `p = 0,5`).**

| Proceso | Llega | CPU |
|---|---:|---:|
| P1 | 12:00 | 2 min |
| P2 | 12:01 | 5 min |
| P3 | 12:15 | 3,5 min |

Determinar el momento de finalización de cada proceso y dibujar el Gantt.

**Caso B (Parcial 2025 T2, `p = 0,5`).**

| Proceso | Llega | CPU |
|---|---:|---:|
| P1 | 17:00 | 9 min |
| P2 | 17:15 | 2,5 min |
| P3 | 17:23 | 2 min |

Determinar el momento de finalización de cada proceso y dibujar el Gantt.

**Caso C (Resumen SAE, `p = 0,8`).**

| Trabajo | Llega | CPU requerida |
|---|---:|---:|
| 1 | 10:00 | 4 min |
| 2 | 10:10 | 4 min |
| 3 | 10:15 | 4 min |
| 4 | 10:20 | 4 min |

Calcular la evolución y tiempos de finalización aplicando el reparto round robin por multiprogramación.

---

## E5. Tabla de páginas invertida

**Caso A (Final julio 2024).** 64 bits, páginas de 8 KB, memoria física de 16 GB, tabla invertida con factor 2. Calcular entradas/páginas sin tabla invertida y con tabla invertida.

**Caso B (Parcial 2025 T1).** 64 bits, páginas de 16 KB, memoria física de 64 GB. Calcular desplazamiento, marcos, bits para acceder a la tabla invertida, páginas virtuales, memoria direccionable y memoria usable.

**Pregunta teórica.** ¿Qué es la TLB y por qué acelera la traducción?

---

## E6. Tabla multinivel

**Caso A (Final julio 2024).** 32 bits, páginas de 4 KB, dos niveles de 10 bits. Explicar la estructura, cantidad de tablas/subtablas y por qué se introduce.

**Caso B (1T Feb 2025).** 32 bits, páginas de 16 KB, 3 niveles de 6 bits. Calcular desplazamiento, bits de página, cantidad de páginas y cantidad de tablas/subtablas.

---

## E7. Fallo de página

**Enunciado.** Explicar qué es un fallo de página y describir los pasos que realiza el SO cuando ocurre un fallo de página, considerando que todos los marcos de memoria están ocupados.

Incluir: trap al SO, elección de víctima, bit M, escritura a disco si corresponde, carga de página, actualización de tabla y reinicio de instrucción.

---

## E8. FIFO, segunda oportunidad y anomalía de Belady

**Caso A (Parcial 2025 T1/T2).** ¿Cuál es el problema del algoritmo FIFO (o FIFO con bit R)? ¿Qué algoritmo lo soluciona y por qué?

**Caso B.** Explicar la anomalía de Belady con la secuencia clásica `1,2,3,4,1,2,5,1,2,3,4,5` comparando 3 marcos vs 4 marcos en FIFO.

**Pregunta teórica.** ¿Por qué el algoritmo del reloj es una implementación eficiente de la segunda oportunidad?

---

## E9. Asignación de memoria: first, next, best y worst fit

**Caso (TP2-4).** Huecos libres: 800, 300, 1500, 600, 700, 1000, 1200. Llegan procesos de 1000, 800 y 700. Asignar usando first fit, best fit, worst fit y next fit.

**Pregunta teórica.** Mencionar también Quick Fit y Buddy System: ventaja y desventaja.

---

## E10. Fragmentación interna y externa

**Enunciado.** Definir fragmentación interna y fragmentación externa. Dar un ejemplo numérico de cada una. Indicar en qué esquemas de administración de memoria aparece cada una y cómo se mitiga.

---

## E11. Mapa de bits vs. listas enlazadas

**Enunciado.** Explicar cómo administra la memoria un mapa de bits y cómo lo hace una lista enlazada. Comparar velocidad, uso de memoria y facilidad para encontrar huecos/fusionar.

**Caso (Final julio 2024).** ¿Qué registra la administración por listas enlazadas? ¿Es más fácil encontrar un hueco con listas enlazadas o con mapa de bits? Justificar.

---

## E12. Multiprogramación y spooling

**Enunciado.** ¿Qué es la multiprogramación? ¿En qué generación se incorpora? ¿Qué relación tiene con el spooling? ¿Por qué sigue siendo importante actualmente?

---

## E13. NRU, LRU y Aging

**Enunciado.** Explicar NRU, LRU y Aging/NFU. Incluir: bits R y M, clases de NRU, matriz o costo de LRU, y mecanismo de envejecimiento de Aging.

**Pregunta.** ¿Qué problema tiene LRU exacto y qué aproximaciones lo solucionan?

---

## E14. Casos trampa de bits

**Caso A (Parcial 2024 T2).** 36 bits, páginas de **5 KB**, memoria física 16 GB. ¿Qué problema hay?

**Caso B (Final 11-12-2024).** 9 bits de dirección virtual, páginas de 8 bytes, memoria física de 2 GB. Calcular desplazamiento, bits de página, páginas, marcos, memoria direccionable y si se puede usar toda la RAM.

**Caso C (Recu 2024 T1 / Final 11-12-2024).** 52 bits de dirección virtual, páginas de 2 KB. Calcular páginas y explicar el problema de la tabla lineal y sus soluciones.

---

## E15. Traducción de dirección con tabla

**Caso (Final 27-11-2024 / TP3-3).** Sistema de 16 bits, páginas de 4 KB. Dirección virtual = 20500. La página 5 está en el marco 3 (según tabla). Calcular: número de página, desplazamiento, verificación, representación binaria, marco y dirección física.

---

## E16. Gantt con E/S del 60% y 90%

**Caso A (1T Febrero 2024, `p = 0,6`).**

| Proceso | Llega | CPU |
|---|---:|---:|
| P1 | 13:00 | 2,32 min |
| P2 | 13:05 | 2,32 min |
| P3 | 13:12 | 4,00 min |

Calcular el momento de finalización de cada proceso.

**Caso B (Recu 2024 Tema 1, `p = 0,9`).**

| Proceso | Llega | CPU |
|---|---:|---:|
| A | 15:00 | 1,38 min |
| B | 15:10 | 1,38 min |

Calcular el momento de finalización de cada proceso.

---

## E17. LRU por hardware: costo de memoria

**Caso (Recu 2025 T2).** Sistema de 32 bits, páginas de 4 KB. ¿Cuánta memoria/estructura necesita LRU por hardware para llevar registro de uso reciente? Explicar por qué es costoso y qué aproximaciones se usan.

---

## E18. Segmentación con paginación: ¿cabe el proceso?

**Caso (Recu 2025 T2).** Sistema de 16 bits, páginas de 1 KB. Programa: código 30145 B, datos 18834 B, pila 14870 B. Se puede asignar todo el direccionamiento de 16 bits al proceso. Una página no puede contener datos de diferentes segmentos. ¿Se puede ejecutar el programa? Justificar numéricamente.

---

## E19. Multinivel 2×14 bits, páginas 64 B, 32 GB

**Caso (Recu 2025 T2, Q1).** 2 niveles de 14 bits cada uno; página de 64 bytes; memoria física de 32 GB. Calcular: offset, bits de tabla, dirección virtual total, memoria virtual direccionable, cantidad de páginas, cantidad de marcos y problema existente.

---

## E20. 64 bits, página 64 B, 32 GB física

**Caso (Recu 2025 T2, según OCR; verificar con original).** Dirección virtual 64 bits; página 64 bytes; memoria física 32 GB. Calcular offset, bits de tabla, páginas virtuales, marcos físicos y memoria direccionable. Indicar el problema de la tabla lineal.

---

## E21. 12 bits, páginas 32 B, 256 B físicos

**Caso (Noviembre 2024, según OCR; verificar con original).** Dirección virtual 12 bits; página 32 bytes; memoria física 256 bytes. Calcular offset, bits de página, cantidad de páginas, cantidad de marcos y memoria direccionable.

---

## E22. Tabla invertida 64 bits, 8 KB, 16 GB (factor 2)

**Caso (junio/Julio 2024 y modelos OCR similares).** 64 bits virtuales; página 8 KB; RAM 16 GB; tabla invertida con factor 2. Calcular offset, marcos, entradas de tabla invertida y páginas virtuales teóricas. Explicar por qué conviene tabla invertida.

---

## Preguntas teóricas de apoyo

- Programa vs. proceso; dónde se almacenan; cómo se pasan datos (IPC).
- Estados de un proceso y transiciones; estados con swapping.
- Multiprogramación y spooling: definición, generación, relación e importancia.
- Máquina virtual: hipervisor, JVM/CLR.
- Tablas multinivel e invertida: para qué se usan.
- Monolítico vs. microkernel.
- Creación y fin de procesos.
- Thrashing y conjunto de trabajo.
