---
tipo: teoria
---

# Respuestas detalladas — Teoría de final

> [!abstract] Cómo usar este archivo
> Acá están las respuestas de [[01 Preguntas de teoria]]. Para el examen escrito usá la estructura: **definición → cómo funciona → por qué existe/límite/trampa**. Si hay cálculo, agregá fórmula y unidades.

## A. Conceptos base y estructura del SO

### 1. ¿Qué es un sistema operativo? ¿Qué funciones principales cumple?
**Definición.** El SO es el software base que administra los recursos del hardware y brinda servicios a los programas y usuarios.

**Funciones principales.**
- **Administrar recursos:** CPU, memoria, discos, dispositivos de E/S, archivos.
- **Abstraer el hardware:** ofrece una interfaz más simple y segura que el hardware crudo.
- **Aislar y proteger:** evita que un proceso dañe a otros o al sistema.
- **Proveer servicios:** syscalls, sistema de archivos, comunicación, planificación, seguridad.

**Respuesta corta.** “El SO administra hardware y recursos, provee servicios a programas/usuarios y aísla procesos para que el sistema sea seguro y eficiente.”

### 2. ¿Qué diferencia hay entre modo usuario y modo kernel? ¿Por qué existe esa separación?
**Definición.** Son dos modos de ejecución de la CPU con distintos privilegios.

| Modo | Qué puede hacer | Quién lo usa |
|---|---|---|
| **Usuario** | Ejecutar instrucciones normales; no accede directo al hardware crítico | Programas/aplicaciones |
| **Kernel** | Ejecutar instrucciones privilegiadas, acceder a hardware, manejar memoria/interrupciones | Núcleo del SO |

**Por qué existe.** Protege al sistema: un error o programa malicioso en modo usuario no debería poder apagar la máquina, tocar memoria ajena o controlar dispositivos directamente.

**Trampa.** La CPU cambia a modo kernel por interrupciones, excepciones/traps o syscalls; no es “el programa elige” libremente.

### 3. ¿Qué es una llamada al sistema (syscall)? Da ejemplos y explicá si `time`/`date` es una syscall.
**Definición.** Una syscall es la interfaz controlada por la cual un programa en modo usuario pide un servicio al kernel.

**Cómo funciona.** Programa → librería/wrapper → instrucción de trap/syscall → CPU pasa a modo kernel → kernel valida y ejecuta → retorna a modo usuario.

**Ejemplos.** `fork`, `execve`, `read`, `write`, `open`, `waitpid`, `exit`.

**`time`/`date`.** No son syscalls: son comandos/programas. Pueden usar syscalls o servicios del SO para obtener la hora del reloj del sistema.

**Trampa.** “Syscall” no es cualquier función de biblioteca; la syscall es el cruce controlado al kernel.

### 4. ¿Qué diferencia hay entre kernel y shell? ¿El shell es parte del SO?
**Kernel.** Núcleo del SO; corre en modo kernel; administra recursos.

**Shell.** Intérprete de comandos; corre en modo usuario; recibe comandos del usuario y lanza programas (usando syscalls como `fork/exec/wait`).

**¿Es parte del SO?** No estrictamente del kernel. Es un programa del sistema / interfaz de usuario. En el examen escrito, aclarar: “el shell no es el kernel; es una interfaz en modo usuario”.

### 5. ¿Qué es una interrupción? Diferenciá interrupción de hardware, excepción/trap y syscall.
**Interrupción.** Señal que altera el flujo normal de ejecución para que la CPU atienda un evento.

| Tipo | Origen | Ejemplo |
|---|---|---|
| **Interrupción de hardware** | Dispositivo externo | Teclado, disco, timer |
| **Excepción / trap** | Evento generado por CPU/programa | División por cero, fallo de página, instrucción inválida |
| **Syscall** | Pedido explícito del programa | `read`, `write`, `fork` |

**Respuesta corta.** “Todas interrumpen el flujo normal, pero difieren en origen: hardware externo, condición interna/trap, o pedido deliberado al kernel.”

