---
tipo: ejercicios
---

# Ejercicios de modelos: lo justo para el examen

> [!abstract] Cómo usar esta nota
> Cada bloque tiene: **cuándo aparece**, **método**, **ejemplo resuelto** y **trampa**. Si tenés poco tiempo, hacé en orden: 1, 4, 5, 6, 7, 8.

## Checklist rápido (antes de entregar)

- [ ] Escribí **dato → fórmula → sustitución → resultado + unidad**.
- [ ] En paginación: calculé **desplazamiento** antes que bits de página.
- [ ] Verifiqué si el tamaño de página es **potencia de 2**.
- [ ] En memoria: comparé **direccionable vs. física** (la usable es la menor).
- [ ] En Gantt: recalculé **U = 1 − pⁿ** y **U/n** cada vez que llega/termina un proceso.
- [ ] En reemplazo: dije **qué criterio usa** cada algoritmo (carga, última ref, R/M, puntero).

## 1. Bits, páginas y marcos (sale casi siempre)

**Método**
1. `desplazamiento = log2(tamaño_página)`
2. `bits_página = bits_virtuales − desplazamiento`
3. `páginas = 2^(bits_página)`
4. `marcos = memoria_física / tamaño_página`
5. `memoria_direccionable = 2^(bits_virtuales)`

**Ejemplos rápidos**

| Caso | Despl. | Bits pág. | Páginas | Marcos | Ojo |
|---|---:|---:|---:|---:|---|
| 42 bits, 8 KB, 8 GB | 13 | 29 | 2^29 | 2^20 | Parcial 2023 |
| 36 bits, 16 KB, 128 GB | 14 | 22 | 2^22 | 2^23 | 1T Feb 2024 |
| 31 bits, desp. 13, 512 MB | 13 | 18 | 2^18 | 2^16 | 2T Feb 2025 |
| 25 bits, desp. 13, 1 GB | 13 | 12 | 4096 | 131072 | direccionable 32 MB < 1 GB |
| 22 bits, 2 K, 16 M | 11 | 11 | 2048 | 8192 | direccionable 4 MB |
| 9 bits, pág. 8 B, 2 GB | 3 | 6 | 64 | 2^28 | direccionable 512 B |
| 52 bits, 2 KB | 11 | 41 | 2^41 | depende | tabla enorme si es de 1 nivel |
| 56 bits, 16 K, 16 GB | 14 | 42 | 2^42 | 2^20 | tabla lineal inviable |

**Trampas**
- Página **5 KB** (Parcial 2024): no es potencia de 2 → desplazamiento no entero. Es un problema de definición del sistema.
- “¿Cuánta memoria se puede utilizar?” → `min(direccionable, física)`.

## 2. Traducir dirección virtual (tabla dada)

**Método**
1. `página = dir_virtual div tamaño_página`
2. `desplazamiento = dir_virtual mod tamaño_página`
3. Buscar marco de esa página en la tabla.
4. `dir_física = marco * tamaño_página + desplazamiento`

**Ejemplo (Final 27-11-2024 / TP3):** 16 bits, 4 KB, dir. virtual 20500.
- 20500 / 4096 = 5, resto 20.
- Página 5 → marco 3 (según tabla).
- Física = 3 × 4096 + 20 = **12308**.
- Binario (16 bits): 20500 = `0101 0000 0001 0100`; física = `0011 0000 0001 0100`.

**Trampa:** si el desplazamiento es mayor o igual al tamaño de página, la dirección es inválida.

## 3. Tabla multinivel (cantidad de tablas)

**Método**
- Repartí los bits de página entre niveles (ej. 10+10+12, o 4+5+5).
- Tablas totales = `1 + 2^(n1) + 2^(n1+n2) + ...`
- Subtablas = totales − 1 (si no cuentan la raíz).

**Ejemplos**
- **32 bits, 4 KB, 10+10+12** (Final julio 2024): despl. 12, bits pág. 20. 1 + 2^10 = 1025 tablas si se usan los dos niveles de 10; justificar que evita tabla única de 2^20 entradas.
- **25 bits, 3 niveles 4+5+5** (Recuperatorio): despl. 11 (2 KB), páginas 2^14=16384. Tablas = 1 + 2^4 + 2^4×2^5 = 1+16+512 = **529** (528 subtablas).
- **32 bits, 16 KB, 3 niveles 6+6+6** (1T Feb 2024/2025): despl. 14, páginas 2^18. Tablas = 1+64+4096 = **4161**.
- **2 niveles de 14 bits, páginas 64 B, 32 GB** (Recu 2025 T2): offset 6, bits tabla 28, virtual 2^34=16 GB, páginas 2^28, marcos 2^29. Problema: física > direccionable; no se usa toda la RAM.

