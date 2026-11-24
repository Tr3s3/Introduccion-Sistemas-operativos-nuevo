---
tipo: lectura-corrida
unidad: 2
---
# Unidad 2 — completa (lectura de corrido)

> [!abstract] Fuente
> Desarrollada a partir de las **diapositivas de cátedra** (Procesos y Memoria) y complementada con explicaciones, ejemplos, trampas de examen y libro (Tanenbaum). Ver [[00 Fuente - Temario de diapositivas]].

---

# 2.1.1 Programa vs. proceso

> [!abstract] En una frase
> Un **programa** es un conjunto pasivo de instrucciones en disco; un **proceso** es un programa en ejecución, con estado, recursos y contexto.

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_02.png]]

La diapositiva define: “Un proceso es la abstracción de un programa en ejecución”. No es solo el código: incluye lo necesario para ejecutar ese código en un momento dado.

## Diapositiva: modelo de proceso

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_03.png]]

El modelo de proceso muestra que cada proceso tiene su propia “vista” de ejecución (contador de programa, registros, pila, memoria). Esto permite que varios procesos avancen de forma independiente.

## Comparación

| Aspecto | Programa | Proceso |
|---|---|---|
| Naturaleza | Pasivo (archivo) | Activo (en ejecución) |
| Dónde está | Disco/almacenamiento | Memoria + estructuras del kernel |
| Tiene estado | No | Sí: listo, ejecutando, bloqueado, etc. |
| Recursos | No propios en ejecución | CPU, memoria, archivos, PCB |
| Instancias | Un programa puede originar varios procesos | Cada proceso es una instancia de ejecución |

## Qué incluye un proceso

- **Código** (texto del programa).
- **Datos** (globales, heap).
- **Pila** (llamadas, variables locales).
- **Contador de programa y registros**.
- **PCB** (información administrativa del kernel).

## Complemento de libro (Tanenbaum)
Tanenbaum enfatiza la analogía: el programa es como una receta; el proceso es la actividad de cocinarla con los ingredientes y el estado actual. Dos procesos pueden ejecutar el mismo programa pero tener datos y estado distintos.

## Cómo responderlo en el final
“Un programa es pasivo, en disco. Un proceso es un programa en ejecución, con PCB, memoria, registros y estado. Un mismo programa puede generar varios procesos”.

> [!warning] Errores típicos
> - Llamar “proceso” al archivo .exe/.bin.
> - Olvidar que el proceso incluye estado y recursos, no solo código.


---

# 2.1.2 El PCB (Process Control Block)

> [!abstract] En una frase
> El **PCB** es la estructura de datos del kernel donde se guarda toda la información necesaria para administrar y reanudar un proceso.

## Diapositivas de cátedra: implementación de procesos

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_12.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_13.png]]

Las diapositivas de “Implementación de procesos” muestran que el SO mantiene una tabla/estructura por proceso con la información necesaria para gestionarlo y cambiar de contexto.

## Qué contiene típicamente un PCB

| Categoría | Ejemplos |
|---|---|
| **Identificación** | PID, PPID, usuario, grupo |
| **Estado del procesador** | PC, SP, registros, PSW |
| **Estado del proceso** | listo, ejecutando, bloqueado, suspendido |
| **Control de memoria** | punteros a tablas de páginas/segmentos, límites |
| **Información de E/S** | archivos abiertos, dispositivos asignados |
| **Planificación/contabilidad** | prioridad, tiempo de CPU, quantum, estadísticas |

## Para qué sirve

- **Cambio de contexto:** guardar el estado del proceso que sale y cargar el del que entra.
- **Planificación:** decidir a quién dar CPU.
- **Gestión de recursos:** saber qué archivos/memoria/dispositivos tiene.
- **Protección y contabilidad:** controlar permisos y uso.

## Complemento de libro (Tanenbaum)
Tanenbaum describe la tabla de procesos como el corazón de la implementación multiproceso: cada entrada contiene campos de administración de proceso, memoria y archivos. En una interrupción, el kernel guarda el estado en el PCB/entrada correspondiente.

## Cómo responderlo en el final
“El PCB es la ficha del proceso en el kernel. Contiene identificación, estado, registros, información de memoria, E/S y planificación. Permite suspender y reanudar procesos correctamente”.

