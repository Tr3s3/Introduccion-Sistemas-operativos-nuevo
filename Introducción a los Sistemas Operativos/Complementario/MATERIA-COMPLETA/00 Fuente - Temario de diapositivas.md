# Temario extraído de las diapositivas de cátedra

> Fuente principal para desarrollar MATERIA-COMPLETA. Extraído de los PDFs de clase subidos por el usuario.

> Regla: usar la diapositiva como columna vertebral; complementar con explicación, ejemplos, trampas y libro (Tanenbaum).


## Unidad 1 — Introducción (diapositivas)

Archivo fuente: `slide_1.txt`

| Pág | Pistas de tema (extraídas del texto de la diapositiva) |
|---:|---|
| 1 | Sistemas Operativos |
| 2 | • Con su software una computadora puede almacenar, / procesar y entregar información. / • Tipos de Software: / • Programas del sistema: |
| 3 | • Una computadora está formada por: / • Uno o mas procesadores / • Memoria principal / • Disco/s |
| 4 | Hardware - Software / . Compiladores, editores e interpretes de comando, entre otros, no son parte del sistema operativo. |
| 5 | • Lenguaje de Máquina: Conjunto de instrucciones / ADD, MOVE, JUMP, etc. / • Microprogramación: Interprete de dichas instrucciones / • Generalmente no son parte del hardware aunque |
| 6 | • Sistema operativo como máquina extendida o virtual / • Permite abstracción del hardware / • Ej: Existen instrucciones para leer en disco, escribir, / mover el brazo del disco, encender el motor, etc. |
| 7 | • Primera generación (1945-1955). Tubos al vacío / • Gran tamaño / • Programación en lenguaje de máquina / • Alto mantenimiento |
| 8 | • Segunda generación (1955-1965). / Transistores y sistemas por lotes. / • Se pueden vender a clientes. “Bajo mantenimiento” / • Constructores, programadores, operadores. |
| 9 | • Sistema por lotes / Historia |
| 10 | • Trabajo por lotes / Historia |
| 11 | • Tercera generación (1965-1980). / Circuitos integrados y Multiprogramación / • Busca terminar con dos líneas de prod. incompatibles / • Orientadas a palabras. Ciencia e ingeniería |
| 12 | • Cuarta generación (desde 1980) Computadora personal / • Circuitos integrados de larga escala / Miles de transistores en 1 cm 2 de silicio / • Bajo precio |
| 13 | Hardware |
| 14 | • Tiempo de acceso y capacidades / Memoria |
| 15 | Dispositivos de E/S e interrupciones |
| 16 | • De mainframe: Gran capacidad E/S / • De servidores: servicios de impresión, web, de archivos. / • De multiprocesadores / • De computadoras personales. |
| 17 | • Procesos / • Espacios de direcciones / • Archivos / • Entrada / Salida |
| 18 | • Un proceso es un programa en ejecución / • Consiste en: / • Programa ejecutable / • Los datos del programa |
| 19 | • Procesos hijos y padres / • Se crean y finalizan mediante llamadas al sistema / • Cada proceso tiene asignado un usuario y un grupo / de seguridad. |
| 20 | • 16 bits -> 64Kb = 65.536 / • 32 bits -> 4Gb = 4.294.967.296 / • 64 bits -> 18.446.744.073.709.551.616 / Espacios de direcciones |
| 21 | • Una de las principales funciones del sistema operativo es / la abstracción del funcionamiento de discos y otras E/S. / • Se utilizan llamadas al sistema para administrarlos. / • Para agrupar y organizar archivos se ... |
| 22 | Archivos |
| 23 | • UNIX los utiliza para acceder a unidades externas: / CD/DVS, discos externos, memorias USB, etc. / • Se montan sobre el directorio raíz / • Eliminan la dependencia de prefijos |
| 24 | • Se utilizan para modelar dispositivos de E/S. / • Permiten realizar una abstracción de los dispositivos / • Existen dos tipos especiales de archivos / • De bloque |
| 25 | • Un canal o un pipe es un pseudo-archivo / • Un canal está relacionado con procesos y archivos / • Permite la comunicación entre procesos / Entrada - Salida |
| 26 | • Los programas se comunican con el sistema operativo por / medio de llamadas al sistema / • Cada llamada del sistema se corresponde con un / procedimiento que es llamado por el programa |
| 27 | Llamadas al sistema |
| 28 | Llamadas al sistema POSIX - Procesos |
| 29 | Llamadas al sistema POSIX - Archivos |
| 30 | Llamadas al sistema POSIX - Archivos |
| 31 | Llamadas al sistema POSIX - Misceláneas |
| 32 | Llamadas al sistema – Un Shell simple |
| 33 | Equivalencias de llamadas al sistema Unix / con procedimientos de la API Win32 |
| 34 | • No es parte del sistema operativo / • El sistema operativo es el código que lleva adelante las / llamadas al sistema / • Es la interface primera entre el usuario y el sistema |
| 35 | Direccionamiento de memoria |
| 36 | • Todo el sistema operativo se ejecuta como un sólo / programa en modo kernel / • Se considera la organización más común / • Un programa principal invoca a los procedimientos de |
| 37 | Estructura de un sistema operativo – / Monolítico |
| 38 | • 5 – El operador / • 4 – Programa de usuario / • 3 – Administración de entrada / salida / • 2 – Comunicación operador – proceso |
| 39 | Estructura de un sistema operativo – / Microkernel / • Symbian y Minix lo utilizan |
| 40 | Estructura de un sistema operativo – / Cliente - Servidor |
| 41 | Estructura de un sistema operativo – / Máquinas virtuales / • VM/370 / • Virtualización |

