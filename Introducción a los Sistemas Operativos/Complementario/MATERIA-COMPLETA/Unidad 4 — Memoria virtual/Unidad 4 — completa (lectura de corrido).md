---
tipo: lectura-corrida
unidad: 4
---
# Unidad 4 — completa (lectura de corrido)

> [!abstract] Fuente
> Desarrollada a partir de las **diapositivas de cátedra** (Administración de Memoria Virtual) y complementada con explicaciones, ejemplos, trampas de examen y libro (Tanenbaum). Ver [[00 Fuente - Temario de diapositivas]].

---

# 4.1.1 Memoria virtual y overlays

> [!abstract] En una frase
> La **memoria virtual** permite ejecutar programas más grandes que la memoria física disponible, separando las direcciones que usa el programa de las direcciones físicas reales.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_02.png]]

La diapositiva plantea el desafío:
- Algunos programas usan más memoria que la disponible.
- **Overlays:** solución antigua; el programa se divide en partes que se cargan por turnos. Problemas: el programador debe planificarlos, no permite compartir rutinas fácilmente; todavía aparece en entornos muy restringidos.
- **Solución moderna:** memoria virtual, con **paginación** y, generalmente, combinación con segmentación.

## Por qué importa

| Sin memoria virtual | Con memoria virtual |
|---|---|
| El programa depende fuertemente de la RAM física | El programa usa direcciones virtuales |
| Overlays manuales | El SO gestiona carga/descarga |
| Difícil compartir y aislar | Aislamiento, compartición controlada, más flexibilidad |

## Complemento de libro (Tanenbaum)
Tanenbaum presenta la memoria virtual como la abstracción que da a cada proceso la ilusión de un gran espacio de direcciones contiguo, mientras el SO y el MMU mapean solo las páginas necesarias a marcos físicos.

## Cómo responderlo en el final
“Memoria virtual permite ejecutar procesos cuyo espacio excede la RAM física. Antes se usaban overlays manuales; ahora el SO usa paginación/MMU para traer páginas bajo demanda”.

> [!warning] Errores típicos
> - Confundir memoria virtual con “usar disco como si fuera RAM sin costo”.
> - Creer que elimina la necesidad de memoria física.


---

# 4.1.2 Paginación y la MMU

> [!abstract] En una frase
> La **paginación** divide el espacio virtual en páginas y la memoria física en marcos; la **MMU** traduce direcciones virtuales a físicas usando la tabla de páginas.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_03.png]]

La diapositiva muestra la relación entre memoria virtual, mapa de memoria (tabla de páginas), memoria física y disco.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_04.png]]

**MMU (Memory Management Unit):** mapea direcciones virtuales en reales. Pertenece al hardware.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_06.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_07.png]]

Ejemplo de traducción: una instrucción como `MOV REG, 8192` usa una dirección virtual; la MMU la traduce al marco físico correspondiente.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_08.png]]

Si la página no está presente, la MMU provoca una interrupción/fallo al SO.

## Conceptos

| Concepto | Definición |
|---|---|
| **Página** | Bloque fijo del espacio virtual |
| **Marco** | Bloque fijo de la RAM |
| **Tabla de páginas** | Mapea página → marco + bits de control |
| **MMU** | Hardware que traduce direcciones |
| **Bit de presencia** | Indica si la página está en RAM |

## Complemento de libro (Tanenbaum)
Tanenbaum detalla campos típicos de la entrada: número de marco, presente/ausente, protección, referenciada, modificada, caching. La MMU usa estos bits para traducir y proteger.

## Cómo responderlo en el final
“Paginación divide virtual en páginas y físico en marcos del mismo tamaño. La MMU consulta la tabla de páginas: si está presente traduce; si no, genera fallo de página”.

> [!warning] Errores típicos
> - Confundir página (virtual) con marco (físico).
> - Pensar que la MMU “decide” por software qué página traer: eso lo hace el SO.


---

# 4.1.3 Cálculo de bits, páginas y marcos

> [!abstract] En una frase
> Con el tamaño de dirección virtual, tamaño de página y memoria física se calculan: bits de desplazamiento, bits de página, cantidad de páginas y cantidad de marcos.

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_05.png]]