### 6. ¿Qué es DMA y qué problema resuelve frente a E/S programada e interrupciones?
**DMA (Direct Memory Access).** Controlador que permite transferir datos entre dispositivo y memoria sin que la CPU copie byte a byte.

| Técnica | Quién mueve datos | Problema |
|---|---|---|
| **E/S programada** | CPU | CPU queda ocupada esperando/copando |
| **E/S por interrupciones** | CPU, pero por bloques/eventos | Mejor que programada, pero CPU sigue interviniendo |
| **DMA** | Controlador DMA | CPU inicia la operación y se libera; DMA interrumpe al finalizar |

**Por qué importa.** Hace viable la multiprogramación: mientras un dispositivo transfiere datos, la CPU puede ejecutar otro proceso.

### 7. ¿Qué es el spooling? ¿En qué generación aparece y por qué es importante?
**Definición.** Spooling (Simultaneous Peripheral Operations On-Line) es la técnica de poner trabajos/datos en un buffer en disco para desacoplar un dispositivo lento de la CPU.

**Generación.** Se asocia fuerte a la **3.ª generación** (sistemas con multiprogramación/batch más avanzados).

**Importancia.** La CPU no espera al dispositivo lento (ej. impresora, lectoras antiguas). Mejora el aprovechamiento de CPU y permite que varios trabajos compartan el dispositivo de forma ordenada.

### 8. ¿Qué es la multiprogramación? ¿Qué problema resuelve y qué relación tiene con el spooling?
**Definición.** Técnica de mantener varios procesos en memoria para que, cuando uno espera E/S, la CPU ejecute otro.

**Problema que resuelve.** Evita que la CPU quede ociosa durante esperas de E/S.

**Relación con spooling.** El spooling alimenta/organiza trabajos en disco, especialmente para dispositivos lentos; la multiprogramación aprovecha esas esperas para ejecutar otros procesos. Juntos mejoran la utilización del sistema.

**Métrica típica.** $U = 1 - p^n$.

### 9. ¿Qué es una máquina virtual? Diferenciá hipervisor/VMM de JVM/CLR.
**Máquina virtual.** Software que ofrece una abstracción de máquina: puede emular hardware completo o un entorno de ejecución.

| Tipo | Qué virtualiza | Ejemplos |
|---|---|---|
| **VM de sistema / hipervisor / VMM** | Hardware completo; ejecuta SOs invitados | VMware, VirtualBox, KVM, Hyper-V |
| **VM de proceso** | Entorno de ejecución de un proceso/programa | JVM, CLR |

**Trampa.** JVM/CLR no virtualizan hardware completo; ejecutan bytecode/IL sobre un runtime.

### 10. Compará kernel monolítico y microkernel: ventajas, desventajas y ejemplos.
| Aspecto | Monolítico | Microkernel |
|---|---|---|
| **Qué va en kernel** | Casi todo: planificación, memoria, FS, drivers, etc. | Mínimo: IPC, interrupciones, planificación básica, memoria básica |
| **Servicios** | En modo kernel | Muchos en modo usuario (servidores) |
| **Ventaja** | Rápido, menos cambios de modo/IPC | Más robusto, modular, fallas aisladas |
| **Desventaja** | Frágil: un bug en driver puede tumbar el kernel | Más lento por IPC/cambios de contexto |
| **Ejemplos** | Linux (monolítico modular), Unix tradicional | Minix, QNX; diseños híbridos: Windows/macOS |

**Respuesta corta.** “Monolítico prioriza rendimiento; microkernel prioriza aislamiento y robustez.”

## B. Procesos, estados y planificación

### 11. ¿Qué diferencia hay entre programa y proceso? ¿Dónde vive cada uno y cómo se comunican dos procesos?
**Programa.** Archivo ejecutable pasivo, en disco. Es un conjunto de instrucciones.

**Proceso.** Programa en ejecución: tiene estado, contador de programa, registros, pila, memoria, PCB y recursos.

