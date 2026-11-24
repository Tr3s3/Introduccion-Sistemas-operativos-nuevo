---
tipo: unidad-completa
unidad: 3
---
# Unidad 3 — Administración de memoria (asignación contigua) — completa

> [!abstract] Qué pide la unidad
> Cómo el SO reparte la memoria RAM entre varios procesos sin paginación: relocación y protección, particiones fijas y variables, fragmentación, control de huecos (mapa de bits y listas enlazadas) y algoritmos de asignación. Es la base para entender por qué apareció la memoria virtual (Unidad 4).

> [!info] Cómo leer este archivo
> Es la unidad entera, en orden: Tema → Subtema. Cada subtema tiene su nota propia en la carpeta del tema, por si querés estudiar uno solo.


---

## Tema 3.1 — La memoria como recurso


### 3.1.1 Funciones del administrador de memoria

> [!abstract] En una frase
> El **administrador de memoria** lleva la cuenta de qué memoria está en uso y cuál libre, la asigna y desasigna a los procesos, y permite **intercambiar** procesos con el disco cuando no alcanza la RAM.

#### Desarrollo
Funciones (cátedra, Procesos y memoria):
1. Registrar la memoria **en uso**.
2. Registrar la memoria **disponible**.
3. **Asignar** memoria a los procesos.
4. **Desasignar** memoria al terminar.
5. **Swapping:** intercambio entre memoria principal y disco.

**Requisitos de diseño:**
- **Transparencia:** varios procesos conviven en memoria y ninguno debe saber que es compartida; cada uno corre sin importar cuántos hay ni dónde están.
- **Seguridad:** ningún proceso puede corromper a otro.
- **Eficiencia:** ni la CPU ni la memoria deben desperdiciarse por ser compartidas.

> [!note] Ley de Parkinson (cátedra)
> "Los programas van creciendo de forma tal que ocupan la memoria disponible." La memoria es un recurso **escaso** aunque cada vez sea más grande.

#### Cómo responderlo en el final
Enumerar las 5 funciones y, para el "por qué", los tres requisitos: transparencia, seguridad y eficiencia.


### 3.1.2 Monoprogramación y sin abstracción de memoria

> [!abstract] En una frase
> Sin abstracción de memoria, el programa usa **direcciones físicas** directamente. La forma más simple es la **monoprogramación**: un proceso de usuario más el SO en memoria. Cuando ese proceso espera E/S, la CPU queda ociosa.

#### Desarrollo
Tres formas de organizar la memoria con un solo proceso (Tanenbaum y cátedra):
- **(a)** SO en la parte baja de la RAM (usado en mainframes; hoy casi no).
- **(b)** SO en ROM en la parte alta y el resto en RAM (palmtops e integrados).
- **(c)** Parte del SO en ROM (**BIOS**) y el resto en RAM abajo (primeras PC con MS-DOS).

**Problemas:**
- **Ineficiencia:** mientras espera E/S, la CPU no hace nada.
- **Riesgo:** en (a) y (c) un error del programa de usuario puede sobrescribir el SO.

**Multiprogramación sin abstracción:** es posible con **intercambio** (guardar todo el contenido de la memoria en disco y traer el siguiente programa) o con **hardware especial**: la IBM 360 dividía la RAM en bloques de 2 KB con una **llave de protección de 4 bits** cada uno.

#### Cómo responderlo en el final
"Sin abstracción, el programa ve la memoria física. Con un solo proceso la CPU se desperdicia en las E/S; para varios hace falta intercambio o protección por hardware."


---

## Tema 3.2 — Relocación y protección


### 3.2.1 Registros base y límite

> [!abstract] En una frase
> La multiprogramación plantea dos problemas: **relocación** (el mismo programa debe poder cargarse en cualquier dirección) y **protección** (ningún proceso debe acceder a la memoria de otro). Se resuelven con dos registros de hardware: **base** y **límite**.

#### Desarrollo
- **Relocación:** las direcciones del programa son **relativas**. Al cargarlo, se suma la base. Dos procesos con las mismas direcciones relativas viven en lugares distintos.
- **Protección:** antes de usar una dirección, el hardware verifica que caiga dentro del límite. Si no, hay una **trampa** (excepción) y el SO aborta el proceso.
- **Funcionamiento:** cuando el planificador elige un proceso, el SO **carga** base y límite con los valores de ese proceso.

**Dirección física = base + dirección generada por el programa**, con la condición de que la dirección generada sea menor que el límite.

> [!note] Dos formas de ver el límite
> La cátedra lo llama "registro límite" y lo describe como el **tamaño** de la partición; Tanenbaum lo describe como la **dirección superior**. En el examen, decí cuál usás y verificá que la comparación sea coherente.

#### Cómo responderlo en el final
Dibujar la suma base + dirección, marcar la comparación con el límite y decir que el SO recarga ambos registros en cada cambio de proceso.

> [!warning] Errores típicos
> - Decir que el registro base guarda la dirección del proceso: guarda el **inicio de la partición**.


---

## Tema 3.3 — Particiones fijas y variables


### 3.3.1 Particiones fijas

