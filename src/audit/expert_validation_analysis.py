"""
Módulo de Análisis Estadístico y Psicométrico de Validación por Juicio de Expertos.
Proyecto: Análisis de Desocupación Juvenil en Bolivia (ECE 4T-2025).
Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX) - CEPI.
Autor: Gonzales Suyo Franz Reinaldo.
"""

from typing import Dict, List, Tuple
import numpy as np
import pandas as pd


def calcular_v_aiken(puntuaciones: List[int], escala_max: int = 5, escala_min: int = 1) -> float:
    """
    Calcula el coeficiente V de Aiken para un reactivo evaluado por n jueces.
    
    Fórmula: V = S / (n * (c - 1))
    Donde:
        S = sum(r_i - l_0)
        r_i = puntuación otorgada por el juez i
        l_0 = calificación mínima de la escala (1)
        n = número de jueces
        c = número total de opciones de respuesta (5 - 1 + 1 = 5)
    """
    n = len(puntuaciones)
    if n == 0:
        return 0.0
    c = escala_max - escala_min + 1
    s_sum = sum(r - escala_min for r in puntuaciones)
    v = s_sum / (n * (c - 1))
    return float(v)


def calcular_alfa_cronbach(df_items: pd.DataFrame) -> float:
    """
    Calcula el coeficiente Alfa de Cronbach para evaluar la consistencia interna.
    
    Fórmula: alpha = (k / (k - 1)) * (1 - sum(var_items) / var_total)
    Donde:
        k = número de ítems evaluados
        var_items = varianza de cada ítem
        var_total = varianza de la suma de puntuaciones de cada encuestado
    """
    k = df_items.shape[1]
    if k <= 1:
        return 0.0
    
    var_items = df_items.var(axis=0, ddof=1).sum()
    total_scores = df_items.sum(axis=1)
    var_total = total_scores.var(ddof=1)
    
    if var_total == 0:
        return 1.0
        
    alfa = (k / (k - 1)) * (1 - (var_items / var_total))
    return float(alfa)


DIMENSIONES_DEFAULT = {
    "Preparación de Datos y Muestreo": [
        "P1_Criterios_Delimitacion",
        "P2_Uso_Ponderador"
    ],
    "Indicadores y Réplica INE": [
        "P3_Tasa_Desocupacion_3.71",
        "P4_Tasa_Subocupacion_8.70",
        "P5_Ratio_Juvenil_General_1.61"
    ],
    "Análisis Estadístico y Pruebas": [
        "P6_Pruebas_Chi2_Cramer",
        "P7_Comparacion_Escolaridad",
        "P8_Asociacion_Sin_Causalidad"
    ],
    "Cuadro de Mando en Power BI": [
        "P9_Estructura_6_Paginas",
        "P10_Visualizaciones_Tarjetas"
    ],
    "Interpretación y Hallazgos": [
        "P11_Brechas_Edad_Genero",
        "P12_Cesantes_Mayoritarios"
    ],
    "Conclusiones y Calidad General": [
        "P13_Conclusiones_Recomendaciones",
        "P14_Calidad_General_Rigor"
    ]
}


def analizar_respuestas_expertos(df_respuestas: pd.DataFrame, 
                                 dimensiones: Dict[str, List[str]] = None) -> Tuple[pd.DataFrame, float]:
    """
    Procesa la matriz de respuestas Likert (1 a 5) y computa promedios,
    desviaciones, V de Aiken y Alfa de Cronbach global.
    """
    if dimensiones is None:
        dimensiones = DIMENSIONES_DEFAULT
        
    filas = []
    todos_los_items = []
    
    for nombre_dim, items in dimensiones.items():
        sub_df = df_respuestas[[col for col in items if col in df_respuestas.columns]]
        if sub_df.empty:
            continue
            
        todos_los_items.extend(sub_df.columns.tolist())
        
        # Cálculo de V de Aiken promedio para la dimensión
        v_aiken_items = [calcular_v_aiken(sub_df[col].dropna().tolist()) for col in sub_df.columns]
        v_promedio = float(np.mean(v_aiken_items))
        
        # Promedio y desviación estándar de las calificaciones
        promedio_likert = float(sub_df.values.mean())
        desv_estandar = float(sub_df.values.std(ddof=1))
        
        # Criterio cualitativo de validación
        if v_promedio >= 0.95:
            dictamen = "Validación Máxima (Consenso Pleno)"
        elif v_promedio >= 0.85:
            dictamen = "Validación Excelente (Metodología Sólida)"
        elif v_promedio >= 0.80:
            dictamen = "Validación Fuerte (Aprobada)"
        elif v_promedio >= 0.70:
            dictamen = "Validación Aceptable con Observaciones Menores"
        else:
            dictamen = "Requiere Revisión de Reactivos"
            
        filas.append({
            "Dimensión Analítica": nombre_dim,
            "N.º Ítems": len(sub_df.columns),
            "Promedio Likert (1-5)": round(promedio_likert, 2),
            "V de Aiken": round(v_promedio, 3),
            "Desv. Estándar": round(desv_estandar, 2),
            "Nivel de Validación": dictamen
        })
        
    df_resumen = pd.DataFrame(filas)
    
    # Alfa de Cronbach sobre el total de ítems evaluados
    df_items_completos = df_respuestas[todos_los_items].dropna()
    alfa_cronbach = calcular_alfa_cronbach(df_items_completos)
    
    return df_resumen, alfa_cronbach


def generar_datos_simulados_piloto(n_jueces: int = 7, seed: int = 42) -> pd.DataFrame:
    """
    Genera un conjunto de datos sintéticos representativo de un panel piloto
    de 7 jueces expertos para verificar la reproducibilidad del código.
    Incorpora un efecto latente por juez para modelar concordancia inter-ítem.
    """
    np.random.seed(seed)
    todos_los_items = [item for sublist in DIMENSIONES_DEFAULT.values() for item in sublist]
    
    # Efecto latente por juez (rigor/benevolencia del evaluador)
    efecto_juez = np.random.normal(0, 0.4, size=n_jueces)
    
    datos = {}
    for item in todos_los_items:
        calificaciones = []
        for i in range(n_jueces):
            # Puntaje base alto con ruido y efecto juez
            val = int(np.clip(np.round(4.7 + efecto_juez[i] + np.random.normal(0, 0.3)), 1, 5))
            calificaciones.append(val)
        datos[item] = calificaciones
        
    return pd.DataFrame(datos)


if __name__ == "__main__":
    print("=== SIMULACIÓN PILOTO DE VALIDACIÓN POR JUICIO DE EXPERTOS ===")
    df_piloto = generar_datos_simulados_piloto(n_jueces=7)
    resumen, alfa = analizar_respuestas_expertos(df_piloto)
    
    print(f"\nAlfa de Cronbach Global: {alfa:.4f} (Excelente consistencia interna)")
    print("\nResultados por Dimensión Analítica:")
    print(resumen.to_string(index=False))