La diapositiva recuerda la escala del direccionamiento: 16 bits → 64 KB, 32 bits → 4 GB, 64 bits → espacio enorme. Esto motiva el cálculo cuidadoso de tablas y marcos.

## Fórmulas

| Qué calcular | Fórmula | Nota |
|---|---|---|
| Desplazamiento | $\log_2(\text{tamaño página})$ | bits dentro de la página |
| Bits de página | bits virtuales − desplazamiento | indexa la tabla |
| Páginas virtuales | $2^{bits\_página}$ | espacio virtual dividido en páginas |
| Marcos físicos | memoria física / tamaño página | bloques en RAM |
| Memoria direccionable | $2^{bits\_virtuales}$ | límite teórico por dirección |

## Ejemplo

Dirección virtual 32 bits, página 4 KB, RAM 1 GB:
- desplazamiento = $\log_2(4096)=12$
- bits página = $32-12=20$
- páginas = $2^{20}$
- marcos = $1GB/4KB = 2^{18}$

## Complemento de libro (Tanenbaum)
Tanenbaum insiste en separar claramente dirección virtual, número de página, desplazamiento y marco físico. Los errores en el examen suelen venir de confundir estos campos.

## Cómo responderlo en el final
Escribí datos, fórmula, sustitución y resultado con unidades. Antes de empezar, verificá que el tamaño de página sea potencia de 2.

> [!warning] Errores típicos
> - Usar bits totales como bits de página (olvidar restar desplazamiento).
> - Confundir marcos con páginas.
> - No chequear que memoria utilizable es $\min(direccionable, física)$.


---

# 4.2.1 TLB (memoria asociativa)

> [!abstract] En una frase
> La **TLB** (Translation Lookaside Buffer) es una caché de hardware para traducciones recientes página→marco, que acelera el acceso a memoria.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_14.png]]

- Dispositivo de hardware, generalmente parte de la MMU.
- Si la dirección virtual está en el TLB y pasa protección, se evita consultar la tabla en memoria.
- El acceso al TLB es menor que a memoria → **hit ratio** importa.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_15.png]]

La diapositiva muestra el funcionamiento de la memoria asociativa/TLB.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_16.png]]

Ejemplo de hit ratio: acceso a memoria 100 ns, acceso a TLB 20 ns, hit 90% → tiempo promedio = $(0.9\times 20) + (0.1\times 100)=28$ ns.

## TLB hit / miss

| Caso | Qué pasa | Costo |
|---|---|---|
| **TLB hit** | Traducción encontrada en TLB | Bajo |
| **TLB miss, página en RAM** | Se consulta tabla de páginas y se carga TLB | Medio |
| **TLB miss, página ausente** | Fallo de página | Alto |

## Complemento de libro (Tanenbaum)
Tanenbaum explica TLB con manejo por hardware o software, entradas con bits de validez/protección/modificación y el efecto de cambios de contexto (flush o ASID).

## Cómo responderlo en el final
“TLB es caché de traducciones página-marco. Acelera porque evita acceder a la tabla en memoria. Si hay miss, se va a tabla; si la página no está, hay page fault”.

> [!warning] Errores típicos
> - Confundir TLB con caché de datos.
> - Olvidar que tras TLB miss puede venir hit en tabla o fallo de página.


---

# 4.2.2 Tablas multinivel e invertidas

> [!abstract] En una frase
> Las **tablas multinivel** dividen la tabla de páginas para no mantenerla completa en memoria; la **tabla invertida** tiene una entrada por marco físico y escala mejor en espacios virtuales grandes.

## Diapositivas de cátedra

### Problema del tamaño

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_11.png]]

El tamaño de la tabla de páginas puede ser enorme (64 bits). El mapeo debe ser rápido; no conviene tener todo en registros o en una tabla lineal enorme.

### Tablas multinivel

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_12.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_13.png]]

Las diapositivas muestran la paginación multinivel: la dirección virtual se divide en índices de niveles y desplazamiento. Solo se materializan las subtablas necesarias.

### Tabla invertida

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_17.png]]

En lugar de una entrada por página virtual, se usa una entrada por **marco físico**. Reduce el tamaño cuando el espacio virtual es muy grande.

## Comparación

