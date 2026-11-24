---
tipo: teoria
---

# Preguntas de teoría — Final (escrito)

> [!abstract] Cómo usar este par de archivos
> Este archivo tiene **solo las preguntas**. Intentá responder cada una por escrito (definición + cómo funciona + por qué existe/límite). Después corregí con [[02 Respuestas detalladas]].
> 
> **Orden de lectura:** seguí las secciones en orden; van de conceptos base a memoria virtual, que es el orden en que se construyen los temas en el final.

## A. Conceptos base y estructura del SO

1. ¿Qué es un sistema operativo? ¿Qué funciones principales cumple?
2. ¿Qué diferencia hay entre modo usuario y modo kernel? ¿Por qué existe esa separación?
3. ¿Qué es una llamada al sistema (syscall)? Da ejemplos y explicá si `time`/`date` es una syscall.
4. ¿Qué diferencia hay entre kernel y shell? ¿El shell es parte del SO?
5. ¿Qué es una interrupción? Diferenciá interrupción de hardware, excepción/trap y syscall.
6. ¿Qué es DMA y qué problema resuelve frente a E/S programada e interrupciones?
7. ¿Qué es el spooling? ¿En qué generación aparece y por qué es importante?
8. ¿Qué es la multiprogramación? ¿Qué problema resuelve y qué relación tiene con el spooling?
9. ¿Qué es una máquina virtual? Diferenciá hipervisor/VMM de JVM/CLR.
10. Compará kernel monolítico y microkernel: ventajas, desventajas y ejemplos.

## B. Procesos, estados y planificación

11. ¿Qué diferencia hay entre programa y proceso? ¿Dónde vive cada uno y cómo se comunican dos procesos?
12. ¿Qué es el PCB (Process Control Block)? ¿Qué información contiene?
13. ¿Cuáles son los estados de un proceso y sus transiciones? ¿Puede pasar de bloqueado a ejecución directo?
14. ¿Qué eventos crean un proceso y qué eventos lo terminan?
15. ¿Qué es la planificación de CPU? Diferenciá planificación de corto, mediano y largo plazo.
16. Explicá FIFO, SJF/SRTF y Round Robin. ¿Qué es el quantum y cómo afecta a la sobrecarga?
17. ¿Qué es el modelo probabilístico de multiprogramación $U = 1 - p^n$? ¿Qué significa cada variable y qué limitaciones tiene?
18. ¿Qué es una condición de carrera? Nombrá mecanismos de sincronización vistos (semáforos, mutex, TSL, Peterson) y cuándo se usan.

## C. Memoria: administración básica

19. ¿Qué es la fragmentación interna y la fragmentación externa? Da un ejemplo numérico de cada una.
20. ¿Qué diferencia hay entre mapa de bits y listas enlazadas para administrar memoria libre?
21. Compará first fit, next fit, best fit y worst fit. ¿Cuál es más rápido y cuál tiende a dejar huecos chicos?
22. ¿Qué es la compactación? ¿Cuándo sirve y cuál es su costo?
23. ¿Qué es el buddy system? ¿Qué es Quick Fit? Mencioná ventaja y desventaja.
24. ¿Qué diferencia hay entre direccionamiento lógico/virtual y físico? ¿Quién hace la traducción?

## D. Paginación, fallos y reemplazo

25. ¿Qué es la paginación? Definí página, marco, tabla de páginas y MMU.
26. ¿Cómo se traduce una dirección virtual a física en paginación? ¿Qué pasa si el bit de presencia es 0?
27. ¿Cómo se calculan desplazamiento, bits de página, cantidad de páginas, marcos y memoria direccionable?
28. ¿Qué es un fallo de página? Enumerá los pasos en orden cuando todos los marcos están ocupados.
29. ¿Qué es la TLB? ¿Qué contiene, por qué acelera y qué pasa en un TLB miss?
30. Compará FIFO, segunda oportunidad/reloj, NRU, LRU y Aging. ¿Qué problema tiene cada uno y qué lo mejora?
31. ¿Qué es la anomalía de Belady? ¿En qué algoritmo ocurre?
32. ¿Qué es el tamaño óptimo de página? Explicá la fórmula $s = \sqrt{2PE}$.
33. ¿Qué son el conjunto de trabajo y el thrashing? ¿Cómo se relacionan?

## E. Tablas avanzadas y segmentación

34. ¿Por qué se usan tablas de páginas multinivel? ¿Cómo se calcula la cantidad de tablas/subtablas?
35. ¿Qué es la tabla de páginas invertida? ¿Cuándo conviene y qué costo tiene su búsqueda?
36. ¿Qué diferencia hay entre paginación, segmentación y segmentación paginada?
37. ¿Cómo se decide si un proceso cabe en un esquema de segmentación con paginación? ¿Qué se calcula por segmento?

## F. Preguntas destacadas / trampa

38. Un tamaño de página de 5 KB, ¿qué problema tiene en un esquema clásico de paginación?
39. En LRU exacto por hardware, ¿cuál es el problema? ¿Cómo lo aproximan Aging/NFU?
40. ¿Por qué la multiprogramación sin DMA pierde sentido? ¿Y qué rol cumple el spooling en la 3.ª generación?
41. Si dos procesos tienen $p$ distintos, ¿cómo se calcula la utilización de CPU?
42. ¿Qué hay que revisar antes de entregar un ejercicio numérico en el final escrito?

---

> [!tip] Siguiente paso
> Corregí tus respuestas con [[02 Respuestas detalladas]]. Después practicá ejercicios en [[01 Enunciados|Enunciados de finales]] y [[02 Resoluciones detalladas|Resoluciones de finales]].
