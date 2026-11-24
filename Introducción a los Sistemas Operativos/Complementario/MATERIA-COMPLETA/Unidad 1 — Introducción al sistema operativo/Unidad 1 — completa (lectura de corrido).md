---
tipo: lectura-corrida
unidad: 1
---
# Unidad 1 — completa (lectura de corrido)

> [!abstract] Fuente
> Desarrollada a partir de las **diapositivas de cátedra** (Introducción a los Sistemas Operativos - Introducción) y complementada con explicaciones, ejemplos, trampas de examen y libro (Tanenbaum). Ver [[00 Fuente - Temario de diapositivas]].

---

# 1.1.1 Definición y funciones

> [!abstract] En una frase
> El **sistema operativo (SO)** es el programa (o conjunto de programas) que se ubica entre el **hardware** y las **aplicaciones**: les da una máquina más simple (abstracción) y administra los recursos de forma ordenada y protegida.

## Diapositiva de cátedra: qué es un SO

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_02.png]]

La diapositiva define el punto de partida: con su software, una computadora puede almacenar, procesar y entregar información. Hay **programas del sistema** (administran la operación; el más importante es el SO) y **programas de aplicación** (dan servicio a los usuarios).

## Diapositiva: hardware y complejidad

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_03.png]]

Una computadora está formada por uno o más procesadores, memoria principal, discos, impresoras y dispositivos de entrada/salida. Es un sistema complejo que debe ser administrado: escribir programas sin una capa de abstracción implicaría controlar cada componente de hardware.

## Diapositiva: ubicación del SO

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_04.png]]

El SO se ubica entre el **hardware** y los **programas de usuario** (editores, compiladores, shell, etc.). Abstrae el hardware y ofrece una interfaz más cómoda y segura para las aplicaciones.

## Las dos funciones principales (diapositiva de cátedra)

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_06.png]]

| Función | Qué significa | Ejemplo de la cátedra / típico |
|---|---|---|
| **Máquina extendida o virtual** (abstracción) | Oculta el hardware y ofrece una vista más simple | Existen instrucciones de bajo nivel para disco; el SO permite trabajar con archivos/operaciones más simples |
| **Administrador de recursos** | Administra piezas de un sistema complejo, asigna recursos de forma ordenada y mediando conflictos | Quién usa qué recurso y por cuánto tiempo; impresión simultánea, uso de memoria |

## Conceptos que el SO debe manejar

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_17.png]]

La diapositiva de conceptos de SO resume el alcance de la materia: **procesos, espacios de direcciones, archivos, entrada/salida, protección, intérprete de comandos (shell) y llamadas al sistema**. Estos temas se desarrollan en las unidades siguientes.

## Complemento de libro (Tanenbaum)
Tanenbaum refuerza la misma idea con dos visiones: el SO como **máquina extendida** (abstracción) y como **administrador de recursos** (multiplexación en tiempo y espacio). También destaca que el SO debe proteger recursos y dar servicios mediante interfaces bien definidas.

## Cómo responderlo en el final
1. Definición: intermediario entre hardware y aplicaciones.
2. Función 1: **abstracción/máquina extendida**, con ejemplo.
3. Función 2: **administrador de recursos**, con ejemplo de conflicto/asignación.
4. Cerrar con protección/servicios.

> [!warning] Errores típicos
> - Decir que el SO es solo “lo que ve el usuario” (eso confunde SO con GUI/shell).
> - Confundir abstracción (simplificar) con administración (repartir/proteger).

## Imágenes de la diapositiva
Las imágenes usadas son capturas de la diapositiva de cátedra “Introducción a los Sistemas Operativos - Introducción”.


---

# 1.1.2 Kernel, shell y programas del sistema

> [!abstract] En una frase
> El **kernel** es el núcleo del SO que corre en modo privilegiado; el **shell** es la interfaz que interpreta comandos del usuario; los **programas del sistema** son utilidades que acompañan al SO pero no son el kernel.

## Diapositiva de cátedra: el shell

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_34.png]]

La diapositiva es clara:
- **No es parte del sistema operativo** (no es el kernel).
- El sistema operativo es el código que lleva adelante las **llamadas al sistema**.
- Es la **primera interfaz** entre el usuario y el sistema operativo.
- Ejemplos: `time`, `date`, `dir`, `sort` (comandos/programas que usan servicios/syscalls).

## Diferencias clave