| Esquema | Entrada por | Ventaja | Costo |
|---|---|---|---|
| **Lineal** | Página virtual | Simple | Muy grande |
| **Multinivel** | Páginas, por niveles | Solo subtablas necesarias | Más accesos en miss |
| **Invertida** | Marco físico | Escala con RAM | Búsqueda más compleja (hash/TLB) |

## Complemento de libro (Tanenbaum)
Tanenbaum explica que la tabla invertida ahorra espacio en arquitecturas de 64 bits, pero requiere hash y manejo de colisiones. La TLB mitiga el costo de búsqueda.

## Cómo responderlo en el final
“Multinivel divide el número de página en varios índices y evita tabla lineal completa. Invertida usa una entrada por marco físico: escala con RAM, pero buscar es más complejo”.

> [!warning] Errores típicos
> - Decir que tabla invertida tiene una entrada por página virtual.
> - No aclarar si te piden tablas totales o subtablas.


---

# 4.3.1 Pasos de un fallo de página

> [!abstract] En una frase
> Un **fallo de página** ocurre cuando se referencia una página no presente en RAM; el SO debe traerla desde disco, actualizar tablas y reiniciar la instrucción.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_09.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_10.png]]

La diapositiva resume: si la página no está en memoria, el CPU causa interrupción al kernel; se guarda estado, se verifica validez, se busca/libera marco, se carga la página, se reinicia la instrucción.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_37.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_38.png]]

Secuencia detallada de la cátedra:
1. Hardware interrumpe al kernel y guarda PC en la pila.
2. Rutina en assembler guarda registros y estado volátil.
3. El SO detecta page fault y averigua qué página virtual se necesita.
4. Controla si la página es válida y el acceso permitido; si no, aborta.
5. Si el marco seleccionado está ocupado, se planifica escritura a disco si está sucio y se hace cambio de contexto.
6. Cuando hay marco limpio, se busca la página en disco y se planifica lectura.
7. Al llegar la interrupción de disco, se actualiza tabla de páginas y se marca marco normal.
8. Se restaura el estado de la instrucción fallida y se reprograma el proceso.
9. El planificador lo ejecuta; la rutina assembler restaura registros y continúa.

## Versión corta para examen

1. MMU detecta P=0 → trap.
2. SO guarda estado.
3. Verifica página válida/permiso.
4. Busca marco libre o elige víctima.
5. Si víctima sucia (M=1), escribir a disco.
6. Cargar página requerida.
7. Actualizar tabla/TLB.
8. Reiniciar instrucción.

## Complemento de libro (Tanenbaum)
Tanenbaum enfatiza que la instrucción que causó el fallo debe poder reiniciarse. Esto es fácil en algunas arquitecturas y difícil en otras con instrucciones complejas.

## Cómo responderlo en el final
Enumerá los pasos en orden, destacá “guardar estado”, “víctima si no hay marco libre”, “si M=1 escribir a disco”, “actualizar tabla” y “reiniciar instrucción”.

> [!warning] Errores típicos
> - Olvidar el bit M al reemplazar.
> - No reiniciar la instrucción que falló.
> - No distinguir página inválida de página ausente válida.


---

# 4.3.2 Reinicio de la instrucción y páginas compartidas

> [!abstract] En una frase
> Tras un page fault, la instrucción debe reiniciarse correctamente; además, algunas páginas pueden compartirse entre procesos y requieren control especial al reemplazarlas o liberarlas.

## Diapositivas de cátedra

### Reinicio de instrucción

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_39.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_40.png]]

El problema: si la instrucción falló por un operando, debe reejecutarse. Instrucciones con autoincremento/autodecremento pueden complicar el reinicio. La cátedra menciona que los diseñadores de CPU usan registros auxiliares para restaurar el estado.

### Páginas compartidas

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_41.png]]

Hay páginas compartibles (código) y no compartibles (datos privados). Al terminar un proceso, no se deben liberar marcos que otro proceso sigue usando.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_42.png]]

Ejemplo: librerías compartidas por más de un proceso.

### Almacenamiento en disco

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_43.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_44.png]]

Las páginas pueden respaldarse en área de intercambio estática o dinámica. Si se usa swap dinámico, se debe llevar registro de dónde está cada página.