> [!warning] Errores típicos
> - Confundir PCB con el código del programa.
> - Olvidar que el PCB lo mantiene el kernel, no el proceso usuario.


---

# 2.1.3 Creación, jerarquía y señales

> [!abstract] En una frase
> Los procesos se **crean** por eventos del sistema o por otros procesos, forman **jerarquías** padre-hijo y pueden controlarse mediante **señales**.

## Diapositivas de cátedra

### Creación de procesos

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_04.png]]

La diapositiva enumera causas típicas de creación:
- Inicialización del sistema.
- Ejecución de una llamada de creación por un proceso en ejecución.
- Solicitud de usuario para crear un proceso.
- Inicio de un trabajo por lotes.

### Terminación de procesos

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_05.png]]

Causas típicas de terminación:
- Salida normal (voluntaria).
- Error fatal.
- Error por otro proceso (killed).
- Salida por error (voluntaria, pero con error detectado).

### Jerarquía y señales

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_06.png]]

La diapositiva muestra:
- Los procesos padres crean procesos hijos.
- Se crean y finalizan mediante llamadas al sistema.
- Cada proceso tiene usuario y grupo de seguridad.
- La ejecución se controla por medio de **señales**.
- Las señales SW son análogas a las interrupciones HW.

## Creación: fork/exec (complemento práctico)

En Unix, un patrón común es:
1. `fork()` crea un proceso hijo (copia lógica del contexto).
2. `execve()` reemplaza la imagen del proceso hijo por otro programa.
3. `waitpid()` permite al padre esperar la finalización.

## Señales

| Señal/concepto | Idea |
|---|---|
| **Señal** | Notificación asincrónica a un proceso |
| **Origen** | kernel, otro proceso, el propio proceso |
| **Efecto** | terminar, ignorar, capturar, detener/continuar (según señal) |

## Complemento de libro (Tanenbaum)
Tanenbaum distingue creación por evento del sistema, por usuario, por batch y por syscall; y explica que la jerarquía de procesos facilita control y herencia de ciertos atributos, aunque no todos los SO la mantienen estrictamente igual.

## Cómo responderlo en el final
“Un proceso puede crearse al iniciar el sistema, por `fork`, por pedido del usuario o por batch. Termina normal, por error voluntario, error fatal o por acción de otro proceso/SO. Los padres pueden crear hijos y las señales permiten control asincrónico”.

> [!warning] Errores típicos
> - Confundir `fork` (crea proceso) con `exec` (cambia programa).
> - Decir que toda terminación es un error.


---

# 2.2.1 Estados de un proceso y transiciones

> [!abstract] En una frase
> Un proceso pasa por **estados** (nuevo, listo, ejecutando, bloqueado, terminado; y variantes suspendidas) según eventos del sistema, E/S y decisiones del planificador.

## Diapositivas de cátedra

### Estados

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_07.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_08.png]]

Las diapositivas presentan los estados y transiciones. El modelo clásico incluye:
- **Listo (Ready):** puede ejecutar, espera CPU.
- **Ejecutando (Running):** tiene la CPU.
- **Bloqueado (Blocked):** espera un evento/E/S.

### Transiciones

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_09.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_10.png]]

Transiciones típicas:
- **Listo → Ejecutando:** el planificador lo despacha.
- **Ejecutando → Listo:** se agota quantum / interrupción / preempción.
- **Ejecutando → Bloqueado:** solicita E/S o espera evento.
- **Bloqueado → Listo:** termina la E/S / ocurre el evento.

### Suspensión (swapping)

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_11.png]]

La diapositiva muestra que el movimiento entre memoria y disco introduce estados **suspendidos**:
- **Listo/Suspendido**
- **Bloqueado/Suspendido**

Esto ocurre cuando el SO saca procesos de memoria para liberar RAM.

## Tabla de transiciones

| Desde | Hacia | Causa típica |
|---|---|---|
| Nuevo | Listo | Admitido por el SO |
| Listo | Ejecutando | Dispatch/planificador |
| Ejecutando | Listo | Quantum/interrupción/preempción |
| Ejecutando | Bloqueado | E/S o espera de evento |
| Bloqueado | Listo | Evento completado |
| Ejecutando | Terminado | Exit normal/error |
| Listo/Bloqueado | Suspendido | Swapping a disco |
| Suspendido | Listo/Bloqueado | Se trae a memoria |

