---
tipo: unidad-completa
unidad: 4
---
# Unidad 4 — Memoria virtual — completa

> [!abstract] Qué pide la unidad
> Cómo un proceso puede usar más memoria que la RAM física: paginación, traducción de direcciones (MMU y TLB), fallo de página, algoritmos de reemplazo (FIFO, reloj, NRU, LRU), tamaño de página, y segmentación. Es la unidad con más cálculos y la que más se repite en los parciales.

> [!info] Cómo leer este archivo
> Es la unidad entera, en orden: Tema → Subtema. Cada subtema tiene su nota propia en la carpeta del tema, por si querés estudiar uno solo.


---

## Tema 4.1 — Concepto y paginación


### 4.1.1 Memoria virtual y overlays

> [!abstract] En una frase
> La **memoria virtual** da a cada proceso un espacio de direcciones propio, dividido en **páginas**. Solo algunas páginas están en RAM; el resto queda en disco, y el hardware traduce cada dirección. Así un programa puede ser más grande que la RAM física.

#### Desarrollo
- **Antes:** los **overlays** (sobrepuestos) dividían el programa a mano: el programador planeaba qué parte cargar. Era tedioso y propenso a errores, y no permitía compartir rutinas. Todavía se usan en celulares y PDA.
- **Idea de la memoria virtual** (Fotheringham, 1961): el SO y el hardware hacen ese trabajo. Si la página pedida no está en RAM, se genera un **fallo de página** y el SO la trae del disco y reinicia la instrucción.
- **Generalización de base y límite:** en vez de reubicar todo el espacio de un golpe, se reubica en unidades pequeñas e iguales (las páginas).
- **Ventaja para multiprogramación:** mientras un proceso espera que una página llegue del disco, la CPU atiende a otro.

#### Cómo responderlo en el final
"Memoria virtual: cada proceso ve un espacio contiguo propio dividido en páginas; sólo algunas están en RAM. Si falta una, hay un fallo de página y el SO la trae del disco."

> [!warning] Errores típicos
> - Confundir memoria virtual con swapping: el swapping mueve **procesos enteros**; la memoria virtual mueve **páginas**.


### 4.1.2 Paginación y la MMU

> [!abstract] En una frase
> Con **paginación**, la memoria virtual se divide en **páginas** y la física en **marcos** del mismo tamaño. Una dirección virtual es un par **(número de página, desplazamiento)**; la **MMU** reemplaza el número de página por el número de marco que tiene en la tabla de páginas.

#### Desarrollo
- **MMU:** parte del hardware (suele estar dentro del chip de CPU). Las direcciones del programa no van directo al bus: pasan por la MMU.
- **Tabla de páginas:** una entrada por página, con el **número de marco**, el bit **V / presente-ausente**, y los bits **R** (referenciada) y **M** (modificada).
- **Dirección física = marco × tamaño de página + desplazamiento.**

### Ejemplo de la cátedra (TP3, pregunta 3): páginas de 2 KB
Tabla: página 1 → marco 4; página 2 → marco 7; página 4 → marco 2. Páginas 0, 3 y 5 ausentes (V = 0).

| Dirección virtual (página, desplazamiento) | Resultado | Dirección física |
|---|---|---|
| (1, 481) | Marco 4 | 4 × 2048 + 481 = **8673** |
| (2, 1324) | Marco 7 | 7 × 2048 + 1324 = **15660** |
| (5, 122) | Página ausente | **Fallo de página** |
| (3, 2051) | Página ausente (además, 2051 > 2048: desplazamiento inválido) | **Fallo de página** |
| (9, 21) | La página 9 no existe en la tabla | **Dirección inválida** |

### Ejemplo de Tanenbaum
Direcciones de 16 bits: 64 KB virtuales, pero 32 KB físicos. Con páginas de 4 KB hay 16 páginas virtuales y 8 marcos: sólo 8 páginas pueden estar en RAM al mismo tiempo.