| | Programa | Proceso |
|---|---|---|
| Naturaleza | Pasivo | Activo |
| Dónde vive | Disco | Memoria + estructuras del kernel |
| Instancias | Una copia puede generar varios procesos | Cada ejecución es un proceso distinto |

**Comunicación entre procesos.** Por **IPC**: memoria compartida, pipes/tuberías, colas de mensajes, sockets, señales (según caso).

### 12. ¿Qué es el PCB (Process Control Block)? ¿Qué información contiene?
**Definición.** Estructura de datos del kernel que almacena toda la información necesaria para administrar un proceso.

**Contiene típicamente.**
- Identificación: PID, PPID, usuario.
- Estado: listo, ejecución, bloqueado, etc.
- Contexto de CPU: registros, PC, SP, flags.
- Información de memoria: tablas de páginas/segmentos, límites.
- Información de E/S: archivos abiertos, dispositivos.
- Contabilidad/planificación: prioridad, tiempos, quantum, estadísticas.

**Por qué importa.** Permite suspender y reanudar un proceso (cambio de contexto).

### 13. ¿Cuáles son los estados de un proceso y sus transiciones? ¿Puede pasar de bloqueado a ejecución directo?
**Estados básicos.** Nuevo, listo, ejecución, bloqueado/espera, terminado.

**Con swapping/suspensión.** Listo suspendido, bloqueado suspendido.

**Transiciones clave.**
- Nuevo → Listo: admitido.
- Listo → Ejecución: el planificador lo despacha.
- Ejecución → Listo: quantum agotado/interrupción/preempción.
- Ejecución → Bloqueado: espera E/S o evento.
- Bloqueado → Listo: ocurre el evento/E/S termina.
- Ejecución → Terminado: finaliza.

**Trampa.** **No** pasa de bloqueado a ejecución directo: primero vuelve a listo y el planificador decide cuándo ejecuta.

### 14. ¿Qué eventos crean un proceso y qué eventos lo terminan?
**Creación.** Arranque del sistema, llamada desde otro proceso (`fork`), solicitud interactiva del usuario, inicio de trabajo batch.

**Terminación.** Salida normal (`exit`), error voluntario (dato inválido detectado), error fatal (acceso inválido, división por cero), terminado por otro proceso/SO (`kill`).

### 15. ¿Qué es la planificación de CPU? Diferenciá planificación de corto, mediano y largo plazo.
**Planificación de CPU.** Decisión de qué proceso usa la CPU y cuándo.

| Plazo | Decide | Frecuencia |
|---|---|---|
| **Largo** | Qué trabajos entran al sistema / grado de multiprogramación | Baja |
| **Mediano** | Suspender/reanudar procesos (swapping) | Media |
| **Corto** | Qué proceso listo pasa a ejecución | Muy alta |

### 16. Explicá FIFO, SJF/SRTF y Round Robin. ¿Qué es el quantum y cómo afecta a la sobrecarga?
**FIFO/FCFS.** Primero en llegar, primero en ejecutarse. Simple; puede causar efecto convoy.

**SJF.** Primero el de menor ráfaga. Optimiza espera promedio; difícil conocer la ráfaga real. SRTF es la versión expropiativa.

**Round Robin.** Cola circular; cada proceso recibe un **quantum**. Bueno para tiempo compartido.

**Quantum.**
- Muy chico: mucha sobrecarga por cambios de contexto.
- Muy grande: se parece a FIFO.
- Sobrecarga aproximada: $\text{sobrecarga} = \frac{\text{cambio}}{\text{cambio} + \text{quantum}}$.

### 17. ¿Qué es el modelo probabilístico de multiprogramación $U = 1 - p^n$? ¿Qué significa cada variable y qué limitaciones tiene?
**Fórmula.** $U = 1 - p^n$.

- $p$: fracción de tiempo que un proceso espera E/S (bloqueado).
- $n$: grado de multiprogramación (procesos en memoria).
- $U$: utilización de CPU.