> [!abstract] En una frase
> Con **particiones fijas** la memoria se divide, antes de empezar, en bloques de tamaño fijo. Cada trabajo ocupa una partición; si no cabe en ninguna libre, espera en cola. Su defecto es la **fragmentación interna**.

#### Desarrollo
- Se divide la RAM en N particiones de tamaño fijo (en TP2, 128 MB).
- Llega un trabajo: si cabe en una partición libre, entra. Si no hay ninguna libre pero el trabajo **no excede el tamaño de la partición**, espera a que una se libere (TP2, pregunta 3b).
- **Problema:** un trabajo de 100 MB en una partición de 128 MB desperdicia 28 MB dentro de la partición: **fragmentación interna**.

#### Cómo responderlo en el final
Describir la división fija, la cola de espera y el desperdicio dentro de la partición, con el ejemplo de 128 MB.


### 3.3.2 Particiones variables, swapping y compactación

> [!abstract] En una frase
> Con **particiones variables** cada proceso recibe exactamente lo que pide, y las particiones cambian de tamaño y de ubicación a medida que entran y salen procesos. Cuando la memoria queda con huecos dispersos, se usa **compactación** para juntarlos.

#### Desarrollo
- Cada trabajo recibe un bloque a su medida: no hay fragmentación interna, pero sí aparecen **huecos** entre procesos.
- **Swapping:** un proceso completo se mueve a disco para liberar RAM y se trae de vuelta después. Es costoso por la lentitud del disco (Tanenbaum: un disco SATA de 100 MB/s tarda ~10 s en mover 1 GB).
- **Compactación:** se mueven los procesos para juntar los huecos en un bloque libre contiguo. Su costo es copiar memoria byte a byte.
- Un segmento que **crece** (pila o heap) necesita espacio libre contiguo al final, o se reubica (cátedra, Swapping).

### Costo de la compactación (TP2, pregunta 5)
Con 1 GB, compactación cada 3 minutos y 150 ns por byte copiado: el tiempo de CPU es (bytes copiados × 150 ns) / 180 s. Si el 75 % de la memoria está en uso, se copian ≈ 805 MB ≈ 120 s por compactación: **≈ 67 % del tiempo de CPU**. Mostrá el método; el número depende de qué bytes asumas copiados.

#### Cómo responderlo en el final
Explicar el beneficio (sin fragmentación interna) y el costo (huecos externos, swapping, compactación), y cerrar con que la compactación es cara.


### 3.3.3 Fragmentación interna y externa

> [!abstract] En una frase
> **Fragmentación interna:** se asigna más de lo que se necesita y lo sobrante queda adentro del bloque, sin uso. **Fragmentación externa:** hay memoria libre total suficiente, pero repartida en huecos no contiguos que ninguno alcanza solo.

#### Desarrollo
| | Interna | Externa |
|---|---|---|
| Dónde aparece | Particiones fijas, paginación | Particiones variables, segmentación |
| Qué pasa | El bloque es más grande que el pedido | Hay huecos chicos sueltos |
| Ejemplo | Partición de 128 KB para 100 KB: **28 KB perdidos** | Huecos de 10, 5 y 12 KB con total 27 KB; llega un proceso de 20 KB: **no entra** |
| Solución | Bloques más chicos | Compactación, o paginación |

**Cuidado:** la misma memoria puede tener las dos según el esquema. La paginación elimina la externa, pero deja la interna (la última página de un proceso no se llena).

#### Cómo responderlo en el final
Dar la definición de cada una con su ejemplo numérico y la tabla de dónde aparece.

> [!warning] Errores típicos
> - Decir que la paginación no tiene fragmentación: tiene **interna**.


---

## Tema 3.4 — Control de la memoria libre


### 3.4.1 Mapa de bits

> [!abstract] En una frase
> El **mapa de bits** divide la memoria en unidades de asignación fijas; cada unidad tiene un bit (0 = libre, 1 = ocupada). Para asignar un proceso de k unidades hay que buscar **k ceros consecutivos**.

#### Desarrollo
- **Tamaño del mapa:** 1 bit por unidad; **no depende** de cuántos procesos haya.
- **Elegir la unidad:** si es muy chica, el mapa crece; si es muy grande, se desperdicia memoria por fragmentación interna. No conviene agrandarla solo para achicar el mapa.
- **Desventaja principal:** la búsqueda de k ceros consecutivos es **lenta**, porque puede recorrer todo el mapa.

#### Cómo responderlo en el final
Dibujar un mapa con 0/1 y explicar que buscar k ceros seguidos es el costo. Remarcar que su tamaño es fijo.


### 3.4.2 Listas enlazadas

> [!abstract] En una frase
> Una **lista enlazada** recorre la memoria por segmentos, cada uno marcado como **P** (proceso) o **H** (hueco), ordenados por dirección. Su tamaño crece con la cantidad de procesos, pero se pueden agregar optimizaciones para buscar más rápido.

