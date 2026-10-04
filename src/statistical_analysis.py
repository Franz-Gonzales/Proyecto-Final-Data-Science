"""
Módulo de cálculo de estadísticas univariadas y bivariadas ponderadas.
Pruebas de independencia Chi-cuadrado de Pearson, coeficiente V de Cramér
y comparativas de escolaridad según la metodología CRISP-DM.
"""
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, mannwhitneyu, ttest_ind
from pathlib import Path

from src.config import DATA_PROCESSED_CSV, OUTPUTS_TABLES_DIR

def calcular_tasa_ponderada(df_sub: pd.DataFrame, var_target: str = 'es_desocupado', col_peso: str = 'peso_trimestral') -> dict:
    """Calcula el total de muestra n, población expandida y tasa porcentual ponderada."""
    n_muestral = len(df_sub)
    if n_muestral == 0:
        return {'n_muestral': 0, 'pob_total': 0.0, 'pob_target': 0.0, 'tasa_pct': 0.0}
    
    pob_total = df_sub[col_peso].sum()
    pob_target = (df_sub[var_target] * df_sub[col_peso]).sum()
    tasa = (pob_target / pob_total * 100) if pob_total > 0 else 0.0
    
    return {
        'n_muestral': int(n_muestral),
        'pob_total': round(pob_total, 1),
        'pob_target': round(pob_target, 1),
        'tasa_pct': round(tasa, 2)
    }

def generar_tabla_descriptiva_ponderada(df: pd.DataFrame, col_grupo: str, var_target: str = 'es_desocupado') -> pd.DataFrame:
    """Genera tabla resumen con frecuencias muestrales, población estimada, tasa ponderada y alerta de representatividad."""
    filas = []
    pob_global_target = (df[var_target] * df['peso_trimestral']).sum()
    
    for val, grupo in df.groupby(col_grupo, observed=False):
        res = calcular_tasa_ponderada(grupo, var_target=var_target)
        peso_relativo_desoc = (res['pob_target'] / pob_global_target * 100) if pob_global_target > 0 else 0.0
        
        filas.append({
            col_grupo: str(val),
            'Casos_Muestra_n': res['n_muestral'],
            'Poblacion_PEA_N': res['pob_total'],
            'Poblacion_Desocupada_N': res['pob_target'],
            'Tasa_Desocupacion_Pct': res['tasa_pct'],
            'Distribucion_Desocupados_Pct': round(peso_relativo_desoc, 2),
            'Representatividad_Muestral': 'Confiable (n >= 30)' if res['n_muestral'] >= 30 else 'Referencial (n < 30)'
        })
        
    tabla = pd.DataFrame(filas)
    return tabla

def calcular_chi2_y_cramer(df: pd.DataFrame, var_x: str, var_y: str = 'es_desocupado') -> dict:
    """
    Calcula la prueba Chi-cuadrado de Pearson y la V de Cramér para medir asociación e intensidad.
    """
    tabla_muestral = pd.crosstab(df[var_x], df[var_y])
    chi2, p_val, dof, _ = chi2_contingency(tabla_muestral)
    
    n = tabla_muestral.values.sum()
    r, c = tabla_muestral.shape
    v_cramer = np.sqrt(chi2 / (n * min(r - 1, c - 1))) if min(r - 1, c - 1) > 0 else 0.0
    
    # Clasificación de intensidad del efecto
    if v_cramer < 0.10:
        intensidad = "Asociación Débil"
    elif v_cramer < 0.30:
        intensidad = "Asociación Moderada"
    else:
        intensidad = "Asociación Fuerte"
        
    return {
        'Variable': var_x,
        'Muestra_n': n,
        'Grados_Libertad': dof,
        'Chi2_Estadistico': round(chi2, 4),
        'p_valor': round(p_val, 6),
        'V_Cramer': round(v_cramer, 4),
        'Intensidad_Efecto': intensidad,
        'Asociacion_Significativa': bool(p_val < 0.05),
        'Veredicto_Estadistico': 'Rechaza H0 (Significativa al 95%)' if p_val < 0.05 else 'No rechaza H0 (Independientes)'
    }