**Trampa:** aclarar si te piden “tablas” o “subtablas”.

## 4. Tabla invertida

**Método**
- Tabla normal: 1 entrada por **página virtual**.
- Tabla invertida: 1 entrada por **marco físico**.
- `marcos = memoria_física / tamaño_página`
- Si piden factor 2: `entradas = 2 × marcos`

**Ejemplos**
- **64 bits, 16 GB, 8 KB, factor 2** (Junio 2026 / Final julio 2024): marcos = 2^34/2^13 = 2^21. Invertida con factor 2 = **2^22 entradas**. Normal = 2^51 entradas → inviable.
- **64 bits, 64 GB, 16 KB** (Parcial 2025): marcos = 2^36/2^14 = 2^22. Despl. 14, bits pág. 50.

**Trampa:** la invertida ahorra porque escala con RAM, no con espacio virtual.

## 5. Fallo de página (todos los marcos ocupados)

**Respuesta modelo (6 pasos)**
1. La MMU detecta bit de presencia = 0 → **fallo de página**.
2. Se genera **trap** al SO; se guarda estado del proceso.
3. SO localiza la página en disco/swap.
4. Elige **marco víctima** (FIFO/LRU/NRU/reloj). Si no hay libres, hay que reemplazar.
5. Si la víctima tiene **M=1**, se escribe a disco; si M=0, se descarta. Se carga la página nueva y se actualiza tabla (P=1, marco, R/M).
6. Se **reinicia la instrucción** que causó el fallo.

**Trampa:** si todos los marcos están ocupados, el paso 4 siempre implica reemplazo.

## 6. Reemplazo: FIFO, reloj, NRU, LRU, Aging

| Algoritmo | Reemplaza | Problema | Solución / nota |
|---|---|---|---|
| **FIFO** | más vieja por carga | Belady; puede sacar página muy usada | Segunda oportunidad / reloj |
| **2ª oportunidad** | FIFO + bit R | puede dar vueltas | Reloj |
| **Reloj** | puntero circular; R=0 sale, R=1 se limpia | aproximación | eficiente |
| **NRU** | clase más baja (R,M): 00,01,10,11 | pocas clases | limpiar R periódicamente |
| **LRU** | menos usada recientemente | caro exacto (matriz/contador) | Aging/NFU |
| **Aging** | contador más chico; shift + R | aproximación | buen costo |

**Respuesta corta de examen**
- FIFO malo porque “solo mira antigüedad”. Solución: **FIFO con bit R / segunda oportunidad**; más eficiente: **reloj**.
- NRU malo porque “solo 4 clases”. Solución: **Aging** o LRU con mejor hardware.
- LRU HW malo por costo en memoria/hardware. En 32 bits, 4 KB: páginas = 2^20; una matriz n×n o contadores por página son costosos; se aproxima con **Aging**.

## 7. Multiprogramación y Gantt (U = 1 − pⁿ)

**Fórmulas**
- `U = 1 − pⁿ`
- `n >= log(1−U_obj) / log(p)`
- Si `p` distintos: `U = 1 − ∏pᵢ`
- Reparto por intervalo: **cada proceso avanza `U/n` minutos de CPU por minuto de reloj** (convención SAE/cátedra). Al llegar/terminar, recalcular `n` y `U`.

**Ejemplos**
- p=0,5, n=3 → U=87,5%. CPU por proceso = 29,17%.
- p=0,75, U objetivo 90% → n=8.
- **60%, 3 procesos** (1T Feb 2024): 13:00 P1(2,32); 13:05 P2(2,32); 13:12 P3(4,00). Hacer tabla por intervalos, sin redondear.
- **90%, 2 procesos** (Recu 2024 T1): 15:00 y 15:10, 1,38 min c/u. U1=0,1; U2=1−0,9²=0,19; velocidad por proceso 0,095.

