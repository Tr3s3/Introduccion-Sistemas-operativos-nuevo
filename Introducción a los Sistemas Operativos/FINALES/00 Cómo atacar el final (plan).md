---
tipo: estrategia
---
# Cómo atacar el final: plan de estudio por frecuencia

> [!abstract] La idea
> El final de Introducción a los SO mezcla **teoría escrita** (definir, explicar un mecanismo, comparar) y **ejercicios de cálculo** (bits de dirección, fallos de página, algoritmos de asignación, modelo probabilístico). Las preguntas **se repiten**: de los 35 parciales posibles, unas 15 aparecen en varias fuentes y el resto son variaciones. Estudiar **por patrón** (no por pregunta) ahorra tiempo.

## Las fuentes que usamos
| Código | Fuente |
|---|---|
| **TP1, TP2, TP3** | Trabajos prácticos 2018/2022 de la cátedra |
| **PP** | *PreguntasPosibles_Parciales* (35 preguntas) |
| **RS** | *RepasoISO* (multiprogramación, paginación, LRU, NRU, spooling) |
| **SAE** | *ResumenISOSAE1* (resumen de SO y memoria virtual, ejemplo de multiprogramación) |
| **Cát** | Presentaciones de la cátedra (Introducción, Procesos y memoria, Administración de memoria virtual) |
| **Tan** | Tanenbaum, *Sistemas Operativos Modernos*, caps. 1, 2 y 3 (memoria virtual) |

> [!note] Material integrado en esta revisión
> Se incorporaron los PDFs adjuntos (**PP**, **RS**, **SAE**) para reforzar definiciones, ejemplos y casos de final. Los gráficos con prefijo `fuente_` en `FINALES/Gráficos/` son extractos de diapositivas/libro y están embebidos en los ejercicios donde aportan contexto.

## Las 10 preguntas núcleo (si solo tenés una semana)
Estas son las que, combinadas, cubren la mayoría de lo que se pregunta:

1. **Multiprogramación y modelo U = 1 − pⁿ** → con ejemplo de 50 % y 90 %. ([[2.5.2 Modelo probabilístico — U = 1 − pⁿ]])
2. **Fragmentación interna vs. externa**, con ejemplo numérico. ([[3.3.3 Fragmentación interna y externa]])
3. **Paginación:** de dirección virtual a física, y los 4 cálculos de bits. ([[4.1.2 Paginación y la MMU]] · [[4.1.3 Cálculo de bits, páginas y marcos]])
4. **Fallo de página:** pasos, en orden. ([[4.3.1 Pasos de un fallo de página]])
5. **Reemplazo de páginas:** FIFO (y Belady), segunda oportunidad, reloj, LRU, NRU. ([[4.4.1 Óptimo, FIFO y anomalía de Belady]] · [[4.4.2 Segunda oportunidad y algoritmo del reloj]] · [[4.4.3 NRU, LRU y aging]])
6. **Tamaño óptimo de página:** derivación y ejemplo. ([[4.5.1 Tamaño de página óptimo — s = √(2PE)]])
7. **Llamadas al sistema y modo kernel/usuario.** ([[1.2.1 Modo usuario y modo kernel]] · [[1.2.2 Llamadas al sistema]])
8. **Kernel vs. shell**, y el código del shell con `fork`/`execve`. ([[1.1.2 Kernel, shell y programas del sistema]])
9. **Proceso vs. programa, PCB, estados.** ([[2.1.1 Programa vs. proceso]] · [[2.1.2 El PCB (Process Control Block)]] · [[2.2.1 Estados de un proceso y transiciones]])
10. **Asignación contigua:** first, next, best, worst, con el ejemplo; mapa de bits vs. listas. ([[3.5.1 Primer ajuste, próximo ajuste, mejor ajuste y peor ajuste]] · [[3.4.1 Mapa de bits]])

## Cómo responder cada pregunta (la plantilla de tres niveles)
1. **Definición en una frase** (lo que dirías si te apuran).
2. **Cómo funciona**: pasos, o un ejemplo numérico si es un algoritmo.
3. **Por qué existe / cuál es el límite**: lo que resuelve y lo que deja sin resolver (esto suele llevar a la pregunta siguiente).

> [!tip] Para los cálculos: 4 renglones siempre
> Dato → fórmula → sustitución → resultado con unidad. Si te equivocás en un paso intermedio, el resultado final igual se califica por el método.

## Plan de ataque en el día del final
- **Primero** lo que sabés de memoria (las 10 núcleo) para ganar confianza.
- **Después** los cálculos: anotá la fórmula antes de sustituir.
- **Si te trabás,** decí lo que sabés del tema y el criterio ("el algoritmo X busca minimizar Y"): en el examen escrito vale más que el silencio.

> [!warning] Errores que más se repiten en las correcciones
> - Confundir **p** (fracción en E/S) con la fracción de CPU.
> - Calcular la cantidad de páginas con bits totales en vez de bits de página (sin restar el desplazamiento).
> - Decir que LRU tiene anomalía de Belady (no la tiene) o que best fit es el más rápido (es el que más recorre).
> - Olvidar que bloqueado → listo **no** va directo a ejecución.
> - Decir que el shell es parte del SO.

## Notas relacionadas
[[01 Temas que más se repiten]] · [[02 Preguntas destacadas (aparecieron una vez)]] · [[03 Ejercicios tipo con resultado]] · [[04 Plan de estudio (cronograma)]] · [[05 Mapa pregunta a subtema]]