def generar_tabla_macromagnitudes(df: pd.DataFrame) -> pd.DataFrame:
    """Genera la tabla con los grandes agregados del mercado laboral juvenil urbano."""
    pob_pea = df['peso_trimestral'].sum()
    pob_ocup = (df['es_ocupado'] * df['peso_trimestral']).sum()
    pob_desoc = (df['es_desocupado'] * df['peso_trimestral']).sum()
    pob_suboc = (df['es_subocupado'] * df['peso_trimestral']).sum()
    pob_cesante = (df['es_cesante'] * df['peso_trimestral']).sum()
    pob_aspirante = (df['es_aspirante'] * df['peso_trimestral']).sum()
    
    tasa_desoc = (pob_desoc / pob_pea) * 100
    tasa_suboc = (pob_suboc / pob_ocup) * 100
    pct_cesantes = (pob_cesante / pob_desoc) * 100
    pct_aspirantes = (pob_aspirante / pob_desoc) * 100
    
    data = [
        {"Indicador": "PEA Juvenil Urbana (16-28 años)", "Muestra_n": len(df), "Poblacion_Expandida": round(pob_pea, 1), "Tasa_o_Proporcion_Pct": 100.0, "Meta_Oficial_INE": "Referencia 100%"},
        {"Indicador": "Población Ocupada Juvenil", "Muestra_n": int(df['es_ocupado'].sum()), "Poblacion_Expandida": round(pob_ocup, 1), "Tasa_o_Proporcion_Pct": round(pob_ocup/pob_pea*100, 2), "Meta_Oficial_INE": "Referencia oficial"},
        {"Indicador": "Población Desocupada Juvenil", "Muestra_n": int(df['es_desocupado'].sum()), "Poblacion_Expandida": round(pob_desoc, 1), "Tasa_o_Proporcion_Pct": round(tasa_desoc, 2), "Meta_Oficial_INE": "3.7%"},
        {"Indicador": "Tasa de Subocupación Juvenil (sobre Ocupados)", "Muestra_n": int(df['es_subocupado'].sum()), "Poblacion_Expandida": round(pob_suboc, 1), "Tasa_o_Proporcion_Pct": round(tasa_suboc, 2), "Meta_Oficial_INE": "8.7%"},
        {"Indicador": "Desocupados Cesantes (Con experiencia previa)", "Muestra_n": int(df['es_cesante'].sum()), "Poblacion_Expandida": round(pob_cesante, 1), "Tasa_o_Proporcion_Pct": round(pct_cesantes, 2), "Meta_Oficial_INE": "89.6% de desocupados"},
        {"Indicador": "Desocupados Aspirantes (Búsqueda de primer empleo)", "Muestra_n": int(df['es_aspirante'].sum()), "Poblacion_Expandida": round(pob_aspirante, 1), "Tasa_o_Proporcion_Pct": round(pct_aspirantes, 2), "Meta_Oficial_INE": "10.4% de desocupados"}
    ]
    return pd.DataFrame(data)

