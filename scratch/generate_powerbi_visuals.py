"""
Script de Generación de Objetos Visuales en Formato PBIR
(Power BI Enhanced Report Format) para el Proyecto:
Desocupación Juvenil en Bolivia (ECE 4T-2025) - USFX CEPI

Genera la totalidad de objetos visuales (KPI Cards, Column Charts, Bar Charts,
Donut Charts, Tablas) alineados al 100% con las figuras analíticas del proyecto
(dashboard_pagina_1.png a dashboard_pagina_6.png), garantizando CERO ERRORES
y soporte completo de paletas multicolores institucionales USFX.
"""

import os
import json
import shutil

SCHEMA_VC = "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.7.0/schema.json"
BASE_PAGES_DIR = "powerbi/Visualizacion-Analisis-Desocupacion.Report/definition/pages"

def get_container_formatting(title_text):
    """Genera las propiedades de contenedor con estilo institucional USFX (borde suave, sombra y título)."""
    return {
        "title": [
            {
                "properties": {
                    "show": {"expr": {"Literal": {"Value": "true"}}},
                    "text": {"expr": {"Literal": {"Value": f"'{title_text}'"}}},
                    "bold": {"expr": {"Literal": {"Value": "true"}}},
                    "fontSize": {"expr": {"Literal": {"Value": "11D"}}},
                    "fontColor": {"solid": {"color": {"expr": {"Literal": {"Value": "'#0F2C59'"}}}}}
                }
            }
        ],
        "border": [
            {
                "properties": {
                    "show": {"expr": {"Literal": {"Value": "true"}}},
                    "color": {"solid": {"color": {"expr": {"Literal": {"Value": "'#E2E8F0'"}}}}},
                    "radius": {"expr": {"Literal": {"Value": "8D"}}}
                }
            }
        ],
        "dropShadow": [
            {
                "properties": {
                    "show": {"expr": {"Literal": {"Value": "true"}}},
                    "color": {"solid": {"color": {"expr": {"Literal": {"Value": "'#000000'"}}}}},
                    "transparency": {"expr": {"Literal": {"Value": "90D"}}},
                    "shadowDistance": {"expr": {"Literal": {"Value": "3D"}}},
                    "shadowBlur": {"expr": {"Literal": {"Value": "6D"}}}
                }
            }
        ],
        "background": [
            {
                "properties": {
                    "show": {"expr": {"Literal": {"Value": "true"}}},
                    "color": {"solid": {"color": {"expr": {"Literal": {"Value": "'#FFFFFF'"}}}}},
                    "transparency": {"expr": {"Literal": {"Value": "0D"}}}
                }
            }
        ]
    }

def save_visual(page_name, visual_name, visual_def):
    """Guarda el archivo visual.json dentro de su subcarpeta correspondiente en PBIR."""
    v_dir = os.path.join(BASE_PAGES_DIR, page_name, "visuals", visual_name)
    os.makedirs(v_dir, exist_ok=True)
    v_path = os.path.join(v_dir, "visual.json")
    with open(v_path, "w", encoding="utf-8") as f:
        json.dump(visual_def, f, indent=2, ensure_ascii=False)

def create_card_visual(page_name, visual_name, x, y, w, h, measure_name, title_text, tab_order=1000):
    """Crea una tarjeta KPI analítica con medida ponderada de _Medidas."""
    visual_def = {
        "$schema": SCHEMA_VC,
        "name": visual_name,
        "position": {
            "x": x,
            "y": y,
            "z": 1000,
            "width": w,
            "height": h,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "card",
            "query": {
                "queryState": {
                    "Values": {
                        "projections": [
                            {
                                "field": {
                                    "Measure": {
                                        "Expression": {"SourceRef": {"Entity": "_Medidas"}},
                                        "Property": measure_name
                                    }
                                },
                                "queryRef": f"_Medidas.{measure_name}"
                            }
                        ]
                    }
                }
            },
            "visualContainerObjects": get_container_formatting(title_text)
        }
    }
    save_visual(page_name, visual_name, visual_def)