## Unidad 2 — Procesos y Memoria (diapositivas)

Archivo fuente: `slide_2.txt`

| Pág | Pistas de tema (extraídas del texto de la diapositiva) |
|---:|---|
| 1 | Sistemas Operativos |
| 2 | • Un proceso es la abstracción de un programa en / ejecución / • Todo software ejecutable es organizado en un / número de procesos secuenciales. |
| 3 | Modelo de proceso / • Multiprogramación de cuatro programas / • Modelo conceptual de 4 procesos independientes/secuenc. / • Sólo un programa se encuentra activo por vez |
| 4 | • Inicialización del sistema / • Ejecución de una llamada al sistema de creación de / proceso (fork() en UNIX) / • Requerimiento del usuario de crear un nuevo proceso |
| 5 | • Salida normal - voluntaria / • Salida por error - voluntaria / • Error fatal - involuntario / • Finalizado por otro procesos – involuntario (kill) |
| 6 | • Procesos padres crean procesos hijos / • Los procesos hijos pueden crear sus propios procesos / hijos. / • Se forma una jerarquía |
| 7 | ESTADOS: / • En ejecución: Utilizando la CPU / • Bloqueado: Inhabilitado para ejecutar hasta que ocurra / un evento externo (ej. I/O) |
| 8 | Estados de los procesos y transiciones |
| 9 | TRANSICIONES: / • Bloqueado por entrada / • El planificador elige otro proceso / • El planificador elige este proceso |
| 10 | Que sucede cuando un proceso se encuentra bloqueado / por I/O? / • Intercambio o “Swapping” / Mueve un proceso de memoria disco (suspendido) |
| 11 | • El movimiento de procesos entre memoria y disco / posibilita dos nuevos estados / Swapping de procesos |
| 12 | Implementación de procesos / • En nivel mas bajo de un sistema operativo estructurado / en procesos administra las interrupciones y la / asignación de tiempo |
| 13 | Implementación de procesos / • Algunos de los campos de la tabla de procesos |
| 14 | Implementación de procesos / • Pasos que sigue el nivel inferior del sistema operativo / cuando ocurre una interrupción / 1. El hardware coloca el contador del programa a la pila, etc. |
| 15 | • Un programa debe ser cargado en memoria para ser / ejecutado / • La CPU solo puede acceder a la memoria principal y los / registros. |
| 16 | • Como un ideal deseamos memoria en grandes / cantidades, que sea rápida y no volátil. / • Ley de Parkinson: “Los programas van creciendo de / forma tal que ocupan la memoria disponible para los |
| 17 | • Funciones que realiza el administrador de memoria: / • Registro de la memoria en uso / • Registro de la memoria disponible / • Asignación de memoria a los procesos |
| 18 | • Consideraciones para la administración de memoria: / • Transparencia / • Varios procesos deben poder coexistir en memoria / • Ningún proceso debe necesitar saber que la |
| 19 | • Monoprogramación / • Ineficiente uso de la CPU / • Un proceso usuario + S.O. en memoria / • Cuando el proceso espera por E/S -> CPU ociosa |
| 20 | • Varios procesos usuarios en memoria / • Mientras un proceso espera por E/S, otro proceso / puede utilizar la CPU -> Incrementa el uso de CPU / • Se debe decidir cuantos procesos deben estar en |
| 21 | • n: cantidad de procesos en memoria / • p: % de tiempo que un proceso espera por I/O / • Probabilidad de que n procesos esperen por I/O = pn / Utilización de CPU = 1 – pn |
| 22 | • Tiempo de llegada y tiempo requerido de CPU para 4 / procesos: / • Utilización de la CPU para 1-4 procesos con 80% de / espera de Entrada/Salida: |
| 23 | • Secuencia de eventos: / Análisis de un Sistema de Multiprogramación |
| 24 | • ¿Cómo debe organizarse la memoria para poder tener / más de un proceso en ejecución? / • Primera aproximación: Particiones fijas / (sin swapping o intercambio de páginas) |
| 25 | • La multiprogramación introduce dos problemas que / deben ser resueltos: / • Relocación: Dirección relativa de acuerdo a la / partición de memoria donde se ubica el programa |
| 26 | • Dos registros especiales de hardware: / • Registro base: Almacena la dirección de inicio de la / partición. / • Registro limite: Almacena el tamaño de la partición. |
| 27 | • Dos procesos: mismas direcciones relativas / Relocación o reubicación |
| 28 | • Cada proceso con su espacio de direcciones / Solución a la relocación: |
| 29 | Relocación o reubicación |
| 30 | • La cantidad de particiones, sus tamaños y ubicaciones / cambian dinámicamente / • Se introduce el concepto de swapping o intercambio: / Mover un proceso entre memoria y disco |
| 31 | • La asignación de memoria cambia a medida que los / procesos ingresan o salen de memoria. / Swapping o intercambio |
| 32 | • Asignando espacio para segmentos que pueden crecer / Swapping o intercambio |
| 33 | • Divide la memoria en unidades de asignación fija / • A cada unidad le corresponde un bit en el mapa: / 0 – No usado 1 – Usado / • Asignación de memoria: |
| 34 | • Estructura de datos: / P: Proceso / H: Hueco / • Ordenado por dirección. |
| 35 | • Ej: 5 procesos y 3 huecos / (b) Mapa de bits (c) Lista enlazada / Administración de memoria con listas enlazadas |
| 36 | • Cuando un proceso termina -> 4 posibles uniones: / Administración de memoria con listas enlazadas |
| 37 | • Primero en entrar (first fit): El primer hueco en que cabe / • Próximo en entrar (next fit): Similar pero no empieza / desde el comienzo, sino en el último encontrado. / • Más se ajusta (best fit): Es más lento porq... |
| 38 | • Rápido en entrar (quick fit): Listas separadas para / huecos de medidas requeridas frecuentemente. Al estar / ordenado por medida dificulta la unión al terminar. / • Si se conocen las distribuciones de probabilidad -> |
| 39 | • Buddy System: / • Listas de bloques libres de 2 0, 2 1, 2 2, ….., 2 k, … bytes / hasta la medida de la memoria / • Por ejemplo para un memoria de 1 MB, se necesitan |

