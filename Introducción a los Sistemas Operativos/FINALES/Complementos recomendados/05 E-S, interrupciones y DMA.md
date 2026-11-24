---
tipo: complemento
---
# 05. E/S, interrupciones y DMA

> [!abstract] Por qué importa
> Aparece como teoría de base: cómo el SO interactúa con dispositivos. Ayuda también a entender por qué existen bloqueos por E/S en los Gantt de multiprogramación.

## Tres formas de hacer E/S

| Técnica | Quién hace el trabajo | CPU durante la transferencia | Uso típico |
|---|---|---|---|
| **E/S programada (polling)** | CPU consulta estado y mueve datos | Ocupada esperando/moviendo | Simple, dispositivos lentos o chicos |
| **E/S por interrupciones** | Dispositivo avisa al terminar | Libre entre inicio y aviso; atiende interrupción | Mejor que polling para esperas |
| **DMA** | Controlador DMA mueve datos memoria↔dispositivo | Libre durante el bloque; interrupción al final | Transferencias grandes/eficientes |

## E/S programada

1. CPU escribe comando en el controlador.
2. CPU lee repetidamente el registro de estado (busy wait).
3. Cuando está listo, CPU lee/escribe el dato.
4. Repite hasta terminar.

**Problema:** desperdicia CPU.

## E/S por interrupciones

1. CPU inicia la operación y puede hacer otra cosa.
2. El dispositivo genera una **interrupción** cuando termina o necesita atención.
3. CPU guarda contexto mínimo, ejecuta rutina de atención (ISR), restaura contexto.

**Mejora:** la CPU no hace polling continuo. **Costo:** overhead por cada interrupción.

## DMA (Direct Memory Access)

1. CPU programa el controlador DMA: dirección de memoria, cantidad, dispositivo, operación.
2. DMA transfiere datos directamente entre memoria y dispositivo.
3. Al terminar, DMA genera una interrupción.

**Ventaja:** la CPU no mueve byte por byte; se libera para otros procesos.

## Interrupción: idea de examen

Una interrupción es una señal que hace que la CPU suspenda temporalmente la ejecución actual, guarde estado necesario y atienda una rutina del kernel. Después, reanuda si corresponde.

Puede venir por:
- **Hardware**: teclado, disco, timer, DMA.
- **Software/trap**: syscall, división por cero, fallo de página.

## Trampas de examen

- **DMA no elimina toda intervención de CPU**: la CPU configura la transferencia y atiende la interrupción final.
- **Interrupción != polling**: en polling la CPU pregunta; en interrupción el dispositivo avisa.
- **Fallo de página es una trap/excepción**, no una interrupción de dispositivo normal, aunque el tratamiento comparte la idea de “interrumpir el flujo”.

## Plantilla de respuesta

1. Nombrar las tres técnicas.
2. Explicar quién mueve los datos y qué hace la CPU.
3. Destacar ventaja/costo de cada una.
4. Si piden DMA, mencionar: configuración por CPU + transferencia por DMA + interrupción final.

## Relación con el temario

- [[1.4.3 E-S programada, interrupciones, DMA]]
- [[1.2.1 Modo usuario y modo kernel]]
- [[1.2.2 Llamadas al sistema]]

---
Volver a: [[00 Índice - Complementos recomendados]]
