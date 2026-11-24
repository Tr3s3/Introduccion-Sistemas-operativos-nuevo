---
tipo: unidad-completa
unidad: 1
---
# Unidad 1 — Introducción al sistema operativo — completa

> [!abstract] Qué pide la unidad
> Qué es un sistema operativo, para qué existe, cómo se separa del hardware y de los programas de usuario, y cómo evolucionó. Base de todo lo demás: sin esto no se entiende por qué existen procesos, memoria virtual ni llamadas al sistema.

> [!info] Cómo leer este archivo
> Es la unidad entera, en orden: Tema → Subtema. Cada subtema tiene su nota propia en la carpeta del tema, por si querés estudiar uno solo.


---

## Tema 1.1 — Qué es un sistema operativo


### 1.1.1 Definición y funciones

> [!abstract] En una frase
> El **sistema operativo (SO)** es el programa (o conjunto de programas) que se ubica entre el **hardware** y las **aplicaciones**: les da una máquina **más simple** (abstracción) y **administra** los recursos (CPU, memoria, E/S, archivos) de forma ordenada y protegida.

#### Desarrollo
Una computadora es un sistema complejo: uno o más procesadores, memoria principal, discos, impresoras, teclado, red y otros dispositivos. Si cada programador tuviera que entender todo eso, no escribiría código. Por eso el SO cumple **dos funciones principales**:

| Función | Qué significa | Ejemplo |
|---|---|---|
| **Abstracción** (máquina extendida) | Oculta el hardware y ofrece objetos simples: archivos, procesos, sockets | Un programa hace `read()` de un archivo; no necesita saber en qué sector del disco está |
| **Administración de recursos** | Decide quién usa qué recurso, cuánto y cuándo; media en los conflictos | Dos impresiones simultáneas se encolan en vez de mezclarse en el papel |

Funciones secundarias que suelen mencionarse: **protección y seguridad** (aislar procesos entre sí), **servicios a los programas** (llamadas al sistema), **contabilidad** del uso de recursos e **interfaz** con el usuario.

> [!note] Dato de escala (Tanenbaum)
> El código de un SO como Linux o Windows ronda los **5 millones de líneas**. Por eso un SO evoluciona durante décadas y casi nunca se reescribe desde cero.

#### Cómo responderlo en el final
1. Definición en una frase: intermediario entre hardware y programas.
2. Función 1, **abstracción**, con el ejemplo del archivo.
3. Función 2, **administración de recursos**, con el ejemplo de la impresora o la memoria.
4. Cerrar con protección como función secundaria.

> [!warning] Errores típicos
> - Decir que el SO **es** lo que ve el usuario (eso es el shell o la GUI; ver 1.1.2).
> - Confundir **abstracción** (simplifica la vista) con **administración** (reparte el recurso real).


### 1.1.2 Kernel, shell y programas del sistema

> [!abstract] En una frase
> El **kernel** es el núcleo del SO y corre en modo privilegiado. El **shell** (o la GUI) es un programa de **usuario** que traduce lo que escribe el usuario en llamadas al sistema: **no es parte del SO**.

#### Desarrollo
- **Kernel:** administra CPU, memoria, E/S e interrupciones, y ofrece las llamadas al sistema.
- **Shell:** intérprete de comandos. Basado en texto (bash, cmd) o gráfico (GUI). Si lo reemplazás por otro shell, el SO sigue igual.
- **Programas del sistema vs. de aplicación:** los primeros administran la operación de la máquina (el SO y sus utilidades); los segundos dan servicio al usuario (navegador, editor).
- Compiladores, editores e intérpretes de comandos **no son parte del SO** (cátedra). Tampoco el programa que permite cambiar la contraseña: se ejecuta en modo usuario aunque haga algo delicado.