#### Cómo responderlo en el final
Dibujar la tabla de páginas con los bits, convertir una dirección (página, offset) a física y mencionar qué pasa si V = 0.


### 4.1.3 Cálculo de bits, páginas y marcos

> [!abstract] En una frase
> Todo ejercicio de paginación se resuelve con cuatro cuentas: **bits de desplazamiento = log₂(tamaño de página)**; **bits de página = bits totales − desplazamiento**; **nº de páginas = 2^(bits de página)**; **nº de marcos = memoria física ÷ tamaño de marco**.

#### Desarrollo
### Fórmulas
| Dato | Cálculo |
|---|---|
| Bits de desplazamiento | log₂(página). Página de 8 KB = 2¹³ → **13 bits** |
| Bits de número de página | Bits de la dirección − desplazamiento |
| Páginas virtuales | 2^(bits de página) |
| Marcos | Memoria física ÷ tamaño de página |
| Bits de dirección física | log₂(memoria física) |

### Casos resueltos
| Enunciado | Desplazamiento | Páginas | Marcos |
|---|---|---|---|
| **Repaso:** 42 bits, páginas de 8 KB, memoria física de 8 GB | 13 bits | 2²⁹ | 8 GB / 8 KB = 2²⁰ |
| **Parcial 13:** 64 bits, 8 KB, 32 GB | 13 bits | 2⁵¹ | 2³⁵ / 2¹³ = **2²²** |
| **Parcial 14:** 64 bits, 16 KB, 65 GB | 14 bits | 2⁵⁰ | 65 GB / 16 KB = 4 259 840 |
| **TP3, 7:** 36 bits, desplazamiento de 13 bits | 13 bits | 2²³ | Con 512 MB: 65 536 marcos |
| **TP3, 5:** 7 páginas de 4096 palabras, 64 bloques físicos | 12 bits | Dirección virtual de **15 bits** (7 × 4096 = 28 672 < 2¹⁵) | Dirección física de **18 bits** (64 × 4096 = 2¹⁸) |
| **TP3, 2:** 32 bits, nivel 1 de 8 bits, nivel 2 de 11 bits | 13 bits (8 KB) | 2¹⁹ páginas | — |

### Tabla de páginas en TP3, pregunta 7
Con entradas de **64 bits** y 2²³ páginas: 2²³ × 8 bytes = **64 MB** solo para la tabla de páginas. Por eso aparecen las tablas multinivel (4.2.2).

#### Cómo responderlo en el final
Escribir las cuatro cuentas en orden y dar cada resultado como potencia de 2 y como número. Sobre todo, mostrar el log₂ del tamaño de página.

> [!warning] Errores típicos
> - Usar 1 KB = 1000 bytes en lugar de 1024: en potencias de 2 siempre binario.
> - Olvidar que el desplazamiento se mide en **bytes** cuando el enunciado habla de palabras (TP3, 5 usa palabras).


---

## Tema 4.2 — Traducción rápida y tablas de páginas


### 4.2.1 TLB (memoria asociativa)

> [!abstract] En una frase
> El **TLB** es una caché pequeña y asociativa dentro de la MMU que guarda traducciones recientes (página → marco). Si la página está en el TLB (**hit**), no hace falta leer la tabla de páginas en RAM; eso acelera casi todos los accesos.

#### Desarrollo
- Sin TLB, cada acceso a memoria implicaría **dos** accesos: uno a la tabla de páginas y otro al dato.
- **Tiempo efectivo** con hit ratio h: `t = h × t_TLB + (1 − h) × t_memoria` (cátedra: TLB 20 ns, memoria 100 ns, 90 % de aciertos → 0,9 × 20 + 0,1 × 100 = **28 ns**).
- Un fallo de TLB no es un fallo de página: la página puede estar en RAM y solo hay que buscar la entrada en la tabla.

#### Cómo responderlo en el final
Dar la definición de TLB, la fórmula del tiempo promedio con el ejemplo de 28 ns y la diferencia entre fallo de TLB y fallo de página.


### 4.2.2 Tablas multinivel e invertidas