| Componente | Qué es | Dónde corre | Ejemplo |
|---|---|---|---|
| **Kernel** | Núcleo del SO; administra CPU, memoria, E/S, procesos | Modo kernel | Planificador, gestor de memoria, drivers |
| **Shell** | Intérprete de comandos / interfaz de usuario | Modo usuario | bash, zsh, PowerShell, cmd |
| **Programas del sistema** | Utilidades que acompañan al entorno | Modo usuario | compiladores, editores, utilidades de archivo |
| **Programas de aplicación** | Resuelven necesidades del usuario | Modo usuario | navegador, editor de texto, reproductor |

## Relación con llamadas al sistema

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_26.png]]

Los programas (incluido el shell) se comunican con el SO mediante **llamadas al sistema**. El shell típicamente usa `fork/exec/wait` para ejecutar comandos: lee el comando, crea un proceso, ejecuta el programa y espera el resultado.

## Complemento de libro (Tanenbaum)
Tanenbaum distingue entre el kernel (modo supervisor) y el resto del software de sistema/usuario. La interfaz de usuario puede ser GUI o CLI; en ambos casos, las operaciones privilegiadas terminan pidiendo servicios al kernel por syscalls.

## Cómo responderlo en el final
“El kernel es la parte del SO que corre en modo kernel y gestiona recursos. El shell no es el kernel: es un programa en modo usuario que interpreta comandos y usa syscalls para pedir servicios al SO”.

> [!warning] Errores típicos
> - Decir que el shell “es” el sistema operativo.
> - Confundir comando `time/date` con una syscall (el comando puede usar syscalls/reloj del sistema).


---

# 1.2.1 Modo usuario y modo kernel

> [!abstract] En una frase
> La CPU distingue al menos dos modos de ejecución: **modo kernel** (privilegiado, puede ejecutar instrucciones críticas y acceder a todo el hardware) y **modo usuario** (restringido, donde corren las aplicaciones).

## Diapositiva de cátedra: ubicación y modos

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_04.png]]

La diapositiva muestra la separación: arriba los programas de usuario (modo usuario), debajo el sistema operativo (modo kernel), y en la base el hardware. Esta separación protege al sistema.

## Diapositiva: por qué existe el modo kernel

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_05.png]]

La cátedra explica que a bajo nivel los dispositivos de E/S se controlan ingresando valores en registros. El **sistema operativo es la parte de software que se ejecuta en modo supervisor o kernel**, con protección de hardware. Así se evita que cualquier programa manipule directamente el hardware crítico.

## Qué permite cada modo

| Modo | Puede | No debe poder | Quién lo usa |
|---|---|---|---|
| **Kernel / supervisor** | Instrucciones privilegiadas, E/S, tablas de memoria, interrupciones | — | Núcleo del SO, handlers, drivers (según diseño) |
| **Usuario** | Instrucciones normales, cálculo, memoria propia | E/S directa, deshabilitar interrupciones, cambiar tablas de memoria | Aplicaciones, shell, utilidades |

## Cambio de modo

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_26.png]]

El cambio a modo kernel ocurre de forma controlada:
- **Syscall / TRAP:** el programa pide un servicio.
- **Interrupción de hardware:** un dispositivo requiere atención.
- **Excepción:** fallo de página, división por cero, instrucción inválida.

Al terminar, el kernel devuelve el control a modo usuario.

## Complemento de libro (Tanenbaum)
Tanenbaum lo presenta como el mecanismo básico de protección: el bit de modo en el PSW/registro de estado permite que el hardware impida operaciones peligrosas en modo usuario. Sin esta separación, un proceso defectuoso o malicioso podría dañar todo el sistema.

## Cómo responderlo en el final
“Modo kernel es privilegiado: ejecuta instrucciones críticas y controla hardware. Modo usuario es restringido: las aplicaciones corren ahí. El paso a kernel ocurre por syscalls, interrupciones o excepciones, y es controlado por el hardware/SO”.

> [!warning] Errores típicos
> - Pensar que el programa “decide” pasar a kernel libremente.
> - Confundir modo kernel con “ser administrador/root” (son conceptos distintos).


---

# 1.2.2 Llamadas al sistema

> [!abstract] En una frase
> Una **llamada al sistema** es el mecanismo por el que un programa en modo usuario pide un servicio al kernel: prepara parámetros, ejecuta una instrucción **TRAP**, el kernel ejecuta el servicio y devuelve el control.

## Diapositiva de cátedra: qué es una syscall

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_26.png]]

