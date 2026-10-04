"""
Módulo de ingesta, limpieza, filtrado y preparación de datos (Data Wrangling).
Aplica las directrices CRISP-DM para microdatos de la Encuesta Continua de Empleo (ECE 4T-2025).
"""
import sys
import pandas as pd
import numpy as np
from pathlib import Path

from src.config import (
    DATA_RAW_CSV,
    DATA_PROCESSED_CSV,
    EDAD_MINIMA,
    EDAD_MAXIMA,
    AREA_URBANA,
    GRUPOS_EDAD_BINS,
    GRUPOS_EDAD_LABELS,
    DEPTO_MAP,
    SEXO_MAP,
    NIV_ED_G_MAP,
    ASISTENCIA_ED_MAP,
    TIPO_HOGAR_MAP,
    PARENTESCO_MAP,
    MECANISMO_BUSQUEDA_MAP,
    COB_GRUPOS_MAP,
    CAEB_RAMAS_MAP
)

def cargar_microdatos_crudos(filepath=DATA_RAW_CSV) -> pd.DataFrame:
    """Carga el archivo CSV crudo de la ECE 4T-2025 con codificación y separador oficiales."""
    print(f"[INFO] Cargando microdatos crudos desde: {filepath}")
    df = pd.read_csv(filepath, sep=';', encoding='latin1', low_memory=False)
    print(f"[OK] Microdatos cargados exitosamente: {df.shape[0]:,} registros y {df.shape[1]} variables.")
    return df