> [!abstract] En una frase
> Una tabla de páginas de un espacio de 64 bits tendría cerca de 20 millones de terabytes. Para reducirla: **multinivel** (la tabla se parte en niveles y solo se crean las tablas de niveles inferiores que se usan) o **invertida** (una entrada por marco, no por página).

#### Desarrollo
### Multinivel
- La dirección se divide en campos: índice del nivel superior, índice del nivel inferior y desplazamiento.
- El nivel superior apunta a tablas de segundo nivel; **solo se crean las que se usan**, lo que ahorra mucha memoria.
- **Ejemplo (TP3, 2):** 32 bits con campos de 8 + 11 bits → desplazamiento de 13 bits → páginas de **8 KB**, y 2¹⁹ páginas virtuales. El nivel superior tiene 2⁸ = 256 entradas; cada segundo nivel, 2¹¹ = 2048.

### Invertida
- Una sola tabla con **una entrada por marco físico**: cada entrada dice qué página virtual (y de qué proceso) está en ese marco.
- Su tamaño depende de la RAM, no del espacio virtual. Para buscar hace falta una tabla de dispersión o asociativa.

#### Cómo responderlo en el final
Dibujar la dirección de 3 campos del multinivel, decir que solo se crean las tablas que se usan y comparar con la invertida (depende de la RAM).


---

## Tema 4.3 — Fallo de página


### 4.3.1 Pasos de un fallo de página

> [!abstract] En una frase
> Un **fallo de página** ocurre cuando se accede a una página con V = 0. La MMU lanza una interrupción; el SO valida el acceso, consigue un marco libre (desalojando si hace falta), trae la página desde el disco, actualiza la tabla y **reinicia la instrucción**.

#### Desarrollo
Pasos (cátedra y Tanenbaum):
1. La MMU detecta que el bit de presente = 0 y dispara una **interrupción** al kernel.
2. El hardware guarda el **contador de programa** en la pila; una rutina en ensamblador guarda los **registros**.
3. El SO identifica qué **página virtual** se necesita y verifica que sea **válida** y que el acceso esté **permitido**. Si no, aborta el proceso.
4. Busca un **marco libre**. Si no hay, elige una página a **desalojar** con un algoritmo de reemplazo (4.4).
5. Si la página desalojada está **modificada** (M = 1), la **escribe en disco** antes de reutilizar el marco.
6. Planifica la **lectura** de la página pedida desde el disco. Mientras tanto, puede pasar a ejecutar otro proceso.
7. Cuando llega la interrupción de disco, **actualiza la tabla de páginas** y marca el marco en estado normal.
8. La instrucción que falló vuelve a su estado previo y el contador apunta a ella: **se reinicia**.
9. Al volver a planificar el proceso, la rutina de ensamblador restaura registros y sigue.

> [!tip] Frase para responder en el examen
> "Interrumpe, valida, libera (guardando si M = 1), trae, actualiza la tabla y reinicia la instrucción."

#### Cómo responderlo en el final
Recitar los 6 pasos del parcial (pregunta 26) y, si hay tiempo, los detalles del paso 5 (M = 1 → escribir en disco) y del paso 8 (reinicio).


### 4.3.2 Reinicio de la instrucción y páginas compartidas

> [!abstract] En una frase
> Reiniciar una instrucción es difícil cuando la instrucción **modificó** registros antes del fallo (por ejemplo, un autoincremento). Los diseñadores guardan el contador y qué registros se modificaron. Las páginas se pueden **compartir** (código de una librería) mientras los datos son privados.

#### Desarrollo
- **Problema del backup:** hay que saber si el fallo fue en el **operando** o en la **instrucción**, para dejar el estado como estaba.
- **Autoincremento:** si el incremento ocurrió antes del acceso, hay que **revertirlo** antes de reiniciar. Solución de hardware: un registro guarda el contador previo y otro indica qué registros se incrementaron.
- **Páginas compartidas:** un programa (código) se puede compartir entre procesos; los datos, no. Si el proceso termina y libera páginas compartidas, los demás tendrían fallos masivos: hace falta una estructura especial para llevar cuenta.
- **Área de swap:** puede ser **estática** (una zona fija del disco) o **dinámica** (hay que llevar registro de dónde está cada página en disco).