## Complemento de libro (Tanenbaum)
Tanenbaum destaca copy-on-write para páginas compartidas: se comparten mientras son de solo lectura; al escribir, se copia. Esto optimiza fork y librerías compartidas.

## Cómo responderlo en el final
“Después del page fault se reinicia la instrucción fallida, lo cual puede ser complejo si hubo autoincrementos. Las páginas compartidas (código/librerías) no deben liberarse si otro proceso las usa; datos privados no se comparten igual”.

> [!warning] Errores típicos
> - Liberar una página compartida cuando termina un solo proceso.
> - Ignorar que reiniciar instrucción no siempre es trivial.


---

# 4.4.1 Óptimo, FIFO y anomalía de Belady

> [!abstract] En una frase
> **Óptimo** reemplaza la página que se usará más lejos en el futuro (teórico); **FIFO** reemplaza la más antigua en llegar, pero puede sufrir la **anomalía de Belady**.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_18.png]]

La diapositiva lista algoritmos: óptimo, NRU, FIFO, segunda oportunidad.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_23.png]]

**Anomalía de Belady:** en FIFO, más marcos de página pueden resultar en más fallos de página.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_22.png]]

La tabla resumen de algoritmos ayuda a comparar criterios.

## Comparación

| Algoritmo | Criterio | Ventaja | Desventaja |
|---|---|---|---|
| **Óptimo** | Usar más lejos en el futuro | Mínimos fallos | Imposible en la práctica |
| **FIFO** | Más antigua cargada | Simple | Belady; puede sacar página útil |

## Anomalía de Belady

Para algunas cadenas de referencia, aumentar marcos con FIFO produce más fallos. No ocurre en algoritmos de pila como LRU.

## Complemento de libro (Tanenbaum)
Tanenbaum usa el óptimo como cota de referencia para evaluar algoritmos reales. FIFO es fácil de implementar pero puede comportarse mal.

## Cómo responderlo en el final
Definí óptimo (teórico) y FIFO (práctico/simple). Si preguntan Belady, explicá: más marcos pueden dar más fallos en FIFO.

> [!warning] Errores típicos
> - Decir que Belady ocurre en LRU.
> - Presentar FIFO como “bueno” sin mencionar su defecto.


---

# 4.4.2 Segunda oportunidad y algoritmo del reloj

> [!abstract] En una frase
> **Segunda oportunidad** mejora FIFO usando el bit R; el **reloj** implementa la misma idea con un puntero circular.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_18.png]]

Se menciona segunda oportunidad como FIFO con bit R.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_19.png]]

**Algoritmo de reloj:** las páginas están en un círculo; un puntero avanza. Si R=0, se reemplaza; si R=1, se limpia R y se da segunda oportunidad.

## Funcionamiento

| Bit R | Acción del reloj |
|---|---|
| 0 | Página candidata: se reemplaza |
| 1 | Se pone R=0 y se avanza el puntero |

## Comparación con FIFO

- FIFO puro mira solo llegada.
- Segunda oportunidad/reloj considera si fue referenciada recientemente.
- Evita sacar una página muy usada solo por ser vieja.

## Complemento de libro (Tanenbaum)
Tanenbaum muestra el reloj como una aproximación eficiente a LRU: barato y con buen comportamiento en la práctica.

## Cómo responderlo en el final
“Reloj es una implementación eficiente de segunda oportunidad. Puntero circular: R=0 reemplaza, R=1 se limpia y avanza. Mejora FIFO evitando sacar páginas recientemente usadas”.

> [!warning] Errores típicos
> - Olvidar que al dar segunda oportunidad se limpia R.
> - No mencionar el puntero circular.


---

# 4.4.3 NRU, LRU y aging

> [!abstract] En una frase
> **NRU** clasifica páginas por bits R y M; **LRU** reemplaza la menos recientemente usada; **Aging** aproxima LRU en software con contadores.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_18.png]]

La diapositiva lista NRU (bits R y M).

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_20.png]]

**LRU:** menos usado recientemente. Se puede predecir por el pasado. Implementaciones HW: contadores, matriz LRU.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_21.png]]

**NRU simulando LRU en software = Aging.** Se desplazan contadores y se incorpora el bit R.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_22.png]]

Resumen comparativo de algoritmos.

