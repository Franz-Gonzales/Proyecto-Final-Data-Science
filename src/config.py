"""
Configuración global, constantes y mapeos de variables para el análisis ECE 4T-2025.
"""
from pathlib import Path

# Rutas del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_RAW_DIR = DATA_DIR / "raw"
DATA_RAW_CSV = DATA_RAW_DIR / "ECE_4T2025.csv" if (DATA_RAW_DIR / "ECE_4T2025.csv").exists() else DATA_DIR / "ECE_4T2025.csv"
DATA_PROCESSED_DIR = DATA_DIR / "processed"
DATA_PROCESSED_CSV = DATA_PROCESSED_DIR / "ECE_4T2025_Jovenes_PEA.csv"

OUTPUTS_DIR = BASE_DIR / "outputs"
OUTPUTS_FIGURES_DIR = OUTPUTS_DIR / "figures"
OUTPUTS_TABLES_DIR = OUTPUTS_DIR / "tables"
OUTPUTS_REPORTS_DIR = OUTPUTS_DIR / "reports"

POWERBI_DIR = BASE_DIR / "powerbi"
POWERBI_MEASURES_DIR = POWERBI_DIR / "measures"

# Asegurar existencia de directorios clave
for d in [DATA_PROCESSED_DIR, OUTPUTS_FIGURES_DIR, OUTPUTS_TABLES_DIR, OUTPUTS_REPORTS_DIR, POWERBI_MEASURES_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# Parámetros del universo de estudio
EDAD_MINIMA = 16
EDAD_MAXIMA = 28
AREA_URBANA = 1  # 1: Urbana, 2: Rural

# Tramos etarios definidos
GRUPOS_EDAD_BINS = [15, 17, 20, 24, 28]
GRUPOS_EDAD_LABELS = ["16 a 17 años", "18 a 20 años", "21 a 24 años", "25 a 28 años"]

# Mapeo de Códigos de Departamento (INE Bolivia)
DEPTO_MAP = {
    1: "Chuquisaca",
    2: "La Paz",
    3: "Cochabamba",
    4: "Oruro",
    5: "Potosí",
    6: "Tarija",
    7: "Santa Cruz",
    8: "Beni",
    9: "Pando"
}

# Mapeo de Sexo
SEXO_MAP = {
    1: "Hombre",
    2: "Mujer"
}

# Mapeo de Condición de Actividad (condact)
CONDACT_MAP = {
    1: "Ocupado",
    2: "Desocupado abierto",
    3: "Cesante",
    4: "Aspirante",
    6: "Inactivo"
}

# Mapeo de Nivel Educativo Agrupado (niv_ed_g)
NIV_ED_G_MAP = {
    1: "Sin instrucción",
    2: "Primaria",
    3: "Secundaria",
    4: "Superior No Universitario (Técnico)",
    5: "Superior Universitario",
    6: "Otros"
}

# Asistencia Educativa (s1_09)
ASISTENCIA_ED_MAP = {
    1: "Asiste",
    2: "No asiste"
}

# Paleta de Colores Institucional USFX / Analítica
COLORS = {
    "usfx_blue": "#0f2c59",
    "usfx_red": "#8b0000",
    "usfx_gold": "#c59b27",
    "accent_cyan": "#17a2b8",
    "desocupado": "#d9534f",
    "ocupado": "#2e7d32",
    "cesante": "#e67e22",
    "aspirante": "#9b59b6",
    "hombre": "#3498db",
    "mujer": "#e91e63"
}
