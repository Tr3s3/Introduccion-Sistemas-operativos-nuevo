---
tipo: complemento
---
# 03. Hilos, condición de carrera y sincronización

> [!abstract] Por qué importa
> Puede aparecer como teoría corta: diferencia proceso/hilo, qué es una condición de carrera y cómo se evita. No es de los más repetidos en los finales recopilados, pero es parte normal de la materia.

## Proceso vs. hilo

| Aspecto | Proceso | Hilo (thread) |
|---|---|---|
| Espacio de memoria | Propio | Comparte memoria del proceso |
| Recursos | Archivos, tablas, PCB propios | Comparte la mayoría; tiene pila, registros y PC propios |
| Creación/cambio | Más costoso | Más liviano |
| Fallo | Aislado (en general) | Puede afectar al proceso completo |
| Comunicación | IPC (pipes, memoria compartida, etc.) | Más directa por memoria compartida, requiere sincronización |

> [!tip] Respuesta corta
> Un proceso es una unidad de recursos y protección; un hilo es una unidad de ejecución dentro de un proceso.

## Condición de carrera

Ocurre cuando **dos o más hilos/procesos acceden a datos compartidos** y el resultado depende del **orden de intercalación** de las ejecuciones.

Ejemplo típico: `contador = contador + 1` en dos hilos.
1. Hilo A lee contador (5).
2. Hilo B lee contador (5).
3. Hilo A escribe 6.
4. Hilo B escribe 6.  
Resultado esperado: 7; resultado real: 6.

## Sección crítica

Porción de código que accede a un recurso compartido. Debe cumplir:

- **Exclusión mutua**: si un hilo está en su sección crítica, ningún otro entra a la misma sección crítica.
- **Progreso**: si nadie está en la sección crítica, la decisión de quién entra no se posterga indefinidamente.
- **Espera acotada**: un hilo no espera para siempre.

## Mecanismos

| Mecanismo | Idea | Cuidado |
|---|---|---|
| **Mutex** | Candado: lock/unlock; solo uno entra | Deadlock si se usa mal |
| **Semáforo** | Contador con wait/P y signal/V | Binario (0/1) o contador; orden correcto |
| **Monitor** | Abstracción de alto nivel con exclusión mutua | Depende del lenguaje/runtime |
| **Spinlock** | Espera activa | Útil si la espera es muy corta; desperdicia CPU |

## Trampas de examen

- **Hilos comparten memoria**, por eso la sincronización es crítica.
- **Condición de carrera** no es “que corran rápido”: es dependencia del orden de ejecución.
- **Mutex != semáforo contador** en uso típico, aunque un semáforo binario puede parecerse.
- **Deadlock** es otro problema: bloqueo circular por recursos; no es lo mismo que race condition.

## Plantilla de respuesta

1. Definir proceso e hilo.
2. Dar ejemplo de condición de carrera.
3. Nombrar sección crítica y exclusión mutua.
4. Mencionar un mecanismo (mutex o semáforo) y cómo evita la carrera.

## Relación con el temario

- [[2.3.1 Proceso vs. hilo]]
- [[2.6.1 Comunicación entre procesos (IPC)]]
- [[2.6.2 Sincronización y condiciones de carrera]]

---
Volver a: [[00 Índice - Complementos recomendados]]
