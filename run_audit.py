"""
Lanzador Principal de la Auditoría Externa de Ciencia de Datos
Proyecto: Análisis de Desocupación Juvenil en Bolivia (ECE 4T-2025)
Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca — CEPI
"""

import sys
from pathlib import Path

# Habilitar salida UTF-8 segura en consolas de Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# Añadir la raíz del proyecto al sys.path para importaciones absolutas
PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.audit import run_full_audit

if __name__ == "__main__":
    try:
        report = run_full_audit(PROJECT_ROOT)
        # Salida 0 si la calificación es aprobatoria (>= 7.0)
        sys.exit(0 if report["summary"]["global_score"] >= 7.0 else 1)
    except Exception as e:
        print(f"\n[ERROR CRÍTICO EN AUDITORÍA]: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(2)
