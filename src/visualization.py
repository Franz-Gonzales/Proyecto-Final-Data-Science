"""
Módulo de generación de visualizaciones analíticas de alta calidad (300 DPI)
para su inserción en la monografía académica y reportes del Diplomado.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from src.config import (
    DATA_PROCESSED_CSV,
    OUTPUTS_FIGURES_DIR,
    COLORS
)

# Configurar estilo visual estándar para publicaciones académicas
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

def generar_grafico_general_vs_juvenil():
    """Genera gráfico de barras comparando la desocupación general urbana vs juvenil."""
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    
    categorias = ['Población urbana\n(14 años o más)', 'Jóvenes\n(16 a 28 años)']
    tasas = [2.30, 3.71]
    colores = ['#7f8c8d', COLORS['usfx_blue']]
    
    barras = ax.bar(categorias, tasas, color=colores, width=0.45, edgecolor='black', linewidth=0.5)
    
    for barra in barras:
        yval = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2.0, yval + 0.12, f'{yval:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
    ax.set_title('Bolivia urbana: Tasa de desocupación general y juvenil\nCuarto Trimestre de 2025', fontsize=12, fontweight='bold', pad=15)
    ax.set_ylabel('Tasa de desocupación (%)', fontsize=10)
    ax.set_ylim(0, 5.0)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.figtext(0.5, -0.05, 'FUENTE: Elaboración propia con base en datos oficiales del INE (ECE 4T-2025).', ha='center', fontsize=9, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_1_desocupacion_general_vs_juvenil.png"
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[OK] Gráfico generado: {out_path.name}")

def generar_grafico_grupo_etario(df: pd.DataFrame):
    """Genera gráfico de desocupación por los 4 tramos etarios."""
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=300)
    
    res = df.groupby('grupo_edad', observed=False).apply(
        lambda g: (g['es_desocupado'] * g['peso_trimestral']).sum() / g['peso_trimestral'].sum() * 100
    )
    
    grupos = list(res.index)
    tasas = list(res.values)
    
    colores = ['#95a5a6', COLORS['usfx_red'], COLORS['usfx_blue'], '#34495e']
    barras = ax.bar(grupos, tasas, color=colores, width=0.55, edgecolor='black', linewidth=0.5)
    
    for barra in barras:
        yval = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2.0, yval + 0.15, f'{yval:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
    ax.set_title('Tasa de desocupación juvenil por tramo etario (Bolivia urbana, 4T-2025)', fontsize=12, fontweight='bold', pad=15)
    ax.set_ylabel('Tasa de desocupación ponderada (%)', fontsize=10)
    ax.set_ylim(0, 6.0)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.figtext(0.5, -0.05, 'FUENTE: Elaboración propia con base en microdatos ECE 4T-2025 (INE). Ponderado por fact_trim_act.', ha='center', fontsize=9, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_2_desocupacion_por_tramo_etario.png"
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[OK] Gráfico generado: {out_path.name}")

def generar_grafico_brecha_sexo(df: pd.DataFrame):
    """Genera gráfico comparativo de la brecha de género."""
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    
    res = df.groupby('sexo', observed=False).apply(
        lambda g: (g['es_desocupado'] * g['peso_trimestral']).sum() / g['peso_trimestral'].sum() * 100
    )
    
    sexos = ['Hombre', 'Mujer']
    tasas = [res['Hombre'], res['Mujer']]
    colores = [COLORS['hombre'], COLORS['mujer']]
    
    barras = ax.bar(sexos, tasas, color=colores, width=0.45, edgecolor='black', linewidth=0.5)
    
    for barra in barras:
        yval = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2.0, yval + 0.15, f'{yval:.2f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
        
    # Anotación de la brecha
    ax.annotate(
        f'Brecha de género:\n+1.84 pp para mujeres',
        xy=(1, tasas[1]), xytext=(0.5, 5.2),
        arrowprops=dict(facecolor='black', arrowstyle='->', lw=1),
        ha='center', fontsize=10, bbox=dict(boxstyle="round,pad=0.3", fc="#fdfefe", ec="#bdc3c7", lw=1)
    )
    
    ax.set_title('Tasa de desocupación juvenil según sexo (Bolivia urbana, 4T-2025)', fontsize=12, fontweight='bold', pad=15)
    ax.set_ylabel('Tasa de desocupación ponderada (%)', fontsize=10)
    ax.set_ylim(0, 6.2)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.figtext(0.5, -0.05, 'FUENTE: Elaboración propia con base en microdatos ECE 4T-2025 (INE). Chi2 significativo (p = 0.022).', ha='center', fontsize=9, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_3_brecha_genero.png"
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[OK] Gráfico generado: {out_path.name}")

def generar_grafico_departamentos(df: pd.DataFrame):
    """Genera gráfico horizontal de desocupación por departamento."""
    fig, ax = plt.subplots(figsize=(8.5, 5.5), dpi=300)
    
    res = df.groupby('departamento', observed=False).apply(
        lambda g: (g['es_desocupado'] * g['peso_trimestral']).sum() / g['peso_trimestral'].sum() * 100
    ).sort_values(ascending=True)
    
    deptos = list(res.index)
    tasas = list(res.values)
    
    barras = ax.barh(deptos, tasas, color=COLORS['usfx_blue'], height=0.6, edgecolor='black', linewidth=0.5)
    
    # Destacar Chuquisaca
    for i, depto in enumerate(deptos):
        if depto == "Chuquisaca":
            barras[i].set_color(COLORS['usfx_red'])
            
    for barra in barras:
        xval = barra.get_width()
        ax.text(xval + 0.1, barra.get_y() + barra.get_height()/2.0, f'{xval:.2f}%', ha='left', va='center', fontsize=9, fontweight='bold')
        
    ax.axvline(3.71, color=COLORS['usfx_gold'], linestyle='--', linewidth=1.5, label='Promedio juvenil nacional (3.71%)')
    ax.legend(loc='lower right', frameon=True)
    
    ax.set_title('Tasa de desocupación juvenil por departamento (Bolivia urbana, 4T-2025)', fontsize=12, fontweight='bold', pad=15)
    ax.set_xlabel('Tasa de desocupación ponderada (%)', fontsize=10)
    ax.set_xlim(0, 7.0)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    
    plt.figtext(0.5, -0.05, 'FUENTE: Elaboración propia con base en microdatos ECE 4T-2025 (INE). Chi2 significativo (p = 0.0026).', ha='center', fontsize=9, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_4_desocupacion_por_departamento.png"
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[OK] Gráfico generado: {out_path.name}")

def generar_todas_las_figuras():
    """Ejecuta la generación de todo el paquete de figuras analíticas."""
    if not DATA_PROCESSED_CSV.exists():
        print(f"[ERROR] Dataset procesado no encontrado.")
        return
        
    df = pd.read_csv(DATA_PROCESSED_CSV, sep=';', encoding='utf-8-sig')
    print(f"[INFO] Generando catálogo de figuras de alta resolución...")
    
    generar_grafico_general_vs_juvenil()
    generar_grafico_grupo_etario(df)
    generar_grafico_brecha_sexo(df)
    generar_grafico_departamentos(df)
    print(f"[OK] Todas las figuras fueron generadas exitosamente en {OUTPUTS_FIGURES_DIR}")

if __name__ == "__main__":
    generar_todas_las_figuras()
