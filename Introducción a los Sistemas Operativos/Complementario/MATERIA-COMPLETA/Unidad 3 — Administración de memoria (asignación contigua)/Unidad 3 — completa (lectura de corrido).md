---
tipo: lectura-corrida
unidad: 3
---
# Unidad 3 — completa (lectura de corrido)

> [!abstract] Fuente
> Desarrollada a partir de las **diapositivas de cátedra** (Procesos y Memoria, sección administración de memoria) y complementada con explicaciones, ejemplos, trampas de examen y libro (Tanenbaum). Ver [[00 Fuente - Temario de diapositivas]].

---

# 3.1.1 Funciones del administrador de memoria

> [!abstract] En una frase
> El **administrador de memoria** del SO controla qué partes de la RAM están libres u ocupadas, asigna y libera memoria para procesos, y soporta mecanismos como swapping, protegiendo y usando eficientemente el recurso.

## Diapositivas de cátedra

### Introducción a memoria

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_15.png]]

Un programa debe cargarse en memoria para ejecutarse. La CPU accede directamente a memoria principal y registros; la memoria es más lenta que los registros, y el cache se ubica en el medio.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_16.png]]

La memoria ideal sería grande, rápida y no volátil. En la práctica es un **recurso escaso**: los programas crecen (Ley de Parkinson) y se necesitan mecanismos eficientes de administración.

### Funciones del administrador

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_17.png]]

La diapositiva enumera las funciones:
- Registro de la memoria en uso.
- Registro de la memoria disponible.
- Asignación de memoria a los procesos.
- Desasignación de memoria a los procesos.
- **Swapping:** intercambio entre memoria principal y disco.

### Consideraciones

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_18.png]]

- **Transparencia:** varios procesos deben coexistir sin necesitar saber que la memoria es compartida.
- Cada proceso debe ejecutarse sin considerar cuántos procesos hay ni su ubicación.
- **Seguridad:** ningún proceso debe corromper a otro.
- **Eficiencia:** CPU y memoria no deben usarse menos eficientemente por ser compartidas.

## Complemento de libro (Tanenbaum)
Tanenbaum enmarca la administración de memoria como un problema de abstracción, asignación, protección y eficiencia. Estas funciones son la base de particiones, paginación y memoria virtual.

## Cómo responderlo en el final
Enumerá funciones (registrar, asignar, liberar, swapping) y consideraciones (transparencia, protección, eficiencia). Si te piden ejemplo, usá asignación/liberación ante creación/terminación de procesos.

> [!warning] Errores típicos
> - Limitar el administrador de memoria a “reservar RAM” sin mencionar protección o transparencia.
> - Olvidar swapping como mecanismo de apoyo.


---

# 3.1.2 Monoprogramación y sin abstracción de memoria

> [!abstract] En una frase
> En **monoprogramación** hay un solo proceso de usuario en memoria junto al SO; es simple pero desaprovecha la CPU cuando el proceso espera E/S.

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_19.png]]

La diapositiva muestra monoprogramación sin abstracción de memoria:
- Uso ineficiente de la CPU.
- Un proceso usuario + SO en memoria.
- Cuando el proceso espera por E/S → CPU ociosa.
- Presenta tres formas de organizar la memoria con un solo proceso.

## Limitaciones

| Aspecto | Monoprogramación |
|---|---|
| Simplicidad | Alta |
| Uso de CPU | Bajo si hay E/S |
| Protección/reubicación | Más simple, pero limitada |
| Concurrencia | No hay múltiples procesos de usuario |

## Complemento de libro (Tanenbaum)
Tanenbaum contrasta este esquema con multiprogramación: cargar varios procesos permite solapar CPU y E/S, pero obliga a resolver reubicación, protección y asignación dinámica.

## Cómo responderlo en el final
“Monoprogramación: un solo proceso usuario en memoria. Es simple, pero si espera E/S la CPU queda ociosa. Por eso se pasa a multiprogramación”.

> [!warning] Errores típicos
> - Confundir monoprogramación con monousuario.
> - No mencionar el motivo principal para abandonarla: CPU ociosa por E/S.


---

# 3.2.1 Registros base y límite

> [!abstract] En una frase
> Los registros **base** y **límite** permiten reubicar un proceso en memoria y protegerlo: la dirección física se calcula como base + dirección lógica, controlando que no supere el límite.

## Diapositivas de cátedra

### Problemas de multiprogramación

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_25.png]]