La diapositiva destaca:
- Los programas se comunican con el SO por medio de **llamadas al sistema**.
- Cada llamada se corresponde con un procedimiento llamado por el programa.
- Se colocan parámetros en lugares convenidos (típicamente registros).
- Se ejecuta una instrucción **TRAP** (llamada protegida).
- Ejemplo UNIX: `count = read(file, buffer, nbytes);`

## Diapositiva: flujo de una syscall

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_27.png]]

El diagrama muestra el paso de espacio de usuario a espacio de kernel: el programa llama a la biblioteca, esta ejecuta TRAP, el kernel despacha el handler correspondiente y luego retorna a modo usuario.

## Syscalls POSIX (diapositivas)

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_28.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_29.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_31.png]]

La cátedra agrupa llamadas POSIX por categoría:
- **Procesos:** `fork`, `execve`, `waitpid`, `exit`, etc.
- **Archivos:** `open`, `read`, `write`, `close`, `lseek`, `stat`, etc.
- **Directorios/misceláneas:** `mkdir`, `rmdir`, `link`, `mount`, `chmod`, `kill`, `time`, etc.

## Ejemplo: shell simple

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_32.png]]

La diapositiva muestra un shell simple: lee comando, hace `fork()`; el hijo ejecuta `execve()` y el padre hace `waitpid()`. Esto conecta syscalls con el funcionamiento real del shell.

## Syscall vs. función de biblioteca

| | Función de biblioteca | Llamada al sistema |
|---|---|---|
| **Dónde corre** | Modo usuario (normalmente) | Cruza a modo kernel |
| **Costo** | Bajo | Mayor (cambio de modo) |
| **Puede bloquear** | No necesariamente | Sí (ej. `read` esperando E/S) |
| **Ejemplo** | `strlen`, parte de `printf` | `read`, `write`, `fork`, `execve` |

## Complemento de libro (Tanenbaum)
Tanenbaum explica que la API oculta el mecanismo de trap: el programador ve una función, pero la implementación hace la transición a kernel. También resalta portabilidad (POSIX) y el costo de las syscalls.

## Cómo responderlo en el final
“Una syscall es el pedido controlado de un servicio al kernel. El programa llama una rutina de biblioteca, se ejecuta TRAP, cambia a modo kernel, el kernel atiende y retorna. No es lo mismo que cualquier función de biblioteca”.

> [!warning] Errores típicos
> - Decir “llamada al sistema = función cualquiera”.
> - Olvidar mencionar el cambio de modo / TRAP.
> - Confundir comandos como `time/date` con syscalls.


---

# 1.3.1 Generaciones de computadoras y su SO

> [!abstract] En una frase
> La evolución de los SO acompaña la evolución del hardware: de tubos al vacío sin SO, a transistores con batch, a circuitos integrados con multiprogramación/tiempo compartido, y a computadoras personales/redes con SO modernos.

## Diapositivas de cátedra

### 1ª generación (1945–1955) — Tubos al vacío

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_07.png]]

- Gran tamaño, alto mantenimiento.
- Programación en lenguaje de máquina.
- **Sin sistemas operativos** ni lenguajes de programación de alto nivel como hoy.
- Operación por paneles de control y luego tarjetas perforadas.

### 2ª generación (1955–1965) — Transistores y sistemas por lotes

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_08.png]]

- Se pueden vender a clientes; menor mantenimiento.
- Aparecen roles: constructores, programadores, operadores.
- Tiempos elevados de operación: programar, perforar tarjetas, cinta, procesar, cinta, impresión.
- **Sistemas por lotes (batch):** antecesor del SO (ej. 1401/7094).

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_09.png]]

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_10.png]]

Las diapositivas muestran el flujo batch: trabajos agrupados, entrada en cinta/tarjetas, procesamiento secuencial y salida.

### 3ª generación (1965–1980) — Circuitos integrados y multiprogramación

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_11.png]]

- Se busca unificar líneas incompatibles (científica/ingeniería vs. comercial).
- Aparece **multiprogramación**.
- **Spooling:** operaciones simultáneas de entrada/salida.
- Sigue siendo batch en muchos casos, pero aparece **tiempo compartido** (múltiples terminales en línea).
- Referencias: Multics (MIT–Bell–GE), deriva hacia Unix.

### 4ª generación (desde 1980) — Computadora personal

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_12.png]]

- LSI: miles de transistores en 1 cm².
- Bajo precio, facilidad de uso, poco mantenimiento.
- Redes de computadoras y sistemas distribuidos.
- Ejemplos: CP/M, DOS, Unix, Windows, Linux, Mac OS X, iOS, Android.

