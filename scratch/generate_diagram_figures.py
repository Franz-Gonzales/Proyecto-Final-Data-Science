"""
Generador de diagramas analíticos en formato PNG (300 DPI) para la monografía.
Genera representaciones visuales del flujo de datos y del esquema en estrella (Star Schema)
sin depender de extensiones Mermaid en visores Markdown ni en Microsoft Word.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Rutas
BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUTS_FIG_DIR = BASE_DIR / "outputs" / "figures"
DOCS_FIG_DIR = BASE_DIR / "docs" / "figures"

OUTPUTS_FIG_DIR.mkdir(parents=True, exist_ok=True)
DOCS_FIG_DIR.mkdir(parents=True, exist_ok=True)

# Paleta USFX
C_AZUL = "#0f2c59"
C_AZUL_MEDIO = "#1b4965"
C_DORADO = "#c59b27"
C_GRIS_FONDO = "#f8f9fa"
C_GRIS_BORDE = "#bdc3c7"
C_ROJO = "#8b0000"
C_VERDE = "#2e7d32"

def crear_diagrama_flujo_datos():
    """Genera diagrama visual del pipeline de depuración y filtrado de microdatos."""
    fig, ax = plt.subplots(figsize=(10, 8.5), dpi=300)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12.5)
    ax.axis('off')
    
    pasos = [
        {
            "num": "1",
            "titulo": "Microdatos Crudos ECE 4T-2025 (INE)",
            "detalle": "Base nacional completa: 52.650 registros y 121 variables\nSeparador de listas ';' y codificación latin1",
            "caja": (1.0, 10.5, 8.0, 1.3),
            "color_fondo": "#eef2f7",
            "color_borde": C_AZUL,
            "badge": "Entrada"
        },
        {
            "num": "2",
            "titulo": "Filtro Geográfico: Área Urbana (area == 1)",
            "detalle": "44.048 registros retenidos (exclusión de 8.602 registros rurales)\nFoco en dinámicas del mercado de trabajo urbano",
            "caja": (1.0, 8.6, 8.0, 1.3),
            "color_fondo": "#ffffff",
            "color_borde": C_AZUL_MEDIO,
            "badge": "Filtro 1"
        },
        {
            "num": "3",
            "titulo": "Filtro Etario: Ley N.º 342 de la Juventud (16 a 28 años)",
            "detalle": "9.612 jóvenes urbanos en total (exclusión de 34.436 registros fuera de rango)\nSegmentación: 16-17, 18-20, 21-24 y 25-28 años",
            "caja": (1.0, 6.7, 8.0, 1.3),
            "color_fondo": "#ffffff",
            "color_borde": C_AZUL_MEDIO,
            "badge": "Filtro 2"
        },
        {
            "num": "4",
            "titulo": "Filtro Económico: Población Económicamente Activa (pea == 1)",
            "detalle": "6.649 jóvenes en la PEA urbana (exclusión de 2.963 inactivos)\nMuestra efectiva final del estudio (n = 6.649)",
            "caja": (1.0, 4.8, 8.0, 1.3),
            "color_fondo": "#fef9e7",
            "color_borde": C_DORADO,
            "badge": "Filtro 3"
        },
        {
            "num": "5",
            "titulo": "Calibración con Factor de Expansión (fact_trim_act -> peso_trimestral)",
            "detalle": "Conversión string con coma decimal a float64 (pesos mayores a cero)\nPoblación expandida estimada: N = 1.380.841 jóvenes en la PEA",
            "caja": (1.0, 2.9, 8.0, 1.3),
            "color_fondo": "#eafaf1",
            "color_borde": C_VERDE,
            "badge": "Ponderación"
        },
        {
            "num": "6",
            "titulo": "Salidas Analíticas y Modelado Dimensional",
            "detalle": "Python: Tasas ponderadas (Desocupación 3,71%, Subocupación 8,70%), Chi2, Cramér\nPower BI: Esquema Star Schema (6 dimensiones) y Dashboard de 6 páginas",
            "caja": (1.0, 1.0, 8.0, 1.3),
            "color_fondo": "#eef2f7",
            "color_borde": C_AZUL,
            "badge": "Resultados"
        }
    ]
    
    for i, p in enumerate(pasos):
        x, y, w, h = p["caja"]
        rect = patches.FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.15,rounding_size=0.15",
            facecolor=p["color_fondo"],
            edgecolor=p["color_borde"],
            linewidth=1.8
        )
        ax.add_patch(rect)
        
        # Badge identificador
        badge_rect = patches.FancyBboxPatch(
            (x + 0.2, y + h - 0.38), 1.3, 0.28,
            boxstyle="round,pad=0.05,rounding_size=0.08",
            facecolor=p["color_borde"],
            edgecolor=p["color_borde"]
        )
        ax.add_patch(badge_rect)
        ax.text(x + 0.85, y + h - 0.24, p["badge"], color="white", fontsize=8.5, fontweight="bold", ha="center", va="center")
        
        # Texto del título
        ax.text(x + 1.65, y + h - 0.24, p["titulo"], color=C_AZUL, fontsize=10.5, fontweight="bold", va="center")
        
        # Texto del detalle
        ax.text(x + 0.4, y + 0.45, p["detalle"], color="#2c3e50", fontsize=9, va="center", linespacing=1.35)
        
        # Flecha conectora hacia el siguiente paso
        if i < len(pasos) - 1:
            ax.annotate(
                '', xy=(5.0, y - 0.05), xytext=(5.0, y + 0.05 - 0.55),
                arrowprops=dict(arrowstyle="-|>", color=C_DORADO, lw=2.2, mutation_scale=16)
            )
            
    ax.set_title("Flujo metodológico de preparación y calibración de microdatos (ECE 4T-2025)", fontsize=12, fontweight="bold", color=C_AZUL, pad=12)
    plt.tight_layout()
    
    for dest in [OUTPUTS_FIG_DIR, DOCS_FIG_DIR]:
        out_file = dest / "figura_diagrama_flujo_datos.png"
        plt.savefig(out_file, bbox_inches='tight', dpi=300)
    plt.close()
    print("[OK] Generado: figura_diagrama_flujo_datos.png en outputs y docs")

def crear_diagrama_star_schema():
    """Genera diagrama visual de la arquitectura Star Schema para Power BI."""
    fig, ax = plt.subplots(figsize=(11, 7.8), dpi=300)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8.5)
    ax.axis('off')
    
    # 1. Tabla Central de Hechos: FACT_MERCADO_LABORAL
    fx, fy, fw, fh = 3.6, 2.7, 3.8, 2.9
    fact_rect = patches.FancyBboxPatch(
        (fx, fy), fw, fh,
        boxstyle="round,pad=0.15,rounding_size=0.15",
        facecolor="#fefefe",
        edgecolor=C_ROJO,
        linewidth=2.2
    )
    ax.add_patch(fact_rect)
    
    # Cabecera de la Fact Table
    fact_hdr = patches.FancyBboxPatch(
        (fx, fy + fh - 0.55), fw, 0.55,
        boxstyle="round,pad=0.15,rounding_size=0.15",
        facecolor=C_ROJO,
        edgecolor=C_ROJO,
        linewidth=1
    )
    ax.add_patch(fact_hdr)
    ax.text(fx + fw/2.0, fy + fh - 0.28, "FACT_MERCADO_LABORAL", color="white", fontsize=10.5, fontweight="bold", ha="center", va="center")
    
    fact_fields = [
        "• id_persona (PK) [int]",
        "• peso_trimestral [float64]",
        "• es_ocupado [0, 1]",
        "• es_desocupado [0, 1]",
        "• es_cesante [0, 1]",
        "• es_aspirante [0, 1]",
        "• es_subocupado [0, 1]",
        "• anios_estudio [0 - 25]"
    ]
    ax.text(fx + 0.3, fy + 1.15, "\n".join(fact_fields), color="#2c3e50", fontsize=8.5, va="center", linespacing=1.25)
    
    # 2. Tablas Dimensionales periféricas
    dims = [
        {
            "nombre": "DIM_TIEMPO",
            "pos": (0.4, 5.7, 2.8, 1.8),
            "campos": "• gestion_trimestre (PK)\n• gestion [2025]\n• trimestre [4T]",
            "target": (fx, fy + 2.3)
        },
        {
            "nombre": "DIM_GEOGRAFIA",
            "pos": (7.8, 5.7, 2.8, 1.8),
            "campos": "• depto_cod (PK)\n• departamento [1-9]\n• area_urbana [1]",
            "target": (fx + fw, fy + 2.3)
        },
        {
            "nombre": "DIM_DEMOGRAFIA",
            "pos": (0.4, 3.2, 2.8, 1.8),
            "campos": "• sexo_cod (PK)\n• sexo [Hombre, Mujer]\n• grupo_edad [4 tramos]\n• edad [16 a 28]",
            "target": (fx, fy + 1.5)
        },
        {
            "nombre": "DIM_EDUCACION",
            "pos": (7.8, 3.2, 2.8, 1.8),
            "campos": "• niv_ed_cod (PK)\n• nivel_educativo\n• asiste_estudio",
            "target": (fx + fw, fy + 1.5)
        },
        {
            "nombre": "DIM_CONDICION_LABORAL",
            "pos": (0.4, 0.7, 2.8, 1.8),
            "campos": "• condact_cod (PK)\n• tipo_condicion_laboral\n• es_subocupado_def",
            "target": (fx, fy + 0.7)
        },
        {
            "nombre": "DIM_HOGAR",
            "pos": (7.8, 0.7, 2.8, 1.8),
            "campos": "• tipohogar_cod (PK)\n• tipo_hogar [7 tipos]\n• parentesco [9 tipos]",
            "target": (fx + fw, fy + 0.7)
        }
    ]
    
    for d in dims:
        dx, dy, dw, dh = d["pos"]
        dim_rect = patches.FancyBboxPatch(
            (dx, dy), dw, dh,
            boxstyle="round,pad=0.15,rounding_size=0.12",
            facecolor="#fdfefe",
            edgecolor=C_AZUL,
            linewidth=1.6
        )
        ax.add_patch(dim_rect)
        
        # Cabecera Dim
        dim_hdr = patches.FancyBboxPatch(
            (dx, dy + dh - 0.45), dw, 0.45,
            boxstyle="round,pad=0.15,rounding_size=0.12",
            facecolor=C_AZUL,
            edgecolor=C_AZUL,
            linewidth=1
        )
        ax.add_patch(dim_hdr)
        ax.text(dx + dw/2.0, dy + dh - 0.23, d["nombre"], color="white", fontsize=9, fontweight="bold", ha="center", va="center")
        
        # Campos
        ax.text(dx + 0.2, dy + 0.6, d["campos"], color="#34495e", fontsize=8, va="center", linespacing=1.2)
        
        # Conexión 1:N hacia la Fact Table
        start_x = dx + dw if dx < fx else dx
        start_y = dy + dh/2.0
        ax.annotate(
            '', xy=d["target"], xytext=(start_x, start_y),
            arrowprops=dict(arrowstyle="-|>", color=C_DORADO, lw=2.0, mutation_scale=15)
        )
        
        # Etiqueta de cardinalidad
        mid_x = (start_x + d["target"][0]) / 2.0
        mid_y = (start_y + d["target"][1]) / 2.0
        ax.text(mid_x, mid_y + 0.12, "1 : N", color=C_AZUL, fontsize=8, fontweight="bold", ha="center",
                bbox=dict(boxstyle="round,pad=0.15", fc="#ffffff", ec=C_DORADO, lw=0.8))
                
    ax.set_title("Arquitectura del modelo dimensional en estrella (Star Schema) para Power BI Desktop", fontsize=12, fontweight="bold", color=C_AZUL, pad=12)
    plt.tight_layout()
    
    for dest in [OUTPUTS_FIG_DIR, DOCS_FIG_DIR]:
        out_file = dest / "figura_diagrama_star_schema.png"
        plt.savefig(out_file, bbox_inches='tight', dpi=300)
    plt.close()
    print("[OK] Generado: figura_diagrama_star_schema.png en outputs y docs")

if __name__ == "__main__":
    crear_diagrama_flujo_datos()
    crear_diagrama_star_schema()