def generar_comparativa_escolaridad(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula estadísticos descriptivos e inferenciales de años de escolaridad entre ocupados y desocupados."""
    df_valid = df[df['anios_estudio'] > 0].copy()
    
    ocupados = df_valid[df_valid['es_ocupado'] == 1]
    desocupados = df_valid[df_valid['es_desocupado'] == 1]
    
    # Medias ponderadas
    media_ocup_pond = (ocupados['anios_estudio'] * ocupados['peso_trimestral']).sum() / ocupados['peso_trimestral'].sum()
    media_desoc_pond = (desocupados['anios_estudio'] * desocupados['peso_trimestral']).sum() / desocupados['peso_trimestral'].sum()
    
    # Medias simples y medianas
    media_ocup_simple = ocupados['anios_estudio'].mean()
    media_desoc_simple = desocupados['anios_estudio'].mean()
    mediana_ocup = ocupados['anios_estudio'].median()
    mediana_desoc = desocupados['anios_estudio'].median()
    std_ocup = ocupados['anios_estudio'].std()
    std_desoc = desocupados['anios_estudio'].std()
    
    # Test de Mann-Whitney U (no paramétrico) y t-test
    stat_u, p_u = mannwhitneyu(ocupados['anios_estudio'], desocupados['anios_estudio'], alternative='two-sided')
    stat_t, p_t = ttest_ind(ocupados['anios_estudio'], desocupados['anios_estudio'], equal_var=False)
    
    res = [
        {"Grupo": "Jóvenes Ocupados", "Muestra_n": len(ocupados), "Media_Ponderada": round(media_ocup_pond, 2), "Media_Simple": round(media_ocup_simple, 2), "Mediana": round(mediana_ocup, 1), "Desv_Estandar": round(std_ocup, 2)},
        {"Grupo": "Jóvenes Desocupados", "Muestra_n": len(desocupados), "Media_Ponderada": round(media_desoc_pond, 2), "Media_Simple": round(media_desoc_simple, 2), "Mediana": round(mediana_desoc, 1), "Desv_Estandar": round(std_desoc, 2)},
        {"Grupo": "Diferencia / Test Estadístico", "Muestra_n": f"t={stat_t:.3f} (p={p_t:.4f})", "Media_Ponderada": round(media_desoc_pond - media_ocup_pond, 2), "Media_Simple": round(media_desoc_simple - media_ocup_simple, 2), "Mediana": f"U={stat_u:.1f} (p={p_u:.4f})", "Desv_Estandar": "Sin dif. significativa" if p_u >= 0.05 else "Dif. significativa"}
    ]
    return pd.DataFrame(res)

def ejecutar_analisis_completo():
    """Ejecuta el análisis estadístico exhaustivo y genera todas las tablas de evidencia empírica."""
    if not DATA_PROCESSED_CSV.exists():
        print(f"[ERROR] Archivo procesado no encontrado en: {DATA_PROCESSED_CSV}")
        return
    
    df = pd.read_csv(DATA_PROCESSED_CSV, sep=';', encoding='utf-8-sig')
    print(f"[INFO] Dataset cargado: {len(df):,} registros.")
    
    OUTPUTS_TABLES_DIR.mkdir(parents=True, exist_ok=True)
    
    # 1. Tabla Macromagnitudes Laborales
    t_macro = generar_tabla_macromagnitudes(df)
    t_macro.to_csv(OUTPUTS_TABLES_DIR / "tabla_desocupacion_macro.csv", index=False, sep=';', encoding='utf-8-sig')
    print("[OK] Exportada: tabla_desocupacion_macro.csv")
    
    # 2. Tablas descriptivas por dimensión
    dimensiones = [
        'grupo_edad',
        'sexo',
        'nivel_educativo',
        'departamento',
        'asiste_estudio',
        'tipo_condicion_laboral',
        'tipo_hogar',
        'parentesco'
    ]
    
    for dim in dimensiones:
        if dim in df.columns:
            t = generar_tabla_descriptiva_ponderada(df, dim)
            csv_path = OUTPUTS_TABLES_DIR / f"tabla_desocupacion_{dim}.csv"
            t.to_csv(csv_path, index=False, sep=';', encoding='utf-8-sig')
            print(f"[OK] Exportada: {csv_path.name}")
            
    # 3. Tablas especializadas para desocupados
    # Cesantes por ocupación anterior
    desoc_ces = df[df['es_cesante'] == 1].copy()
    if 'cob_uo_grupo' in desoc_ces.columns:
        t_cob = desoc_ces.groupby('cob_uo_grupo', observed=False).apply(
            lambda g: pd.Series({'Casos_Muestra': len(g), 'Poblacion_Estimada': round(g['peso_trimestral'].sum(), 1)})
        ).reset_index()
        t_cob['Distribucion_Pct'] = round(t_cob['Poblacion_Estimada'] / t_cob['Poblacion_Estimada'].sum() * 100, 2)
        t_cob = t_cob.sort_values(by='Poblacion_Estimada', ascending=False)
        t_cob.to_csv(OUTPUTS_TABLES_DIR / "tabla_desocupados_cesantes_por_ocupacion.csv", index=False, sep=';', encoding='utf-8-sig')
        print("[OK] Exportada: tabla_desocupados_cesantes_por_ocupacion.csv")
        
    # Desocupados por mecanismos de búsqueda
    desoc_all = df[df['es_desocupado'] == 1].copy()
    if 'mecanismo_busqueda' in desoc_all.columns:
        t_mec = desoc_all.groupby('mecanismo_busqueda', observed=False).apply(
            lambda g: pd.Series({'Casos_Muestra': len(g), 'Poblacion_Estimada': round(g['peso_trimestral'].sum(), 1)})
        ).reset_index()
        t_mec['Distribucion_Pct'] = round(t_mec['Poblacion_Estimada'] / t_mec['Poblacion_Estimada'].sum() * 100, 2)
        t_mec = t_mec.sort_values(by='Poblacion_Estimada', ascending=False)
        t_mec.to_csv(OUTPUTS_TABLES_DIR / "tabla_desocupados_mecanismo_busqueda.csv", index=False, sep=';', encoding='utf-8-sig')
        print("[OK] Exportada: tabla_desocupados_mecanismo_busqueda.csv")
        
    # 4. Pruebas bivariadas de asociación (Chi2 y V de Cramér)
    vars_asoc = ['grupo_edad', 'sexo', 'nivel_educativo', 'departamento', 'asiste_estudio', 'tipo_hogar', 'parentesco']
    res_asociaciones = []
    
    for v in vars_asoc:
        if v in df.columns:
            stat = calcular_chi2_y_cramer(df, v, 'es_desocupado')
            res_asociaciones.append(stat)
            
    df_asoc = pd.DataFrame(res_asociaciones)
    csv_asoc = OUTPUTS_TABLES_DIR / "tabla_pruebas_chi2_cramer.csv"
    df_asoc.to_csv(csv_asoc, index=False, sep=';', encoding='utf-8-sig')
    print(f"[OK] Exportada: {csv_asoc.name}")
    
    # 5. Comparativa de escolaridad
    t_esc = generar_comparativa_escolaridad(df)
    t_esc.to_csv(OUTPUTS_TABLES_DIR / "tabla_comparativa_escolaridad.csv", index=False, sep=';', encoding='utf-8-sig')
    print("[OK] Exportada: tabla_comparativa_escolaridad.csv")
    
    print("\n--- RESUMEN DE PRUEBAS DE ASOCIACIÓN (CHI-CUADRADO Y V DE CRAMÉR) ---")
    print(df_asoc[['Variable', 'Grados_Libertad', 'Chi2_Estadistico', 'p_valor', 'V_Cramer', 'Intensidad_Efecto', 'Veredicto_Estadistico']].to_string(index=False))

if __name__ == "__main__":
    ejecutar_analisis_completo()