La multiprogramación introduce dos problemas:
- **Relocación:** direcciones relativas según la partición donde se carga el programa.
- **Protección:** impedir que un proceso acceda a memoria de otro.

### Solución por hardware

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_26.png]]

- **Registro base:** almacena la dirección de inicio de la partición.
- **Registro límite:** almacena el tamaño de la partición.
- Al planificar un proceso, el SO carga ambos registros.
- Dirección física = **base + dirección generada por el programa**.
- El SO/hardware controla que no supere el límite.

### Ejemplos de reubicación

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_27.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_28.png]]

Las diapositivas muestran procesos con mismas direcciones relativas cargados en distintas posiciones físicas, resolviendo la relocación.

## Resumen

| Registro | Función | Protege/Resuelve |
|---|---|---|
| **Base** | Suma al offset lógico | Relocación |
| **Límite** | Verifica tamaño máximo | Protección |

## Complemento de libro (Tanenbaum)
Tanenbaum explica esta técnica como la forma simple de dar a cada proceso un espacio de direcciones propio en asignación contigua. Es eficiente, pero limitada frente a fragmentación y necesidades de memoria virtual.

## Cómo responderlo en el final
“Base contiene inicio de partición y límite su tamaño. Dirección física = base + lógica. Si supera límite, hay protección/fallo. Así se resuelve relocación y protección en particiones contiguas”.

> [!warning] Errores típicos
> - Olvidar verificar el límite (solo sumar base no protege).
> - Confundir dirección lógica con física.


---

# 3.3.1 Particiones fijas

> [!abstract] En una frase
> En **particiones fijas**, la memoria se divide previamente en bloques de tamaño fijo (iguales o distintos); son simples, pero pueden generar **fragmentación interna**.

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_24.png]]

La diapositiva plantea la organización de memoria para multiprogramación y menciona como primera aproximación las **particiones fijas** (sin swapping o intercambio de páginas).

## Características

| Aspecto | Particiones fijas |
|---|---|
| Tamaño | Definido al inicio (fijo) |
| Asignación | Un proceso ocupa una partición |
| Ventaja | Simple de administrar |
| Desventaja | Fragmentación interna; límite de procesos/tamaños |

## Fragmentación interna

Si un proceso ocupa menos que su partición, el sobrante dentro de la partición se desperdicia. Ej.: partición 128 KB, proceso 100 KB → 28 KB internos.

## Complemento de libro (Tanenbaum)
Tanenbaum distingue particiones fijas de igual tamaño y de tamaños distintos, y analiza colas por partición o cola única. El problema principal es la rigidez frente a cargas variables.

## Cómo responderlo en el final
“Particiones fijas: memoria dividida en bloques predefinidos. Simples, pero generan fragmentación interna y poca flexibilidad”.

> [!warning] Errores típicos
> - Confundir fragmentación interna (dentro de la partición) con externa (huecos entre particiones/procesos).


---

# 3.3.2 Particiones variables, swapping y compactación

> [!abstract] En una frase
> En **particiones variables**, cada proceso recibe el tamaño que necesita; al entrar/salir procesos aparecen huecos, por lo que se usan **swapping** y a veces **compactación**.

## Diapositivas de cátedra

### Particiones variables y swapping

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_30.png]]

La diapositiva indica:
- La cantidad de particiones, sus tamaños y ubicaciones cambian dinámicamente.
- **Swapping/intercambio:** mover un proceso entre memoria y disco.
- **Compactación:** unir procesos en memoria para que el espacio disponible quede adyacente.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_31.png]]

La asignación cambia a medida que procesos entran o salen de memoria.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_32.png]]

También se considera el caso de segmentos/procesos que pueden crecer, lo que complica la asignación.

## Swapping

| Acción | Efecto |
|---|---|
| **Swap out** | Saca proceso de RAM a disco |
| **Swap in** | Trae proceso de disco a RAM |
| **Beneficio** | Más procesos activos lógicamente que RAM disponible |
| **Costo** | E/S de disco, tiempo, reubicación |

## Compactación

- Junta huecos libres en uno solo.
- Reduce fragmentación externa.
- Costosa: hay que mover memoria y actualizar referencias/base.

## Complemento de libro (Tanenbaum)
Tanenbaum resalta que las particiones variables eliminan la fragmentación interna fija, pero introducen **fragmentación externa** y la necesidad de algoritmos de asignación.

