---
tipo: ejercicios
---
# Ejercicios de los modelos (resueltos)

> [!abstract] Cómo usar esta nota
> Cada bloque es un **tipo de ejercicio** que se repite en los exámenes. Primero el método, después el caso real con su resultado. Los resultados fueron recalculados. Donde el examen o la resolución manuscrita tenía un error, se indica.

## 1. Bits de una dirección (el ejercicio que más se repite)
**Método (4 pasos):**
1. Desplazamiento = log₂(tamaño de página).
2. Bits de página = bits totales − desplazamiento.
3. Páginas virtuales = 2^(bits de página).
4. Marcos = memoria física ÷ tamaño de página.

| Enunciado | Desplazamiento | Bits de página | Páginas | Marcos | Memoria direccionable |
|---|---|---|---|---|---|
| 16 bits, 8 K, memoria física 32 K (Modelos) | 13 | 3 | 8 | 4 | 2¹⁶ = 64 KB |
| 22 bits, 2 K, 16 M (Modelos y Parcial 2022) | 11 | 11 | 2 K (2¹¹) | 8 K (2¹³) | 4 MB |
| 42 bits, 8 K, 8 GB (Parcial 2023) | 13 | 29 | 2²⁹ | 2²⁰ | 2⁴² = 4 TB |
| 9 bits, páginas de 8 bytes (Final de Diciembre 2024) | 3 | 6 | 64 | 2 GB ÷ 8 = 2²⁸ | **512 bytes** |
| 52 bits, 2 K (Recuperatorio 2025 y Diciembre 2024) | 11 | 41 | 2⁴¹ | depende de la memoria física | 2⁵² = 4 PB |
| 36 bits, 16 K, 16 GB (Parcial 2024, con páginas de 5 K como trampa) | 14 | 22 | 2²² | 16 GB ÷ 16 K = 2²⁰ | 2³⁶ = 64 GB |
| 25 bits, 13 de desplazamiento (Noviembre 2023) | 13 | 12 | 2¹² = 4096 | 1 GB ÷ 8 K = 131 072 | **32 MB** (2²⁵) |

> [!warning] El error de la pregunta "¿cuánta memoria puede utilizar el sistema?"
> La memoria que se puede **usar** es la **menor** entre la direccionable (virtual) y la física. Con 25 bits y 1 GB de RAM, solo se pueden usar **32 MB**. Con 9 bits y 2 GB de RAM, solo **512 bytes**. Esto aparece en los finales y casi todos lo pierden.

Teoría: [[4.1.3 Cálculo de bits, páginas y marcos]].

## 2. Tabla de páginas completa (dada en el enunciado)
**Método:** cada fila es una página. Los bits de marco van en el medio y el último bit es **presente (1) o ausente (0)**.

Tabla de 8 bits del examen 1T Febrero 2024 (verificada contra la hoja original). Cada fila es una página, con marco de 2 bits y una columna aparte de presencia:

| Página | Marco | En memoria |
|---|---|---|
| 7 | 00 | 0 |
| 6 | 00 | 0 |
| 5 | 00 | 0 |
| 4 | 10 | 1 |
| 3 | 00 | 1 |
| 2 | 11 | 1 |
| 1 | 00 | 0 |
| 0 | 01 | 1 |

**Resultados (memoria de 256 bytes, páginas de 32 bytes), como están en la hoja:**
- Memoria direccionable: 2⁸ = **256 bytes**.
- Desplazamiento: 5 bits (32 = 2⁵). Acceso a la tabla de páginas: log₂(256 ÷ 32) = **3 bits**.
- Páginas virtuales: **8**. Marcos totales: 256 ÷ 32 = **8**.
- Marcos ocupados: **4** (páginas 4, 3, 2 y 0 están en memoria).

**Resultados base (memoria de 256 bytes, páginas de 32 bytes):**
- Memoria direccionable: 2⁸ = **256 bytes**.
- Desplazamiento: 5 bits (32 = 2⁵). Bits para la página: **3 bits**.
- Páginas virtuales: **8**. Marcos: 256 ÷ 32 = **8**.