## Complemento de libro (Tanenbaum)
Tanenbaum agrega que el modelo exacto varía según SO, pero la lógica es la misma: la CPU es escasa, la E/S es lenta, y el kernel debe rastrear el estado para planificar correctamente.

## Cómo responderlo en el final
Nombrá los estados, dibujá o describí transiciones, y aclaralo: **bloqueado no pasa directo a ejecutando**, pasa a listo.

> [!warning] Errores típicos
> - Poner transición Bloqueado → Ejecutando directa.
> - Olvidar estados suspendidos cuando hay swapping.


---

# 2.2.2 Interrupción y cambio de contexto (pasos)

> [!abstract] En una frase
> Ante una interrupción, el hardware y el kernel guardan el estado del proceso actual, atienden el evento, el planificador decide el próximo proceso y se restaura su contexto.

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_14.png]]

La diapositiva muestra los pasos que sigue el nivel inferior del SO cuando ocurre una interrupción:

1. El hardware coloca el contador del programa en la pila, etc.
2. El hardware carga el nuevo contador de programa del vector de interrupciones.
3. Un procedimiento en lenguaje ensamblador guarda los registros.
4. El procedimiento en ensamblador establece la nueva pila.
5. El servicio de interrupción en C se ejecuta (por lo general lee y guarda la entrada en el búfer).
6. El planificador decide qué proceso se va a ejecutar a continuación.
7. El procedimiento en C regresa al código de ensamblador.
8. El procedimiento en lenguaje ensamblador inicia el nuevo proceso actual.

## Qué es cambio de contexto

El **cambio de contexto** es guardar el estado de ejecución de un proceso (registros, PC, SP, etc., en su PCB) y cargar el de otro. Es necesario para la multiprogramación, pero tiene costo.

## Costos y consideraciones

| Costo | Por qué ocurre |
|---|---|
| Guardar/restaurar registros | El kernel debe preservar el estado |
| Cambiar estructuras de planificación | Decidir el próximo proceso |
| Efectos en caché/TLB | El nuevo proceso puede invalidar localidad |

## Complemento de libro (Tanenbaum)
Tanenbaum aclara que las interrupciones son el mecanismo que permite al SO recuperar el control: timer, E/S, syscalls/excepciones. El cambio de contexto debe ser correcto y rápido, pero no es gratis.

## Cómo responderlo en el final
Enumerá los pasos de la diapositiva: hardware guarda PC/vector, ensamblador guarda registros/pila, rutina C atiende, planificador elige, se restaura contexto del siguiente proceso.

> [!warning] Errores típicos
> - Decir que “la interrupción ejecuta directamente el proceso usuario”.
> - Olvidar que el planificador puede elegir otro proceso distinto al interrumpido.


---

# 2.3.1 Proceso vs. hilo

> [!abstract] En una frase
> Un **proceso** es la unidad de recursos y protección; un **hilo** (thread) es la unidad de ejecución dentro de un proceso, que comparte memoria y recursos con otros hilos del mismo proceso.

## Contexto de diapositivas

El deck “Procesos y Memoria” se enfoca en el modelo de proceso, estados e implementación; el detalle de hilos se complementa con Tanenbaum/cátedra.

## Comparación

| Aspecto | Proceso | Hilo |
|---|---|---|
| **Recursos** | Propios (espacio de direcciones, archivos, etc.) | Comparte recursos del proceso |
| **Ejecución** | Al menos un hilo | Unidad de ejecución ligera |
| **Cambio de contexto** | Más costoso | Más liviano (dentro del mismo proceso) |
| **Comunicación** | IPC explícito | Memoria compartida dentro del proceso |
| **Fallo** | Aislado de otros procesos | Un hilo puede afectar al proceso completo |

## Qué comparten y qué no

**Comparten:** espacio de direcciones, archivos abiertos, variables globales, señales/handlers (según SO).
**Propio de cada hilo:** PC, registros, pila, estado.

## Complemento de libro (Tanenbaum)
Tanenbaum explica hilos de usuario vs. kernel, ventajas (responsividad, paralelismo, economía) y riesgos (condiciones de carrera, sincronización).

## Cómo responderlo en el final
“Proceso = unidad de recursos; hilo = unidad de ejecución dentro del proceso. Los hilos comparten memoria y recursos, pero cada uno tiene su PC, registros y pila”.