**Ejemplo.** $p=0.5, n=4 \Rightarrow U=1-0.5^4=93.75\%$.

**Si $p$ es distinto por proceso.** $U = 1 - \prod p_i$.

**Limitaciones.** Modelo simplificado: supone independencia, comportamiento estable, y no modela costos de cambio de contexto, contención de memoria, scheduling real ni overhead de E/S.

### 18. ¿Qué es una condición de carrera? Nombrá mecanismos de sincronización vistos (semáforos, mutex, TSL, Peterson) y cuándo se usan.
**Condición de carrera.** Resultado depende del orden no controlado en que varios procesos/hilos acceden a datos compartidos.

**Mecanismos.**
- **Mutex:** exclusión mutua simple; un hilo a la vez.
- **Semáforo:** contador + operaciones atómicas; binario o general; sincroniza acceso/orden.
- **TSL/Test-and-Set:** instrucción atómica de hardware para spinlocks simples.
- **Peterson:** algoritmo por software para dos procesos (interés + turno).

**Trampa.** La exclusión mutua evita carrera, pero hay que cuidar deadlock, inanición y espera ocupada según el mecanismo.

## C. Memoria: administración básica

### 19. ¿Qué es la fragmentación interna y la fragmentación externa? Da un ejemplo numérico de cada una.
**Interna.** Espacio desperdiciado **dentro** de un bloque asignado. Típica en particiones fijas/paginación.
- Ej.: bloque de 128 KB asignado a proceso de 100 KB → 28 KB internos.

**Externa.** Espacio libre total suficiente, pero disperso en huecos no contiguos. Típica en particiones variables/segmentación.
- Ej.: huecos de 10 KB, 5 KB y 12 KB (total 27 KB), llega proceso de 20 KB → no entra contiguo.

### 20. ¿Qué diferencia hay entre mapa de bits y listas enlazadas para administrar memoria libre?
| Criterio | Mapa de bits | Listas enlazadas |
|---|---|---|
| **Representación** | 1 bit por unidad de asignación | Nodo por segmento libre/ocupado |
| **Tamaño** | Fijo | Variable, depende de segmentos |
| **Búsqueda de hueco** | Buscar corrida de bits en 0 | Recorrer lista según algoritmo |
| **Fusión** | Ajustar bits | Fácil fusionar nodos adyacentes libres |
| **Uso típico** | Memoria/disco con unidades fijas | Asignación variable |

### 21. Compará first fit, next fit, best fit y worst fit. ¿Cuál es más rápido y cuál tiende a dejar huecos chicos?
| Algoritmo | Cómo elige | Ventaja | Desventaja |
|---|---|---|---|
| **First fit** | Primer hueco que alcanza | Rápido, simple | Fragmenta el inicio |
| **Next fit** | Desde la última posición | Reparte búsqueda | Puede romper huecos grandes |
| **Best fit** | Hueco más chico que alcanza | Ahorra huecos grandes | Lento; deja restos muy chicos |
| **Worst fit** | Hueco más grande | Deja restos más grandes | Rompe huecos grandes; suele rendir mal |

**Trampa.** Best fit no es “el mejor” en velocidad; suele ser más lento por recorrer más.

### 22. ¿Qué es la compactación? ¿Cuándo sirve y cuál es su costo?
**Definición.** Mover procesos/bloques en memoria para juntar huecos libres y formar uno grande.

**Cuándo sirve.** En fragmentación externa (particiones variables/segmentación).

**Costo.** Alto: copiar memoria consume tiempo de CPU/bus; requiere reubicación de direcciones y puede pausar procesos. Solo se hace si el beneficio lo justifica.

### 23. ¿Qué es el buddy system? ¿Qué es Quick Fit? Mencioná ventaja y desventaja.
**Buddy system.** Divide memoria en bloques de potencias de 2; al liberar, fusiona buddies si ambos están libres.
- Ventaja: fusión rápida y simple.
- Desventaja: fragmentación interna (redondeo a potencia de 2).