### Ejemplo: un shell simple (TP1, pregunta 13)
```c
while (TRUE) {
    type_prompt();                      // muestra el prompt
    read_command(command, parameters);  // lee la línea del usuario
    if (fork() != 0) {                  // el padre crea un hijo y espera
        waitpid(-1, &status, 0);
    } else {                            // el hijo reemplaza su imagen por el comando
        execve(command, parameters, 0);
    }
}
```
- `fork()` crea un **proceso hijo** idéntico al shell. En el padre devuelve el PID del hijo (≠ 0); en el hijo devuelve **0**.
- El padre espera con `waitpid` a que termine el hijo, y vuelve a mostrar el prompt.
- El hijo ejecuta `execve`, que **reemplaza** su programa por el comando pedido (`ls`, `cp`…).
- Todo esto son **llamadas al sistema**: el shell en sí no toca el disco ni la CPU, pide servicios al kernel.

#### Cómo responderlo en el final
"El shell es un programa de usuario que lee el comando y pide al kernel que lo ejecute con `fork` + `execve`; el kernel es el que realmente administra el hardware."

> [!warning] Errores típicos
> - "El shell es parte del SO porque el usuario lo usa." **No**: se ejecuta en modo usuario y se puede cambiar.
> - Olvidar que `fork` devuelve valores distintos en padre e hijo.


---

## Tema 1.2 — Modos de operación y llamadas al sistema


### 1.2.1 Modo usuario y modo kernel

> [!abstract] En una frase
> El hardware tiene **dos modos**: **kernel** (o supervisor), con acceso a todas las instrucciones, y **usuario**, con un subconjunto limitado. Solo el SO corre en kernel; cualquier otro programa pasa a kernel únicamente mediante una interrupción o una llamada al sistema.

#### Desarrollo
| | Modo kernel / supervisor | Modo usuario |
|---|---|---|
| Quién corre | El kernel del SO | Aplicaciones, shell, bibliotecas |
| Instrucciones | Todas, incluidas las **privilegiadas** | Solo un subconjunto |
| Acceso a E/S y memoria ajena | Sí | No (la protección del hardware lo impide) |

**Instrucciones privilegiadas** (que solo puede ejecutar el kernel): cambiar el mapa de memoria, deshabilitar interrupciones, grabar el reloj del día, controlar dispositivos de E/S.

### Ejercicio TP1, pregunta 7
| Instrucción | ¿Solo en kernel? | Por qué |
|---|---|---|
| a. Cambiar el mapa de memoria | **Sí** | Podría dar acceso a la memoria de otro proceso |
| b. Leer la hora del día | No | Es una lectura inofensiva; no altera al resto del sistema |
| c. Grabar la hora del día | **Sí** | Alteraría la hora para todos los procesos |
| d. Deshabilitar todas las interrupciones | **Sí** | Un programa podría acaparar la CPU para siempre |

**Respuesta:** a, c y d.

### ¿Por qué el código del SO debe ser lo más chico posible?
Todo lo que corre en kernel tiene poder total: un error ahí puede tirar abajo todo el sistema o comprometer la seguridad. Por eso la idea subyacente es **minimizar la parte privilegiada**: lo que no necesita ser kernel se saca a modo usuario (cuanto menos código privilegiado, menos superficie de error y más fácil de verificar).

#### Cómo responderlo en el final
"Hay dos modos. En kernel se ejecuta el SO con todas las instrucciones; en usuario, los programas con un subconjunto. El cambio se hace por interrupción o llamada al sistema. El código del SO debe ser mínimo porque todo lo que está en kernel puede dañar al sistema entero."

> [!warning] Errores típicos
> - Decir que "el usuario corre en modo usuario y el SO en modo supervisor" sin explicar **por qué** importa la protección.
> - Olvidar que leer la hora **no** es privilegiado y grabarla sí.


### 1.2.2 Llamadas al sistema

> [!abstract] En una frase
> Una **llamada al sistema** es el mecanismo por el que un programa en modo usuario pide un servicio al kernel: coloca los parámetros, ejecuta una instrucción **TRAP** que cambia a modo kernel, el kernel hace el trabajo y devuelve el control.