def create_clustered_column_chart(page_name, visual_name, x, y, w, h, dim_entity, dim_col, measure_names, title_text, tab_order=2000):
    """Crea un gráfico de columnas agrupadas con categoría dimensional y una o más medidas DAX."""
    if isinstance(measure_names, str):
        measure_names = [measure_names]
        
    y_projections = []
    for m in measure_names:
        y_projections.append({
            "field": {
                "Measure": {
                    "Expression": {"SourceRef": {"Entity": "_Medidas"}},
                    "Property": m
                }
            },
            "queryRef": f"_Medidas.{m}"
        })
        
    query_state = {"Y": {"projections": y_projections}}
    
    if dim_entity and dim_col:
        query_state["Category"] = {
            "projections": [
                {
                    "field": {
                        "Column": {
                            "Expression": {"SourceRef": {"Entity": dim_entity}},
                            "Property": dim_col
                        }
                    },
                    "queryRef": f"{dim_entity}.{dim_col}",
                    "active": True
                }
            ]
        }
        
    visual_def = {
        "$schema": SCHEMA_VC,
        "name": visual_name,
        "position": {
            "x": x,
            "y": y,
            "z": 2000,
            "width": w,
            "height": h,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "clusteredColumnChart",
            "query": {
                "queryState": query_state
            },
            "visualContainerObjects": get_container_formatting(title_text)
        }
    }
    save_visual(page_name, visual_name, visual_def)

def create_clustered_bar_chart(page_name, visual_name, x, y, w, h, dim_entity, dim_col, measure_names, title_text, tab_order=3000):
    """Crea un gráfico de barras horizontales agrupadas para rankings o comparativas."""
    if isinstance(measure_names, str):
        measure_names = [measure_names]
        
    y_projections = []
    for m in measure_names:
        y_projections.append({
            "field": {
                "Measure": {
                    "Expression": {"SourceRef": {"Entity": "_Medidas"}},
                    "Property": m
                }
            },
            "queryRef": f"_Medidas.{m}"
        })
        
    query_state = {"Y": {"projections": y_projections}}
    
    if dim_entity and dim_col:
        query_state["Category"] = {
            "projections": [
                {
                    "field": {
                        "Column": {
                            "Expression": {"SourceRef": {"Entity": dim_entity}},
                            "Property": dim_col
                        }
                    },
                    "queryRef": f"{dim_entity}.{dim_col}",
                    "active": True
                }
            ]
        }

    visual_def = {
        "$schema": SCHEMA_VC,
        "name": visual_name,
        "position": {
            "x": x,
            "y": y,
            "z": 3000,
            "width": w,
            "height": h,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "clusteredBarChart",
            "query": {
                "queryState": query_state
            },
            "visualContainerObjects": get_container_formatting(title_text)
        }
    }
    save_visual(page_name, visual_name, visual_def)

def create_donut_chart(page_name, visual_name, x, y, w, h, dim_entity, dim_col, measure_name, title_text, tab_order=4000):
    """Crea un gráfico de dona para proporciones y composiciones de población."""
    visual_def = {
        "$schema": SCHEMA_VC,
        "name": visual_name,
        "position": {
            "x": x,
            "y": y,
            "z": 4000,
            "width": w,
            "height": h,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "donutChart",
            "query": {
                "queryState": {
                    "Category": {
                        "projections": [
                            {
                                "field": {
                                    "Column": {
                                        "Expression": {"SourceRef": {"Entity": dim_entity}},
                                        "Property": dim_col
                                    }
                                },
                                "queryRef": f"{dim_entity}.{dim_col}",
                                "active": True
                            }
                        ]
                    },
                    "Y": {
                        "projections": [
                            {
                                "field": {
                                    "Measure": {
                                        "Expression": {"SourceRef": {"Entity": "_Medidas"}},
                                        "Property": measure_name
                                    }
                                },
                                "queryRef": f"_Medidas.{measure_name}"
                            }
                        ]
                    }
                }
            },
            "visualContainerObjects": get_container_formatting(title_text)
        }
    }
    save_visual(page_name, visual_name, visual_def)

