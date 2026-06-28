from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

OUTPUTS = {
    'docs/02_trazabilidad/matriz_ejecucion.md': '# Matriz de ejecucion y trazabilidad\n\nPendiente de generacion automatica.\n',
    'docs/03_riesgos/README.md': '# Matriz de riesgos\n\nPendiente de generacion automatica.\n',
    'docs/08_tablero/tablero_vsest_lite.md': '# Tablero VSEST-Lite\n\nPendiente de generacion automatica.\n',
}

for path, content in OUTPUTS.items():
    full = BASE / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding='utf-8')

print('Reportes generados')