## Tabla resumen

| Generación | Hardware | Característica clave | SO / modo de operación |
|---|---|---|---|
| 1ª (1945–55) | Tubos al vacío | Programación manual | Sin SO; paneles/tarjetas |
| 2ª (1955–65) | Transistores | Batch | Sistemas por lotes |
| 3ª (1965–80) | CI | Multiprogramación | Batch + spooling + tiempo compartido |
| 4ª (1980–) | LSI/VLSI | PC y redes | SO personales, redes, móviles |

## Complemento de libro (Tanenbaum)
Tanenbaum agrega contexto histórico y ejemplos (OS/360, MULTICS, Unix, MS-DOS, Windows). La idea central coincide con la diapositiva: cada salto de hardware habilita una nueva forma de usar la computadora y exige un SO más complejo.

## Cómo responderlo en el final
Nombrá generación, tecnología de hardware, problema/necesidad y la solución/rasgo del SO. Si te piden 2ª y 3ª, enfatizá **batch** vs. **multiprogramación/spooling/tiempo compartido**.

> [!warning] Errores típicos
> - Confundir spooling con multiprogramación (relacionados, pero no iguales).
> - Decir que en la 1ª generación había SO moderno.


---

# 1.3.2 Multiprogramación, spooling y tiempo compartido

> [!abstract] En una frase
> **Multiprogramación** mantiene varios procesos en memoria para aprovechar la CPU cuando uno espera E/S; **spooling** desacopla dispositivos lentos usando disco como buffer; **tiempo compartido** da la ilusión de uso simultáneo a varios usuarios/procesos.

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_11.png]]

La diapositiva de 3ª generación introduce juntos estos conceptos:
- **Multiprogramación**: varios trabajos en memoria.
- **Spooling**: operaciones simultáneas de entrada/salida (Simultaneous Peripheral Operations On Line).
- Seguía habiendo batch, pero aparece el **tiempo compartido**: múltiples terminales en línea.

## Comparación

| Técnica | Problema que ataca | Cómo lo resuelve | Métrica/efecto típico |
|---|---|---|---|
| **Multiprogramación** | CPU ociosa mientras un proceso espera E/S | Mantiene varios procesos listos en memoria | $U = 1-p^n$ |
| **Spooling** | Dispositivos lentos bloquean el flujo de trabajos | Usa disco como cola/buffer | CPU y periféricos trabajan desacoplados |
| **Tiempo compartido** | Un solo usuario monopoliza el sistema interactivo | Asigna quantum/turnos rápidos a varios usuarios | Mejor tiempo de respuesta |

## Multiprogramación

- Varios procesos cargados en memoria.
- Si uno se bloquea por E/S, el planificador elige otro listo.
- Aumenta utilización de CPU, pero requiere administración de memoria, protección y planificación.

## Spooling

- Ejemplo clásico: impresión. Los trabajos se envían a una cola en disco; la impresora los consume a su ritmo.
- En la 3ª generación, evitaba que la CPU quedara atada a lectores/impresoras lentas.

## Tiempo compartido

- Evolución interactiva: varios usuarios con terminales.
- El sistema rota la CPU entre procesos (quantum).
- Prioriza respuesta percibida, no solo throughput batch.

## Complemento de libro (Tanenbaum)
Tanenbaum relaciona multiprogramación con el modelo probabilístico y con la necesidad de planificación; spooling como técnica clave en batch; time-sharing como base de sistemas interactivos y de Unix/MULTICS.

## Cómo responderlo en el final
Definí cada técnica, el problema que resuelve y una diferencia: “spooling desacopla E/S lenta; multiprogramación solapa CPU y E/S en memoria; tiempo compartido reparte CPU entre usuarios interactivos”.

> [!warning] Errores típicos
> - Usar spooling y multiprogramación como sinónimos.
> - Olvidar que el tiempo compartido necesita planificación por quantum/respuesta.


---

# 1.3.3 Tipos de sistemas operativos

> [!abstract] En una frase
> Los SO se clasifican según el entorno y objetivo: mainframe, servidores, multiprocesadores, personales, móviles/handheld, embebidos, nodos sensores y tiempo real.

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_16.png]]

La diapositiva enumera tipos de sistemas operativos:
- De mainframe: gran capacidad de E/S.
- De servidores: servicios de impresión, web, archivos.
- De multiprocesadores.
- De computadoras personales.
- De PDA o HandHeld.
- Integrados o embebidos.
- De nodos sensores.
- En tiempo real.

## Desarrollo por tipo

