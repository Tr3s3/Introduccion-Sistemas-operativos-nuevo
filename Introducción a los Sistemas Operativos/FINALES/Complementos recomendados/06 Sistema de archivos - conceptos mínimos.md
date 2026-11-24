---
tipo: complemento
---
# 06. Sistema de archivos — conceptos mínimos

> [!abstract] Por qué importa
> No es el bloque más preguntado en los finales recopilados, pero cierra conceptos básicos de Unidad 1: archivo, directorio, ruta, montaje y tipos especiales.

## Conceptos base

| Concepto | Idea corta |
|---|---|
| **Archivo** | Colección nombrada de datos, administrada por el SO |
| **Directorio** | Estructura que mapea nombres a archivos/subdirectorios |
| **Ruta absoluta** | Desde la raíz (`/` en Unix) |
| **Ruta relativa** | Desde el directorio actual |
| **Metadatos** | Nombre, tamaño, permisos, dueño, fechas, punteros/bloques, etc. |

## Tipos de archivos (visión Unix)

| Tipo | Qué representa | Ejemplo |
|---|---|---|
| **Regular** | Datos o programa | texto, binario |
| **Directorio** | Contenedor de entradas | `/home` |
| **Especial de bloque** | Dispositivo que transfiere en bloques | disco |
| **Especial de carácter** | Dispositivo que transfiere como flujo | teclado, terminal |

## Operaciones típicas

Crear, abrir, leer, escribir, cerrar, borrar, renombrar, cambiar permisos/atributos. Estas operaciones suelen involucrar **llamadas al sistema**.

## Directorio raíz y montaje

- En Unix, la jerarquía empieza en `/`.
- Un sistema de archivos se **monta** en un directorio (punto de montaje) para integrarlo al árbol.
- Esto permite tener distintos discos/particiones bajo una sola jerarquía lógica.

## Bloque vs. carácter

- **Bloque**: acceso por bloques, direccionable; permite leer/escribir bloques específicos. Ej.: disco.
- **Carácter**: flujo de bytes; no se suele direccionar por bloque. Ej.: teclado, puerto serie.

## Trampas de examen

- **El nombre del archivo no es el contenido**: el directorio guarda la asociación nombre→entrada/metadatos.
- **Archivo especial != archivo regular**: representa un dispositivo.
- **Montaje** no es copiar archivos; es hacer visible un FS en un punto del árbol.

## Plantilla de respuesta

1. Definir archivo y directorio.
2. Mencionar metadatos/operaciones.
3. Distinguir archivo regular, bloque y carácter.
4. Si preguntan montaje, explicar punto de montaje y árbol único.

## Relación con el temario

- [[1.4.1 Sistema de archivos y directorios]]
- [[1.4.2 Archivos especiales de bloque y de caracteres]]
- [[1.2.2 Llamadas al sistema]]

---
Volver a: [[00 Índice - Complementos recomendados]]