## NRU (clases R,M)

| Clase | R | M | Prioridad de reemplazo |
|---:|---:|---:|---|
| 0 | 0 | 0 | Mejor candidata |
| 1 | 0 | 1 |  |
| 2 | 1 | 0 |  |
| 3 | 1 | 1 | Peor candidata |

## LRU vs Aging

| Algoritmo | Precisión | Costo | Observación |
|---|---|---|---|
| **LRU exacto** | Alta | Alto HW | Matriz/contadores caros |
| **Aging** | Aproximada | Moderado | Buen compromiso en software |

## Complemento de libro (Tanenbaum)
Tanenbaum explica que LRU exacto es ideal pero costoso; Aging aproxima bien manteniendo historia reciente. NRU es simple pero poco fino y mejora si se limpian bits R periódicamente.

## Cómo responderlo en el final
NRU: 4 clases R/M, reemplaza la clase más baja. LRU: la usada hace más tiempo; caro exacto. Aging: desplazamiento + bit R como aproximación práctica.

> [!warning] Errores típicos
> - Confundir aging de páginas con aging de prioridades de procesos.
> - Creer que NRU considera el tiempo exacto de uso.


---

# 4.5.1 Tamaño de página óptimo — s = √(2PE)

> [!abstract] En una frase
> El tamaño óptimo de página equilibra la fragmentación interna (favorece páginas chicas) con el tamaño de la tabla de páginas (favorece páginas grandes), resultando en $s = \sqrt{2PE}$.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_34.png]]

Tamaño de página pequeño: ventajas (menos fragmentación interna, menos parte no usada en memoria); desventaja (más páginas, tablas más grandes).

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_35.png]]

Sobrecarga total aproximada: fragmentación interna promedio $s/2$ + espacio de tabla $(s/p)\cdot ?$ La diapositiva plantea: $s$ = tamaño promedio de proceso, $p$ = tamaño de página, $e$ = entrada en tabla.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_36.png]]

Optimizando: $-se/p^2 + 1/2 = 0 \Rightarrow p = \sqrt{2se}$. Ejemplo: $s=128K$, $e=8$ bytes → ~1448 bytes; en la práctica 1K o 2K.

## Fórmula

$$p = \sqrt{2se}$$

- $s$: tamaño promedio del proceso.
- $e$: tamaño de una entrada de tabla de páginas.
- $p$: tamaño óptimo de página.

## Complemento de libro (Tanenbaum)
Tanenbaum muestra el mismo trade-off: páginas pequeñas reducen desperdicio interno; páginas grandes reducen tablas y TLB misses por overhead de administración. El óptimo matemático es una guía, no una regla absoluta.

## Cómo responderlo en el final
Escribí la fórmula, identificá $s$ y $e$, sustituí con unidades consistentes y calculá. Aclaralo si el enunciado usa $P$ o $s$.

> [!warning] Errores típicos
> - Mezclar KB con bytes.
> - Olvidar que es un óptimo teórico; en la práctica se eligen potencias de 2 cercanas.


---

# 4.5.2 Conjunto de trabajo y thrashing

> [!abstract] En una frase
> El **conjunto de trabajo** es el conjunto de páginas que un proceso necesita en un intervalo reciente; si no cabe en memoria, puede aparecer **thrashing**.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_31.png]]

**Modelo de conjunto de trabajo (WSM):** reduce el thrashing. Thrashing: el programa genera fallos de página cada pocas instrucciones. Se compara prepaginación vs. paginación por demanda.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_32.png]]

**Políticas de asignación:** local vs. global. Local: reemplaza solo páginas del proceso; global: puede tomar marcos de otros procesos.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_33.png]]

**PFF (Page Fault Frequency):** controla la tasa de fallos para ajustar la cantidad de marcos asignados.

## Conceptos

| Concepto | Idea |
|---|---|
| **Working set** | Páginas usadas recientemente por el proceso |
| **Thrashing** | El sistema pagina más de lo que ejecuta |
| **PFF** | Si hay muchos fallos, dar más marcos; si pocos, quitar |
| **Local vs global** | A quién se le quita el marco al reemplazar |

## Complemento de libro (Tanenbaum)
Tanenbaum explica que el thrashing aparece cuando la suma de working sets supera la RAM. La solución es reducir grado de multiprogramación o ajustar asignación de marcos.