#### Desarrollo
Secuencia típica (ejemplo UNIX: `count = read(file, buffer, nbytes);`):
1. El programa llama a un **procedimiento de biblioteca** (`read`).
2. Ese procedimiento coloca los parámetros en lugares convenidos (típicamente registros).
3. Ejecuta la instrucción **TRAP** (una "llamada a procedimiento protegida") que pasa a modo kernel.
4. El kernel identifica la llamada, la ejecuta y **vuelve a modo usuario** con el resultado.

Familias de llamadas POSIX (la cátedra las lista por categoría):
- **Procesos:** `fork`, `execve`, `waitpid`, `exit`.
- **Archivos:** `open`, `read`, `write`, `close`, `unlink`.
- **Comunicación:** `pipe`, `socket`, `send`, `recv`.
- **Varias:** `chdir`, `time`/reloj, señales.

> [!important] Llamada al sistema ≠ función de biblioteca
> Desde el código **se ven igual** (es una función con parámetros y retorno), pero no todas las funciones de biblioteca hacen una llamada al sistema: `strlen` o un `printf` sin vaciar el buffer no cruzan a kernel. **Sí importa** que el programador lo sepa, porque una syscall es más **costosa** (cambio de modo), puede **bloquear** el proceso, depende del sistema operativo (**portabilidad**) y puede **fallar** (hay que revisar el valor de retorno).

#### Cómo responderlo en el final
"Un programa pide un servicio con una función de biblioteca que ejecuta TRAP; el kernel valida, ejecuta y devuelve. Desde el código parece una función común, pero cambia el modo de ejecución y tiene costo y posibles bloqueos."

> [!warning] Errores típicos
> - Decir que "la syscall es una función más" sin mencionar el cambio a modo kernel.
> - Creer que todo lo de la biblioteca estándar es una syscall.


---

## Tema 1.3 — Historia y tipos de sistemas operativos


### 1.3.1 Generaciones de computadoras y su SO

> [!abstract] En una frase
> La historia del SO es la historia de **reducir el tiempo que la máquina cara pasa esperando al operador**: de los paneles de control a los lotes, luego multiprogramación y tiempo compartido, y por último la PC.

#### Desarrollo
| Generación | Años | Tecnología | Sistema operativo |
|---|---|---|---|
| **1.ª** | 1945–1955 | Tubos de vacío | No hay SO ni lenguajes: se programa en lenguaje de máquina con paneles y, después, tarjetas perforadas |
| **2.ª** | 1955–1965 | Transistores | **Sistemas por lotes** (batch): el antecesor del SO (IBM 1401 y 7094) |
| **3.ª** | 1965–1980 | Circuitos integrados | **Multiprogramación, spooling y tiempo compartido** (OS/360, Multics → UNIX) |
| **4.ª** | desde 1980 | Integración a gran escala | PC, redes y sistemas distribuidos: CP/M, DOS, UNIX, Windows, Linux, Android |

### El procedimiento de la 2.ª generación (TP1, pregunta 10)
1. El programador escribe el programa en **tarjetas perforadas**.
2. Un operador (con el **IBM 1401**, de bajo costo) lee las tarjetas y las copia a una **cinta** de entrada.
3. El **IBM 7094** (el de cálculo) lee la cinta, procesa el trabajo y escribe el resultado en otra cinta.
4. El 1401 lee esa cinta y **imprime** los resultados.

**Analogía con hoy:** las tarjetas son el archivo que subís a una cola; la cinta es el **spool en disco**; el 7094 es la CPU; la impresora es la cola de impresión. Lo que cambió: hoy el **SO** hace la cola y la planificación, hay discos y controladores de E/S que trabajan en paralelo con la CPU (y DMA, ver 1.4.3), y no hace falta mover cintas a mano.