## Unidad 3/4 — Administración de Memoria Virtual (diapositivas)

Archivo fuente: `slide_3.txt`

| Pág | Pistas de tema (extraídas del texto de la diapositiva) |
|---:|---|
| 1 | Sistemas Operativos / Administración de / Memoria Virtual |
| 2 | • Algunos programas utilizan más memoria que la / disponible / • Una solución: Programas divididos en overlays / • El programador debe planificar los overlays |
| 3 | Paginación / Memoria Virtual     Mapa de Memoria      Memoria Física                   Disco |
| 4 | • MMU: Unidad de administración de memoria / • Mapea direcciones virtuales en reales / • Pertenece al hardware / Direcciones Virtuales - MMU |
| 5 | • Direccionamiento de memoria / • 16 bits -> 64Kb = 65.536 / • 32 bits -> 4Gb = 4.294.967.296 / • 64 bits -> 18.446.744.073.709.551.616 |
| 6 | Direcciones Virtuales / MOV  REG, 8192 / MOV  REG, 24576 |
| 7 | Direcciones virtuales - MMU |
| 8 | Direcciones Virtuales / El CPU causa una / interrupción al SO |
| 9 | • Si la página no está en memoria, el CPU causa una / interrupción al Kernel del SO. / • El CPU graba el contador del programa en la pila / • Una rutina en assembler graba los registros generales |
| 10 | Page Fault |
| 11 | • El tamaño de la tabla de páginas puede ser muy / grande. / • 64 bits -> 18.446.744.073.709.551.616 / cerca de 20 millones de Terabytes |
| 12 | Tablas de páginas multinivel |
| 13 | Tablas de páginas multinivel / Item o entrada de la tabla de páginas |
| 14 | • Dispositivo de Hardware / • Generalmente es parte del MMU / • Cuando una dirección virtual se presenta primero / chequea si se encuentra en el TLB y el bit de protec. |
| 15 | TLB o memoria asociativa / (Translation Lookaside Buffer) |
| 16 | • Hit Ratio (Ejemplo) / • Acceso a memoria = 100 nseg. / • Acceso a TLB = 20 nseg. / • Acc. Prom. = (0,9 * 20) + (0,1 * 100) = 28 nseg. |
| 17 | • El tamaño de la tabla de páginas puede ser muy / grande.        (64 bits -> 18.446.744.073.709.551.616 / cerca de 20 millones de Terabytes) / Tabla de páginas invertida |
| 18 | • Algoritmo de remplazo óptimo / • NRU: No usado recientemente (bits R y M) / • First In First Out (Low overhead) / • Segunda oportunidad (FIFO con bit R) |
| 19 | • Algoritmo de Reloj / Algoritmos de remplazo de página |
| 20 | • Algoritmo LRU: Menos usado recientemente (HW) / (Se puede predecir en base al pasado) – LL – 64bit Counter – LRU HW Matrix / Algoritmos de remplazo de página |
| 21 | • NRU: Simulando LRU en software = Aging / Algoritmos de remplazo de página |
| 22 | • Resumen / Algoritmos de remplazo de página |
| 23 | • En FIFO, más marcos de página pueden resultar en / más fallos de página / • Ej: / Anomalía de Belady |
| 24 | • Un sistema de paginación se caracteriza por: / • La cadena de referencia del proceso en ejecución: / Lista ordenada de números de páginas utilizadas / por un proceso. |
| 25 | • Siendo: / • M un array que mantiene el estado de memoria. / Dividido en m entradas que están actualmente en / memoria y n – m paginas que han sido |
| 26 | • Cadena de distancias: / • Concepto útil para el modelado y predecir fallos / • Consiste en la distancia entre el tope de la pila y la / ubicación de la página en la misma |
| 27 | Algoritmos de pila |
| 28 | • Distintas funciones de densidad de probabilidad para / las referencias con una cadena de distancia d / Algoritmos de pila |
| 29 | Siendo: / • n = número de páginas virtuales / • Ci = número de ocurrencias con distancia i / • Fm = número de fallos de página que se darán con la |
| 30 | Ejemplo de índice de fallos de página |
| 31 | • Modelo de conjunto de trabajo: WSM / • Reduce el “Thrashing”: cuando un programa genera / fallos de página cada pocas instrucciones / • Prepaginación vs Paginación a demanda |
| 32 | • Políticas de asignación Local vs. Global / Consideraciones para sistemas de paginación |
| 33 | • Indice de frecuencia de fallo de pagina: PFF / Consideraciones para sistemas de paginación |
| 34 | • Tamaño de página pequeño / Ventajas: / • menos fragmentación interna / • menos parte del programa no usado en memoria |
| 35 | • Sobrecarga debido a la tabla de páginas y la / fragmentación interna / s = Tamaño promedio de los procesos en bytes / p = Tamaño de página en bytes |
| 36 | • Optimizando: Busco el mínimo / -se/p 2 + ½ = 0 / • Ej: s = 128K, e = 8 bytes -> Tamaño optimo = 1448 bytes / En la práctica se elige 1K o 2K |
| 37 | • El hardware interrumpe al kernel y graba el contador / del programa en la pila / • Una rutina en código assembler se inicia para grabar / los registros generales y otra información volátil |
| 38 | • Cuando el marco de página se encuentra limpio, el / S.O. busca la dirección de disco donde está la página y / planifica una operación de disco para traerla. / • Cuando una interrupción de disco indica que la página |
| 39 | Instrucción Backup: / Luego del fallo de página se debe reiniciar la instrucción / El problema consiste en identificar si el fallo de página fue / en los operandos o la instrucción. |
| 40 | Instrucción Backup: / Un problema mayor se da con instrucciones con / autoincrementos. / El autoincremeto se puede hacer antes de la referencia a |
| 41 | • Hay páginas que pueden compartirse y otras no, por / ejemplo el programa se puede compartir y los datos no. / • Cuando un proceso / termina no deben |
| 42 | Librerias compartidas por más de un proceso |
| 43 | • Cuando una página es seleccionada para salir de memoria / • Paginación con un área de intercambio estática: / Almacenamiento de páginas en disco |
| 44 | • Cuando una página es seleccionada para salir de memoria / • Paginación dinámica: / Se debe llevar registro / de las páginas en disco |
| 45 | Un espacio de direcciones Espacios separados / Soluciona el problema de aumento de tamaño del espacio / Espacios separados para datos e instrucciones |
| 46 | • Se divide en 3 partes: / • Un administrador de MMU de bajo nivel / • Un administrador de fallos de página que es parte del / kernel |
| 47 | • Administración de fallos de página con un paginador externo / Sistema de gestión de memoria: |
| 48 | Segmentación - Introducción / • Un compilador utiliza varias tablas para poder compilar / Posiblemente incluye: / • El código fuente. El cual puede ser impreso |
| 49 | Segmentación: / • En un espacio de direccionamiento unidireccional, las / tablas crecen y pueden superponerse. |
| 50 | Segmentación: / • Sistema de segmentación: / • Acceder a archivos utilizando direccionamientos de / memoria. |
| 51 | Segmentación: / • Una memoria segmentada permite a cada tabla crecer o / contraerse independientemente de las otras tablas |
| 52 | Segmentación: / • Comparación entre paginación y segmentación: |
| 53 | Segmentación: / • (b)-(d) La fragmentación externa inutiliza memoria / • (e) Compactación para liberar memoria |
| 54 | Segmentación: / • Combinación de segmentación con paginación: / • Cada segmento debe empezar en el límite de una / página |
| 55 | Segmentación: / • Ejemplo de segmentación con paginación: MULTICS / El descriptor del segmento apunta a las tablas de página |
| 56 | Segmentación: / • Ejemplo de segmentación con paginación: MULTICS / Descriptor de segmento |
| 57 | Segmentación: / • Ejemplo de segmentación con paginación: MULTICS / Algoritmo utilizado cuando ocurre una referencia a memoria: / • Por medio del número de segmento se busca el |
| 58 | Segmentación: / • Ejemplo de segmentación con paginación: MULTICS / Algoritmo utilizado cuando ocurre una referencia a memoria: / • Se examina la entrada de la tabla de páginas para la |
| 59 | Segmentación: / • Ejemplo de segmentación con paginación: MULTICS / Dirección virtual de 34 bits |
| 60 | Segmentación: / • Ejemplo de segmentación con paginación: MULTICS / Conversión de la dirección de dos partes |
| 61 | Segmentación: / • Ejemplo de segmentación con paginación: MULTICS / Versión simplificada de la TLB o memoria asociativa / (La versión original soporta dos tamaños de página) |
| 62 | Segmentación: / • Ejemplo de segmentación con paginación: INTEL / El selector |
| 63 | Segmentación: / • Ejemplo de segmentación con paginación: INTEL / Descriptor del segmento |
| 64 | Segmentación: / • Ejemplo de segmentación con paginación: INTEL / Conversión de un par (selector + offset) en una dirección / lineal. |
| 65 | Segmentación: / • Ejemplo de segmentación con paginación: INTEL / Mapeo de una dirección lineal en una dirección física |
| 66 | Segmentación: / • Ejemplo de segmentación con paginación: INTEL / Niveles de protección |