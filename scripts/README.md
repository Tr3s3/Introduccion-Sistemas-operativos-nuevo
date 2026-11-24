# Scripts

## `extract_scanned_content.py`

Extrae texto de PDFs e imágenes (JPEG/PNG/WebP/TIFF/BMP), con OCR automático para PDFs escaneados.

### Dependencias

```bash
python3 -m pip install pymupdf rapidocr-onnxruntime opencv-python-headless --break-system-packages
```

Si aparece `libGL.so.1: cannot open shared object file`, usar `opencv-python-headless` en lugar de `opencv-python`.

### Uso

```bash
# Un archivo
python3 scripts/extract_scanned_content.py archivo.pdf -o salida.txt

# Imagen
python3 scripts/extract_scanned_content.py examen.jpg -o salida.txt

# Carpeta completa
python3 scripts/extract_scanned_content.py /ruta/carpeta -o /ruta/salida/
```

### Notas

- **PDF con texto embebido**: extrae texto directamente.
- **PDF escaneado o página con poco texto**: renderiza la página y aplica OCR.
- **Calidad OCR**: puede fallar en manuscrito, fórmulas o escaneos de baja calidad; revisar manualmente.