> [!warning] Errores típicos
> - Decir que los hilos tienen memoria separada como procesos.
> - Olvidar que compartir memoria implica necesidad de sincronización.


---

# 2.4.1 Objetivos de la planificación

> [!abstract] En una frase
> La **planificación de CPU** decide qué proceso listo ejecuta a continuación, buscando equilibrar utilización, throughput, tiempo de respuesta, espera y equidad.

## Contexto de diapositivas

El deck “Procesos y Memoria” introduce estados, transiciones y el rol del planificador en interrupciones/cambios de contexto; los objetivos y algoritmos se complementan con Tanenbaum/cátedra.

## Objetivos típicos

| Objetivo | Qué busca | Más importante en |
|---|---|---|
| **Utilización de CPU** | Mantener la CPU ocupada | Sistemas batch |
| **Throughput** | Completar más trabajos por unidad de tiempo | Batch |
| **Tiempo de retorno** | Minimizar tiempo total de un trabajo | Batch |
| **Tiempo de espera** | Minimizar tiempo en cola de listos | General |
| **Tiempo de respuesta** | Responder rápido a interacción | Interactivos/time-sharing |
| **Equidad** | Repartir CPU razonablemente | General |

## Tipos de planificación

- **No apropiativa (non-preemptive):** el proceso libera CPU voluntariamente o al bloquearse/terminar.
- **Apropiativa (preemptive):** el SO puede quitar la CPU (timer, prioridad, quantum).

## Complemento de libro (Tanenbaum)
Tanenbaum distingue sistemas batch, interactivos y de tiempo real: los objetivos cambian según el contexto. No hay un algoritmo perfecto para todos los casos.

## Cómo responderlo en el final
Mencioná el objetivo que optimiza el escenario (respuesta en interactivo, throughput en batch) y aclaralo si la política es apropiativa o no.

> [!warning] Errores típicos
> - Creer que “más CPU ocupada” siempre es mejor sin mirar tiempo de respuesta.
> - Confundir tiempo de espera con tiempo de retorno.


---

# 2.4.2 FIFO, SJF y Round Robin (quantum)

> [!abstract] En una frase
> **FIFO** ejecuta en orden de llegada, **SJF** prioriza la ráfaga más corta y **Round Robin** reparte CPU por turnos de quantum.

## Contexto de diapositivas

El deck “Procesos y Memoria” establece la base de estados/transiciones; estos algoritmos se desarrollan con complemento de libro/cátedra.

## Comparación

| Algoritmo | Criterio | Apropiativo | Ventaja | Desventaja |
|---|---|---|---|---|
| **FIFO/FCFS** | Orden de llegada | No | Simple | Efecto convoy |
| **SJF** | Ráfaga más corta | No (SRTF sí) | Buen tiempo promedio | Difícil estimar ráfaga; inanición |
| **Round Robin** | Turno por quantum | Sí | Buena respuesta | Overhead si quantum chico; peor promedio si quantum grande |

## Round Robin y quantum

- **Quantum grande:** se parece a FIFO.
- **Quantum chico:** mejor respuesta, pero más cambios de contexto.
- Sobrecarga aproximada: $\frac{cambio}{cambio + quantum}$.

## Complemento de libro (Tanenbaum)
Tanenbaum analiza estos algoritmos con ejemplos de Gantt y métricas de espera/retorno. RR es el clásico para time-sharing; SJF es óptimo en espera promedio si se conocen las ráfagas.

## Cómo responderlo en el final
Identificá el criterio del algoritmo, armá el Gantt si piden cálculo, y mencioná una ventaja y una trampa (convoy en FIFO, inanición en SJF, overhead en RR).

> [!warning] Errores típicos
> - En RR, no encolar correctamente el proceso que llega al mismo tiempo que vence el quantum (seguir la convención del enunciado).
> - Confundir SJF con prioridad por importancia de usuario.


---

# 2.4.3 Prioridades, hambre y aging

> [!abstract] En una frase
> La planificación por **prioridades** elige el proceso más importante; puede causar **inanición** (starvation), que se mitiga con **aging** (envejecimiento).

## Contexto de diapositivas

Complemento de libro/cátedra sobre planificación. Se relaciona con el rol del planificador visto en interrupciones/cambio de contexto.

