#!/usr/bin/env python3
"""
Servidor HTTP local para el deck, igual que `python3 -m http.server` pero
forzando charset=utf-8 en los Content-Type de texto. Sin esto, Python le
manda `text/markdown` (sin charset) a los .md, y el navegador adivina mal
la codificación -> tildes/ñ/¿¡ rotos ("Ã©" en vez de "é").

Uso:
    python3 serve.py            # puerto 8000 por defecto
    python3 serve.py 8080       # puerto custom
"""
import http.server
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000


class UTF8Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".md": "text/markdown; charset=utf-8",
        ".html": "text/html; charset=utf-8",
        ".css": "text/css; charset=utf-8",
        ".js": "application/javascript; charset=utf-8",
        "": "application/octet-stream",
    }

    def end_headers(self):
        # Nunca cachear: evita que el navegador "se demore en reaccionar"
        # a cambios en clase0.md/css/figuras mientras editas en vivo.
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        super().end_headers()


with socketserver.TCPServer(("", PORT), UTF8Handler) as httpd:
    print(f"Sirviendo en http://localhost:{PORT}  (Ctrl+C para parar)")
    print(f"Abre: http://localhost:{PORT}/?p=clase0.md")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