**Quick Fit.** Mantiene listas separadas para tamaños frecuentes.
- Ventaja: asignación muy rápida para tamaños comunes.
- Desventaja: difícil fusionar/coalescer; compleja administración.

### 24. ¿Qué diferencia hay entre direccionamiento lógico/virtual y físico? ¿Quién hace la traducción?
**Lógico/virtual.** Dirección generada por el CPU/proceso.

**Físico.** Dirección real en memoria RAM.

**Traducción.** La realiza el hardware de administración de memoria, principalmente la **MMU**, usando tablas de páginas/segmentos definidas por el SO.

## D. Paginación, fallos y reemplazo

### 25. ¿Qué es la paginación? Definí página, marco, tabla de páginas y MMU.
**Paginación.** Esquema de memoria que divide el espacio virtual en **páginas** fijas y la memoria física en **marcos** del mismo tamaño.

- **Página:** bloque fijo del espacio virtual.
- **Marco:** bloque fijo de la RAM.
- **Tabla de páginas:** estructura que mapea página virtual → marco físico + bits de control (P, R, M, permisos).
- **MMU:** hardware que traduce direcciones virtuales a físicas consultando la tabla/TLB.

**Ventaja.** Elimina fragmentación externa; queda fragmentación interna solo en la última página.

### 26. ¿Cómo se traduce una dirección virtual a física en paginación? ¿Qué pasa si el bit de presencia es 0?
**Pasos.**
1. Separar dirección virtual en **número de página** y **desplazamiento**.
2. Verificar que la página sea válida.
3. Consultar tabla/TLB: obtener marco y bit de presencia.
4. Si $P=1$: física = $marco \times tamaño\_página + desplazamiento$.
5. Si $P=0$: **fallo de página**; el SO debe traer la página desde disco.

**Trampa.** Si el desplazamiento es mayor o igual al tamaño de página, la dirección es inválida.

### 27. ¿Cómo se calculan desplazamiento, bits de página, cantidad de páginas, marcos y memoria direccionable?
Para página de tamaño potencia de 2:
- $desplazamiento = \log_2(tamaño\_página)$
- $bits\_página = bits\_virtuales - desplazamiento$
- $páginas = 2^{bits\_página}$
- $marcos = \frac{memoria\_física}{tamaño\_página}$
- $memoria\_direccionable = 2^{bits\_virtuales}$

**Trampa.** Memoria utilizable real = $\min(direccionable, física)$. Si la página no es potencia de 2, el esquema clásico no aplica limpio.

### 28. ¿Qué es un fallo de página? Enumerá los pasos en orden cuando todos los marcos están ocupados.
**Definición.** Ocurre cuando el proceso referencia una página válida pero no presente en RAM ($P=0$).

**Pasos.**
1. MMU detecta $P=0$ y genera trap/fallo de página.
2. El SO guarda el estado del proceso.
3. Localiza la página en disco/swap.
4. Busca marco libre; si no hay, elige víctima por algoritmo de reemplazo.
5. Si la víctima tiene $M=1$, se escribe a disco; si $M=0$, se descarta. Se carga la página nueva.
6. Se actualiza la tabla de páginas/TLB (P, marco, R/M).
7. Se reinicia la instrucción que causó el fallo.

### 29. ¿Qué es la TLB? ¿Qué contiene, por qué acelera y qué pasa en un TLB miss?
**TLB (Translation Lookaside Buffer).** Caché rápida, asociativa, de traducciones recientes página→marco.

**Contiene.** Página virtual, marco, bits de protección/presencia/modificación, etc.

**Por qué acelera.** Evita ir a memoria a consultar la tabla de páginas en cada acceso.

**TLB miss.** Si la traducción no está en TLB, se busca en la tabla de páginas; si está en RAM se carga en TLB; si no, ocurre fallo de página.