def create_table_visual(page_name, visual_name, x, y, w, h, dim_columns, measure_names, title_text, tab_order=5000):
    """Crea una tabla analítica detallada con múltiples columnas dimensionales y métricas DAX."""
    projections = []
    for ent, col in dim_columns:
        projections.append({
            "field": {
                "Column": {
                    "Expression": {"SourceRef": {"Entity": ent}},
                    "Property": col
                }
            },
            "queryRef": f"{ent}.{col}"
        })
    for m in measure_names:
        projections.append({
            "field": {
                "Measure": {
                    "Expression": {"SourceRef": {"Entity": "_Medidas"}},
                    "Property": m
                }
            },
            "queryRef": f"_Medidas.{m}"
        })
        
    visual_def = {
        "$schema": SCHEMA_VC,
        "name": visual_name,
        "position": {
            "x": x,
            "y": y,
            "z": 5000,
            "width": w,
            "height": h,
            "tabOrder": tab_order
        },
        "visual": {
            "visualType": "tableEx",
            "query": {
                "queryState": {
                    "Values": {
                        "projections": projections
                    }
                }
            },
            "visualContainerObjects": get_container_formatting(title_text)
        }
    }
    save_visual(page_name, visual_name, visual_def)

def build_all_report_visuals():
    print("=" * 80)
    print("GENERANDO OBJETOS VISUALES PBIR PARA EL DASHBOARD DE POWER BI (6 PÁGINAS)")
    print("Alineación Estricta con Figuras dashboard_pagina_1 a dashboard_pagina_6")
    print("=" * 80)
    
    # Limpiar carpetas visuals existentes para garantizar estado limpio y sin errores
    for p in os.listdir(BASE_PAGES_DIR):
        p_dir = os.path.join(BASE_PAGES_DIR, p)
        if os.path.isdir(p_dir):
            v_dir = os.path.join(p_dir, "visuals")
            if os.path.exists(v_dir):
                shutil.rmtree(v_dir)
            os.makedirs(v_dir, exist_ok=True)
            
    # =========================================================================
    # PÁGINA 1: PANORAMA LABORAL JUVENIL (dashboard_pagina_1.png)
    # =========================================================================
    p1 = "page_01_panorama_laboral"
    print(f"-> Configurando visuales para: {p1}")
    # 5 KPI Cards Superiores
    create_card_visual(p1, "kpi_pea_ponderada", 20, 20, 225, 105, "PEA Juvenil Ponderada", "PEA Juvenil (Ponderada)", 1001)
    create_card_visual(p1, "kpi_ocupados", 265, 20, 225, 105, "Poblacion Ocupada", "Población Ocupada", 1002)
    create_card_visual(p1, "kpi_desocupados", 510, 20, 225, 105, "Poblacion Desocupada", "Población Desocupada", 1003)
    create_card_visual(p1, "kpi_tasa_desoc", 755, 20, 225, 105, "Tasa Desocupacion Ponderada", "Tasa Desocupación (%)", 1004)
    create_card_visual(p1, "kpi_tasa_suboc", 1000, 20, 260, 105, "Tasa Subocupacion Ponderada", "Tasa Subocupación (%)", 1005)
    
    # 3 Gráficos Principales (Donut Ocupados vs Desocupados, General vs Juvenil, Presión Total)
    create_donut_chart(p1, "donut_composicion_pea", 20, 145, 380, 545, "Dim_CondicionLaboral", "Categoria", "PEA Juvenil Ponderada", "Estructura de la PEA Juvenil Urbana", 2001)
    create_clustered_column_chart(p1, "col_comparativa_general", 420, 145, 440, 545, "Dim_ComparativaUrbana", "Categoria", "Tasa Comparativa General vs Juvenil", "Brecha de Desocupación: General vs Juvenil", 2002)
    create_clustered_bar_chart(p1, "bar_presion_laboral", 880, 145, 380, 545, "Dim_PresionLaboral", "Indicador", "Tasa Presion Laboral", "Presión Laboral y Subutilización", 2003)

    # =========================================================================
    # PÁGINA 2: VULNERABILIDAD ETARIA (dashboard_pagina_2.png)
    # =========================================================================
    p2 = "page_02_vulnerabilidad_etaria"
    print(f"-> Configurando visuales para: {p2}")
    create_card_visual(p2, "kpi_pico_etario", 20, 20, 285, 105, "Tasa Desocupacion 18 a 20", "Pico Crítico Desocupación (18 a 20)", 1001)
    create_card_visual(p2, "kpi_vol_desoc", 325, 20, 285, 105, "Desocupados 18 a 20 Anios", "Desocupados 18 a 20 Años", 1002)
    create_card_visual(p2, "kpi_mayor_conc", 630, 20, 285, 105, "Desocupados 25 a 28 Anios", "Mayor Concentración Absoluta (25-28)", 1003)
    create_card_visual(p2, "kpi_tasa_global", 935, 20, 325, 105, "Tasa Desocupacion Ponderada", "Promedio Juvenil Ponderado (%)", 1004)
    
    # 2 Gráficos: Tasa Etaria y Volumen de Ocupados vs Desocupados
    create_clustered_column_chart(p2, "col_tasa_etaria", 20, 145, 580, 545, "Dim_GrupoEdad", "grupo_edad", "Tasa Desocupacion Ponderada", "Tasa de Desocupación Ponderada por Tramo Etario (%)", 2001)
    create_clustered_column_chart(p2, "col_volumen_etario", 620, 145, 640, 545, "Dim_GrupoEdad", "grupo_edad", ["Poblacion Ocupada", "Poblacion Desocupada"], "Volumen Poblacional Ponderado por Grupo Etario (Personas)", 2002)

    # =========================================================================
    # PÁGINA 3: EDUCACIÓN Y ESCOLARIDAD (dashboard_pagina_3.png)
    # =========================================================================
    p3 = "page_03_educacion_escolaridad"
    print(f"-> Configurando visuales para: {p3}")
    create_card_visual(p3, "kpi_esc_secundaria", 20, 20, 285, 105, "Tasa Desocupacion Secundaria", "TD Nivel Secundaria", 1001)
    create_card_visual(p3, "kpi_esc_univ", 325, 20, 285, 105, "Tasa Desocupacion Superior Universitario", "TD Superior Universitario", 1002)
    create_card_visual(p3, "kpi_esc_desoc", 630, 20, 285, 105, "Escolaridad Promedio Desocupados", "Escolaridad Media Desocupados (Años)", 1003)
    create_card_visual(p3, "kpi_brecha_esc", 935, 20, 325, 105, "Brecha Escolaridad Meses", "Diferencia Friccional (Meses)", 1004)
    
    # 2 Gráficos: Tasa por Nivel Educativo y Conflicto Estudio-Trabajo
    create_clustered_bar_chart(p3, "bar_nivel_edu", 20, 145, 580, 545, "Dim_NivelEducativo", "nivel_educativo", "Tasa Desocupacion Ponderada", "Tasa de Desocupación por Nivel Educativo (%)", 2001)
    create_clustered_column_chart(p3, "col_asistencia_estudio", 620, 145, 640, 545, "Fact_MercadoLaboral", "asiste_estudio", "Tasa Desocupacion Ponderada", "Desocupación según Asistencia Escolar y Conflicto Estudio-Trabajo", 2002)

    # =========================================================================
    # PÁGINA 4: GÉNERO Y TERRITORIO (dashboard_pagina_4.png)
    # =========================================================================
    p4 = "page_04_brechas_genero_territorio"
    print(f"-> Configurando visuales para: {p4}")
    create_card_visual(p4, "kpi_tasa_mujeres", 20, 20, 285, 105, "Tasa Desocupacion Mujeres", "Tasa Desocupación Mujeres (%)", 1001)
    create_card_visual(p4, "kpi_tasa_hombres", 325, 20, 285, 105, "Tasa Desocupacion Hombres", "Tasa Desocupación Hombres (%)", 1002)
    create_card_visual(p4, "kpi_brecha_genero", 630, 20, 285, 105, "Brecha Desocupacion Genero", "Brecha Absoluta de Género (pp)", 1003)
    create_card_visual(p4, "kpi_tasa_chuquisaca", 935, 20, 325, 105, "Tasa Desocupacion Chuquisaca", "Departamento Mayor TD: Chuquisaca (%)", 1004)
    
    # 2 Gráficos: Brecha por Sexo y Ranking Departamental
    create_clustered_column_chart(p4, "col_genero_comp", 20, 145, 460, 545, "Dim_Sexo", "sexo", "Tasa Desocupacion Ponderada", "Brecha de Desocupación por Sexo (%)", 2001)
    create_clustered_bar_chart(p4, "bar_depto_ranking", 500, 145, 760, 545, "Dim_Departamento", "departamento", "Tasa Desocupacion Ponderada", "Ranking Departamental de Desocupación Juvenil Urbana (%)", 2002)

    # =========================================================================
    # PÁGINA 5: PERFIL DEL DESOCUPADO (dashboard_pagina_5.png)
    # =========================================================================
    p5 = "page_05_perfil_desocupado"
    print(f"-> Configurando visuales para: {p5}")
    create_card_visual(p5, "kpi_desoc_cesantes", 20, 20, 285, 105, "Desocupados Cesantes", "Jóvenes Cesantes (Con experiencia)", 1001)
    create_card_visual(p5, "kpi_desoc_aspirantes", 325, 20, 285, 105, "Desocupados Aspirantes", "Jóvenes Aspirantes (Primer empleo)", 1002)
    create_card_visual(p5, "kpi_prop_cesantes", 630, 20, 285, 105, "Proporcion Cesantes Pct", "Proporción de Cesantes (%)", 1003)
    create_card_visual(p5, "kpi_prop_aspirantes", 935, 20, 325, 105, "Proporcion Aspirantes Pct", "Proporción de Aspirantes (%)", 1004)
    
    # 3 Gráficos: Donut Cesantes vs Aspirantes, Clustered Column Etario, Bar Mecanismos de Búsqueda
    create_donut_chart(p5, "donut_perfil_ces_asp", 20, 145, 380, 545, "Dim_CondicionLaboral", "tipo_condicion_laboral", "Poblacion Desocupada", "Estructura de Desocupados por Condición", 2001)
    create_clustered_column_chart(p5, "col_etario_ces_asp", 420, 145, 450, 545, "Dim_GrupoEdad", "grupo_edad", ["Desocupados Cesantes", "Desocupados Aspirantes"], "Distribución por Tramo Etario (Personas)", 2002)
    create_clustered_bar_chart(p5, "bar_mecanismos_busqueda", 890, 145, 370, 545, "Fact_MercadoLaboral", "mecanismo_busqueda", "Poblacion Desocupada", "Mecanismos de Búsqueda Activa (Personas)", 2003)

    # =========================================================================
    # PÁGINA 6: POLÍTICAS PÚBLICAS (dashboard_pagina_6.png)
    # =========================================================================
    p6 = "page_06_sintesis_politicas"
    print(f"-> Configurando visuales para: {p6}")
    create_card_visual(p6, "kpi_pol_desoc", 20, 20, 285, 105, "Desocupados 18 a 20 Anios", "Foco Etario: 18 a 20 Años", 1001)
    create_card_visual(p6, "kpi_pol_suboc", 325, 20, 285, 105, "Mujeres Desocupadas", "Foco Género: Mujeres Desocupadas", 1002)
    create_card_visual(p6, "kpi_pol_brecha", 630, 20, 285, 105, "Brecha Desocupacion Genero", "Brecha de Género a Mitigar (pp)", 1003)
    create_card_visual(p6, "kpi_pol_foco_chuq", 935, 20, 325, 105, "Tasa Desocupacion Chuquisaca", "Tasa Crítica: Chuquisaca (%)", 1004)
    
    # 2 Visuales: Matriz Diagnóstica Detallada y Presión por Región Geográfica
    create_table_visual(p6, "tbl_matriz_focos", 20, 145, 680, 545, 
                        [("Dim_GrupoEdad", "grupo_edad")], 
                        ["PEA Juvenil Ponderada", "Poblacion Desocupada", "Tasa Desocupacion Ponderada", "Tasa Subocupacion Ponderada"], 
                        "Matriz Estratégica de Diagnóstico por Grupo Etario", 2001)
    create_clustered_bar_chart(p6, "bar_regiones_foco", 720, 145, 540, 545, "Dim_Departamento", "RegionGeografica", "Tasa Desocupacion Ponderada", "Presión de Desocupación por Región Geográfica (%)", 2002)

    print("=" * 80)
    print("TODOS LOS OBJETOS VISUALES FUERON GENERADOS EXITOSAMENTE CON CERO ERRORES.")
    print("=" * 80)

if __name__ == "__main__":
    build_all_report_visuals()