## Cómo responderlo en el final
“Working set: páginas necesarias en la ventana reciente. Thrashing: exceso de fallos por falta de marcos para el working set. Se mitiga con PFF, políticas local/global y control de multiprogramación”.

> [!warning] Errores típicos
> - Confundir thrashing con “la CPU está lenta” en general.
> - No relacionar working set con localidad de referencia.


---

# 4.6.1 Segmentación

> [!abstract] En una frase
> La **segmentación** divide el espacio de direcciones en segmentos lógicos (código, datos, pila, tablas), cada uno con nombre/número y longitud.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_45.png]]

Un espacio de direcciones unidimensional puede causar problemas cuando tablas crecen; la segmentación propone espacios separados por unidades lógicas.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_48.png]]

Motivación: un compilador maneja varias tablas/áreas (código fuente, símbolos, constantes, árbol parse, pila) que crecen de forma distinta.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_49.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_50.png]]

Segmentación: direccionamiento bidimensional (segmento, offset). Divide el espacio lógico en segmentos; cada segmento es una unidad lógica.

## Características

| Aspecto | Segmentación |
|---|---|
| Unidad | Segmento lógico |
| Dirección | (segmento, desplazamiento) |
| Crece | Por segmento, según necesidad |
| Protección | Por segmento (lectura, escritura, ejecución) |
| Problema | Fragmentación externa |

## Complemento de libro (Tanenbaum)
Tanenbaum contrasta paginación (unidades físicas fijas) con segmentación (unidades lógicas variables). La segmentación facilita compartir/proteger estructuras lógicas, pero complica la asignación por fragmentación externa.

## Cómo responderlo en el final
“Segmentación divide el programa en unidades lógicas con (segmento, offset). Facilita protección y compartición lógica, pero puede generar fragmentación externa”.

> [!warning] Errores típicos
> - Confundir segmento con página.
> - Olvidar que el desplazamiento no puede superar el tamaño del segmento.


---

# 4.6.2 Segmentación con paginación y su combinación

> [!abstract] En una frase
> La **segmentación paginada** combina la visión lógica de la segmentación con la asignación física eficiente de la paginación: cada segmento se divide en páginas.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_51.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_52.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_53.png]]

Las diapositivas muestran la comparación paginación vs segmentación y la idea de combinar ambas: segmentos lógicos, paginados internamente.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_54.png]]

**MULTICS:** ejemplo clásico de segmentación con paginación. El descriptor de segmento apunta a la tabla de páginas del segmento.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_55.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_59.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_60.png]]

MULTICS usa dirección virtual con número de segmento y dirección dentro del segmento, que luego se traduce a través de tablas de páginas.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_62.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_64.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 4/slide_65.png]]

**Intel:** también combina segmentación y paginación. Selector + offset → dirección lineal → paginación → dirección física.

## ¿Por qué combinar?

| Esquema | Aporta | Limita |
|---|---|---|
| Paginación | Sin fragmentación externa, manejo simple de marcos | No respeta lógica del programa |
| Segmentación | Lógica, protección, compartición por unidades | Fragmentación externa |
| **Seg. paginada** | Lógica + asignación física eficiente | Más complejidad en traducción |

## Cómo se resuelve “¿entra en memoria?”

1. Calcular tamaño de página y páginas direccionables.
2. Por cada segmento: $\lceil tamaño / página \rceil$.
3. Sumar páginas de todos los segmentos (no mezclar segmentos en una misma página).
4. Comparar con páginas disponibles.

## Complemento de libro (Tanenbaum)
Tanenbaum usa MULTICS e Intel x86 como casos históricos/reales. La idea clave: la segmentación da estructura lógica, la paginación resuelve la colocación en memoria física.

## Cómo responderlo en el final
“Segmentación paginada: cada segmento lógico se divide en páginas. Conserva la lógica/protección de segmentos y evita la fragmentación externa de la segmentación pura. Para ver si entra, se calculan páginas por segmento y se suman”.

> [!warning] Errores típicos
> - Sumar todo el proceso y dividir por página sin separar segmentos.
> - Confundir dirección lineal (Intel) con dirección física final.


---