## Cómo responderlo en el final
“Particiones variables asignan tamaño exacto al proceso. Con el tiempo quedan huecos: swapping mueve procesos a disco y compactación junta huecos, pero compactar es costoso”.

> [!warning] Errores típicos
> - Decir que compactación es gratis.
> - Confundir swapping con paginación.


---

# 3.3.3 Fragmentación interna y externa

> [!abstract] En una frase
> La **fragmentación interna** es espacio desperdiciado dentro de una unidad asignada; la **fragmentación externa** son huecos libres dispersos que impiden asignar un bloque contiguo grande.

## Diapositiva de cátedra (contexto)

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_30.png]]

El cambio dinámico de particiones y los huecos que quedan al entrar/salir procesos explican la aparición de fragmentación externa y la necesidad de compactación.

## Comparación

| Tipo | Dónde ocurre | Causa típica | Ejemplo | Mitigación |
|---|---|---|---|---|
| **Interna** | Dentro del bloque asignado | Partición fija/página mayor que lo necesario | Bloque 128 KB, proceso 100 KB → 28 KB | Tamaños adecuados, paginación |
| **Externa** | Entre bloques asignados | Huecos dispersos en particiones variables | Huecos 10+5+12 KB, proceso 20 KB no entra | Compactación, paginación |

## Regla práctica

- Si el sobrante está **dentro** de lo asignado → interna.
- Si el sobrante está **fuera**, en huecos libres separados → externa.

## Complemento de libro (Tanenbaum)
Tanenbaum relaciona fragmentación externa con asignación contigua variable y segmentación; la paginación la elimina casi por completo, pero deja fragmentación interna en la última página.

## Cómo responderlo en el final
Definí ambas, da un ejemplo numérico breve y mencioná la mitigación: compactación para externa, mejor ajuste de tamaños/paginación para interna.

> [!warning] Errores típicos
> - Invertir las definiciones.
> - Decir que la paginación elimina toda fragmentación (queda interna en la última página).


---

# 3.4.1 Mapa de bits

> [!abstract] En una frase
> Un **mapa de bits** representa la memoria como unidades fijas: cada bit indica si la unidad está libre (0) u ocupada (1).

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_33.png]]

La diapositiva explica:
- Divide la memoria en unidades de asignación fija.
- A cada unidad le corresponde un bit: 0 = no usado, 1 = usado.
- Asignar implica buscar $k$ bits consecutivos en 0.
- **Desventaja:** lento buscar huecos.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_35.png]]

Ejemplo con mapa de bits y lista enlazada para los mismos procesos/huecos.

## Características

| Aspecto | Mapa de bits |
|---|---|
| Estructura | Vector de bits |
| Tamaño | Fijo, depende de memoria/unidad |
| Búsqueda | Buscar corrida de 0s |
| Ventaja | Simple, tamaño fijo |
| Desventaja | Búsqueda puede ser lenta |

## Complemento de libro (Tanenbaum)
Tanenbaum compara mapa de bits con listas enlazadas: el mapa es compacto cuando la unidad es chica, pero la búsqueda de una corrida puede costar. El tamaño de unidad es un compromiso: chica = mapa grande; grande = más fragmentación interna.

## Cómo responderlo en el final
“Mapa de bits: 1 bit por unidad de asignación. 0 libre, 1 ocupado. Para asignar se busca una corrida de 0s. Es simple, pero buscar puede ser lento”.

> [!warning] Errores típicos
> - Olvidar que el tamaño del mapa depende del tamaño de unidad elegida.
> - Confundir 0/1 al revés (aclarar convención).


---

# 3.4.2 Listas enlazadas

> [!abstract] En una frase
> Una **lista enlazada** de memoria mantiene nodos para huecos (H) y procesos (P), indicando inicio, tamaño y enlace; facilita fusión de huecos al liberar memoria.

## Diapositivas de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_34.png]]

La diapositiva muestra la estructura: P = proceso, H = hueco; ordenada por dirección.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_35.png]]

Compara mapa de bits y lista enlazada para el mismo estado de memoria.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_36.png]]

Cuando un proceso termina, hay 4 posibles casos de unión con huecos adyacentes:
1. Huecos a ambos lados → fusionar en uno.
2. Hueco a la izquierda → fusionar.
3. Hueco a la derecha → fusionar.
4. Sin huecos adyacentes → crear nodo hueco.

## Comparación con mapa de bits

