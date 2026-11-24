---
tipo: complemento
---
# 04. Working set, thrashing y PFF

> [!abstract] Por qué importa
> Completa el tema de memoria virtual. Puede aparecer como pregunta conceptual: qué es thrashing, por qué ocurre y cómo se controla.

## Conceptos

| Concepto | Definición corta |
|---|---|
| **Localidad de referencia** | Los programas tienden a usar un subconjunto de páginas durante un intervalo |
| **Working set** | Conjunto de páginas que un proceso necesita en una ventana de tiempo reciente |
| **Thrashing** | El sistema pasa más tiempo paginando que ejecutando procesos útiles |
| **PFF (Page Fault Frequency)** | Controla la tasa de fallos para ajustar marcos asignados |

## Working set

El modelo de **conjunto de trabajo** dice: para ejecutar eficientemente, un proceso necesita tener en memoria las páginas que está usando activamente.

- Si el proceso tiene **menos marcos** que su working set → muchos fallos de página.
- Si tiene **los marcos necesarios** → los fallos bajan.

## Thrashing

Causa típica:
1. Hay demasiados procesos en memoria (grado de multiprogramación alto).
2. A cada proceso le tocan pocos marcos.
3. Los procesos no tienen su working set completo.
4. Aumentan los fallos de página.
5. El disco se satura y la CPU queda ociosa esperando I/O de paginación.

> [!warning] Señal clásica
> CPU con baja utilización + disco de paginación muy ocupado. Agregar más procesos en ese estado puede empeorar todo.

## PFF (Page Fault Frequency)

Regla práctica:
- **Tasa de fallos alta** → el proceso necesita más marcos.
- **Tasa de fallos baja** → el proceso tiene marcos de sobra; se pueden reasignar.

## Local vs. global

| Política | Al reemplazar, se elige marco de... | Efecto |
|---|---|---|
| **Local** | El mismo proceso | Aísla procesos; puede ser rígida |
| **Global** | Cualquier proceso | Más flexible; puede propagar thrashing |

## Trampas de examen

- **Thrashing no es “falta de CPU”**: es falta de marcos para los working sets activos.
- **Más multiprogramación no siempre mejora**: pasado cierto punto, empeora por thrashing.
- **Working set depende del tiempo**: cambia según la fase del programa.

## Plantilla de respuesta

1. Definir working set.
2. Definir thrashing como exceso de paginación.
3. Explicar causa: suma de working sets > memoria disponible.
4. Mencionar control: PFF, ajustar multiprogramación, política local/global.

## Relación con el temario

- [[4.5.2 Conjunto de trabajo y thrashing]]
- [[4.3.1 Pasos de un fallo de página]]
- [[4.1.1 Memoria virtual y overlays]]

---
Volver a: [[00 Índice - Complementos recomendados]]