#### Cómo responderlo en el final
Decir qué es el problema del backup con el autoincremento y mencionar la compartición de páginas como complicación.


---

## Tema 4.4 — Algoritmos de reemplazo de páginas


### 4.4.1 Óptimo, FIFO y anomalía de Belady

> [!abstract] En una frase
> El **óptimo** reemplaza la página que tardará más en volver a usarse (no es implementable, pero sirve de referencia). **FIFO** reemplaza la más antigua en RAM: es simple, pero no mira el uso y puede empeorar al tener más marcos (**anomalía de Belady**).

#### Desarrollo
- **Óptimo:** reemplaza la que **no se va a usar por más tiempo**. Requiere conocer el futuro; se usa para comparar.
- **FIFO:** cola en orden de llegada a RAM. Reemplaza el frente. Problemas: puede sacar una página muy usada solo porque "entró hace mucho", y presenta **anomalía de Belady**.
- **Anomalía de Belady:** con más marcos, puede haber **más** fallos. Ocurre en FIFO, no en los algoritmos de pila (LRU, óptimo).

### Ejemplo clásico de Belady
Cadena de referencias: **1 2 3 4 1 2 5 1 2 3 4 5**
- Con **3 marcos** en FIFO: **9 fallos**.
- Con **4 marcos** en FIFO: **10 fallos**. Más memoria, más fallos.

> [!tip] Cómo se repasa
> Hacé la tabla de marcos paso a paso: en cada referencia, anotá qué queda en RAM. Es el ejercicio que más se pide.

#### Cómo responderlo en el final
"FIFO reemplaza la más antigua; tiene bajo costo pero no mira el uso y puede tener anomalía de Belady: el ejemplo 1 2 3 4 1 2 5 1 2 3 4 5 da 9 fallos con 3 marcos y 10 con 4."

> [!warning] Errores típicos
> - Decir que el óptimo es implementable.
> - Decir que LRU tiene anomalía de Belady: no la tiene.


### 4.4.2 Segunda oportunidad y algoritmo del reloj

> [!abstract] En una frase
> **Segunda oportunidad** es FIFO con el bit **R**: la página más vieja se reemplaza solo si R = 0; si R = 1, se pone R = 0 y se manda al final de la cola. El **reloj** hace lo mismo pero con las páginas en **círculo** y un puntero que avanza: es más eficiente.

#### Desarrollo
### Segunda oportunidad
1. Mirar la página más vieja (frente de la cola).
2. Si **R = 0**: reemplazarla.
3. Si **R = 1**: poner R = 0 y moverla al **final** de la cola ("segunda oportunidad").

**Problema:** si casi todas tienen R = 1, da muchas vueltas antes de encontrar una con R = 0: cuesta CPU.

### Reloj (Clock)
- Las páginas están en un **anillo** y un **puntero** recorre el anillo.
- Si R = 0 → reemplazar y avanzar. Si R = 1 → poner R = 0 y avanzar.
- Es una forma **eficiente** de implementar segunda oportunidad. Puede combinarse con M (reloj mejorado).

#### Cómo responderlo en el final
Dibujar el anillo con los bits R, mover el puntero y explicar el paso de R = 1 → R = 0. Decir que es una aproximación de LRU.


### 4.4.3 NRU, LRU y aging

> [!abstract] En una frase
> **NRU** clasifica las páginas por los bits R y M en cuatro clases y reemplaza de la clase más baja. **LRU** reemplaza la menos usada recientemente; es buen predictor, pero caro de implementar exacto. **Aging** es una aproximación de LRU por software: un contador por página que se desplaza y suma R en cada tick.