| Aspecto | Mapa de bits | Lista enlazada |
|---|---|---|
| Tamaño | Fijo | Variable |
| Representa | Unidades | Segmentos P/H |
| Fusión | Ajustar bits | Fusionar nodos |
| Búsqueda | Corrida de 0s | Recorrer lista |

## Complemento de libro (Tanenbaum)
Tanenbaum señala que las listas pueden ordenarse por dirección (facilita coalescing) o por tamaño (facilita best/worst fit). La elección impacta en velocidad y fragmentación.

## Cómo responderlo en el final
“Lista enlazada: nodos P/H con dirección y tamaño. Al liberar, se fusionan huecos adyacentes. Es flexible, pero su tamaño depende de la cantidad de segmentos”.

> [!warning] Errores típicos
> - No considerar los 4 casos de fusión al terminar un proceso.
> - Confundir lista ordenada por dirección con ordenada por tamaño.


---

# 3.5.1 Primer ajuste, próximo ajuste, mejor ajuste y peor ajuste

> [!abstract] En una frase
> Son algoritmos para elegir en qué hueco colocar un proceso: **first fit**, **next fit**, **best fit** y **worst fit**.

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_37.png]]

La diapositiva define:
- **Primer ajuste (first fit):** el primer hueco en que cabe.
- **Próximo ajuste (next fit):** similar, pero empieza desde el último encontrado.
- **Mejor ajuste (best fit):** busca el hueco que más se ajusta; más lento porque recorre toda la lista; puede dejar huecos muy chicos.
- **Peor ajuste (worst fit):** busca que resulten huecos grandes.

## Comparación

| Algoritmo | Estrategia | Velocidad | Fragmentación típica |
|---|---|---|---|
| **First fit** | Primer hueco suficiente | Rápido | Huecos chicos al inicio |
| **Next fit** | Desde última posición | Rápido/medio | Distribuye, puede fragmentar más |
| **Best fit** | Hueco más chico suficiente | Lento | Muchos restos pequeños |
| **Worst fit** | Hueco más grande | Lento | Rompe huecos grandes |

## Complemento de libro (Tanenbaum)
Tanenbaum comenta que first fit suele funcionar bien en la práctica; best fit tiende a crear muchos huecos diminutos; worst fit no es tan bueno como suena. La performance depende de la carga.

## Cómo responderlo en el final
Definí los 4, nombrá criterio y una ventaja/desventaja. Si te dan ejemplo, simulá la lista de huecos paso a paso y mostrala.

> [!warning] Errores típicos
> - Confundir best fit con “mejor en general”.
> - Olvidar que next fit continúa desde la última asignación.


---

# 3.5.2 Quick fit y buddy system

> [!abstract] En una frase
> **Quick fit** mantiene listas separadas para tamaños frecuentes; **buddy system** asigna bloques en potencias de 2, facilitando la fusión.

## Diapositivas de cátedra

### Quick fit

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_38.png]]

- Listas separadas para huecos de medidas requeridas frecuentemente.
- Es rápido para esos tamaños.
- Dificulta la unión al terminar, porque está ordenado por medida/tipo.

### Buddy system

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_39.png]]

- Listas de bloques libres de $2^0, 2^1, 2^2, ..., 2^k$ hasta el tamaño de memoria.
- Ejemplo: memoria de 1 MB → 21 listas de 1 byte a 1 MB.
- Un proceso de 70 KB usa un bloque de 128 KB (potencia de 2 más cercana).
- Si no hay de 128 KB, toma uno de 256 KB, lo divide en dos de 128 KB y usa uno.
- Se facilita la unión de bloques contiguos (buddies).

## Comparación

| Algoritmo | Ventaja | Desventaja |
|---|---|---|
| **Quick fit** | Asignación rápida para tamaños comunes | Fusión/coalescing difícil |
| **Buddy system** | Fusión simple (buddies) | Fragmentación interna por redondeo a potencia de 2 |

## Complemento de libro (Tanenbaum)
Tanenbaum describe buddy system como un compromiso práctico: rápido para asignar/liberar y fusionar, pero con desperdicio interno. Se usa en allocators reales (variantes en kernels).

## Cómo responderlo en el final
“Quick fit: listas por tamaños frecuentes, rápido pero difícil de fusionar. Buddy: potencias de 2, fácil fusión, pero puede desperdiciar por redondeo”.

> [!warning] Errores típicos
> - Decir que buddy no tiene fragmentación interna.
> - No mencionar la condición de “buddy” (mismo tamaño y alineación adecuada) al fusionar.


---
