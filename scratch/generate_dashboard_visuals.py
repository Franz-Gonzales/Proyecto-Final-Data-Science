"""
Script para generar las capturas visuales en alta resolución (300 DPI)
de las 6 páginas del Dashboard analítico interactivo de Power BI.
Alineado estrictamente con la paleta de colores institucional USFX y
los datos oficiales de la ECE 4T-2025.
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Configurar estilos globales
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Segoe UI', 'DejaVu Sans', 'Arial']
plt.rcParams['text.color'] = '#212529'
plt.rcParams['axes.labelcolor'] = '#495057'
plt.rcParams['xtick.color'] = '#495057'
plt.rcParams['ytick.color'] = '#495057'

# Paleta USFX
C_PRIMARY = '#0F2C59'    # Azul Marino Institucional
C_ACCENT = '#8B0000'     # Rojo Colonial / Granate
C_GOLD = '#C59B27'       # Dorado Institucional
C_GREEN = '#2E7D32'      # Verde Ocupación
C_PURPLE = '#8E44AD'     # Púrpura Aspirantes
C_ORANGE = '#E67E22'     # Naranja Cesantes
C_BG = '#F8F9FA'         # Fondo gris suave
C_CARD = '#FFFFFF'       # Blanco tarjeta
C_BORDER = '#E2E8F0'     # Borde sutil
C_TEXT_MUTED = '#6C757D'

OUTPUT_DIRS = [
    'docs/figures',
    'outputs/figures'
]

for d in OUTPUT_DIRS:
    os.makedirs(d, exist_ok=True)

def draw_header(fig, title, subtitle, page_num):
    """Dibuja la barra de encabezado institucional estilo Power BI."""
    # Banner superior
    header_ax = fig.add_axes([0, 0.91, 1, 0.09])
    header_ax.set_facecolor(C_PRIMARY)
    header_ax.axis('off')
    
    # Textos institucionales
    header_ax.text(0.02, 0.62, "UNIVERSIDAD MAYOR, REAL Y PONTIFICIA DE SAN FRANCISCO XAVIER DE CHUQUISACA", 
                   color=C_GOLD, fontsize=9, fontweight='bold', va='center')
    header_ax.text(0.02, 0.28, f"PÁGINA {page_num}: {title.upper()}", 
                   color='#FFFFFF', fontsize=15, fontweight='bold', va='center')
    
    header_ax.text(0.98, 0.62, "CEPI | DIPLOMADO EN DATA SCIENCE", 
                   color='#FFFFFF', fontsize=9, fontweight='bold', ha='right', va='center')
    header_ax.text(0.98, 0.28, f"{subtitle} | ECE 4T-2025 (INE)", 
                   color='#CBD5E1', fontsize=8.5, ha='right', va='center')
    
    # Barra de acento dorado
    accent_ax = fig.add_axes([0, 0.905, 1, 0.005])
    accent_ax.set_facecolor(C_GOLD)
    accent_ax.axis('off')

def draw_footer(fig):
    """Dibuja la barra de pie con metadatos técnicos."""
    footer_ax = fig.add_axes([0, 0, 1, 0.035])
    footer_ax.set_facecolor('#E9ECEF')
    footer_ax.axis('off')
    footer_ax.text(0.02, 0.5, "Filtros Activos: Área = Urbana | Edad = 16 a 28 años | Condición = PEA | Ponderación = fact_trim_act", 
                   color=C_TEXT_MUTED, fontsize=8, va='center')
    footer_ax.text(0.98, 0.5, "Power BI Desktop | Modelo Semántico Dimensional (Star Schema) | Medidas DAX Oficiales", 
                   color=C_TEXT_MUTED, fontsize=8, ha='right', va='center')

def create_card(ax, title, value, subtext="", color_accent=C_PRIMARY, badge=""):
    """Dibuja una tarjeta KPI estilo Power BI."""
    ax.set_facecolor(C_CARD)
    for spine in ax.spines.values():
        spine.set_color(C_BORDER)
        spine.set_linewidth(1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Barra superior de acento de la tarjeta
    rect = patches.Rectangle((0, 0.92), 1, 0.08, transform=ax.transAxes, 
                             facecolor=color_accent, edgecolor='none', zorder=2)
    ax.add_patch(rect)
    
    # Título de métrica
    ax.text(0.08, 0.76, title.upper(), fontsize=7.5, fontweight='bold', 
            color=C_TEXT_MUTED, transform=ax.transAxes)
    
    # Valor principal
    ax.text(0.08, 0.40, value, fontsize=17, fontweight='bold', 
            color=color_accent, transform=ax.transAxes)
    
    # Subtexto / contexto
    if subtext:
        ax.text(0.08, 0.18, subtext, fontsize=7.5, color=C_TEXT_MUTED, transform=ax.transAxes)
    
    # Badge lateral
    if badge:
        ax.text(0.92, 0.76, badge, fontsize=7, fontweight='bold', 
                color='#FFFFFF', bbox=dict(boxstyle='round,pad=0.2', facecolor=color_accent, edgecolor='none'),
                ha='right', transform=ax.transAxes)

# ==============================================================================
# PÁGINA 1: PANORAMA LABORAL JUVENIL
# ==============================================================================
def render_page_1():
    fig = plt.figure(figsize=(16, 9), dpi=300, facecolor=C_BG)
    draw_header(fig, "Panorama Laboral Juvenil en Bolivia Urbana", "Indicadores Macroeconómicos y Composición de la PEA", 1)
    draw_footer(fig)
    
    # 5 KPI Cards Superiores
    # [left, bottom, width, height]
    card_w = 0.18
    gap = 0.015
    y_card = 0.76
    h_card = 0.12
    
    ax_kpi1 = fig.add_axes([0.02 + 0*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi1, "PEA Juvenil Ponderada", "1.380.841", "Muestra: 6.649 jóvenes", C_PRIMARY, "OFICIAL")
    
    ax_kpi2 = fig.add_axes([0.02 + 1*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi2, "Población Ocupada", "1.329.645", "96,29% de la PEA", C_GREEN, "OCUPADOS")
    
    ax_kpi3 = fig.add_axes([0.02 + 2*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi3, "Población Desocupada", "51.196", "Muestra: 243 desocupados", C_ACCENT, "DESOCUPADOS")
    
    ax_kpi4 = fig.add_axes([0.02 + 3*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi4, "Tasa Desocupación", "3,71%", "Población ponderada 4T-2025", C_ACCENT, "TD JUVENIL")
    
    ax_kpi5 = fig.add_axes([0.02 + 4*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi5, "Tasa Subocupación", "8,70%", "115.736 personas subempleadas", C_GOLD, "SUBOCUPACIÓN")
    
    # Visual 1: Donut Chart - Composición de la PEA
    ax_v1 = fig.add_axes([0.02, 0.06, 0.31, 0.66])
    ax_v1.set_facecolor(C_CARD)
    for s in ax_v1.spines.values():
        s.set_color(C_BORDER)
    ax_v1.set_title("Estructura de la PEA Juvenil Urbana", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    sizes = [1329645, 51196]
    colors = [C_PRIMARY, C_ACCENT]
    explode = (0, 0.08)
    wedges, texts, autotexts = ax_v1.pie(sizes, explode=explode, labels=['Ocupados\n(1.33M)', 'Desocupados\n(51.2K)'],
                                         colors=colors, autopct='%1.2f%%', startangle=45, pctdistance=0.75,
                                         textprops=dict(color='#212529', fontsize=9))
    plt.setp(autotexts, size=9.5, weight="bold", color="white")
    centre_circle = plt.Circle((0,0), 0.55, fc=C_CARD)
    ax_v1.add_artist(centre_circle)
    ax_v1.text(0, 0, "PEA TOTAL\n1.38M", ha='center', va='center', fontsize=10, fontweight='bold', color=C_PRIMARY)
    
    # Visual 2: Barras Agrupadas - Comparación Tasa General vs Juvenil
    ax_v2 = fig.add_axes([0.35, 0.06, 0.31, 0.66])
    ax_v2.set_facecolor(C_CARD)
    for s in ax_v2.spines.values():
        s.set_color(C_BORDER)
    ax_v2.set_title("Brecha de Desocupación: General vs Juvenil", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    categories = ['Población Total\nUrbana (INE)', 'Jóvenes Urbanos\n(16 a 28 años)']
    rates = [2.30, 3.71]
    bar_colors = ['#64748B', C_ACCENT]
    bars = ax_v2.bar(categories, rates, color=bar_colors, width=0.45)
    ax_v2.set_ylim(0, 4.5)
    ax_v2.set_ylabel("Tasa de Desocupación Abierta (%)", fontsize=9)
    ax_v2.grid(axis='y', linestyle='--', alpha=0.5)
    
    for bar in bars:
        h = bar.get_height()
        ax_v2.text(bar.get_x() + bar.get_width()/2., h + 0.1, f"{h:.2f}%", 
                   ha='center', va='bottom', fontsize=11, fontweight='bold', color=C_PRIMARY)
    
    # Anotación de sobre-exposición
    ax_v2.annotate("Sobrerrepresentación de +1.41 pp\n(1.61 veces mayor en jóvenes)", 
                   xy=(1, 3.71), xytext=(0.5, 4.0),
                   arrowprops=dict(facecolor=C_GOLD, shrink=0.08, width=1.5, headwidth=6),
                   ha='center', fontsize=8.5, fontweight='bold', color=C_ACCENT,
                   bbox=dict(boxstyle="round,pad=0.3", fc="#FEF3C7", ec=C_GOLD, lw=1))
    
    # Visual 3: Subutilización Laboral (Subocupación vs Desocupación)
    ax_v3 = fig.add_axes([0.68, 0.06, 0.30, 0.66])
    ax_v3.set_facecolor(C_CARD)
    for s in ax_v3.spines.values():
        s.set_color(C_BORDER)
    ax_v3.set_title("Presión Laboral y Subutilización", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    metrics = ['Desocupación\nAbierta', 'Subocupación\npor Tiempo', 'Presión Total\nde Empleo']
    metric_vals = [3.71, 8.70, 3.71 + 8.70]
    m_colors = [C_ACCENT, C_GOLD, C_PRIMARY]
    bars_m = ax_v3.barh(metrics, metric_vals, color=m_colors, height=0.5)
    ax_v3.set_xlim(0, 15)
    ax_v3.set_xlabel("Porcentaje sobre la PEA Juvenil (%)", fontsize=9)
    ax_v3.grid(axis='x', linestyle='--', alpha=0.5)
    
    for bar in bars_m:
        w = bar.get_width()
        ax_v3.text(w + 0.3, bar.get_y() + bar.get_height()/2., f"{w:.2f}%", 
                   ha='left', va='center', fontsize=10, fontweight='bold', color=C_PRIMARY)
        
    for d in OUTPUT_DIRS:
        fig.savefig(os.path.join(d, 'dashboard_pagina_1.png'), bbox_inches='tight', dpi=300)
    plt.close(fig)
    print("[OK] Pagina 1 generada exitosamente.")

# ==============================================================================
# PÁGINA 2: VULNERABILIDAD ETARIA
# ==============================================================================
def render_page_2():
    fig = plt.figure(figsize=(16, 9), dpi=300, facecolor=C_BG)
    draw_header(fig, "Desocupación por Grupo Etario y Trayectoria", "Análisis de la Transición de la Secundaria al Mercado Calificado", 2)
    draw_footer(fig)
    
    card_w = 0.23
    gap = 0.02
    y_card = 0.76
    h_card = 0.12
    
    ax_kpi1 = fig.add_axes([0.02 + 0*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi1, "Pico Crítico de Desocupación", "4,65%", "Grupo 18 a 20 años", C_ACCENT, "MÁXIMO")
    
    ax_kpi2 = fig.add_axes([0.02 + 1*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi2, "Desocupados 18 a 20 Años", "17.518", "34,22% del total de desocupados", C_ACCENT, "VOLUMEN")
    
    ax_kpi3 = fig.add_axes([0.02 + 2*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi3, "Mayor Concentración Absoluta", "19.349", "Grupo 25 a 28 años (37,79%)", C_PRIMARY, "CONSOLIDACIÓN")
    
    ax_kpi4 = fig.add_axes([0.02 + 3*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi4, "Significancia Chi-Cuadrado", "p = 0,0105", "chi2 = 11,23 (Asociación significativa)", C_GOLD, "ESTADÍSTICA")
    
    # Visual 1: Tasa de Desocupación por Grupo Etario (Columnas)
    ax_v1 = fig.add_axes([0.02, 0.06, 0.47, 0.66])
    ax_v1.set_facecolor(C_CARD)
    for s in ax_v1.spines.values():
        s.set_color(C_BORDER)
    ax_v1.set_title("Tasa de Desocupación Ponderada por Tramo Etario (%)", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    groups = ['16 a 17 años\n(Secundaria)', '18 a 20 años\n(Transición)', '21 a 24 años\n(Técnico/Univ)', '25 a 28 años\n(Consolidación)']
    rates = [1.87, 4.65, 3.55, 3.88]
    colors = ['#94A3B8', C_ACCENT, '#3B82F6', C_PRIMARY]
    bars = ax_v1.bar(groups, rates, color=colors, width=0.5)
    ax_v1.set_ylim(0, 5.5)
    ax_v1.set_ylabel("Tasa de Desocupación (%)", fontsize=9)
    ax_v1.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Línea promedio nacional
    ax_v1.axhline(3.71, color=C_GOLD, linestyle=':', linewidth=2, label='Promedio Juvenil (3,71%)')
    ax_v1.legend(loc='upper left', frameon=True, facecolor=C_CARD, edgecolor=C_BORDER)
    
    for bar in bars:
        h = bar.get_height()
        ax_v1.text(bar.get_x() + bar.get_width()/2., h + 0.12, f"{h:.2f}%", 
                   ha='center', va='bottom', fontsize=10.5, fontweight='bold', color=C_PRIMARY)
        
    ax_v1.annotate("Vulnerabilidad Máxima:\nSalida escolar sin experiencia", 
                   xy=(1, 4.65), xytext=(1.2, 5.0),
                   arrowprops=dict(facecolor=C_ACCENT, shrink=0.08, width=1.5, headwidth=6),
                   ha='left', fontsize=8.5, fontweight='bold', color=C_ACCENT,
                   bbox=dict(boxstyle="round,pad=0.3", fc="#FEE2E2", ec=C_ACCENT, lw=1))
    
    # Visual 2: Volumen Absoluto de Ocupados vs Desocupados
    ax_v2 = fig.add_axes([0.52, 0.06, 0.46, 0.66])
    ax_v2.set_facecolor(C_CARD)
    for s in ax_v2.spines.values():
        s.set_color(C_BORDER)
    ax_v2.set_title("Volumen Poblacional Ponderado por Grupo Etario (Personas)", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    x = np.arange(len(groups))
    width = 0.35
    ocupados = [100650, 358941, 390771, 479283]
    desocupados = [1919, 17518, 14410, 19349]
    
    rects1 = ax_v2.bar(x - width/2, [o/1000 for o in ocupados], width, label='Ocupados (Miles)', color=C_PRIMARY)
    rects2 = ax_v2.bar(x + width/2, [d/1000 for d in desocupados], width, label='Desocupados (Miles)', color=C_ACCENT)
    
    ax_v2.set_xticks(x)
    ax_v2.set_xticklabels(groups, fontsize=8.5)
    ax_v2.set_ylabel("Miles de Personas (Ponderadas)", fontsize=9)
    ax_v2.grid(axis='y', linestyle='--', alpha=0.5)
    ax_v2.legend(loc='upper left', frameon=True, facecolor=C_CARD, edgecolor=C_BORDER)
    
    for r in rects2:
        h = r.get_height()
        ax_v2.text(r.get_x() + r.get_width()/2., h + 5, f"{h:.1f}k", 
                   ha='center', va='bottom', fontsize=9, fontweight='bold', color=C_ACCENT)
        
    for d in OUTPUT_DIRS:
        fig.savefig(os.path.join(d, 'dashboard_pagina_2.png'), bbox_inches='tight', dpi=300)
    plt.close(fig)
    print("[OK] Pagina 2 generada exitosamente.")

# ==============================================================================
# PÁGINA 3: EDUCACIÓN Y ESCOLARIDAD
# ==============================================================================
def render_page_3():
    fig = plt.figure(figsize=(16, 9), dpi=300, facecolor=C_BG)
    draw_header(fig, "Nivel Educativo y Escolaridad en la Inserción Laboral", "Análisis del Capital Humano y Paradojas de Inserción Juvenil", 3)
    draw_footer(fig)
    
    card_w = 0.23
    gap = 0.02
    y_card = 0.76
    h_card = 0.12
    
    ax_kpi1 = fig.add_axes([0.02 + 0*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi1, "TD Nivel Secundaria", "4,07%", "Mayor tasa por nivel formal", C_ACCENT, "PICO NIVEL")
    
    ax_kpi2 = fig.add_axes([0.02 + 1*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi2, "TD Superior Universitario", "3,74%", "Fricción de inserción profesional", C_PRIMARY, "PROFESIONAL")
    
    ax_kpi3 = fig.add_axes([0.02 + 2*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi3, "Años de Estudio Promedio", "12,2 años", "Desocupados: 12,5 años promedio", C_GOLD, "ESCOLARIDAD")
    
    ax_kpi4 = fig.add_axes([0.02 + 3*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi4, "Brecha por Asistencia Escolar", "+0,62 pp", "Asiste (4,14%) vs No Asiste (3,52%)", C_ORANGE, "ASISTENCIA")
    
    # Visual 1: Tasa de Desocupación por Nivel Educativo (Barras Horizontales)
    ax_v1 = fig.add_axes([0.02, 0.06, 0.47, 0.66])
    ax_v1.set_facecolor(C_CARD)
    for s in ax_v1.spines.values():
        s.set_color(C_BORDER)
    ax_v1.set_title("Tasa de Desocupación por Nivel Educativo (%)", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    levels = ['Sin instrucción', 'Primaria', 'Superior Técnico', 'Superior Universitario', 'Secundaria']
    rates = [0.00, 1.89, 3.42, 3.74, 4.07]
    bar_colors = ['#94A3B8', '#64748B', '#3B82F6', C_PRIMARY, C_ACCENT]
    
    bars = ax_v1.barh(levels, rates, color=bar_colors, height=0.5)
    ax_v1.set_xlim(0, 5.0)
    ax_v1.set_xlabel("Tasa de Desocupación Ponderada (%)", fontsize=9)
    ax_v1.grid(axis='x', linestyle='--', alpha=0.5)
    
    for bar in bars:
        w = bar.get_width()
        ax_v1.text(w + 0.1, bar.get_y() + bar.get_height()/2., f"{w:.2f}%", 
                   ha='left', va='center', fontsize=10, fontweight='bold', color=C_PRIMARY)
        
    ax_v1.axvline(3.71, color=C_GOLD, linestyle=':', linewidth=2, label='Promedio Juvenil (3,71%)')
    ax_v1.legend(loc='lower right', frameon=True, facecolor=C_CARD, edgecolor=C_BORDER)
    
    # Visual 2: Desocupación según Asistencia a Centros de Estudio y Tramo
    ax_v2 = fig.add_axes([0.52, 0.06, 0.46, 0.66])
    ax_v2.set_facecolor(C_CARD)
    for s in ax_v2.spines.values():
        s.set_color(C_BORDER)
    ax_v2.set_title("Desocupación según Asistencia Escolar y Conflicto Estudio-Trabajo", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    conds = ['Asiste Actualmente\na Estudio', 'No Asiste\na Estudio']
    rates_asist = [4.14, 3.52]
    b_asist = ax_v2.bar(conds, rates_asist, color=[C_ACCENT, C_PRIMARY], width=0.45)
    ax_v2.set_ylim(0, 5.5)
    ax_v2.set_ylabel("Tasa de Desocupación (%)", fontsize=9)
    ax_v2.grid(axis='y', linestyle='--', alpha=0.5)
    
    for b in b_asist:
        h = b.get_height()
        ax_v2.text(b.get_x() + b.get_width()/2., h + 0.15, f"{h:.2f}%", 
                   ha='center', va='bottom', fontsize=11, fontweight='bold', color=C_PRIMARY)
        
    ax_v2.annotate("Conflicto Horario:\nMayor desocupación en quienes\nestudian y buscan trabajar a la vez", 
                   xy=(0, 4.14), xytext=(0.3, 4.8),
                   arrowprops=dict(facecolor=C_ACCENT, shrink=0.08, width=1.5, headwidth=6),
                   ha='left', fontsize=8.5, fontweight='bold', color=C_ACCENT,
                   bbox=dict(boxstyle="round,pad=0.3", fc="#FEE2E2", ec=C_ACCENT, lw=1))
    
    for d in OUTPUT_DIRS:
        fig.savefig(os.path.join(d, 'dashboard_pagina_3.png'), bbox_inches='tight', dpi=300)
    plt.close(fig)
    print("[OK] Pagina 3 generada exitosamente.")

# ==============================================================================
# PÁGINA 4: BRECHAS DE GÉNERO Y TERRITORIO
# ==============================================================================
def render_page_4():
    fig = plt.figure(figsize=(16, 9), dpi=300, facecolor=C_BG)
    draw_header(fig, "Disparidades de Género y Desigualdades Territoriales", "Brecha Estructural Mujer-Hombre y Ranking Departamental", 4)
    draw_footer(fig)
    
    card_w = 0.23
    gap = 0.02
    y_card = 0.76
    h_card = 0.12
    
    ax_kpi1 = fig.add_axes([0.02 + 0*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi1, "Tasa Desocupación Mujeres", "4,69%", "28.718 mujeres desocupadas", C_ACCENT, "BRECHA GÉNERO")
    
    ax_kpi2 = fig.add_axes([0.02 + 1*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi2, "Tasa Desocupación Hombres", "2,85%", "22.478 hombres desocupados", C_PRIMARY, "HOMBRES")
    
    ax_kpi3 = fig.add_axes([0.02 + 2*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi3, "Brecha Absoluta de Género", "+1,84 pp", "Razón: 1,65 veces mayor en mujeres", C_GOLD, "DISPARIDAD")
    
    ax_kpi4 = fig.add_axes([0.02 + 3*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi4, "Departamento con Mayor TD", "5,80%", "Chuquisaca lidera desempleo juvenil", C_ACCENT, "REGIONAL")
    
    # Visual 1: Brecha de Género (Barras Agrupadas con KPI diferencial)
    ax_v1 = fig.add_axes([0.02, 0.06, 0.40, 0.66])
    ax_v1.set_facecolor(C_CARD)
    for s in ax_v1.spines.values():
        s.set_color(C_BORDER)
    ax_v1.set_title("Brecha de Desocupación por Sexo (%)", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    sexes = ['Hombres', 'Mujeres']
    s_rates = [2.85, 4.69]
    s_colors = [C_PRIMARY, C_ACCENT]
    bars_s = ax_v1.bar(sexes, s_rates, color=s_colors, width=0.45)
    ax_v1.set_ylim(0, 6.0)
    ax_v1.set_ylabel("Tasa de Desocupación Ponderada (%)", fontsize=9)
    ax_v1.grid(axis='y', linestyle='--', alpha=0.5)
    
    for bar in bars_s:
        h = bar.get_height()
        ax_v1.text(bar.get_x() + bar.get_width()/2., h + 0.15, f"{h:.2f}%", 
                   ha='center', va='bottom', fontsize=12, fontweight='bold', color=C_PRIMARY)
        
    ax_v1.annotate("Brecha de +1.84 pp\nchi2 = 5,24 (p = 0,0221)\nEstadísticamente significativa", 
                   xy=(1, 4.69), xytext=(0.4, 5.2),
                   arrowprops=dict(facecolor=C_ACCENT, shrink=0.08, width=1.5, headwidth=6),
                   ha='center', fontsize=8.5, fontweight='bold', color=C_ACCENT,
                   bbox=dict(boxstyle="round,pad=0.3", fc="#FEE2E2", ec=C_ACCENT, lw=1))
    
    # Visual 2: Ranking Departamental de Desocupación Juvenil
    ax_v2 = fig.add_axes([0.45, 0.06, 0.53, 0.66])
    ax_v2.set_facecolor(C_CARD)
    for s in ax_v2.spines.values():
        s.set_color(C_BORDER)
    ax_v2.set_title("Ranking Departamental de Desocupación Juvenil Urbana (%)", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    deptos = ['Pando', 'Potosí', 'Beni', 'Oruro', 'Santa Cruz', 'La Paz', 'Cochabamba', 'Tarija', 'Chuquisaca']
    d_rates = [2.41, 2.56, 2.98, 3.19, 3.33, 3.84, 4.71, 4.72, 5.80]
    
    # Paleta condicional: > 4.5 rojo, > 3.7 dorado, resto azul/gris
    bar_d_colors = []
    for r in d_rates:
        if r >= 4.7:
            bar_d_colors.append(C_ACCENT)
        elif r >= 3.7:
            bar_d_colors.append(C_GOLD)
        else:
            bar_d_colors.append('#3B82F6')
            
    bars_d = ax_v2.barh(deptos, d_rates, color=bar_d_colors, height=0.6)
    ax_v2.set_xlim(0, 7.0)
    ax_v2.set_xlabel("Tasa de Desocupación Ponderada (%)", fontsize=9)
    ax_v2.grid(axis='x', linestyle='--', alpha=0.5)
    
    for bar in bars_d:
        w = bar.get_width()
        ax_v2.text(w + 0.12, bar.get_y() + bar.get_height()/2., f"{w:.2f}%", 
                   ha='left', va='center', fontsize=9.5, fontweight='bold', color=C_PRIMARY)
        
    ax_v2.axvline(3.71, color=C_GOLD, linestyle=':', linewidth=2, label='Promedio Nacional Juvenil (3,71%)')
    ax_v2.legend(loc='lower right', frameon=True, facecolor=C_CARD, edgecolor=C_BORDER)
    
    for d in OUTPUT_DIRS:
        fig.savefig(os.path.join(d, 'dashboard_pagina_4.png'), bbox_inches='tight', dpi=300)
    plt.close(fig)
    print("[OK] Pagina 4 generada exitosamente.")

# ==============================================================================
# PÁGINA 5: PERFIL DEL JOVEN DESOCUPADO
# ==============================================================================
def render_page_5():
    fig = plt.figure(figsize=(16, 9), dpi=300, facecolor=C_BG)
    draw_header(fig, "Perfil del Joven Desocupado: Cesantes vs. Aspirantes", "Caracterización de la Pérdida de Empleo y Búsqueda del Primer Trabajo", 5)
    draw_footer(fig)
    
    card_w = 0.23
    gap = 0.02
    y_card = 0.76
    h_card = 0.12
    
    ax_kpi1 = fig.add_axes([0.02 + 0*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi1, "Desocupados Cesantes", "45.882", "89,62% (Tuvieron empleo previo)", C_ORANGE, "CESANTES")
    
    ax_kpi2 = fig.add_axes([0.02 + 1*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi2, "Desocupados Aspirantes", "5.314", "10,38% (Buscan primer empleo)", C_PURPLE, "ASPIRANTES")
    
    ax_kpi3 = fig.add_axes([0.02 + 2*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi3, "Pico Aspirantes (18 a 20)", "2.420", "45,5% de aspirantes en transición", C_PURPLE, "PRIMER EMPLEO")
    
    ax_kpi4 = fig.add_axes([0.02 + 3*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi4, "Canal Informal de Búsqueda", "62,3%", "Redes de amigos y familiares", C_GOLD, "REDES")
    
    # Visual 1: Donut Chart - Proporción Cesantes vs Aspirantes
    ax_v1 = fig.add_axes([0.02, 0.06, 0.32, 0.66])
    ax_v1.set_facecolor(C_CARD)
    for s in ax_v1.spines.values():
        s.set_color(C_BORDER)
    ax_v1.set_title("Estructura de Desocupados por Condición", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    sizes = [45882, 5314]
    colors = [C_ORANGE, C_PURPLE]
    explode = (0, 0.08)
    wedges, texts, autotexts = ax_v1.pie(sizes, explode=explode, labels=['Cesantes\n(45.9K)', 'Aspirantes\n(5.3K)'],
                                         colors=colors, autopct='%1.1f%%', startangle=60, pctdistance=0.75,
                                         textprops=dict(color='#212529', fontsize=9))
    plt.setp(autotexts, size=10, weight="bold", color="white")
    centre_circle = plt.Circle((0,0), 0.55, fc=C_CARD)
    ax_v1.add_artist(centre_circle)
    ax_v1.text(0, 0, "TOTAL\n51.2K", ha='center', va='center', fontsize=10, fontweight='bold', color=C_PRIMARY)
    
    # Visual 2: Columnas Clúster - Cesantes vs Aspirantes por Grupo Etario
    ax_v2 = fig.add_axes([0.36, 0.06, 0.32, 0.66])
    ax_v2.set_facecolor(C_CARD)
    for s in ax_v2.spines.values():
        s.set_color(C_BORDER)
    ax_v2.set_title("Distribución por Tramo Etario (Personas)", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    groups = ['16-17', '18-20', '21-24', '25-28']
    x = np.arange(len(groups))
    w = 0.35
    ces = [1158, 15098, 10952, 18674]
    asp = [761, 2420, 1458, 675]
    
    ax_v2.bar(x - w/2, [c/1000 for c in ces], w, label='Cesantes (Miles)', color=C_ORANGE)
    ax_v2.bar(x + w/2, [a/1000 for a in asp], w, label='Aspirantes (Miles)', color=C_PURPLE)
    
    ax_v2.set_xticks(x)
    ax_v2.set_xticklabels(groups, fontsize=9)
    ax_v2.set_ylabel("Miles de Personas Ponderadas", fontsize=9)
    ax_v2.grid(axis='y', linestyle='--', alpha=0.5)
    ax_v2.legend(loc='upper left', frameon=True, facecolor=C_CARD, edgecolor=C_BORDER)
    
    # Visual 3: Mecanismos de Búsqueda Activa (Barras horizontales)
    ax_v3 = fig.add_axes([0.70, 0.06, 0.28, 0.66])
    ax_v3.set_facecolor(C_CARD)
    for s in ax_v3.spines.values():
        s.set_color(C_BORDER)
    ax_v3.set_title("Mecanismos de Búsqueda Activa (%)", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    methods = ['Convocatorias públicas', 'Avisos e internet', 'Presentación directa', 'Contactos y familiares']
    m_pcts = [4.7, 13.2, 19.8, 62.3]
    bars_m = ax_v3.barh(methods, m_pcts, color=[C_PRIMARY, '#3B82F6', C_GOLD, C_ACCENT], height=0.5)
    ax_v3.set_xlim(0, 75)
    ax_v3.set_xlabel("Porcentaje de Desocupados (%)", fontsize=9)
    ax_v3.grid(axis='x', linestyle='--', alpha=0.5)
    
    for bar in bars_m:
        w_val = bar.get_width()
        ax_v3.text(w_val + 1.2, bar.get_y() + bar.get_height()/2., f"{w_val:.1f}%", 
                   ha='left', va='center', fontsize=9.5, fontweight='bold', color=C_PRIMARY)
        
    for d in OUTPUT_DIRS:
        fig.savefig(os.path.join(d, 'dashboard_pagina_5.png'), bbox_inches='tight', dpi=300)
    plt.close(fig)
    print("[OK] Pagina 5 generada exitosamente.")

# ==============================================================================
# PÁGINA 6: SÍNTESIS DE POLÍTICAS PÚBLICAS
# ==============================================================================
def render_page_6():
    fig = plt.figure(figsize=(16, 9), dpi=300, facecolor=C_BG)
    draw_header(fig, "Síntesis Estratégica y Políticas de Inserción Laboral", "Matriz de Priorización, Frentes de Acción y Hoja de Ruta de Empleo Juvenil", 6)
    draw_footer(fig)
    
    card_w = 0.23
    gap = 0.02
    y_card = 0.76
    h_card = 0.12
    
    ax_kpi1 = fig.add_axes([0.02 + 0*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi1, "Foco Etario Prioritario", "17.518", "Jóvenes 18 a 20 años en riesgo", C_ACCENT, "FOCO 1")
    
    ax_kpi2 = fig.add_axes([0.02 + 1*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi2, "Foco Brecha de Género", "28.718", "Mujeres jóvenes desocupadas", C_ACCENT, "FOCO 2")
    
    ax_kpi3 = fig.add_axes([0.02 + 2*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi3, "Foco Territorial Crítico", "Chuquisaca y Tarija", "Tasas superiores al 4,7%", C_GOLD, "FOCO 3")
    
    ax_kpi4 = fig.add_axes([0.02 + 3*(card_w+gap), y_card, card_w, h_card])
    create_card(ax_kpi4, "Foco Fricción Profesional", "25 a 28 Años", "37,8% del volumen desocupado", C_PRIMARY, "FOCO 4")
    
    # Visual 1: Matriz de Priorización Estratégica (Impacto vs Factibilidad)
    ax_v1 = fig.add_axes([0.02, 0.06, 0.45, 0.66])
    ax_v1.set_facecolor(C_CARD)
    for s in ax_v1.spines.values():
        s.set_color(C_BORDER)
    ax_v1.set_title("Matriz de Priorización de Intervenciones Públicas", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    
    # Cuadrantes
    ax_v1.axvline(5, color='#CBD5E1', linestyle='--', linewidth=1)
    ax_v1.axhline(5, color='#CBD5E1', linestyle='--', linewidth=1)
    
    ax_v1.text(2.5, 9.5, "ALTO IMPACTO / BAJA FACTIBILIDAD\n(Proyectos Estructurales)", ha='center', fontsize=8, color=C_TEXT_MUTED)
    ax_v1.text(7.5, 9.5, "ALTO IMPACTO / ALTA FACTIBILIDAD\n(Ganancias Rápidas / Prioridad 1)", ha='center', fontsize=8, fontweight='bold', color=C_ACCENT)
    ax_v1.text(2.5, 0.5, "BAJO IMPACTO / BAJA FACTIBILIDAD", ha='center', fontsize=8, color=C_TEXT_MUTED)
    ax_v1.text(7.5, 0.5, "BAJO IMPACTO / ALTA FACTIBILIDAD", ha='center', fontsize=8, color=C_TEXT_MUTED)
    
    # Proyectos
    initiatives = [
        {"name": "P1: Subsidio Primer Empleo\n(18-20 años)", "x": 8.5, "y": 8.8, "c": C_ACCENT, "size": 350},
        {"name": "P2: Cuotas de Género y Cuidados\n(Mujeres jóvenes)", "x": 7.8, "y": 8.2, "c": C_PRIMARY, "size": 320},
        {"name": "P3: Reactivación Productiva\nChuquisaca y Tarija", "x": 6.5, "y": 7.5, "c": C_GOLD, "size": 300},
        {"name": "P4: Bolsa Digital de Empleo\n(Transparencia vacantes)", "x": 8.2, "y": 6.5, "c": '#3B82F6', "size": 280},
        {"name": "P5: Reformas Curriculares\nUniversitarias (Largo plazo)", "x": 3.5, "y": 7.8, "c": C_TEXT_MUTED, "size": 250},
    ]
    
    for init in initiatives:
        ax_v1.scatter(init['x'], init['y'], s=init['size'], color=init['c'], alpha=0.85, edgecolors='black', linewidth=1)
        ax_v1.text(init['x'], init['y'] - 0.45, init['name'], ha='center', va='top', fontsize=8, fontweight='bold', color=C_PRIMARY)
        
    ax_v1.set_xlim(0, 10)
    ax_v1.set_ylim(0, 10)
    ax_v1.set_xlabel("Factibilidad de Implementación (1 a 10)", fontsize=9)
    ax_v1.set_ylabel("Impacto Potencial en Reducción de Desocupación (1 a 10)", fontsize=9)
    ax_v1.grid(True, linestyle=':', alpha=0.4)
    
    # Visual 2: Tarjetas de Programas Estratégicos Recomendados
    ax_v2 = fig.add_axes([0.49, 0.06, 0.49, 0.66])
    ax_v2.set_facecolor(C_CARD)
    for s in ax_v2.spines.values():
        s.set_color(C_BORDER)
    ax_v2.set_title("Hoja de Ruta: Tres Frentes de Acción Inmediata", fontsize=11, fontweight='bold', color=C_PRIMARY, pad=15)
    ax_v2.axis('off')
    
    # 3 Cajas de programas
    progs = [
        {
            "num": "01",
            "title": "Programa 'Mi Primer Empleo Digno' (Foco 18 a 20 años)",
            "desc": "Subsidio estatal temporal al 30% del salario mínimo para contratos de primer empleo en empresas privadas, con certificación de competencias y tutoría técnica laboral.",
            "color": C_ACCENT,
            "y": 0.70
        },
        {
            "num": "02",
            "title": "Estrategia 'Emplea Joven Mujer' (Reducción de Brecha de Género)",
            "desc": "Incentivos fiscales a empresas que contraten mujeres en áreas STEM e intermediación con servicios públicos de cuidado infantil para mitigar la penalización por maternidad temprana.",
            "color": C_PRIMARY,
            "y": 0.38
        },
        {
            "num": "03",
            "title": "Fondo de Fomento Productivo Territorial (Chuquisaca y Tarija)",
            "desc": "Líneas de crédito blando y capital semilla orientadas a emprendimientos juveniles de base tecnológica, agroindustrial y servicios calificados en valles del sur.",
            "color": C_GOLD,
            "y": 0.06
        }
    ]
    
    for p in progs:
        # Contenedor
        p_box = patches.FancyBboxPatch((0.02, p['y']), 0.96, 0.28, boxstyle="round,pad=0.02,rounding_size=0.03",
                                       facecolor='#F8FAFC', edgecolor=p['color'], linewidth=1.5,
                                       transform=ax_v2.transAxes)
        ax_v2.add_patch(p_box)
        
        # Badge numérico
        ax_v2.text(0.06, p['y'] + 0.20, p['num'], fontsize=14, fontweight='bold', color=p['color'], 
                   transform=ax_v2.transAxes, va='center')
        
        # Título
        ax_v2.text(0.14, p['y'] + 0.20, p['title'], fontsize=10, fontweight='bold', color=C_PRIMARY, 
                   transform=ax_v2.transAxes, va='center')
        
        # Descripción
        ax_v2.text(0.06, p['y'] + 0.08, p['desc'], fontsize=8.5, color='#334155', 
                   transform=ax_v2.transAxes, va='center', wrap=True)
        
    for d in OUTPUT_DIRS:
        fig.savefig(os.path.join(d, 'dashboard_pagina_6.png'), bbox_inches='tight', dpi=300)
    plt.close(fig)
    print("[OK] Pagina 6 generada exitosamente.")

if __name__ == "__main__":
    print("Iniciando renderizado de las 6 páginas del Dashboard de Power BI...")
    render_page_1()
    render_page_2()
    render_page_3()
    render_page_4()
    render_page_5()
    render_page_6()
    print("Todas las páginas fueron exportadas a 300 DPI en docs/figures/ y outputs/figures/.")