### 30. Compará FIFO, segunda oportunidad/reloj, NRU, LRU y Aging. ¿Qué problema tiene cada uno y qué lo mejora?
| Algoritmo | Criterio | Problema | Mejora/aproximación |
|---|---|---|---|
| **FIFO** | Saca la más vieja en carga | Puede sacar página útil; Belady | Segunda oportunidad/reloj |
| **Segunda oportunidad** | FIFO + bit R | Puede recorrer varias páginas | Reloj (puntero circular) |
| **Reloj** | R=0 reemplaza; R=1 limpia y avanza | Aproximación | Eficiente en la práctica |
| **NRU** | Clase por R,M: 00,01,10,11 | Pocas clases, poco fino | Limpiar R periódicamente; Aging/LRU |
| **LRU** | Menos recientemente usada | Exacto es caro en hardware | Aging/NFU |
| **Aging** | Contadores con shift + bit R | Aproximado | Buen costo/beneficio |

### 31. ¿Qué es la anomalía de Belady? ¿En qué algoritmo ocurre?
**Definición.** Aumentar la cantidad de marcos puede producir **más** fallos de página en algunas secuencias.

**Dónde ocurre.** En **FIFO**. 

**No ocurre** en algoritmos de pila como LRU óptimo/LRU (en el sentido clásico estudiado en la materia).

### 32. ¿Qué es el tamaño óptimo de página? Explicá la fórmula $s = \sqrt{2PE}$.
**Idea.** Equilibrar fragmentación interna y tamaño de la tabla de páginas.

- Fragmentación interna promedio: $s/2$.
- Tamaño de tabla: $\frac{P}{s}E$.
- Costo total aproximado: $\frac{s}{2} + \frac{PE}{s}$.
- Minimizando: $s = \sqrt{2PE}$.

Donde $P$ = tamaño promedio del proceso, $E$ = tamaño de entrada de tabla, $s$ = tamaño de página.

**Trampa.** Usar unidades consistentes (bytes).

### 33. ¿Qué son el conjunto de trabajo y el thrashing? ¿Cómo se relacionan?
**Conjunto de trabajo (working set).** Páginas que un proceso necesita en un intervalo reciente para ejecutarse eficientemente.

**Thrashing.** Estado en que el sistema pasa más tiempo paginando que ejecutando, por falta de marcos para los conjuntos de trabajo activos.

**Relación.** Si la suma de working sets excede la memoria física disponible, suben los fallos de página y aparece thrashing. Solución típica: reducir grado de multiprogramación, ajustar asignación de marcos o mejorar localidad.

## E. Tablas avanzadas y segmentación

### 34. ¿Por qué se usan tablas de páginas multinivel? ¿Cómo se calcula la cantidad de tablas/subtablas?
**Motivo.** Una tabla lineal puede ser enorme, sobre todo con espacios virtuales grandes (32/64 bits). Multinivel divide el número de página en varios índices y permite materializar solo subtablas necesarias.

**Cálculo.**
- Desplazamiento = $\log_2(página)$.
- Bits de página = bits virtuales - desplazamiento.
- Repartir bits de página entre niveles (ej. 10+10+12).
- Tablas totales = $1 + 2^{n1} + 2^{n1+n2} + ...$ (según niveles usados).
- Subtablas = totales - 1 (si la raíz no se cuenta como subtabla).

**Trampa.** Aclarar si piden “tablas” o “subtablas”.

### 35. ¿Qué es la tabla de páginas invertida? ¿Cuándo conviene y qué costo tiene su búsqueda?
**Definición.** Tabla con una entrada por **marco físico**, no por página virtual.

**Cuándo conviene.** Espacios virtuales muy grandes (ej. 64 bits), donde una tabla directa por proceso sería inviable.

**Costo.** La búsqueda es más compleja (hay que encontrar qué página virtual está en un marco). Se mitiga con TLB y hash.

**Cálculo.** $marcos = RAM / tamaño\_página$; entradas invertidas = marcos (o $k \times marcos$ si hay factor/hash).