**Trampa:** no confundir p=E/S con CPU. No usar duración como reloj si el enunciado la da como CPU.

## 8. Segmentación, paginación y segmentación paginada

**Para responder en 3 líneas**
- **Paginación pura**: divide en páginas fijas. Elimina fragmentación externa, pero tiene interna y tablas grandes.
- **Segmentación pura**: divide en segmentos lógicos variables. Buena para protección/compartición lógica, pero genera **fragmentación externa**.
- **Segmentación con paginación**: segmenta lógicamente y pagina cada segmento. Reduce externa de segmentación y facilita manejo; es la más usada en la práctica.

**Ejercicio típico (cabe/no cabe)**
- Páginas por segmento = `ceil(tamaño / página)`, por cada segmento por separado.
- Total páginas necesarias × tamaño página vs. espacio direccionable.
- **Caso Junio 2026**: 16 bits, 2 KB (32 páginas direccionables). SO 6+3+3=12; Prog 6+11+5=22; total 34 → **no entra**. Con 1 KB (64 páginas): 22+42=64 → **entra justo**.

## 9. Fragmentación, bitmap vs. listas, asignación

**Fragmentación**
- **Interna**: sobra dentro del bloque asignado (particiones fijas/paginación). Ej: proceso 200 KB en bloque 320 KB → 120 KB internos.
- **Externa**: huecos libres dispersos, no alcanza uno contiguo (particiones variables/segmentación). Solución: compactación/paginación.

**Bitmap vs. listas**
- Bitmap: 1 bit por unidad. Tamaño fijo; buscar k ceros seguidos puede ser lento.
- Listas: nodo por segmento (P/H, inicio, tamaño, siguiente). Más flexible; crece con segmentos; fusión fácil.

**Asignación**: first fit (primero que alcanza), next fit (desde último), best fit (menor sobra), worst fit (mayor hueco). Nombrar también Quick Fit y Buddy si piden alternativas.

## 10. Teoría corta que siempre suma

- **Syscall**: interfaz controlada de modo usuario a kernel; provoca trap/cambio de modo. `time` no es syscall: es comando/programa que usa syscalls/servicios del SO.
- **Spooling**: bufferiza trabajos en disco para dispositivos lentos (impresora). Surge fuerte en 3ª generación; desacopla CPU de E/S.
- **TLB**: caché de traducciones página→marco. Acelera acceso; en TLB se guarda página virtual porque la búsqueda es por página virtual.
- **VM**: abstrae hardware; hipervisor/VMM. JVM/CLR son VM de proceso, no de hardware.
- **Estados**: nuevo, listo, ejecución, bloqueado, terminado; con swapping: listo suspendido, bloqueado suspendido. No hay bloqueado→ejecución directo.

## 11. Casos adicionales extraídos por OCR (verificar con original si hay duda)

> Fuente: `Complementario/OCR/`. El OCR puede contener errores en símbolos/números; estos casos se incluyen cuando el enunciado es interpretable.

| Caso (según OCR) | Datos | Resultado clave |
|---|---|---|
| Recu 2025 T2 | 64 bits, página 64 B, RAM 32 GB | Offset 6, tabla 58, 2^58 páginas, 2^29 marcos; tabla lineal inviable → multinivel/invertida |
| Noviembre 2024 | 12 bits, página 32 B, RAM 256 B | Offset 5, página 7 bits=128 páginas, 8 marcos, 4 KB direccionables |
| Junio/Julio 2024 / 2TFeb2025 | 64 bits, 8 KB, 16 GB, invertida factor 2 | Offset 13, 2^21 marcos, 2^22 entradas invertida; directa sería 2^51 |
| Diciembre 2025 | 64 bits, 16 KB, 64 GB | Offset 14, tabla 50, 2^50 páginas, 2^22 marcos; tabla lineal inviable |
| 2T Febrero 2024 | 56 bits, 16 KB, 16 GB | Offset 14, tabla 42, 2^42 páginas, 2^20 marcos; tabla lineal muy grande |
| Recu 2024 / Junio 2026 | Gantt con 90% E/S | `Tcpu = n/0.1`, dividir CPU entre `n` procesos activos; no CPU ociosa si hay listo |

> [!tip] Si te trabás en el examen escrito
> Decí la definición, el criterio del algoritmo, y una trampa típica. Eso muestra dominio aunque no recuerdes un número.