## Prioridades

| Tipo | Cómo se asigna | Riesgo |
|---|---|---|
| **Estática** | Fija (usuario, tipo de proceso) | Inanición |
| **Dinámica** | Cambia según comportamiento/espera | Más compleja |

## Inanición y aging

- **Inanición:** un proceso listo nunca recibe CPU porque siempre hay otros de mayor prioridad.
- **Aging:** aumentar gradualmente la prioridad de procesos que esperan mucho tiempo.

## Complemento de libro (Tanenbaum)
Tanenbaum presenta prioridades como mecanismo flexible, pero advierte que deben combinarse con envejecimiento o cuotas para evitar starvation.

## Cómo responderlo en el final
“Prioridades asignan CPU al más importante; el riesgo es inanición. Aging incrementa la prioridad de los que esperan mucho para garantizar progreso”.

> [!warning] Errores típicos
> - Confundir aging de prioridades con aging de reemplazo de páginas (misma idea de envejecimiento, distinto contexto).


---

# 2.5.1 Multiprogramación — concepto y beneficios

> [!abstract] En una frase
> La **multiprogramación** mantiene varios procesos en memoria para que la CPU pueda ejecutar otro cuando uno se bloquea por E/S.

## Diapositivas de cátedra

### Monoprogramación vs. multiprogramación

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_19.png]]

Con **monoprogramación** hay un proceso usuario + SO en memoria; cuando el proceso espera E/S, la CPU queda ociosa.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_20.png]]

Con **multiprogramación** hay varios procesos usuarios en memoria: mientras uno espera E/S, otro puede usar la CPU. Se incrementa el uso de CPU. Se debe decidir cuántos procesos mantener en memoria → modelo probabilístico.

### Organización de memoria

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_24.png]]

La diapositiva plantea la pregunta clave: ¿cómo organizar la memoria para tener más de un proceso en ejecución? Primera aproximación: particiones fijas (sin swapping).

## Beneficios y costos

| Beneficio | Costo/complicación |
|---|---|
| Mejor utilización de CPU | Más complejidad de planificación |
| Solapamiento CPU/E/S | Necesidad de protección y reubicación |
| Mejor throughput en sistemas batch | Más presión sobre memoria |

## Complemento de libro (Tanenbaum)
Tanenbaum vincula multiprogramación con el grado de multiprogramación, planificación, administración de memoria y el modelo $U=1-p^n$. También advierte que demasiada multiprogramación puede causar thrashing en memoria virtual.

## Cómo responderlo en el final
“Multiprogramación es tener varios procesos en memoria para aprovechar la CPU durante esperas de E/S. Mejora utilización, pero exige planificación, protección y administración de memoria”.

> [!warning] Errores típicos
> - Confundir multiprogramación con multiprocesamiento (varias CPUs).
> - Ignorar el costo de administrar más procesos.


---

# 2.5.2 Modelo probabilístico — U = 1 − pⁿ

> [!abstract] En una frase
> El modelo probabilístico estima la utilización de CPU como $U = 1 - p^n$, donde $p$ es la fracción de tiempo que un proceso espera E/S y $n$ el grado de multiprogramación.

## Diapositivas de cátedra

### Fórmula

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_21.png]]

La diapositiva define:
- $n$: cantidad de procesos en memoria.
- $p$: % de tiempo que un proceso espera por E/S.
- Probabilidad de que $n$ procesos esperen por E/S = $p^n$.
- **Utilización de CPU = $1-p^n$**.

### Ejemplo y análisis

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_22.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 2/slide_23.png]]

Las diapositivas muestran el análisis para 4 procesos con 80% de espera de E/S: a medida que aumenta $n$, sube la utilización, pero con rendimientos decrecientes. También se analiza la secuencia de eventos/llegadas.

## Cálculo

| Variable | Significado |
|---|---|
| $p$ | Fracción de tiempo en espera de E/S (0 a 1) |
| $n$ | Grado de multiprogramación |
| $U$ | Utilización estimada de CPU |

Ejemplo: $p=0.8$, $n=4$ → $U=1-0.8^4=1-0.4096=59.04\%$.

Si $p$ varía por proceso: $U = 1-\prod p_i$.

## Limitaciones del modelo