#### Desarrollo
### NRU (Not Recently Used)
| Clase | R | M | Descripción |
|---|---|---|---|
| 0 | 0 | 0 | No usada, no modificada |
| 1 | 0 | 1 | No usada recientemente, modificada |
| 2 | 1 | 0 | Usada, no modificada |
| 3 | 1 | 1 | Usada y modificada |

- Se reemplaza una página de la **clase más baja** disponible.
- Periódicamente se pone R = 0 en todas para "olvidar" el pasado.

### LRU (Least Recently Used)
- Reemplaza la que hace **más tiempo** no se usa.
- **Costo:** mantener el orden exacto en cada acceso es caro. Por eso hay aproximaciones.
- **Método de la matriz (Repaso):** matriz n × n. Al usar la página i: poner 1 en **toda la fila i** y 0 en **toda la columna i**. La fila con la **suma más baja** es la menos usada recientemente.

Ejemplo del Repaso con P0…P3, accesos P1, P2, P0, P3: sumas finales 4, 2, 4, 4 → **P1** es la menos usada.

### Aging (NFU, por software)
1. Cada página tiene un **contador** en 0.
2. En cada interrupción de reloj: se **corre el contador a la derecha** y se suma el bit R al bit más significativo.
3. En un fallo, se reemplaza la página con el **contador más chico**.

#### Cómo responderlo en el final
Dar las 4 clases de NRU y decir que LRU es ideal pero caro; aging lo aproxima con contadores. Si piden un ejemplo, usar la matriz del Repaso.

> [!warning] Errores típicos
> - Decir que NRU elige la página menos usada: elige **de la clase más baja**, sin orden fino dentro de la clase.


---

## Tema 4.5 — Tamaño de página y rendimiento


### 4.5.1 Tamaño de página óptimo — s = √(2PE)

> [!abstract] En una frase
> Las páginas chicas reducen la fragmentación interna pero agrandan la tabla de páginas; las grandes hacen lo contrario. El **tamaño óptimo** minimiza la suma de ambas: **s = √(2·P·E)**, donde P es el tamaño medio del proceso y E el tamaño de cada entrada de la tabla.

#### Desarrollo
Modelo (cátedra, parcial 12 y Tanenbaum):
- Pérdida por **fragmentación interna** (promedio): **s / 2**.
- Pérdida por **tabla de páginas**: (P / s) · E.
- **Total:** W(s) = s/2 + P·E/s.
- Derivando e igualando a cero: 1/2 − P·E/s² = 0 ⇒ **s = √(2·P·E)**.

### Ejemplos
| Dato | Resultado |
|---|---|
| P = 8 KB = 8192 bytes, E = 4 bytes (parcial 34) | s = √(2 × 8192 × 4) = √65 536 = **256 bytes** |
| P = 2 MB, E = 16 bytes (TP3, 11) | s = √(2 × 2²¹ × 16) = √2²⁶ = **8 KB** |
| s = 128 KB, E = 8 bytes (Tanenbaum) | ≈ **1448 bytes**; en la práctica se elige 1 KB o 2 KB |

> [!note] En la práctica
> El modelo da un número teórico. Los sistemas reales usan potencias de 2 cercanas (1, 2, 4 u 8 KB). Decilo en el examen escrito.

#### Cómo responderlo en el final
Escribir W(s), derivar, dar s = √(2PE) y resolver el ejemplo de 8 KB y 4 bytes → 256 bytes.


### 4.5.2 Conjunto de trabajo y thrashing

> [!abstract] En una frase
> **Thrashing** es cuando un proceso genera fallos de página cada pocas instrucciones: pasa más tiempo trayendo páginas que ejecutando. El **conjunto de trabajo** es el conjunto de páginas que el proceso usó en sus últimas Δ referencias; asignarle al menos ese conjunto evita el thrashing.

