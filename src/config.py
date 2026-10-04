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

DOCS_DIR = BASE_DIR / "docs"
DOCS_FIGURES_DIR = DOCS_DIR / "figures"
DOCS_REPORTS_DIR = DOCS_DIR / "reports"

POWERBI_DIR = BASE_DIR / "powerbi"
POWERBI_MEASURES_DIR = POWERBI_DIR / "measures"

# Asegurar existencia de directorios clave
for d in [DATA_PROCESSED_DIR, OUTPUTS_FIGURES_DIR, OUTPUTS_TABLES_DIR, OUTPUTS_REPORTS_DIR, DOCS_FIGURES_DIR, DOCS_REPORTS_DIR, POWERBI_MEASURES_DIR]:
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

# Tipo de Hogar (tipohogar)
TIPO_HOGAR_MAP = {
    1: "Unipersonal",
    2: "Nuclear monoparental",
    3: "Nuclear biparental sin hijos",
    4: "Nuclear biparental con hijos",
    5: "Extendido",
    6: "Compuesto",
    7: "Otros / Sin núcleo"
}

# Relación de Parentesco (s1_05)
PARENTESCO_MAP = {
    1: "Jefe(a) de hogar",
    2: "Cónyuge / Conviviente",
    3: "Hijo(a) / Hijastro(a)",
    4: "Yerno / Nuera",
    5: "Nieto(a)",
    6: "Hermano(a) / Cuñado(a)",
    7: "Padre / Madre / Suegro(a)",
    8: "Otros parientes",
    9: "Otros no parientes"
}

# Mecanismo Principal de Búsqueda (s2_08a)
MECANISMO_BUSQUEDA_MAP = {
    1: "Presentó solicitudes / currículum",
    2: "Preguntó en lugares de trabajo",
    3: "Consultó a amigos o parientes",
    4: "Avisos por prensa, internet o redes",
    5: "Gestiones para negocio propio",
    8: "Otra forma de búsqueda"
}

# Grandes Grupos Ocupacionales COB (Primer dígito cob_uo)
COB_GRUPOS_MAP = {
    "1": "Directores y gerentes",
    "2": "Profesionales científicos e intelectuales",
    "3": "Técnicos y profesionales medios",
    "4": "Personal de apoyo administrativo",
    "5": "Servicios y vendedores de comercio",
    "6": "Trabajadores agropecuarios calificados",
    "7": "Oficiales, operarios y artesanos",
    "8": "Operadores de instalaciones y máquinas",
    "9": "Ocupaciones elementales"
}

# Grandes Ramas de Actividad CAEB (caeb_uo simplificado)
CAEB_RAMAS_MAP = {
    "1": "Agricultura, ganadería y pesca",
    "2": "Minería e hidrocarburos",
    "3": "Industria manufacturera",
    "4": "Servicios básicos (electricidad/agua)",
    "5": "Construcción",
    "6": "Comercio al por mayor y menor",
    "7": "Transporte y almacenamiento",
    "8": "Alojamiento y servicios de comida",
    "9": "Información y comunicaciones",
    "10": "Actividades financieras y seguros",
    "11": "Actividades inmobiliarias y profesionales",
    "12": "Administración pública y defensa",
    "13": "Educación",
    "14": "Salud y asistencia social",
    "15": "Otros servicios comunitarios y personales",
    "16": "Servicio doméstico en hogares"
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