- Supone independencia entre procesos.
- No modela overhead de cambio de contexto.
- No considera contención de memoria/disco.
- Es una aproximación útil para razonar, no una medición exacta.

## Complemento de libro (Tanenbaum)
Tanenbaum usa el mismo modelo para justificar multiprogramación y mostrar por qué agregar memoria (más procesos) puede mejorar uso de CPU, hasta que otros recursos se vuelven cuello de botella.

## Cómo responderlo en el final
Escribí fórmula, definí $p$ y $n$, hacé la sustitución y concluí. Si te dan procesos con distinto $p$, usá el producto: $U=1-\prod p_i$.

> [!warning] Errores típicos
> - Confundir $p$ con porcentaje de CPU.
> - Usar $n$ como cantidad de CPUs.
> - No recalcular $U$ cuando entra/sale un proceso en un Gantt.


---

# 2.6.1 Comunicación entre procesos (IPC)

> [!abstract] En una frase
> **IPC** (Inter-Process Communication) son los mecanismos que permiten a procesos intercambiar datos y coordinarse: memoria compartida, mensajes, pipes, sockets, señales, etc.

## Contexto de diapositivas

El deck de Introducción menciona pipes como pseudo-archivo para comunicación entre procesos; el desarrollo completo de IPC se complementa con Tanenbaum/cátedra.

## Mecanismos comunes

| Mecanismo | Idea | Ventaja | Cuidado |
|---|---|---|---|
| **Pipe** | Flujo unidireccional de bytes | Simple, común en Unix | Sincronización/orden del flujo |
| **Memoria compartida** | Región común en memoria | Muy rápido | Requiere sincronización |
| **Mensajes** | `send/recv` con kernel | Aislamiento claro | Overhead/copias |
| **Sockets** | Comunicación por endpoints | Local o red | Complejidad de protocolo |
| **Señales** | Notificación asincrónica | Control simple | Información limitada |

## Complemento de libro (Tanenbaum)
Tanenbaum distingue comunicación (pasar datos) de sincronización (coordinar tiempos). Memoria compartida es rápida pero peligrosa sin semáforos/mutex; mensajes son más seguros pero más costosos.

## Cómo responderlo en el final
Nombrá al menos dos mecanismos, explicá cómo pasan datos y qué problema de sincronización puede aparecer.

> [!warning] Errores típicos
> - Creer que memoria compartida “se sincroniza sola”.
> - Confundir señal con mensaje de datos.


---

# 2.6.2 Sincronización y condiciones de carrera

> [!abstract] En una frase
> Una **condición de carrera** ocurre cuando el resultado depende del orden no controlado de ejecución; la **sincronización** impone orden/exclusión para evitarlo.

## Contexto de diapositivas

El deck de Procesos y Memoria no desarrolla semáforos en detalle, pero la necesidad surge al compartir CPU/memoria/recursos. Se complementa con Tanenbaum/cátedra.

## Condición de carrera

- Dos o más procesos/hilos acceden a datos compartidos.
- Al menos uno modifica.
- El resultado depende del interleaving.

## Mecanismos de sincronización

| Mecanismo | Idea | Uso típico |
|---|---|---|
| **Mutex** | Exclusión mutua: uno a la vez | Proteger sección crítica |
| **Semáforo** | Contador con wait/signal atómicos | Exclusión y coordinación |
| **Monitor** | Abstracción de alto nivel | Exclusión + condición |
| **TSL / Test-and-Set** | Instrucción atómica de HW | Spinlocks |
| **Peterson** | Algoritmo software (2 procesos) | Didáctico/histórico |

## Requisitos de una buena solución

- **Exclusión mutua**.
- **Progreso**.
- **Espera acotada**.
- Sin suponer velocidad de CPU.

## Complemento de libro (Tanenbaum)
Tanenbaum desarrolla sección crítica, algoritmos de software, instrucciones atómicas, semáforos, mutexes, monitores y problemas clásicos (productor-consumidor, lectores-escritores, filósofos).

## Cómo responderlo en el final
Definí condición de carrera con ejemplo simple, después nombrá un mecanismo (semáforo/mutex) y explicá cómo garantiza exclusión mutua.

> [!warning] Errores típicos
> - Proponer deshabilitar interrupciones como solución general en modo usuario.
> - Confundir exclusión mutua con sincronización de orden.


---