Con la tabla de 16 bits del mismo bloque (páginas de **8 K**, 13 bits de desplazamiento, 3 bits para la página, 8 páginas), la memoria direccionable es 64 KB.

**Traducción de una dirección** (el que se pide en el final de 16 bits con 4 K): dirección virtual 20500 en binario = `0101 0000 0001 0100`. Página = 20500 ÷ 4096 = **5** (`0101`), desplazamiento = **20** (`0000 0000 0001 0100`). La página 5 está en el **marco 3** (según la tabla dada). Dirección física = 3 × 4096 + 20 = **12308** = `0011 0000 0001 0100`.

Teoría: [[4.1.2 Paginación y la MMU]].

## 3. Tablas multinivel: cantidad de tablas y de páginas
**Caso 32 bits, páginas de 16 K, 3 niveles de 6 bits (1T Febrero 2024 y 1T Febrero 2025):**
- Desplazamiento: 32 − 14 = **18 bits** para páginas (6 + 6 + 6). Páginas: 2¹⁸ = **262 144**.
- Tablas: 1 principal + 2⁶ tablas de nivel 2 + 2⁶ × 2⁶ tablas de nivel 3 = 1 + 64 + 4096 = **4161 tablas en total**. Sin contar la principal: **4160 subtablas**.

> [!note] Cuidado con la pregunta
> Si el enunciado pide "subtablas", no cuentes la tabla principal. Si pide "tablas", sumala. Aclaralo en el final.

**Caso 25 bits, 3 niveles de 4, 5 y 5 bits (Recuperatorio 2025):**
- Desplazamiento: 25 − 14 = **11 bits**, así que las páginas son de **2 K**.
- Páginas: 2¹⁴ = **16 384**.
- Tablas: 1 + 2⁴ + 2⁴ × 2⁵ = 1 + 16 + 512 = **529 tablas** (528 subtablas sin contar la principal).
- Con 2 GB de RAM: 2³¹ ÷ 2¹¹ = **2²⁰ marcos** (1 048 576). Memoria direccionable: 2²⁵ = 32 MB, así que **no se puede usar toda la RAM**.

Teoría: [[4.2.2 Tablas multinivel e invertidas]].

## 4. Tabla invertida vs. tabla normal (Junio 2026)
**Caso:** 64 bits, memoria física 16 GB, páginas de 8 K.
- Marcos: 16 GB ÷ 8 K = 2³⁴ ÷ 2¹³ = **2²¹ entradas** (una por marco). Con factor 2 (como pide el examen), la tabla invertida tiene 2 × 2²¹ = **2²² entradas**.
- Sin tabla invertida: 2⁶⁴ ÷ 2¹³ = **2⁵¹ entradas** (una por página virtual), que es un número imposible de guardar.

**Por qué es necesaria:** la tabla normal crece con el espacio **virtual** (2⁵¹ entradas), y la invertida crece con la **física** (2²¹). Cuando la memoria virtual es mucho más grande que la RAM, la invertida es la que entra.

Teoría: [[4.2.2 Tablas multinivel e invertidas]].

## 5. Tamaño de página: problemas y casos especiales
- **Página que no es potencia de 2** (Parcial 2024, 36 bits con páginas de **5 KB**): el tamaño tiene que ser 2^k para que el desplazamiento sea una cantidad exacta de bits. Con 5 KB el desplazamiento no es entero. Esa es la respuesta al "¿encuentra algún problema?".
- **Tabla de páginas muy grande** (Parcial 2022, 32 bits, 4 K, PC de 4 MB, entrada de 4 bytes): 2²⁰ páginas × 4 bytes = **4 MB**, o sea **toda la memoria física**. Solución: tablas multinivel o invertidas.
- **Tabla de 56 bits con páginas de 16 K** (2T Febrero 2024): 2⁴² páginas. La respuesta "aumentar el tamaño de página" es correcta pero incompleta: lo que realmente se usa son **tablas multinivel** o **invertidas**.
- **Tamaño óptimo de página** (Modelos, PP): s = √(2PE) con P = 2 MB y E = 16 bytes da **8 KB**, con la fórmula de [[4.5.1 Tamaño de página óptimo — s = √(2PE)]].