| Tipo | Objetivo principal | Ejemplos/rasgos |
|---|---|---|
| **Mainframe** | Alto throughput, mucha E/S, muchos trabajos | Batch, procesamiento masivo |
| **Servidor** | Atender múltiples usuarios/servicios en red | Web, archivos, impresión, bases de datos |
| **Multiprocesador** | Aprovechar varias CPUs/núcleos | Planificación SMP, sincronización |
| **PC / escritorio** | Usabilidad, aplicaciones interactivas | Windows, Linux desktop, macOS |
| **Handheld / móvil** | Energía, conectividad, interfaz táctil | Android, iOS |
| **Embebido** | Función específica dentro de un dispositivo | Routers, electrodomésticos, autos |
| **Nodos sensores** | Bajo consumo, red distribuida, eventos | IoT, redes de sensores |
| **Tiempo real** | Cumplir plazos temporales | Control industrial, médico; hard/soft real-time |

## Complemento de libro (Tanenbaum)
Tanenbaum agrega la distinción entre **hard real-time** (no se puede perder el plazo) y **soft real-time** (se tolera degradación ocasional), y explica que los SO móviles/embebidos priorizan energía, memoria y confiabilidad.

## Cómo responderlo en el final
Elegí el tipo según el escenario: si hay plazos estrictos, tiempo real; si hay muchos servicios en red, servidor; si es un dispositivo con función específica, embebido. Nombrá el objetivo y una característica.

> [!warning] Errores típicos
> - Confundir “tiempo real” con “muy rápido”.
> - Describir un SO de servidor como si fuera solo un SO de PC con más RAM.


---

# 1.4.1 Sistema de archivos y directorios

> [!abstract] En una frase
> El **sistema de archivos** es la abstracción que el SO ofrece para almacenar datos persistentes: organiza información en **archivos** y **directorios**, ocultando detalles del disco.

## Diapositiva de cátedra: archivos

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_21.png]]

La diapositiva indica que una función principal del SO es la **abstracción** del funcionamiento de discos y otras E/S.
- Se usan **llamadas al sistema** para administrar archivos.
- Para agrupar y organizar archivos se usan **directorios**.
- Los directorios permiten crear **jerarquías (árboles)**.
- Cada archivo tiene su **path** desde el directorio raíz.
- En cada instante un proceso tiene un **directorio de trabajo**.

## Diapositiva: jerarquía

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_22.png]]

La imagen muestra la organización jerárquica típica: directorio raíz, subdirectorios y archivos.

## Diapositiva: archivos montados

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_23.png]]

En Unix, los sistemas de archivos de dispositivos externos (CD/DVD, discos, USB) se **montan** sobre el directorio raíz. Esto elimina dependencia de prefijos de unidad y unifica la vista del árbol.

## Diapositiva: pipes

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_25.png]]

Un **canal o pipe** es un pseudo-archivo relacionado con procesos y archivos: permite la **comunicación entre procesos**.

## Conceptos clave

| Concepto | Qué es | Ejemplo |
|---|---|---|
| **Archivo** | Unidad lógica de información persistente | `informe.txt` |
| **Directorio** | Contenedor que organiza archivos/otros directorios | `/home/usuario` |
| **Path** | Ruta desde raíz o desde directorio actual | `/etc/passwd` |
| **Directorio de trabajo** | Contexto actual del proceso | `pwd` |
| **Montaje** | Integrar un FS en el árbol | montar USB en `/media/...` |
| **Pipe** | Canal de comunicación con interfaz tipo archivo | `ls | grep txt` |

## Complemento de libro (Tanenbaum)
Tanenbaum detalla implementación (inodos, bloques, journaling), permisos, enlaces duros/simbólicos y consistencia. Para el final de intro, alcanza con la abstracción, jerarquía, montaje y la idea de pipe como mecanismo de IPC con interfaz de archivo.

## Cómo responderlo en el final
“El SO abstrae el disco como archivos y directorios. Los directorios forman una jerarquía, cada archivo tiene un path, los FS se montan y los pipes permiten comunicación entre procesos con interfaz de archivo”.

> [!warning] Errores típicos
> - Confundir archivo lógico con bloque físico del disco.
> - Olvidar que el directorio de trabajo es por proceso.


---

# 1.4.2 Archivos especiales de bloque y de caracteres

> [!abstract] En una frase
> En Unix, muchos dispositivos se representan como **archivos especiales**: de **bloque** (acceso por bloques direccionables) o de **caracteres** (flujo de caracteres), lo que permite una interfaz uniforme.

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_24.png]]

