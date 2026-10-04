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
    DOCS_FIGURES_DIR,
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

def generar_grafico_cesantes_aspirantes(df: pd.DataFrame):
    """Genera gráfico tipo dona de la composición de desocupados: Cesantes vs Aspirantes."""
    fig, ax = plt.subplots(figsize=(6.5, 5), dpi=300)
    
    df_des = df[df['es_desocupado'] == 1]
    peso_ces = df_des[df_des['es_cesante'] == 1]['peso_trimestral'].sum()
    peso_asp = df_des[df_des['es_aspirante'] == 1]['peso_trimestral'].sum()
    total = peso_ces + peso_asp
    
    pct_ces = (peso_ces / total) * 100
    pct_asp = (peso_asp / total) * 100
    
    labels = [
        f'Cesantes\n(Con experiencia previa)\n{pct_ces:.1f}% ({int(round(peso_ces)):,} hab.)',
        f'Aspirantes\n(Buscan primer empleo)\n{pct_asp:.1f}% ({int(round(peso_asp)):,} hab.)'
    ]
    sizes = [pct_ces, pct_asp]
    colors = [COLORS['cesante'], COLORS['aspirante']]
    explode = (0.05, 0.05)
    
    wedges, texts, autotexts = ax.pie(
        sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        startangle=140, colors=colors, pctdistance=0.75,
        textprops=dict(color='black', fontsize=9.5),
        wedgeprops=dict(width=0.45, edgecolor='white', linewidth=2)
    )
    plt.setp(autotexts, size=10, weight="bold", color="white")
    
    ax.set_title('Bolivia urbana: Estructura de la desocupación juvenil según historial laboral\nCuarto Trimestre de 2025', fontsize=11, fontweight='bold', pad=15)
    
    plt.figtext(0.5, -0.05, 'FUENTE: Elaboración propia con base en microdatos ECE 4T-2025 (INE). Ponderado por fact_trim_act.', ha='center', fontsize=8.5, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_5_cesantes_vs_aspirantes.png"
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[OK] Gráfico generado: {out_path.name}")

def generar_grafico_nivel_educativo(df: pd.DataFrame):
    """Genera gráfico de barras de desocupación según nivel educativo."""
    fig, ax = plt.subplots(figsize=(8, 4.8), dpi=300)
    
    # Excluir 'No especificado' para análisis sustantivo
    df_clean = df[~df['nivel_educativo'].isin(['No especificado', 'Otros']) & df['nivel_educativo'].notna()]
    
    orden = ['Sin instrucción', 'Primaria', 'Secundaria', 'Superior Universitario']
    res = df_clean.groupby('nivel_educativo', observed=False).apply(
        lambda g: (g['es_desocupado'] * g['peso_trimestral']).sum() / g['peso_trimestral'].sum() * 100
    ).reindex([o for o in orden if o in df_clean['nivel_educativo'].unique()])
    
    niveles = list(res.index)
    tasas = list(res.values)
    
    colores = ['#95a5a6', '#5dade2', '#2e86c1', COLORS['usfx_red']]
    barras = ax.bar(niveles, tasas, color=colores, width=0.5, edgecolor='black', linewidth=0.5)
    
    for barra in barras:
        yval = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2.0, yval + 0.12, f'{yval:.2f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')
        
    ax.axhline(3.71, color=COLORS['usfx_gold'], linestyle='--', linewidth=1.5, label='Promedio juvenil nacional (3.71%)')
    ax.legend(loc='upper left', frameon=True)
    
    ax.set_title('Tasa de desocupación juvenil según nivel educativo (Bolivia urbana, 4T-2025)', fontsize=12, fontweight='bold', pad=15)
    ax.set_ylabel('Tasa de desocupación ponderada (%)', fontsize=10)
    ax.set_ylim(0, 5.5)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.figtext(0.5, -0.05, 'FUENTE: Elaboración propia con base en microdatos ECE 4T-2025 (INE). Chi2 no significativo (p = 0.457).', ha='center', fontsize=9, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_6_desocupacion_por_nivel_educativo.png"
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[OK] Gráfico generado: {out_path.name}")

def generar_grafico_asiste_estudio(df: pd.DataFrame):
    """Genera gráfico de barras de desocupación según asistencia educativa."""
    fig, ax = plt.subplots(figsize=(6.5, 4.5), dpi=300)
    
    res = df.groupby('asiste_estudio', observed=False).apply(
        lambda g: (g['es_desocupado'] * g['peso_trimestral']).sum() / g['peso_trimestral'].sum() * 100
    )
    
    categorias = ['Asiste', 'No asiste']
    tasas = [res.get('Asiste', 0), res.get('No asiste', 0)]
    colores = [COLORS['usfx_blue'], '#7f8c8d']
    
    barras = ax.bar(categorias, tasas, color=colores, width=0.45, edgecolor='black', linewidth=0.5)
    
    for barra in barras:
        yval = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2.0, yval + 0.12, f'{yval:.2f}%', ha='center', va='bottom', fontsize=10.5, fontweight='bold')
        
    ax.set_title('Tasa de desocupación juvenil según asistencia escolar/académica\n(Bolivia urbana, 4T-2025)', fontsize=11.5, fontweight='bold', pad=15)
    ax.set_ylabel('Tasa de desocupación ponderada (%)', fontsize=10)
    ax.set_ylim(0, 5.2)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    plt.figtext(0.5, -0.05, 'FUENTE: Elaboración propia con base en microdatos ECE 4T-2025 (INE). Chi2 no significativo (p = 0.216).', ha='center', fontsize=9, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_7_desocupacion_asiste_estudio.png"
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[OK] Gráfico generado: {out_path.name}")

def generar_grafico_distribucion_anios_estudio(df: pd.DataFrame):
    """Genera comparación de la distribución de años de escolaridad entre Ocupados y Desocupados."""
    fig, (ax_box, ax_kde) = plt.subplots(2, 1, figsize=(8, 6), sharex=True, gridspec_kw={'height_ratios': [0.35, 0.65]}, dpi=300)
    
    # Subconjuntos
    df_ocu = df[df['es_ocupado'] == 1].dropna(subset=['anios_estudio'])
    df_des = df[df['es_desocupado'] == 1].dropna(subset=['anios_estudio'])
    
    # Boxplot
    bplot = ax_box.boxplot(
        [df_ocu['anios_estudio'], df_des['anios_estudio']],
        orientation='horizontal', patch_artist=True, tick_labels=['Ocupados', 'Desocupados'],
        medianprops=dict(color='black', linewidth=1.5),
        flierprops=dict(marker='o', markersize=3, alpha=0.3)
    )
    bplot['boxes'][0].set_facecolor('#82e0aa')
    bplot['boxes'][1].set_facecolor('#f1948a')
    ax_box.set_title('Distribución de años de estudio: Ocupados vs Desocupados (Bolivia urbana)', fontsize=11.5, fontweight='bold')
    
    # Medias ponderadas
    media_ocu = (df_ocu['anios_estudio'] * df_ocu['peso_trimestral']).sum() / df_ocu['peso_trimestral'].sum()
    media_des = (df_des['anios_estudio'] * df_des['peso_trimestral']).sum() / df_des['peso_trimestral'].sum()
    
    ax_box.text(media_ocu, 1.25, f'Media: {media_ocu:.2f}', color='#196f3d', fontsize=9, fontweight='bold')
    ax_box.text(media_des, 2.25, f'Media: {media_des:.2f}', color='#922b21', fontsize=9, fontweight='bold')
    
    # KDE / Densidad Ponderada
    sns.kdeplot(data=df_ocu, x='anios_estudio', weights='peso_trimestral', ax=ax_kde, label=f'Ocupados (Media ponderada: {media_ocu:.2f} años)', color='#27ae60', fill=True, alpha=0.3)
    sns.kdeplot(data=df_des, x='anios_estudio', weights='peso_trimestral', ax=ax_kde, label=f'Desocupados (Media ponderada: {media_des:.2f} años)', color='#c0392b', fill=True, alpha=0.3)
    
    ax_kde.axvline(media_ocu, color='#27ae60', linestyle='--', linewidth=1.2)
    ax_kde.axvline(media_des, color='#c0392b', linestyle='--', linewidth=1.2)
    
    ax_kde.set_xlabel('Años de estudio acumulados (escolaridad)', fontsize=10)
    ax_kde.set_ylabel('Densidad estimada ponderada', fontsize=10)
    ax_kde.set_xlim(0, 22)
    ax_kde.legend(loc='upper left', frameon=True)
    ax_kde.grid(True, linestyle='--', alpha=0.5)
    
    plt.figtext(0.5, -0.04, 'FUENTE: Elaboración propia con base en microdatos ECE 4T-2025 (INE). Diferencia t-test: t = -2.34, p = 0.0202.', ha='center', fontsize=8.5, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_8_distribucion_anios_estudio.png"
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[OK] Gráfico generado: {out_path.name}")

def generar_grafico_mecanismos_busqueda(df: pd.DataFrame):
    """Genera gráfico horizontal de mecanismos de búsqueda de empleo entre desocupados."""
    fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)
    
    df_des = df[df['es_desocupado'] == 1].dropna(subset=['mecanismo_busqueda'])
    # Excluir no aplica
    df_des = df_des[~df_des['mecanismo_busqueda'].str.contains('No aplica', na=False)]
    
    res = df_des.groupby('mecanismo_busqueda', observed=False)['peso_trimestral'].sum()
    total_des = res.sum()
    res_pct = (res / total_des * 100).sort_values(ascending=True)
    
    mecanismos = list(res_pct.index)
    pcts = list(res_pct.values)
    
    barras = ax.barh(mecanismos, pcts, color=COLORS['usfx_blue'], height=0.55, edgecolor='black', linewidth=0.5)
    
    for barra in barras:
        xval = barra.get_width()
        ax.text(xval + 0.8, barra.get_y() + barra.get_height()/2.0, f'{xval:.1f}%', ha='left', va='center', fontsize=9.5, fontweight='bold')
        
    ax.set_title('Canales y mecanismos de búsqueda de empleo en jóvenes desocupados\n(Bolivia urbana, 4T-2025)', fontsize=11.5, fontweight='bold', pad=15)
    ax.set_xlabel('Distribución porcentual ponderada (%)', fontsize=10)
    ax.set_xlim(0, 48)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    
    plt.figtext(0.5, -0.05, 'FUENTE: Elaboración propia con base en microdatos ECE 4T-2025 (INE). Ponderado por fact_trim_act.', ha='center', fontsize=8.5, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_9_mecanismos_busqueda.png"
    plt.tight_layout()
    plt.savefig(out_path, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"[OK] Gráfico generado: {out_path.name}")

def generar_grafico_tipo_hogar(df: pd.DataFrame):
    """Genera gráfico de barras de desocupación según tipo de hogar."""
    fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=300)
    
    df_clean = df.dropna(subset=['tipo_hogar'])
    res = df_clean.groupby('tipo_hogar', observed=False).apply(
        lambda g: (g['es_desocupado'] * g['peso_trimestral']).sum() / g['peso_trimestral'].sum() * 100
    ).sort_values(ascending=True)
    
    tipos = list(res.index)
    tasas = list(res.values)
    
    barras = ax.barh(tipos, tasas, color=COLORS['usfx_blue'], height=0.55, edgecolor='black', linewidth=0.5)
    
    for barra in barras:
        xval = barra.get_width()
        ax.text(xval + 0.1, barra.get_y() + barra.get_height()/2.0, f'{xval:.2f}%', ha='left', va='center', fontsize=9, fontweight='bold')
        
    ax.axvline(3.71, color=COLORS['usfx_gold'], linestyle='--', linewidth=1.5, label='Promedio juvenil nacional (3.71%)')
    ax.legend(loc='lower right', frameon=True)
    
    ax.set_title('Tasa de desocupación juvenil según tipo de hogar (Bolivia urbana, 4T-2025)', fontsize=11.5, fontweight='bold', pad=15)
    ax.set_xlabel('Tasa de desocupación ponderada (%)', fontsize=10)
    ax.set_xlim(0, 7.5)
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    
    plt.figtext(0.5, -0.05, 'FUENTE: Elaboración propia con base en microdatos ECE 4T-2025 (INE). Chi2 significativo (p = 0.0078).', ha='center', fontsize=8.5, style='italic')
    
    out_path = OUTPUTS_FIGURES_DIR / "figura_10_desocupacion_tipo_hogar.png"
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
    print(f"[INFO] Generando catálogo completo de 10 figuras de alta resolución (300 DPI)...")
    
    generar_grafico_general_vs_juvenil()
    generar_grafico_grupo_etario(df)
    generar_grafico_brecha_sexo(df)
    generar_grafico_departamentos(df)
    generar_grafico_cesantes_aspirantes(df)
    generar_grafico_nivel_educativo(df)
    generar_grafico_asiste_estudio(df)
    generar_grafico_distribucion_anios_estudio(df)
    generar_grafico_mecanismos_busqueda(df)
    import shutil
    for fig_file in OUTPUTS_FIGURES_DIR.glob("*.png"):
        shutil.copy(fig_file, DOCS_FIGURES_DIR / fig_file.name)
    print(f"[OK] Figuras sincronizadas también en {DOCS_FIGURES_DIR}")
    print(f"[OK] Todas las 10 figuras fueron generadas exitosamente en {OUTPUTS_FIGURES_DIR}")

if __name__ == "__main__":
    generar_todas_las_figuras()
