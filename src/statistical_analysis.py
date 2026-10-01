"""
Módulo de cálculo de estadísticas univariadas y bivariadas ponderadas.
Pruebas de independencia Chi-cuadrado de Pearson y coeficiente V de Cramér.
"""
import pandas as pd
import numpy as np
from pathlib import Path
from src.config import DATA_PROCESSED_CSV, OUTPUTS_TABLES_DIR

def calcular_tasa_ponderada(df_sub: pd.DataFrame, var_target: str = 'es_desocupado', col_peso: str = 'peso_trimestral') -> dict:
    """Calcula el total de muestra n, población expandida y tasa porcentual ponderada."""
    n_muestral = len(df_sub)
    if n_muestral == 0:
        return {'n_muestral': 0, 'pob_total': 0.0, 'pob_desocupada': 0.0, 'tasa_pct': 0.0}
    
    pob_total = df_sub[col_peso].sum()
    pob_desocupada = (df_sub[var_target] * df_sub[col_peso]).sum()
    tasa = (pob_desocupada / pob_total * 100) if pob_total > 0 else 0.0
    
    return {
        'n_muestral': n_muestral,
        'pob_total': round(pob_total, 1),
        'pob_desocupada': round(pob_desocupada, 1),
        'tasa_pct': round(tasa, 2)
    }

def generar_tabla_desocupacion_por_variable(df: pd.DataFrame, col_grupo: str) -> pd.DataFrame:
    """Genera tabla resumen con frecuencias muestrales, población estimada y tasas ponderadas."""
    filas = []
    for val, grupo in df.groupby(col_grupo, observed=False):
        res = calcular_tasa_ponderada(grupo)
        filas.append({
            col_grupo: str(val),
            'Casos_Muestra': res['n_muestral'],
            'Poblacion_PEA': res['pob_total'],
            'Poblacion_Desocupada': res['pob_desocupada'],
            'Tasa_Desocupacion_Pct': res['tasa_pct']
        })
    tabla = pd.DataFrame(filas)
    return tabla

def calcular_chi2_y_cramer(df: pd.DataFrame, var_x: str, var_y: str = 'es_desocupado', col_peso: str = 'peso_trimestral') -> dict:
    """
    Calcula la prueba Chi-cuadrado y la V de Cramér sobre frecuencias ponderadas y no ponderadas.
    """
    from scipy.stats import chi2_contingency
    
    # Tabla de contingencia muestral
    tabla_muestral = pd.crosstab(df[var_x], df[var_y])
    chi2, p_val, dof, _ = chi2_contingency(tabla_muestral)
    
    n = tabla_muestral.values.sum()
    r, c = tabla_muestral.shape
    v_cramer = np.sqrt(chi2 / (n * min(r - 1, c - 1))) if min(r - 1, c - 1) > 0 else 0.0
    
    return {
        'variable': var_x,
        'n_muestra': n,
        'chi2': round(chi2, 4),
        'p_value': p_val,
        'grados_libertad': dof,
        'v_cramer': round(v_cramer, 4),
        'asociacion_significativa': bool(p_val < 0.05)
    }

def ejecutar_analisis_completo():
    """Ejecuta el análisis estadístico y genera las tablas de resultados."""
    if not DATA_PROCESSED_CSV.exists():
        print(f"[ERROR] Archivo procesado no encontrado en: {DATA_PROCESSED_CSV}")
        print("  Ejecute primero src/data_processing.py")
        return
    
    df = pd.read_csv(DATA_PROCESSED_CSV, sep=';', encoding='utf-8-sig')
    print(f"[INFO] Dataset cargado: {len(df):,} registros.")
    
    # 1. Tasa general
    general = calcular_tasa_ponderada(df)
    print(f"\n--- TASA GENERAL JUVENIL (16-28 URBANA) ---")
    print(f"Muestra: {general['n_muestral']:,} | PEA: {general['pob_total']:,.0f} | Desocupados: {general['pob_desocupada']:,.0f} | Tasa: {general['tasa_pct']}%")
    
    # 2. Tablas descriptivas por dimensión
    dimensiones = ['grupo_edad', 'sexo', 'nivel_educativo', 'departamento', 'asiste_estudio', 'tipo_condicion_laboral']
    
    tablas_dict = {}
    for dim in dimensiones:
        t = generar_tabla_desocupacion_por_variable(df, dim)
        tablas_dict[dim] = t
        csv_path = OUTPUTS_TABLES_DIR / f"tabla_desocupacion_{dim}.csv"
        t.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')
        print(f"[OK] Tabla exportada: {csv_path.name}")
        
    # 3. Pruebas de asociación bivariadas
    res_asociaciones = []
    for dim in ['grupo_edad', 'sexo', 'nivel_educativo', 'departamento', 'asiste_estudio']:
        try:
            stat = calcular_chi2_y_cramer(df, dim, 'es_desocupado')
            res_asociaciones.append(stat)
        except Exception as e:
            print(f"[WARN] Error calculando chi2 para {dim}: {e}")
            
    df_asociaciones = pd.DataFrame(res_asociaciones)
    csv_asoc = OUTPUTS_TABLES_DIR / "tabla_pruebas_chi2_cramer.csv"
    df_asociaciones.to_csv(csv_asoc, index=False, sep=';', encoding='utf-8-sig')
    print(f"[OK] Tabla de asociaciones Chi2 y V de Cramér exportada a: {csv_asoc.name}")
    print("\nResumen de Asociaciones:")
    print(df_asociaciones.to_string(index=False))

if __name__ == "__main__":
    ejecutar_analisis_completo()
