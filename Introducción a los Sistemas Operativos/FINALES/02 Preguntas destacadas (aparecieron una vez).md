---
tipo: excepcionales
---
# Preguntas destacadas (aparecieron una sola vez)

> [!abstract] Por qué están acá
> Son preguntas que **no se repiten** pero que, por su formato (un problema largo, una práctica de código, una tabla con errores), son las que más pueden sorprender en el final. No hace falta memorizarlas: hay que **entender el patrón** que usan. Cada una remite al subtema que la resuelve.

## Ejercicios de cálculo
| Fuente | Qué pide | Patrón a dominar | Dónde |
|---|---|---|---|
| **TP1-18** | 2 CPU con 2 hilos cada una; tres programas de 5, 10 y 20 ms | Con 4 hilos para 3 programas, cada uno corre en su hilo: el total es el del **más largo**, **20 ms** (sin penalidad por compartir núcleo) | [[03 Ejercicios tipo con resultado]] |
| **TP1-19** | Caché (1,5 ns), RAM (7 ns) y disco (6 ms), con aciertos de 93 % y 97 % | Tiempo medio **jerárquico**: t = h₁·t₁ + (1 − h₁)·[h₂·t₂ + (1 − h₂)·t₃] ≈ **12,6 µs** | [[03 Ejercicios tipo con resultado]] |
| **TP1-23** | Conversiones: microaño a segundos, gigamicrómetro a km, 512 GB a bytes, 6000 Yg a kg | Usar la unidad base y multiplicar por potencias de 10 o de 2: microaño ≈ 31,6 s; 1 Gµm = 1 km; 6000 Yg = **6 × 10²⁴ kg** | [[03 Ejercicios tipo con resultado]] |
| **TP2-8** | Procesos con 50 % de E/S y horarios de inicio y duración | Es un problema de **simulación**: se va sumando el tiempo de CPU de cada proceso según el reparto. Se resuelve con la tabla de eventos del Repaso | [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] |
| **TP2-5** | Compactación de 1 GB cada 3 minutos, 150 ns por byte | Costo = (bytes copiados × 150 ns) ÷ 180 s; mostrar el método antes que el número | [[3.3.2 Particiones variables, swapping y compactación]] |
| **TP3-6** | Procesos en páginas, memoria virtual de 16 páginas, tabla máxima de 128 bytes | Contar páginas por proceso (3, 6, 1, 2, 4 = 16 páginas); el tamaño de entrada sale de la tabla máxima | [[4.1.3 Cálculo de bits, páginas y marcos]] |
| **TP3-9** | Programa de 16 bits con páginas de 4 KB y luego de 256 bytes | Redondear **por segmento** (una página no mezcla segmentos): 17 páginas de 4 KB no entran; 252 de 256 bytes sí | [[4.6.2 Segmentación con paginación y su combinación]] |
| **TP3-7** | 36 bits de dirección, desplazamiento de 13 | Páginas de 8 KB, 2²³ páginas, 65 536 marcos con 512 MB, tabla de 64 MB | [[4.1.3 Cálculo de bits, páginas y marcos]] |
| **PP33** | 64 bits, páginas de 16 KB y 65 GB de RAM | Bits de página = 50; marcos ≈ 4,26 millones | [[4.1.3 Cálculo de bits, páginas y marcos]] |
| **RS, SAE** | Procesos con p distintas (50 % y 90 %) | Si cada proceso tiene su p, la CPU queda ociosa cuando **todos** esperan: U = 1 − ∏pᵢ = 1 − 0,5 × 0,9 = **55 %** | [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] |
| **SAE** | 4 trabajos que esperan 80 % de E/S con llegadas a las 10:00, 10:10, 10:15 y 10:20 | Se recalcula U = 1 − pⁿ **cada vez que llega un trabajo** y se reparte la CPU con round robin | [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] |

## Análisis y criterio
| Fuente | Qué pide | Qué hay que notar | Dónde |
|---|---|---|---|
| **TP3-8** | Tabla de 5 marcos con tiempos de carga y de última referencia; cuál reemplaza NRU, FIFO, LRU y reloj; y "encontrá una inconsistencia" | Aplicar cada criterio con **su** bit o tiempo; la inconsistencia está en la tabla (hay marcos sin usar y páginas con datos que no corresponden a su estado) | [[03 Ejercicios tipo con resultado]] |
| **TP2-2** | Qué fragmentación genera una lista enlazada, y la relación huecos-procesos | Los huecos no pueden estar pegados (se fusionan): con n procesos hay como máximo **n + 1** huecos | [[3.4.2 Listas enlazadas]] |
| **TP3-4** (parte d) | Relación entre los fallos y la cantidad de marcos | Anomalía de Belady: en FIFO, más marcos pueden dar más fallos | [[4.4.1 Óptimo, FIFO y anomalía de Belady]] |
| **PP29** | FIFO con bit R: cómo se mejora | Segunda oportunidad → reloj: mismo criterio, puntero circular | [[4.4.2 Segunda oportunidad y algoritmo del reloj]] |

## Teoría con trampa
| Fuente | Pregunta | Trampa |
|---|---|---|
| **TP1-10** | Procedimiento de la 2.ª generación (IBM 1401 y 7094) y analogía actual | No basta con listar: hay que **comparar** cada paso con su equivalente actual (cola, spool en disco, DMA) |
| **TP1-5 y 6** | Consultar fecha y hora desde el shell y desde un programa propio | Describir la cadena completa: usuario → shell → proceso → biblioteca → **syscall** → kernel → reloj de hardware |
| **TP1-13** | Explicar el shell de código (`fork`, `waitpid`, `execve`) | Explicar qué devuelve `fork` en padre y en hijo, y que `execve` reemplaza la imagen |
| **TP1-22** | JVM y .NET CLR vs. hipervisor | La JVM/CLR no simulan hardware; son VM de **proceso** |
| **TP1-17** | Multiprogramación sin DMA | La CPU copia byte a byte y no hay solapamiento: la multiprogramación pierde sentido |
| **TP2-9** | Programa que simula multiprogramación | Entender el modelo (p, n, reparto) para poder escribir la simulación; el código no se pide literal en el oral |
| **SAE** | Monolítico vs. microkernel | Monolítico: todo en modo kernel, rápido pero frágil. Microkernel: solo lo esencial en kernel, el resto en modo usuario; más robusto pero más lento por IPC |
| **SAE** | Creación y finalización de procesos | Creación: arranque del sistema, llamada (`fork`), solicitud de usuario, trabajo por lotes. Fin: salida normal, error voluntario, error fatal, muerte por otro proceso/SO |
| **SAE** | Buddy system y Quick Fit | Buddy: bloques en potencias de 2, facilita fusión. Quick Fit: listas separadas por tamaños frecuentes, rápido pero difícil de fusionar |

> [!warning] Cuidado con los enunciados de la cátedra
> Algunos ejercicios tienen **datos que no cierran** (por ejemplo, la tabla de TP3-8 o la cantidad de bits de la tabla de TP3-6). En el parcial, decí cuál es el supuesto que usás y seguí. La cátedra valora el método.