### 36. ¿Qué diferencia hay entre paginación, segmentación y segmentación paginada?
| Esquema | Divide en | Ventaja | Problema |
|---|---|---|---|
| **Paginación** | Páginas fijas | Sin fragmentación externa | Interna; tablas grandes |
| **Segmentación** | Segmentos lógicos variables | Respeta lógica del programa; protección/compartición | Fragmentación externa |
| **Segmentación paginada** | Segmentos, y cada uno paginado | Combina lógica + manejo eficiente de memoria | Más complejidad de traducción |

### 37. ¿Cómo se decide si un proceso cabe en un esquema de segmentación con paginación? ¿Qué se calcula por segmento?
**Pasos.**
1. Calcular tamaño de página y cantidad de páginas direccionables.
2. Para cada segmento, calcular páginas necesarias: $\lceil tamaño\_segmento / tamaño\_página \rceil$ (redondear hacia arriba por segmento; una página no se comparte entre segmentos).
3. Sumar páginas de todos los segmentos del proceso (código, datos, pila, etc.).
4. Comparar con páginas disponibles/direccionables.

**Trampa.** No dividir el total del proceso “de una”: cada segmento se pagina por separado.

## F. Preguntas destacadas / trampa

### 38. Un tamaño de página de 5 KB, ¿qué problema tiene en un esquema clásico de paginación?
5 KB no es potencia de 2. Eso complica el cálculo de desplazamiento/bits de página porque $\log_2(5120)$ no es entero. En paginación clásica se usan tamaños potencia de 2 para separar página/desplazamiento por bits.

**Respuesta corta.** “El problema es que 5 KB no es potencia de 2; la división página/desplazamiento no queda en bits enteros y el esquema clásico queda mal definido.”

### 39. En LRU exacto por hardware, ¿cuál es el problema? ¿Cómo lo aproximan Aging/NFU?
**Problema.** LRU exacto requiere registrar el orden de uso de todas las páginas: caro en hardware, memoria y actualizaciones en cada acceso.

**Aproximaciones.**
- **NFU:** contador por página; suma bit R periódicamente. Pierde historia fina.
- **Aging:** desplaza contador a la derecha e inserta bit R en el bit más alto; da más peso a referencias recientes.

### 40. ¿Por qué la multiprogramación sin DMA pierde sentido? ¿Y qué rol cumple el spooling en la 3.ª generación?
**Sin DMA.** La CPU debe copiar datos byte a byte entre dispositivo y memoria. Durante E/S queda ocupada, por lo que no puede ejecutar otro proceso útil: se pierde el solapamiento que justifica la multiprogramación.

**Spooling en 3.ª generación.** Almacena trabajos en disco para desacoplar CPU de dispositivos lentos; permite que la CPU siga procesando otros trabajos mientras el dispositivo consume/produce datos a su ritmo.

### 41. Si dos procesos tienen $p$ distintos, ¿cómo se calcula la utilización de CPU?
Si las esperas de E/S son independientes: $U = 1 - \prod p_i$.

**Ejemplo.** $p_1=0.5, p_2=0.9 \Rightarrow U = 1 - (0.5)(0.9) = 1 - 0.45 = 55\%$.

**Trampa.** No promediar $p$ sin justificar; el producto modela que la CPU queda ociosa solo cuando **todos** esperan E/S.

### 42. ¿Qué hay que revisar antes de entregar un ejercicio numérico en el final escrito?
- Escribí **dato → fórmula → sustitución → resultado + unidad**.
- En paginación, calculá primero el **desplazamiento**.
- Verificá si el tamaño de página es **potencia de 2**.
- Compará **memoria direccionable vs. física** (la utilizable es la menor).
- En Gantt, recalculá $U=1-p^n$ y $U/n$ al llegar/terminar un proceso.
- En reemplazo, nombrá el **criterio** (carga, última ref, R/M, puntero).
- Si el enunciado está ambiguo, declaralo como supuesto y seguí con método.

---

> [!tip] Práctica
> Después de esta teoría, pasá a [[01 Enunciados|Enunciados de finales]] y corregí con [[02 Resoluciones detalladas|Resoluciones detalladas]].
