---
tipo: complemento
---
# 01. TLB — tiempo efectivo de acceso

> [!abstract] Por qué importa
> La TLB ya aparece en la teoría de memoria virtual. En un final escrito puede pedirse el **tiempo efectivo de acceso a memoria (EAT)** con hit/miss de TLB. Es un cálculo corto si se dejan claras las suposiciones.

## Idea clave

La **TLB** (Translation Lookaside Buffer) es una caché pequeña y rápida de traducciones recientes página→marco. 

- **Hit de TLB:** la traducción está en TLB.
- **Miss de TLB:** hay que consultar la tabla de páginas en memoria (y, según el esquema, puede haber varios niveles).

## Fórmula base (tabla de páginas de 1 nivel, en memoria)

Supuestos habituales:
- $t_{TLB}$ = tiempo de acceso a TLB.
- $t_m$ = tiempo de acceso a memoria.
- $h$ = tasa de hit de TLB ($0 \le h \le 1$).
- La tabla de páginas está en memoria.
- No hay fallo de página.

| Caso | Qué pasa | Tiempo |
|---|---|---:|
| **Hit** | Buscar en TLB + acceder al dato en memoria | $t_{TLB} + t_m$ |
| **Miss** | Buscar en TLB + leer entrada de tabla en memoria + acceder al dato | $t_{TLB} + t_m + t_m = t_{TLB} + 2t_m$ |

$$
EAT = h(t_{TLB}+t_m) + (1-h)(t_{TLB}+2t_m)
$$

Forma simplificada:

$$
EAT = t_{TLB} + (2-h)t_m
$$

## Ejemplo resuelto

> TLB: 20 ns, memoria: 100 ns, hit rate: 98%. Calcular EAT.

$$
EAT = 0.98(20+100) + 0.02(20+200)
$$
$$
EAT = 0.98(120) + 0.02(220) = 117.6 + 4.4 = 122\text{ ns}
$$

**Lectura:** aunque el miss es solo 2%, agrega costo porque obliga a un acceso extra a memoria.

## Variante: tabla multinivel

Con 2 niveles en memoria y miss de TLB:

$$
T_{miss} = t_{TLB} + 3t_m
$$

(un acceso por cada nivel de tabla + un acceso al dato). La fórmula cambia según cuántos niveles haya y si hay caché; **siempre escribir el supuesto**.

## Trampas de examen

- **No confundir hit de TLB con hit de caché de datos**: son caches distintas.
- **Contar accesos a memoria**: en miss, primero tabla(s), después dato.
- **Si hay fallo de página**, el costo de disco domina; el EAT simple de TLB ya no alcanza.
- **Unidades**: ns, µs, ms. Convertir antes de sumar.

## Plantilla de respuesta

1. Escribir supuesto (niveles de tabla, sin page fault).
2. Escribir $T_{hit}$ y $T_{miss}$.
3. Plantear $EAT=hT_{hit}+(1-h)T_{miss}$.
4. Sustituir y dar resultado con unidad.

## Relación con el temario

- [[4.2.1 TLB (memoria asociativa)]]
- [[4.2.2 Tablas multinivel e invertidas]]
- [[4.3.1 Pasos de un fallo de página]]

---
Volver a: [[00 Índice - Complementos recomendados]]
