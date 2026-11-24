---
tipo: complemento
---
# 02. Planificación de CPU — FIFO, SJF, SRTF y Round Robin

> [!abstract] Por qué importa
> En los finales recopilados apareció mucho el **Gantt de multiprogramación** ($U=1-p^n$, CPU/E/S). Este complemento cubre otro tipo de Gantt: **planificación de CPU** entre procesos listos, con métricas como espera y turnaround. No son lo mismo.

## Diferencia clave

| Gantt de multiprogramación (E3/E4) | Gantt de planificación de CPU |
|---|---|
| Varios procesos compiten por CPU; algunos se bloquean por E/S | Procesos en cola de listos compiten por CPU |
| Interesa uso de CPU: $U=1-p^n$ | Interesan espera, turnaround, respuesta, equidad |
| El bloqueo por E/S es central | La ráfaga de CPU es central (salvo variante con E/S) |

## Métricas

- **Tiempo de llegada** (Arrival): cuándo entra al sistema.
- **Ráfaga de CPU** (Burst): cuánto CPU necesita.
- **Tiempo de finalización** (Completion, $C$).
- **Turnaround** ($TAT$): $C - Arrival$.
- **Espera** ($WT$): $TAT - Burst$.
- **Respuesta**: desde llegada hasta primera vez que obtiene CPU.

## Algoritmos

| Algoritmo | Regla | Preemptivo | Ventaja | Problema |
|---|---|---:|---|---|
| **FIFO/FCFS** | El que llegó primero | No | Simple | Efecto convoy |
| **SJF** | Ráfaga más corta entre los listos | No | Buen promedio de espera | Puede haber inanición; requiere estimar ráfaga |
| **SRTF** | Versión preemptiva de SJF | Sí | Mejor ante llegadas tardías cortas | Inanición; overhead |
| **Round Robin** | Turno por quantum | Sí | Buena respuesta en time-sharing | Quantum chico: overhead; grande: se parece a FIFO |

## Ejemplo corto

Procesos: P1(0,5), P2(1,3), P3(2,1) = (llegada, ráfaga).

### FIFO
Orden: P1, P2, P3.  
Gantt: `P1 0-5 | P2 5-8 | P3 8-9`

| P | C | TAT=C-A | WT=TAT-B |
|---|---:|---:|---:|
| P1 | 5 | 5 | 0 |
| P2 | 8 | 7 | 4 |
| P3 | 9 | 7 | 6 |

### SJF (no preemptivo)
En t=5 terminaron P2 y P3; entre P2(3) y P3(1), elige P3.  
Gantt: `P1 0-5 | P3 5-6 | P2 6-9`

### Round Robin (q=2)
Cola por llegada/rotación.  
Gantt típico: `P1 0-2 | P2 2-4 | P3 4-5 | P1 5-7 | P2 7-8 | P1 8-9`

> [!tip] En RR
> Si un proceso llega justo cuando otro agota su quantum, seguir el criterio del enunciado/cátedra para el desempate. Si no lo dice, explicitar el criterio adoptado.

## Trampas de examen

- **No confundir FIFO de CPU con FIFO de reemplazo de páginas**.
- **SJF no es lo mismo que SRTF**: SRTF puede desalojar.
- **RR:** el quantum importa; con $q \to \infty$ se parece a FIFO.
- **Starvation/inanición**: SJF/SRTF/prioridades pueden postergar procesos largos/bajos.
- **Aging**: solución a inanición en prioridades (envejece/sube prioridad). No confundir con aging de páginas.

## Plantilla de respuesta

1. Listar llegada y ráfaga.
2. Dibujar Gantt.
3. Calcular $C$, $TAT$, $WT$ por proceso.
4. Si piden promedio, promediar y mostrar cuenta.

## Relación con el temario

- [[2.4.1 Objetivos de la planificación]]
- [[2.4.2 FIFO, SJF y Round Robin (quantum)]]
- [[2.4.3 Prioridades, hambre y aging]]
- [[2.5.2 Modelo probabilístico — U = 1 − pⁿ]] (otro tipo de Gantt)

---
Volver a: [[00 Índice - Complementos recomendados]]
