"""
Script de Auditoría y Verificación de Calidad (QA-01 a QA-10)
Verifica rigurosamente todas las aserciones numéricas y estadísticas
del proyecto antes de emitir el informe final.
"""
import sys
from pathlib import Path
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind, mannwhitneyu

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def run_qa_checks():
    data_path = Path("data/processed/ECE_4T2025_Jovenes_PEA.csv")
    assert data_path.exists(), "Falta el archivo procesado."
    
    df = pd.read_csv(data_path, sep=';', encoding='utf-8-sig')
    
    print("=" * 70)
    print("AUDITORÍA DE CONTROL DE CALIDAD Y CONSISTENCIA CIENTÍFICA")
    print("=" * 70)
    
    # QA-01
    n_obs = len(df)
    assert n_obs == 6649, f"QA-01 Fallido: n = {n_obs} != 6649"
    print(f"✓ QA-01 Aprobado: Tamaño de muestra juvenil urbana n = {n_obs:,}")
    
    # QA-02
    pob_pea = df['peso_trimestral'].sum()
    assert round(pob_pea) == 1380841, f"QA-02 Fallido: N = {round(pob_pea)} != 1380841"
    print(f"✓ QA-02 Aprobado: Población expandida PEA N = {round(pob_pea):,}")
    
    # QA-03
    pob_desoc = (df['es_desocupado'] * df['peso_trimestral']).sum()
    tasa_desoc = (pob_desoc / pob_pea) * 100
    assert abs(tasa_desoc - 3.7075) < 0.05, f"QA-03 Fallido: Tasa = {tasa_desoc:.2f}%"
    print(f"✓ QA-03 Aprobado: Tasa de Desocupación = {tasa_desoc:.2f}% (Meta oficial: 3.7%)")
    
    # QA-04
    pob_ocup = (df['es_ocupado'] * df['peso_trimestral']).sum()
    pob_suboc = (df['es_subocupado'] * df['peso_trimestral']).sum()
    tasa_suboc = (pob_suboc / pob_ocup) * 100
    assert abs(tasa_suboc - 8.704) < 0.05, f"QA-04 Fallido: Tasa subocupación = {tasa_suboc:.2f}%"
    print(f"✓ QA-04 Aprobado: Tasa de Subocupación = {tasa_suboc:.2f}% (Meta oficial: 8.7%)")
    
    # QA-05
    assert (df['es_ocupado'] + df['es_desocupado'] == df['pea_val']).all(), "QA-05 Fallido en registros individuales"
    assert round(pob_ocup + pob_desoc) == round(pob_pea), "QA-05 Fallido en suma ponderada"
    print(f"✓ QA-05 Aprobado: Consistencia aditiva Ocupados ({round(pob_ocup):,}) + Desocupados ({round(pob_desoc):,}) = PEA ({round(pob_pea):,})")
    
    # QA-06
    pob_ces = (df['es_cesante'] * df['peso_trimestral']).sum()
    pob_asp = (df['es_aspirante'] * df['peso_trimestral']).sum()
    assert round(pob_ces + pob_asp) == round(pob_desoc), "QA-06 Fallido en cesantes + aspirantes"
    prop_ces = pob_ces / pob_desoc * 100
    prop_asp = pob_asp / pob_desoc * 100
    print(f"✓ QA-06 Aprobado: Desocupados = Cesantes ({prop_ces:.1f}%) + Aspirantes ({prop_asp:.1f}%)")
    
    # QA-07
    ct_sexo = pd.crosstab(df['sexo'], df['es_desocupado'])
    chi2_s, p_s, _, _ = chi2_contingency(ct_sexo)
    assert p_s < 0.05, f"QA-07 Fallido: p_s = {p_s}"
    print(f"✓ QA-07 Aprobado: Brecha de género estadísticamente significativa (Chi2 = {chi2_s:.4f}, p = {p_s:.5f} < 0.05)")
    
    # QA-08
    ct_edad = pd.crosstab(df['grupo_edad'], df['es_desocupado'])
    chi2_e, p_e, _, _ = chi2_contingency(ct_edad)
    assert p_e < 0.05, f"QA-08 Fallido: p_e = {p_e}"
    print(f"✓ QA-08 Aprobado: Tramos etarios estadísticamente significativos (Chi2 = {chi2_e:.4f}, p = {p_e:.5f} < 0.05)")
    
    # QA-09
    ct_depto = pd.crosstab(df['departamento'], df['es_desocupado'])
    chi2_d, p_d, _, _ = chi2_contingency(ct_depto)
    assert p_d < 0.05, f"QA-09 Fallido: p_d = {p_d}"
    print(f"✓ QA-09 Aprobado: Heterogeneidad departamental estadísticamente significativa (Chi2 = {chi2_d:.4f}, p = {p_d:.5f} < 0.05)")
    
    # QA-10
    df_ocu_e = df[df['es_ocupado'] == 1].dropna(subset=['anios_estudio'])
    df_des_e = df[df['es_desocupado'] == 1].dropna(subset=['anios_estudio'])
    m_ocu = (df_ocu_e['anios_estudio'] * df_ocu_e['peso_trimestral']).sum() / df_ocu_e['peso_trimestral'].sum()
    m_des = (df_des_e['anios_estudio'] * df_des_e['peso_trimestral']).sum() / df_des_e['peso_trimestral'].sum()
    t_stat, p_t = ttest_ind(df_ocu_e['anios_estudio'], df_des_e['anios_estudio'], equal_var=False)
    assert m_des > m_ocu, "QA-10 Fallido: Desocupados no tienen más escolaridad"
    assert p_t < 0.05, f"QA-10 Fallido: Diferencia de escolaridad no es significativa (p = {p_t})"
    print(f"✓ QA-10 Aprobado: Paradoja educativa confirmada (Desocupados {m_des:.2f} años vs Ocupados {m_ocu:.2f} años, t = {t_stat:.2f}, p = {p_t:.4f})")
    
    print("=" * 70)
    print("RESULTADO GLOBAL: 10/10 PRUEBAS QA SUPERADAS CON ÉXITO")
    print("=" * 70)

if __name__ == "__main__":
    run_qa_checks()