def filtrar_universo_estudio(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtra la población objetivo:
    - Área urbana (area == 1)
    - Jóvenes de 16 a 28 años cumplidos (16 <= s1_03a <= 28)
    - Población Económicamente Activa (pea == 1)
    """
    print("[INFO] Aplicando filtros del universo de estudio...")
    n_inicial = len(df)
    
    # Conversión segura de columnas de filtro
    df['area_num'] = pd.to_numeric(df['area'], errors='coerce').fillna(0).astype(int)
    df['edad_num'] = pd.to_numeric(df['s1_03a'], errors='coerce').fillna(0).astype(int)
    df['pea_num'] = pd.to_numeric(df['pea'], errors='coerce').fillna(0).astype(int)
    
    # Filtro área urbana
    df_urb = df[df['area_num'] == AREA_URBANA].copy()
    print(f"  - Filtro Área Urbana (area == 1): {len(df_urb):,} registros (eliminados {n_inicial - len(df_urb):,})")
    
    # Filtro edad 16 a 28
    df_edad = df_urb[(df_urb['edad_num'] >= EDAD_MINIMA) & (df_urb['edad_num'] <= EDAD_MAXIMA)].copy()
    print(f"  - Filtro Rango Etario (16 <= s1_03a <= 28): {len(df_edad):,} registros (eliminados {len(df_urb) - len(df_edad):,})")
    
    # Filtro PEA
    df_pea = df_edad[df_edad['pea_num'] == 1].copy()
    print(f"  - Filtro Condición PEA (pea == 1): {len(df_pea):,} registros (eliminados {len(df_edad) - len(df_pea):,})")
    
    return df_pea

def transformar_y_recodificar(df: pd.DataFrame) -> pd.DataFrame:
    """Genera segmentos etarios, mapea etiquetas y crea campos analíticos legibles."""
    print("[INFO] Generando transformaciones e ingeniería de variables...")
    df = df.copy()
    
    # Variables sociodemográficas
    df['edad'] = pd.to_numeric(df['s1_03a'], errors='coerce').astype(int)
    df['sexo_cod'] = pd.to_numeric(df['s1_02'], errors='coerce').fillna(0).astype(int)
    df['sexo'] = df['sexo_cod'].map(SEXO_MAP).fillna("No identificado")
    
    # Grupos de edad (4 tramos analíticos)
    df['grupo_edad'] = pd.cut(
        df['edad'],
        bins=GRUPOS_EDAD_BINS,
        labels=GRUPOS_EDAD_LABELS,
        right=True
    )
    
    # Departamento
    df['depto_cod'] = pd.to_numeric(df['depto'], errors='coerce').fillna(0).astype(int)
    df['departamento'] = df['depto_cod'].map(DEPTO_MAP).fillna("Desconocido")
    
    # Nivel educativo agrupado
    if 'niv_ed_g' in df.columns:
        df['niv_ed_cod'] = pd.to_numeric(df['niv_ed_g'], errors='coerce').fillna(0).astype(int)
        df['nivel_educativo'] = df['niv_ed_cod'].map(NIV_ED_G_MAP).fillna("No especificado")
    
    # Años de estudio
    if 'aestudio' in df.columns:
        df['anios_estudio'] = pd.to_numeric(df['aestudio'], errors='coerce').fillna(0).astype(int)
        
    # Asistencia educativa
    if 's1_09' in df.columns:
        df['asistencia_cod'] = pd.to_numeric(df['s1_09'], errors='coerce').fillna(2).astype(int)
        df['asiste_estudio'] = df['asistencia_cod'].map(ASISTENCIA_ED_MAP).fillna("No asiste")
        
    # Variables de condición de actividad y PEA
    df['pea_val'] = pd.to_numeric(df['pea'], errors='coerce').fillna(0).astype(int)
    df['peao_val'] = pd.to_numeric(df['peao'], errors='coerce').fillna(0).astype(int)
    df['pead_val'] = pd.to_numeric(df['pead'], errors='coerce').fillna(0).astype(int)
    df['peadces_val'] = pd.to_numeric(df['peadces'], errors='coerce').fillna(0).astype(int)
    df['peadasp_val'] = pd.to_numeric(df['peadasp'], errors='coerce').fillna(0).astype(int)
    df['psubocup_val'] = pd.to_numeric(df['psubocup'], errors='coerce').fillna(0).astype(int)
    
    # Subcategoría de desocupación (Aspirante vs Cesante vs Ocupado)
    condiciones = [
        (df['peao_val'] == 1),
        (df['pead_val'] == 1) & (df['peadces_val'] == 1),
        (df['pead_val'] == 1) & (df['peadasp_val'] == 1)
    ]
    elecciones = ['Ocupado', 'Desocupado Cesante', 'Desocupado Aspirante']
    df['tipo_condicion_laboral'] = np.select(condiciones, elecciones, default='Desocupado no clasificado')
    
    df['es_desocupado'] = df['pead_val']
    df['es_ocupado'] = df['peao_val']
    df['es_cesante'] = df['peadces_val']
    df['es_aspirante'] = df['peadasp_val']
    df['es_subocupado'] = df['psubocup_val']
    
    # Estructura del hogar y parentesco
    if 'tipohogar' in df.columns:
        df['tipohogar_cod'] = pd.to_numeric(df['tipohogar'], errors='coerce').fillna(0).astype(int)
        df['tipo_hogar'] = df['tipohogar_cod'].map(TIPO_HOGAR_MAP).fillna("Otros / Sin núcleo")
    if 's1_05' in df.columns:
        df['parentesco_cod'] = pd.to_numeric(df['s1_05'], errors='coerce').fillna(0).astype(int)
        df['parentesco'] = df['parentesco_cod'].map(PARENTESCO_MAP).fillna("Otros parientes")
        
    # Trayectoria de búsqueda y antecedentes para desocupados
    if 's2_08a' in df.columns:
        df['mecanismo_cod'] = pd.to_numeric(df['s2_08a'], errors='coerce').fillna(0).astype(int)
        df['mecanismo_busqueda'] = df['mecanismo_cod'].map(MECANISMO_BUSQUEDA_MAP).fillna("No aplica / No declaró")
        
    # Grupo ocupacional previo (COB) y rama previa (CAEB) para cesantes
    if 'cob_uo' in df.columns:
        cob_dig = df['cob_uo'].astype(str).str.strip().str[:1]
        df['cob_uo_grupo'] = cob_dig.map(COB_GRUPOS_MAP).fillna("No aplica / Sin ocupación previa")
    if 'caeb_uo' in df.columns:
        caeb_clean = df['caeb_uo'].astype(str).str.strip()
        df['caeb_uo_grupo'] = caeb_clean.map(CAEB_RAMAS_MAP).fillna("No aplica / Sin rama previa")
    
    # Ponderador trimestral (maneja coma decimal del INE)
    df['peso_trimestral'] = df['fact_trim_act'].astype(str).str.replace(',', '.').astype(float)
    
    return df

def validar_consistencia(df: pd.DataFrame) -> bool:
    """Verifica reglas lógicas y matemáticas del dataset procesado."""
    print("[INFO] Verificando consistencia estadística...")
    # Coherencia: Ocupados + Desocupados = PEA
    suma_peao_pead = df['es_ocupado'].sum() + df['es_desocupado'].sum()
    total_pea = df['pea_val'].sum()
    assert suma_peao_pead == total_pea, f"Inconsistencia en PEA: Ocupados ({df['es_ocupado'].sum()}) + Desocupados ({df['es_desocupado'].sum()}) != PEA ({total_pea})"
    
    # Ponderaciones mayores a cero
    assert (df['peso_trimestral'] > 0).all(), "Existen registros con factor de expansión <= 0"
    
    # Resumen poblacional estimado
    pob_pea_estimada = df['peso_trimestral'].sum()
    pob_ocupada_est = (df['es_ocupado'] * df['peso_trimestral']).sum()
    pob_desocupada_est = (df['es_desocupado'] * df['peso_trimestral']).sum()
    pob_subocupada_est = (df['es_subocupado'] * df['peso_trimestral']).sum()
    
    tasa_desocupacion_pond = (pob_desocupada_est / pob_pea_estimada) * 100
    tasa_subocupacion_pond = (pob_subocupada_est / pob_ocupada_est) * 100
    
    print(f"[OK] Verificación matemática superada con éxito:")
    print(f"  - Muestra muestral n: {len(df):,} jóvenes en la PEA urbana")
    print(f"  - Población PEA estimada: {pob_pea_estimada:,.0f} personas")
    print(f"  - Población Ocupada estimada: {pob_ocupada_est:,.0f} personas")
    print(f"  - Población Desocupada estimada: {pob_desocupada_est:,.0f} personas")
    print(f"  - Tasa de Desocupación Ponderada: {tasa_desocupacion_pond:.2f}% (Meta oficial: 3.7%)")
    print(f"  - Tasa de Subocupación Ponderada: {tasa_subocupacion_pond:.2f}% (Meta oficial: 8.7%)")
    return True

def procesar_pipeline():
    """Ejecuta el pipeline completo de preparación de datos."""
    df_raw = cargar_microdatos_crudos()
    df_filtrado = filtrar_universo_estudio(df_raw)
    df_procesado = transformar_y_recodificar(df_filtrado)
    validar_consistencia(df_procesado)
    
    print(f"[INFO] Exportando dataset procesado a: {DATA_PROCESSED_CSV}")
    DATA_PROCESSED_CSV.parent.mkdir(parents=True, exist_ok=True)
    df_procesado.to_csv(DATA_PROCESSED_CSV, index=False, sep=';', encoding='utf-8-sig')
    print(f"[OK] Archivo guardado con éxito ({DATA_PROCESSED_CSV.stat().st_size / (1024*1024):.2f} MB).")

if __name__ == "__main__":
    procesar_pipeline()