#### Cómo responderlo en el final
Dar la tabla en tres renglones (generación → tecnología → SO) y, si piden el procedimiento, recitar los 4 pasos del 1401/7094 y su equivalente actual.

> [!warning] Errores típicos
> - Mezclar generación (hardware) con tipo de SO (uso).
> - Decir que la 2.ª generación ya tenía multiprogramación: no, eso es de la 3.ª.


### 1.3.2 Multiprogramación, spooling y tiempo compartido

> [!abstract] En una frase
> **Multiprogramación:** varios procesos en memoria y la CPU alterna entre ellos. **Spooling:** las E/S se encolan en disco y se procesan a su ritmo. **Tiempo compartido:** muchos usuarios en terminales reciben la CPU por turnos cortos.

#### Desarrollo
### Multiprogramación
Mientras un proceso espera una E/S (lenta), otro usa la CPU. Se justifica por dos razones (TP1, pregunta 8):
1. **Aprovechar la CPU:** se reducen los tiempos muertos en que la CPU espera al disco o a la impresora.
2. **Mejorar la respuesta y el uso de recursos:** varios trabajos avanzan a la vez en vez de hacerse uno detrás del otro.

Se formaliza con el modelo probabilístico (ver 2.5.2).

### Spooling
*Simultaneous Peripheral Operations On-Line*. Los datos destinados a un dispositivo lento (impresora) se guardan en un área intermedia (disco) y el dispositivo los consume después. La CPU queda libre apenas escribió en la cola.
- **Ejemplos:** cola de impresión; cola de envío de correo; lectura de tarjetas en el 1401.
- **¿Se usa hoy?** Sí: es la base de las colas de impresión y de cualquier buffer de E/S.
- **¿Por qué no en la 2.ª generación?** No había multiprogramación que aprovechara esa libertad de la CPU, y el almacenamiento intermedio era cinta, lenta y secuencial; el disco aún no era la base de la E/S.

### Tiempo compartido
Varias terminales conectadas a la misma máquina. La CPU da a cada usuario un **quantum** breve, y la alternancia es tan rápida que cada uno siente que la máquina es suya. Multics (MIT, Bell, General Electric) fue el precursor, y de ahí sale UNIX.

#### Cómo responderlo en el final
Definir las tres en una frase cada una, dar un ejemplo de spooling y decir que la multiprogramación es lo que hace posible el tiempo compartido.

> [!warning] Errores típicos
> - Confundir spooling con multiprogramación: el spooling es para **E/S**, la multiprogramación para **CPU**.
> - Decir que el tiempo compartido es "multiprogramación sin quantum": el quantum es lo que lo define.


### 1.3.3 Tipos de sistemas operativos

> [!abstract] En una frase
> El SO cambia según el **uso**: por lotes, interactivo o de tiempo real en la clasificación clásica; y mainframe, servidor, PC, móvil o embebido según el equipo.

#### Desarrollo
Según el tipo de equipo (cátedra):
- **Mainframe:** gran capacidad de E/S, muchos trabajos.
- **Servidores:** impresión, web, archivos.
- **Multiprocesadores:** varios CPU en un mismo sistema.
- **Computadoras personales.**
- **PDA / handheld** y **móviles** (Android, iOS).
- **Integrados o embebidos.**
- **Nodos sensores.**
- **En tiempo real:** la respuesta tiene un plazo garantizado (deadline).

Según el **criterio de servicio** (útil para planificación, ver Unidad 2):
- **Por lotes:** se busca rendimiento (trabajos completados por hora).
- **Interactivo:** se busca tiempo de respuesta corto.
- **Tiempo real:** se busca cumplir plazos.

#### Cómo responderlo en el final
Clasificar por equipo en una lista corta y, si piden "tipo de SO", dar el criterio de servicio y ejemplificar con uno de cada uno.

> [!warning] Errores típicos
> - Llamar "tipo" a la generación o al contrario.