La diapositiva explica:
- Se utilizan para **modelar dispositivos de E/S**.
- Permiten realizar una **abstracción** de los dispositivos.
- Existen dos tipos especiales:
  - **De bloque:** colección de bloques direccionables al azar; modelan dispositivos como discos.
  - **De caracteres:** flujos de caracteres; modelan dispositivos como impresoras, terminales, etc.

## Comparación

| Tipo | Acceso | Ejemplos típicos | Operación típica |
|---|---|---|---|
| **Bloque** | Bloques direccionables al azar | discos, SSD, particiones | leer/escribir bloque N |
| **Caracteres** | Flujo/secuencia de bytes/caracteres | terminal, impresora, puerto serie | leer/escribir flujo |

## Por qué importa

- Permite usar la misma interfaz (`open`, `read`, `write`, `close`) sobre dispositivos distintos.
- Encapsula detalles de hardware detrás del driver.
- Facilita redirecciones y tuberías en Unix.

## Complemento de libro (Tanenbaum)
Tanenbaum agrega que los drivers de dispositivo implementan la interfaz específica, y que la abstracción de “todo es un archivo” simplifica la programación, aunque no todos los dispositivos encajan perfectamente.

## Cómo responderlo en el final
“Los archivos especiales abstraen dispositivos: los de bloque permiten acceso aleatorio por bloques (discos) y los de caracteres manejan flujos (impresoras/terminales). Ambos se usan con syscalls similares”.

> [!warning] Errores típicos
> - Decir que una impresora es archivo de bloque.
> - Confundir “archivo especial” con “archivo normal con datos del usuario”.


---

# 1.4.3 E/S programada, interrupciones, DMA

> [!abstract] En una frase
> Son tres técnicas para realizar entrada/salida: en la **E/S programada** la CPU espera/gestiona activamente; con **interrupciones** el dispositivo avisa al terminar; con **DMA** el controlador transfiere datos a memoria y la CPU queda libre.

## Diapositivas de cátedra

### Jerarquía de memoria (contexto)

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_14.png]]

La diapositiva muestra tiempos de acceso y capacidades: registros, caché, memoria principal, disco. Esta jerarquía explica por qué la E/S de disco es mucho más lenta que la CPU/memoria y por qué conviene solapar trabajo.

### Dispositivos de E/S e interrupciones

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_15.png]]

La diapositiva presenta la relación entre dispositivos de E/S e interrupciones: el hardware de E/S necesita coordinarse con la CPU sin obligarla a esperar inútilmente.

## Comparación de técnicas

| Técnica | Quién mueve los datos | CPU durante la operación | Ventaja | Desventaja |
|---|---|---|---|---|
| **E/S programada** | CPU | Ocupada esperando/polling | Simple | Desperdicia CPU |
| **E/S por interrupciones** | CPU, por evento/bloque | Puede hacer otra cosa entre interrupciones | Mejor uso de CPU | Overhead por interrupción |
| **DMA** | Controlador DMA | Libre tras iniciar la transferencia | Muy eficiente para bloques grandes | Requiere hardware DMA; coordinación |

## Flujo resumido

1. **Programada:** CPU pregunta “¿listo?” repetidamente; cuando listo, copia dato.
2. **Interrupciones:** CPU inicia operación; dispositivo interrumpe cuando termina; CPU atiende.
3. **DMA:** CPU configura origen/destino/tamaño; DMA transfiere; DMA interrumpe al finalizar.

## Complemento de libro (Tanenbaum)
Tanenbaum detalla controladores de dispositivo, buffers, interrupciones y el rol del DMA en E/S de bloques. El punto clave: reducir tiempo de CPU desperdiciado y aumentar solapamiento, lo que habilita multiprogramación.

## Cómo responderlo en el final
Nombrá las tres técnicas en orden de evolución, explicá quién mueve los datos y qué hace la CPU. Cerrá con: “DMA libera más a la CPU y es clave para solapar E/S con cómputo”.

> [!warning] Errores típicos
> - Decir que en DMA “no hay ninguna interrupción”: sí hay, normalmente al finalizar.
> - Confundir interrupción con polling.


---

# 1.4.4 Máquinas virtuales, hipervisor, JVM y CLR

> [!abstract] En una frase
> Una **máquina virtual** es una abstracción de una máquina: puede virtualizar hardware completo (hipervisor/VMM) o proveer un entorno de ejecución para procesos (JVM, CLR).

## Diapositiva de cátedra

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_41.png]]