#### Desarrollo
- Cada entrada indica: si es **P** o **H**, dirección de inicio y tamaño (y un puntero al siguiente).
- **Al terminar un proceso** hay cuatro casos: el hueco se une con el de arriba, con el de abajo, con ambos, o queda aislado (H P P H → se fusiona según vecinos).
- **Ventaja en espacio:** con pocos procesos ocupa menos que un mapa de bits. **Desventaja:** con muchos procesos supera al mapa.
- **Optimizaciones** (sacrificando espacio): mantener la lista **ordenada por tamaño**, usar **dos listas** (procesos y huecos), o un índice de huecos.

### Mapa vs. lista (comparación del Repaso)
| | Mapa de bits | Lista enlazada |
|---|---|---|
| Tamaño | Fijo (depende de la memoria) | Crece con los procesos |
| Velocidad | Lenta (buscar ceros) | Rápida con optimizaciones |
| Pocos procesos | Ocupa lo mismo | Ocupa menos |

#### Cómo responderlo en el final
Comparar con la tabla y decir que el mapa es fijo y lento, la lista crece pero se puede acelerar.


---

## Tema 3.5 — Algoritmos de asignación


### 3.5.1 Primer ajuste, próximo ajuste, mejor ajuste y peor ajuste

> [!abstract] En una frase
> Cuando llega un proceso, el SO elige un hueco entre los que alcanzan: **first fit** el primero que sirva; **next fit** el primero desde la última búsqueda; **best fit** el más chico que sirva; **worst fit** el más grande.

#### Desarrollo
| Algoritmo | Criterio | Velocidad | Efecto sobre la memoria |
|---|---|---|---|
| **First fit** | El primer hueco que alcanza | Rápido (se detiene al encontrar) | Tiende a dejar huecos chicos al principio de la lista |
| **Next fit** | Como first fit, pero arranca donde terminó la última búsqueda | Rápido | Reparte mejor los huecos |
| **Best fit** | El hueco más chico que alcanza | **Lento** (recorre toda la lista) | Deja muchos huecos **muy chicos**, inutilizables |
| **Worst fit** | El hueco más grande | Lento (también recorre todo) | Deja huecos grandes para futuros procesos |

### Ejercicio resuelto (TP2, pregunta 4)
Huecos en orden: 800, 300, 1500, 600, 700, 1000, 1200 KB. Procesos: 1000, 800 y 700 KB.

| Algoritmo | 1000 KB | 800 KB | 700 KB |
|---|---|---|---|
| First fit | 1500 (sobran 500) | 800 (exacto) | 700 (exacto) |
| Next fit | 1500 (sobran 500) | 1000 (sobran 200) | 1200 (sobran 500) |
| Best fit | 1000 (exacto) | 800 (exacto) | 700 (exacto) |
| Worst fit | 1500 (sobran 500) | 1200 (sobran 400) | 1000 (sobran 300) |

**Lectura:**
- **Más rápido:** first fit (se detiene en el primero que sirve). **Más lento:** best fit y worst fit (recorren toda la lista). Next fit es rápido, aunque puede recorrer más que first fit.
- **Mejor aprovechamiento en este caso:** **best fit**, porque no deja sobrante en ninguna asignación.
- **Mejora de worst fit (d):** conservar el hueco sobrante como lista de huecos grandes; es lo que lo hace útil. Estadísticamente, deja huecos grandes que sirven para procesos grandes futuros.

> [!note] Cómo se responde "¿cuál es más rápido?"
> La cátedra no da una proporción exacta; decí "first fit se detiene en el primer hueco que sirve; best y worst recorren los n huecos siempre" y, si te piden un número, usá n como factor.

#### Cómo responderlo en el final
Mostrar la tabla de los cuatro algoritmos con el ejemplo y decir cuál aprovecha mejor y por qué.

> [!warning] Errores típicos
> - Decir que best fit es el más rápido: es el que más recorre.


### 3.5.2 Quick fit y buddy system

> [!abstract] En una frase
> **Quick fit** mantiene listas separadas de los tamaños más pedidos para acelerar la búsqueda. **Buddy system** usa bloques de tamaño **potencia de 2** que se dividen en "compañeros" (buddies) y se vuelven a unir al liberar, lo que facilita la fusión.

#### Desarrollo
- **Quick fit:** listas de huecos por tamaño frecuente. Búsqueda rápida, pero **cuesta unir huecos vecinos** al liberar.
- **Buddy:** listas de bloques libres de tamaños 2⁰, 2¹, …, 2ᵏ hasta el tamaño de la memoria. Para una memoria de 1 MB hacen falta **21 listas** (de 1 byte a 1 MB, potencias de 2 que van de 2⁰ a 2²⁰).
- **Ejemplo:** un proceso de 70 KB usa un bloque de **128 KB**, que es el que más se aproxima (la potencia de 2 superior). Si no hay de 128, se divide uno de 256 en dos de 128.
- **Ventaja:** dos buddies libres se unen fácilmente, porque solo hay que mirar el compañero.
- **Desventaja:** cada asignación se redondea a potencia de 2, y eso produce **fragmentación interna**.

#### Cómo responderlo en el final
Dar el ejemplo de 70 KB → 128 KB y decir que la unión es sencilla. Mencionar la fragmentación interna como costo.