#### Desarrollo
- **Thrashing:** la CPU trabaja poco y el disco mucho. Con multiprogramación, si cada proceso tiene menos marcos que su conjunto, todos empeoran.
- **Modelo de conjunto de trabajo (WSM):** se miran las referencias recientes; el tamaño del conjunto en el tiempo t define cuántos marcos merece el proceso.
- **Asignación local vs. global:** local = cada proceso reemplaza sus propios marcos; global = puede quitarle marcos a otro.
- **Índice de frecuencia de fallos (PFF):** si el proceso falla muy seguido, se le dan más marcos; si casi no falla, se le quitan.
- **Prepaginación vs. paginación por demanda:** prepaginar trae páginas antes de usarlas; demanda espera al fallo.

#### Cómo responderlo en el final
Definir thrashing con su causa (poca RAM para los procesos) y decir que el conjunto de trabajo es la forma de evitarlo asignando marcos según el uso reciente.


---

## Tema 4.6 — Segmentación y esquemas combinados


### 4.6.1 Segmentación

> [!abstract] En una frase
> La **segmentación** divide el espacio lógico en **segmentos** de tamaño variable (código, datos, pila, tablas), cada uno con su base, su longitud y sus permisos. Una dirección es un par **(segmento, desplazamiento)**. Al tener tamaño variable, produce **fragmentación externa**.

#### Desarrollo
- **Ventajas:** refleja la estructura lógica del programa; permite **permisos distintos** por segmento (código solo lectura, pila lectura/escritura); facilita **compartir** segmentos (bibliotecas).
- **Tabla de segmentos:** base, longitud y bits de protección por segmento.
- **Control:** si el desplazamiento ≥ longitud → **trampa** (violación de segmento).
- **Desventaja:** fragmentación externa; por eso la segmentación se combina con paginación (4.6.2).

### Ejercicio resuelto (TP3, 10)
| Segmento | Base | Longitud |
|---|---|---|
| 0 | 23 | 310 |
| 1 | 350 | 600 |
| 2 | 1700 | 700 |
| 3 | 2700 | 68 |
| 4 | 950 | 450 |

| Dirección (segmento, desplazamiento) | Resultado |
|---|---|
| (0, 230) | 23 + 230 = **253** |
| (1, 2) | 350 + 2 = **352** |
| (1, 602) | 602 ≥ 600 → **fuera del segmento** |
| (2, 699) | 1700 + 699 = **2399** |
| (3, 400) | 400 ≥ 68 → **fuera del segmento** |
| (4, 700) | 700 ≥ 450 → **fuera del segmento** |

#### Cómo responderlo en el final
Definir el par (segmento, desplazamiento), dar la regla base + desplazamiento con control de longitud, y mencionar la fragmentación externa como costo.


### 4.6.2 Segmentación con paginación y su combinación

> [!abstract] En una frase
> El esquema más usado (modelo Intel) divide el espacio **primero en segmentos lógicos** y **después pagina cada segmento**. Así se conservan los permisos y la estructura lógica, y se elimina la fragmentación externa.

#### Desarrollo
| Esquema | Primero se divide en | Después |
|---|---|---|
| **Segmentación con paginación** (Intel) | Segmentos lógicos de tamaño variable | Cada segmento se pagina en unidades fijas |
| Paginación con segmentación (menos común) | Páginas fijas | Se agrupan en segmentos lógicos |

- Cada segmento tiene su tabla de páginas; los segmentos pueden cargarse en RAM **de forma no contigua**.
- **Regla práctica (TP3, 9):** una página **no puede contener datos de segmentos distintos**. Por eso el tamaño de página se redondea por segmento.

### Ejemplo (TP3, 9): programa de 16 bits
Código 31 945 bytes, datos 15 386, pila 16 870.
- Con páginas de **4 KB**: 8 + 4 + 5 = **17 páginas** = 69 632 bytes > 65 536 (no entra en 16 bits).
- Con páginas de **256 bytes**: 125 + 61 + 66 = **252 páginas** = 64 512 bytes ≤ 65 536 → **sí entra**.

#### Cómo responderlo en el final
Explicar el orden (segmentos y después páginas), mencionar que elimina la externa, y resolver el ejemplo del programa de 16 bits con las dos páginas.