La diapositiva de “Estructura de un sistema operativo – Máquinas virtuales” menciona:
- **VM/370**
- **Virtualización**
- **JVM - CLR**

Esto marca dos familias que en el examen se suelen confundir.

## Dos familias

| Tipo | Qué virtualiza | Qué corre encima | Ejemplos |
|---|---|---|---|
| **VM de sistema / hipervisor / VMM** | Hardware completo | Sistemas operativos invitados | VM/370, VMware, VirtualBox, KVM, Hyper-V |
| **VM de proceso** | Entorno de ejecución | Un proceso/programa | JVM, CLR |

## Hipervisor / VMM

- Se interpone entre hardware y SOs invitados.
- Multiplexa CPU, memoria, disco y dispositivos.
- Aísla máquinas virtuales entre sí.
- Útil para consolidación, pruebas, aislamiento y compatibilidad.

## JVM y CLR

- **JVM:** ejecuta bytecode Java.
- **CLR:** ejecuta CIL/IL de .NET.
- Proveen runtime: carga de clases/ensamblados, GC, verificación, JIT/interpretación.
- **No** virtualizan hardware completo; virtualizan un entorno de proceso.

## Complemento de libro (Tanenbaum)
Tanenbaum explica la virtualización como técnica de aislamiento y portabilidad. También distingue la virtualización de lenguaje/runtime (JVM) de la virtualización de máquina real (hipervisores tipo 1 y 2).

## Cómo responderlo en el final
“Un hipervisor virtualiza hardware y permite ejecutar SOs invitados. JVM y CLR son VM de proceso: ejecutan bytecode/IL en un runtime, no simulan hardware completo”.

> [!warning] Errores típicos
> - Llamar a JVM/CLR “hipervisor”.
> - Decir que la VM siempre ejecuta un SO invitado completo.


---

# 1.4.5 Práctica — consultar fecha y hora del sistema (TP1, preguntas 5 y 6)

> [!abstract] En una frase
> Un comando como `date` o un programa que lee la hora **pide** la fecha al kernel mediante una llamada al sistema; el kernel la lee del reloj de hardware y la devuelve al programa, que la muestra.

## Desarrollo
Secuencia (válida para Linux y Windows):
1. El usuario escribe `date` (Linux) o `date /t` / `time /t` (Windows) en el shell.
2. El shell crea un proceso hijo y lo ejecuta (`fork` + `execve`, ver 1.1.2).
3. El programa llama a una función de biblioteca de tiempo, que hace la **llamada al sistema** correspondiente.
4. El kernel lee el **reloj de hardware** (RTC) y lo convierte a fecha y hora.
5. Devuelve el valor por el mecanismo de retorno; el programa lo formatea y lo imprime.

**Qué pasa dentro del SO** (pasos 3–4) y **qué pasa fuera** (el shell, el programa, la pantalla). La pregunta 6 pide lo mismo desde un programa propio (C#, VB .NET o C): el código llama a la API de fecha y la biblioteca de .NET termina en una syscall.

> [!tip] Para el examen escrito
> Describí la cadena: **usuario → shell → proceso hijo → biblioteca → syscall (TRAP) → kernel → reloj de hardware → vuelta a modo usuario → pantalla**.

## Cómo responderlo en el final
Recitar la cadena de arriba. Es la pregunta que más une teoría (modo kernel, syscall, fork) con práctica.


---

# 1.5.1 Estructuras de sistemas operativos

> [!abstract] En una frase
> La **estructura** de un SO define cómo se organiza su código y dónde se ejecutan sus componentes: puede ser un bloque único en modo kernel (monolítico), organizado en capas, reducido a un núcleo mínimo (microkernel), distribuido como cliente-servidor, o basado en máquinas virtuales.

## Diapositivas de cátedra

Las diapositivas de Introducción cierran con las estructuras típicas de un SO. Se usan como base de este subtema.

## 1. Monolítico

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_36.png]]

**Idea de la diapositiva:** todo el sistema operativo se ejecuta como un solo programa en modo kernel. Es la organización más común.

- Un **programa principal** invoca procedimientos de servicio.
- Un conjunto de **procedimientos de servicio** realiza las llamadas al sistema.
- Los procedimientos pueden llamarse entre sí, pero conviene estructurarlos.
- Hay **procedimientos utilitarios** que ayudan a los de servicio.

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_37.png]]

**Estructura típica (diapositiva):** programa de usuario → programa principal → procedimientos de servicio → procedimientos utilitarios; debajo, el hardware. La llamada entra al kernel y se despacha internamente.

