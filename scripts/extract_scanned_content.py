#!/usr/bin/env python3
"""Extrae texto de PDFs y imágenes (JPEG/PNG), con OCR automático para escaneos.

Uso:
  python3 scripts/extract_scanned_content.py archivo.pdf [otro.jpg ...] [-o salida.txt]
  python3 scripts/extract_scanned_content.py carpeta/ -o salida_dir/

Estrategia:
- PDF: intenta extraer texto embebido con PyMuPDF. Si una página tiene poco texto,
  renderiza la página a imagen y aplica OCR.
- Imagen: aplica OCR directamente.
- OCR: usa rapidocr-onnxruntime (instalable por pip, sin dependencias de sistema).
"""
from __future__ import annotations
import argparse, os, sys, io
from pathlib import Path

def load_ocr():
    try:
        from rapidocr_onnxruntime import RapidOCR
    except Exception as e:
        print("ERROR: falta rapidocr-onnxruntime. Instalá con:", file=sys.stderr)
        print("  python3 -m pip install rapidocr-onnxruntime --break-system-packages", file=sys.stderr)
        raise
    return RapidOCR()

def ocr_image(ocr, img_input):
    """img_input: path, bytes, or numpy array/PIL image."""
    result, _ = ocr(img_input)
    if not result:
        return ""
    # result: [[box, text, score], ...]
    lines = []
    for item in result:
        if isinstance(item, (list, tuple)) and len(item) >= 2:
            lines.append(str(item[1]))
        elif isinstance(item, dict) and 'text' in item:
            lines.append(str(item['text']))
    return "\n".join(lines)

def extract_pdf(path: Path, ocr, min_chars=40, dpi=220):
    import pymupdf as fitz  # PyMuPDF
    doc = fitz.open(path)
    parts = []
    for i, page in enumerate(doc):
        text = page.get_text("text") or ""
        if len(text.strip()) >= min_chars:
            parts.append(f"--- page {i+1} (text) ---\n{text.strip()}")
            continue
        # scanned / low text: render + OCR
        pix = page.get_pixmap(dpi=dpi)
        img_bytes = pix.tobytes("png")
        ocr_text = ocr_image(ocr, img_bytes)
        parts.append(f"--- page {i+1} (ocr) ---\n{ocr_text.strip()}")
    return "\n\n".join(parts)

def extract_image(path: Path, ocr):
    return f"--- image {path.name} (ocr) ---\n{ocr_image(ocr, str(path)).strip()}"

def gather_inputs(inputs):
    exts_img = {'.jpg','.jpeg','.png','.webp','.bmp','.tif','.tiff'}
    files = []
    for inp in inputs:
        p = Path(inp)
        if p.is_dir():
            for child in sorted(p.rglob('*')):
                if child.suffix.lower() in exts_img or child.suffix.lower() == '.pdf':
                    files.append(child)
        elif p.is_file():
            files.append(p)
        else:
            print(f"WARN: no existe {inp}", file=sys.stderr)
    # dedupe preserving order
    seen=set(); out=[]
    for f in files:
        r=f.resolve()
        if r not in seen:
            seen.add(r); out.append(f)
    return out

def main():
    ap = argparse.ArgumentParser(description="Extrae texto de PDFs/JPEGs con OCR automático")
    ap.add_argument('inputs', nargs='+', help='Archivos o carpetas PDF/JPEG/PNG')
    ap.add_argument('-o','--output', help='Archivo .txt de salida, o carpeta de salida')
    ap.add_argument('--min-chars', type=int, default=40, help='Mínimo de chars para considerar página con texto')
    ap.add_argument('--dpi', type=int, default=220, help='DPI para renderizar páginas escaneadas')
    args = ap.parse_args()

    files = gather_inputs(args.inputs)
    if not files:
        print("No se encontraron archivos.", file=sys.stderr)
        sys.exit(1)

    ocr = load_ocr()
    outputs = {}
    for f in files:
        ext = f.suffix.lower()
        print(f"[extract] {f}", file=sys.stderr)
        try:
            if ext == '.pdf':
                content = extract_pdf(f, ocr, min_chars=args.min_chars, dpi=args.dpi)
            else:
                content = extract_image(f, ocr)
        except Exception as e:
            content = f"--- ERROR {f.name} ---\n{e}"
            print(f"  ERROR: {e}", file=sys.stderr)
        outputs[f] = content

    out = args.output
    if out:
        outp = Path(out)
        if outp.suffix.lower() == '.txt' or len(outputs) == 1 and not outp.exists() and not out.endswith('/'):
            outp.parent.mkdir(parents=True, exist_ok=True)
            with outp.open('w', encoding='utf-8') as w:
                for f, content in outputs.items():
                    w.write(f"===== {f} =====\n{content}\n\n")
            print(f"[ok] escrito {outp}", file=sys.stderr)
        else:
            outp.mkdir(parents=True, exist_ok=True)
            for f, content in outputs.items():
                dest = outp / (f.stem + '.txt')
                dest.write_text(f"===== {f} =====\n{content}\n", encoding='utf-8')
            print(f"[ok] escritos {len(outputs)} archivos en {outp}", file=sys.stderr)
    else:
        for f, content in outputs.items():
            print(f"===== {f} =====")
            print(content)
            print()

if __name__ == '__main__':
    main()