---

## Tema 1.4 — Sistemas de archivos, E-S y máquinas virtuales


### 1.4.1 Sistema de archivos y directorios

> [!abstract] En una frase
> El **sistema de archivos** organiza los datos del disco en archivos con nombre, agrupados en **directorios** jerárquicos, y los ofrece al proceso como una abstracción simple, sin que vea sectores ni bloques.

#### Desarrollo
- **Archivo:** unidad lógica con nombre; el usuario no sabe dónde está en el disco.
- **Directorio:** agrupa archivos; permite jerarquías (árboles). Cada archivo tiene una **ruta (path)** desde la **raíz**.
- **Directorio de trabajo:** en cada instante, cada proceso tiene uno, y las rutas relativas se resuelven desde ahí.
- **Montaje:** en UNIX/Linux, dispositivos externos (CD, USB, discos) se **montan** sobre el árbol de la raíz; no hay "letras" de unidad.

### Raíz: UNIX/Linux vs. Windows (TP1, pregunta 15)
| | UNIX / Linux | Windows |
|---|---|---|
| Raíz | Una sola: `/`. Todo cuelga de ahí | Una raíz **por unidad**: `C:\`, `D:\` |
| Dispositivos | Se montan dentro del árbol (`/mnt/usb`) | Reciben una letra propia |

### ¿Qué es un sistema de archivos? (TP1, pregunta 21)
La forma en que el SO organiza el almacenamiento: nombres, metadatos (tamaño, dueño, permisos, fechas), asignación de bloques del disco a cada archivo y control de acceso.

#### Cómo responderlo en el final
"El sistema de archivos abstrae el disco en archivos y directorios con rutas desde una raíz. En UNIX hay una sola raíz y los discos se montan; en Windows hay una raíz por unidad."

> [!warning] Errores típicos
> - Creer que el archivo "es" el sector del disco.
> - Olvidar el directorio de trabajo al hablar de rutas relativas.


### 1.4.2 Archivos especiales de bloque y de caracteres

> [!abstract] En una frase
> Los **archivos especiales** modelan dispositivos de E/S como si fueran archivos. **De bloque:** accesibles al azar, por bloques (disco). **De caracteres:** flujo secuencial de caracteres (impresora, terminal).

#### Desarrollo
| | De bloque | De caracteres |
|---|---|---|
| Acceso | Bloques **direccionables al azar** (se puede leer el bloque 500 sin leer el 499) | **Flujo secuencial**, un carácter tras otro |
| Ejemplo típico | Disco, SSD, CD | Impresora, terminal, teclado, puerto serie |
| Por qué | Modela un dispositivo con "posiciones" | Modela un dispositivo que "emite o recibe" datos |

Otro pseudo-archivo que aparece en la cátedra: el **pipe** (canal), que enlaza procesos (ver 2.6.1).

#### Cómo responderlo en el final
"Un archivo de bloque representa un dispositivo con posiciones direccionables, como un disco; uno de caracteres, un dispositivo que transmite un flujo, como una impresora."

> [!warning] Errores típicos
> - Invertir los nombres. Regla fácil: **bloque = disco** (se accede por bloques), **caracteres = impresora/terminal**.


### 1.4.3 E-S programada, interrupciones, DMA

> [!abstract] En una frase
> En la **E/S programada** la CPU copia cada byte del dispositivo a la memoria. Con **DMA** un controlador hace esa copia en bloque y avisa con una **interrupción** al terminar, liberando a la CPU.

#### Desarrollo
### Sin DMA (TP1, pregunta 17)
Si cada byte lo lee o escribe la CPU, aparecen tres problemas para la multiprogramación:
1. La CPU está **ocupada copiando** en vez de ejecutar otros procesos.
2. No hay **solapamiento** real entre cálculo y E/S: mientras el dispositivo trabaja, la CPU espera.
3. Cuantos más procesos hay, más tiempo de CPU se consume en E/S, y la multiprogramación pierde sentido.

### Con DMA
El controlador de DMA recibe la dirección de memoria y el tamaño, transfiere el bloque y **genera una interrupción** al final: la CPU interviene una vez por bloque, no una vez por byte.

### Interrupciones
Señal que hace que la CPU deje lo que hace y ejecute una **rutina de servicio** del SO. Hay de hardware (dispositivo, reloj) y de software (señales, syscalls). Ver el procedimiento completo en 2.2.2.

#### Cómo responderlo en el final
"Sin DMA la CPU copia byte a byte y se queda sin tiempo para otros procesos. Con DMA, el controlador mueve el bloque y avisa con una interrupción."

> [!warning] Errores típicos
> - Decir que DMA "hace la E/S más rápida": lo que hace es **liberar la CPU**.


### 1.4.4 Máquinas virtuales, hipervisor, JVM y CLR

> [!abstract] En una frase
> Una **máquina virtual** simula una computadora completa sobre una real. El **hipervisor** reparte el hardware físico entre varias VMs aisladas. La **JVM** y el **CLR** son máquinas virtuales de **proceso**: simulan un entorno de ejecución, no el hardware entero.

#### Desarrollo
- **Hipervisor (monitor de VM):** divide CPU, memoria y dispositivos entre las VMs y las aísla, como si fueran máquinas distintas.
- **Usos:** correr varios SO en una misma máquina física, pruebas, servidores aislados.
- **JVM / .NET CLR (TP1, pregunta 22):** no simulan todo el hardware; ejecutan **bytecode** (o IL) en un entorno que administra memoria y tipos. Una VM de proceso vive dentro de un SO; un hipervisor vive debajo de varios SO.

| | Hipervisor | JVM / CLR |
|---|---|---|
| Qué simula | Una computadora completa | Un entorno para un programa |
| Qué ejecuta | Otros sistemas operativos | Bytecode / IL |
| Dónde corre | Directamente sobre el hardware | Como un proceso más del SO |

#### Cómo responderlo en el final
"El hipervisor simula hardware completo para correr varios SO aislados. La JVM y el CLR son VMs de proceso: ejecutan bytecode y no reemplazan al SO."

> [!warning] Errores típicos
> - Llamar "máquina virtual" a la JVM como si simulara hardware físico.


### 1.4.5 Práctica — consultar fecha y hora del sistema (TP1, preguntas 5 y 6)

> [!abstract] En una frase
> Un comando como `date` o un programa que lee la hora **pide** la fecha al kernel mediante una llamada al sistema; el kernel la lee del reloj de hardware y la devuelve al programa, que la muestra.

#### Desarrollo
Secuencia (válida para Linux y Windows):
1. El usuario escribe `date` (Linux) o `date /t` / `time /t` (Windows) en el shell.
2. El shell crea un proceso hijo y lo ejecuta (`fork` + `execve`, ver 1.1.2).
3. El programa llama a una función de biblioteca de tiempo, que hace la **llamada al sistema** correspondiente.
4. El kernel lee el **reloj de hardware** (RTC) y lo convierte a fecha y hora.
5. Devuelve el valor por el mecanismo de retorno; el programa lo formatea y lo imprime.

**Qué pasa dentro del SO** (pasos 3–4) y **qué pasa fuera** (el shell, el programa, la pantalla). La pregunta 6 pide lo mismo desde un programa propio (C#, VB .NET o C): el código llama a la API de fecha y la biblioteca de .NET termina en una syscall.

> [!tip] Para el oral
> Describí la cadena: **usuario → shell → proceso hijo → biblioteca → syscall (TRAP) → kernel → reloj de hardware → vuelta a modo usuario → pantalla**.

#### Cómo responderlo en el final
Recitar la cadena de arriba. Es la pregunta que más une teoría (modo kernel, syscall, fork) con práctica.