| Ventaja | Desventaja |
|---|---|
| Rendimiento: llamadas internas rápidas, sin mucho overhead | Un bug en un componente kernel puede tumbar todo el sistema |
| Diseño simple y directo | Difícil de mantener cuando crece mucho |

## 2. Sistemas por capas

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_38.png]]

**Idea de la diapositiva:** el SO se organiza en niveles, donde cada capa usa servicios de la inferior. Ejemplo clásico de la cátedra:

| Capa | Rol |
|---:|---|
| 5 | Operador |
| 4 | Programas de usuario |
| 3 | Administración de entrada/salida |
| 2 | Comunicación operador–proceso |
| 1 | Administración de memoria |
| 0 | Asignación de procesador y multiprogramación |

> [!note] Dato de cátedra
> Multics lo utilizaba en forma de anillos concéntricos.

| Ventaja | Desventaja |
|---|---|
| Modularidad, separación de responsabilidades | Puede ser difícil definir bien las capas; overhead por cruces entre niveles |

## 3. Microkernel

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_39.png]]

**Idea de la diapositiva:** el kernel se reduce al mínimo; servicios como drivers, sistemas de archivos o servidores corren en modo usuario como procesos separados. La cátedra menciona **Symbian** y **Minix**.

- **En kernel:** IPC, interrupciones, planificación básica, manejo básico de memoria/protección.
- **En modo usuario:** servidores/drivers (archivos, dispositivos, red, etc.).

| Ventaja | Desventaja |
|---|---|
| Más robusto y seguro: un fallo en un servidor no tumba el kernel | Mayor costo por comunicación entre procesos (IPC) y cambios de modo |

## 4. Cliente–servidor

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_40.png]]

**Idea de la diapositiva:** los servicios del sistema se ofrecen como servidores; los clientes (programas o componentes) piden servicios mediante mensajes. Es una forma natural de organizar sistemas distribuidos o basados en microkernel.

- **Cliente:** solicita un servicio (ej. archivo, impresión, nombre).
- **Servidor:** recibe la solicitud, la procesa y responde.
- Puede funcionar en una misma máquina o sobre red.

| Ventaja | Desventaja |
|---|---|
| Modularidad, distribución, aislamiento | Overhead de mensajería; complejidad en fallos de red/servicio |

## 5. Máquinas virtuales

![[Complementario/MATERIA-COMPLETA/_slides/Unidad 1/slide_41.png]]

**Idea de la diapositiva:** se presenta la virtualización como estructura/técnica de SO. La cátedra menciona **VM/370**, virtualización, y también **JVM / CLR**.

- **VM de sistema / hipervisor:** abstrae hardware y permite ejecutar varios SO invitados. Ej.: VM/370, VMware, VirtualBox.
- **VM de proceso:** no virtualiza hardware completo; ejecuta un programa en un entorno de ejecución. Ej.: JVM, CLR.

> [!warning] Trampa de examen
> JVM y CLR **no son hipervisores**: son máquinas virtuales de proceso. Ver desarrollo completo en [[1.4.4 Máquinas virtuales, hipervisor, JVM y CLR]].

## Comparación rápida

| Estructura | Núcleo en kernel | Punto fuerte | Punto débil |
|---|---|---|---|
| Monolítico | Casi todo | Velocidad | Fragilidad/mantenimiento |
| Capas | Todo, pero organizado por niveles | Modularidad conceptual | Definir capas y overhead |
| Microkernel | Mínimo | Robustez/aislamiento | Costo de IPC |
| Cliente–servidor | Depende; común con microkernel | Distribución/modularidad | Mensajería/fallos |
| Máquinas virtuales | Hipervisor/VMM | Aislamiento, múltiples SO | Overhead de virtualización |

## Complemento de libro (Tanenbaum)
Tanenbaum presenta estas estructuras como respuestas al problema de complejidad de los SO modernos: monolíticos por eficiencia, por capas por diseño ordenado, microkernels por confiabilidad, cliente-servidor por distribución y máquinas virtuales por aislamiento/compatibilidad. La elección depende del objetivo: rendimiento, seguridad, mantenimiento o portabilidad.

## Cómo responderlo en el final
Nombrá la estructura, decí **qué va en kernel**, una **ventaja**, una **desventaja** y un **ejemplo**. Si comparan monolítico vs. microkernel, cerrá con: “monolítico prioriza rendimiento; microkernel prioriza aislamiento/robustez”.


---