## 6. Multiprogramación: segmentación con paginación (Junio 2026)
**Caso:** 16 bits, páginas de **2 K**. Sistema operativo: código 10 648, datos 4 329, pila 5 633. Programa: código 10 557, datos 21 297, pila 9 747.
- Cada segmento se redondea hacia arriba a páginas (una página no mezcla segmentos).
- Con páginas de 2 K: SO = 6 + 3 + 3 = **12 páginas**. Programa = 6 + 11 + 5 = **22 páginas**. Total **34 páginas**. El espacio direccionable de 16 bits son 2¹⁶ ÷ 2¹¹ = **32 páginas**. **No entra.**
- Con páginas de 1 K: SO = 11 + 5 + 6 = 22, programa = 11 + 21 + 10 = 42. Total **64 páginas** = 64 de 64. **Entra justo**, sin margen. Decilo así, con el número.

Teoría: [[4.6.2 Segmentación con paginación y su combinación]].

## 7. Modelo probabilístico y Gantt de E/S
**Fórmula:** U = 1 − pⁿ.
- Grado mínimo de multiprogramación para un objetivo: pⁿ ≤ 1 − U_objetivo ⇒ n ≥ log(1 − U) ÷ log(p).
- **Ejemplo de los Modelos:** p = 0,75 y U = 0,90 ⇒ 0,75ⁿ ≤ 0,1 ⇒ **n = 8** (log 0,1 ÷ log 0,75 ≈ 7,96).
- **Ejemplo del Parcial 2023:** p = 0,5, tres procesos ⇒ U = 1 − 0,5³ = **87,5 %**. Uso de CPU por proceso = 87,5 % ÷ 3 ≈ **29,2 %** cada uno, si se reparten por igual.
- **Ejemplo con dos procesos (p = 0,5 y p = 0,9):** U = 1 − 0,5 × 0,9 = **55 %**.

**Gantt (método del resumen SAE, con reparto round robin):** al llegar un trabajo, se recalcula U = 1 − pⁿ con el n actual. Cada proceso recibe U ÷ n de CPU por minuto de reloj. El tiempo que tarda un proceso es su duración de CPU dividido ese reparto. Los exámenes piden **no redondear** (usar todos los decimales) y mostrar el cálculo antes del Gantt. Confirmá la convención con la cátedra antes del final, porque hay variantes.

Teoría: [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] · [[2.4.2 FIFO, SJF y Round Robin (quantum)]].

## 8. Reemplazo de páginas (con tabla)
- **FIFO:** la página con menor tiempo de carga.
- **LRU:** la página con menor tiempo de última referencia.
- **NRU:** la de clase más baja (R, M): (0,0) < (0,1) < (1,0) < (1,1).
- **Reloj:** puntero circular. R = 0 se reemplaza; R = 1 pasa a R = 0 y el puntero avanza.

Teoría: [[4.4.1 Óptimo, FIFO y anomalía de Belady]] · [[4.4.2 Segunda oportunidad y algoritmo del reloj]] · [[4.4.3 NRU, LRU y aging]].

## 9. Asignación de procesos a memoria (la técnica de la hoja de cuentas)
En los exámenes de 2025 se pide la cantidad de **páginas que ocupa cada segmento** (código, datos, pila): redondear hacia arriba, por segmento. Cuando el total de páginas es mayor que las páginas del espacio direccionable, el programa **no entra**. Ver el caso del punto 6.

## 10. Un error de los modelos que conviene conocer
La resolución de la 3.ª pregunta del Modelo (sistema de 32 bits, 4 K, PC de 4 MB) habla de la tabla en la que 2²⁰ entradas de 4 bytes ocupan 4 MB. Eso es exactamente toda la memoria física, y el problema no es solo "la tabla es grande": **la tabla no entra**. Así se explica al final.

> [!tip] Cronómetro de examen
> Un bloque de bits = 2 minutos si lo tenés practicado. Escribí siempre: **datos → desplazamiento → bits de página → páginas → marcos → lo que pidan**.
