import pandas as pd, numpy as np, json, glob
from scipy.stats import chi2_contingency, mannwhitneyu, ttest_ind

df_raw = pd.read_csv('data/raw/ECE_4T2025.csv', sep=';', encoding='latin1', low_memory=False)
df_raw['area_num'] = pd.to_numeric(df_raw['area'], errors='coerce').fillna(0).astype(int)
df_raw['edad_num'] = pd.to_numeric(df_raw['s1_03a'], errors='coerce').fillna(0).astype(int)
df_raw['pea_num'] = pd.to_numeric(df_raw['pea'], errors='coerce').fillna(0).astype(int)
df_raw['peso'] = df_raw['fact_trim_act'].astype(str).str.replace(',', '.').astype(float)

df_urb14 = df_raw[(df_raw['area_num']==1) & (df_raw['edad_num']>=14) & (df_raw['pea_num']==1)]
pead_gen = pd.to_numeric(df_urb14['pead'], errors='coerce').fillna(0)
tasa_gen = (pead_gen * df_urb14['peso']).sum() / df_urb14['peso'].sum() * 100
print(f"Tasa general urbana 14+: {tasa_gen:.4f}% (n={len(df_urb14)})")

df_j = df_raw[(df_raw['area_num']==1) & (df_raw['edad_num']>=16) & (df_raw['edad_num']<=28) & (df_raw['pea_num']==1)].copy()
df_j['psub'] = pd.to_numeric(df_j['psubocup'], errors='coerce').fillna(0).astype(int)
df_j['pead_v'] = pd.to_numeric(df_j['pead'], errors='coerce').fillna(0).astype(int)
df_j['peao_v'] = pd.to_numeric(df_j['peao'], errors='coerce').fillna(0).astype(int)
df_j['aest'] = pd.to_numeric(df_j['aestudio'], errors='coerce').fillna(0)
print(f"Jovenes PEA: n={len(df_j)}, PEA_N={df_j['peso'].sum():.1f}")
print(f"Subocupados raw filter: n={df_j['psub'].sum()}, N={(df_j['psub']*df_j['peso']).sum():.1f}")

for cond_name, sub in [('all', df_j), ('aest > 0', df_j[df_j['aest']>0])]:
    oc = sub[sub['peao_v']==1]
    de = sub[sub['pead_v']==1]
    m_oc = (oc['aest']*oc['peso']).sum()/oc['peso'].sum()
    m_de = (de['aest']*de['peso']).sum()/de['peso'].sum()
    t_s, p_t = ttest_ind(oc['aest'], de['aest'], equal_var=False)
    u_s, p_u = mannwhitneyu(oc['aest'], de['aest'], alternative='two-sided')
    print(f"Escolaridad [{cond_name}]: n_oc={len(oc)}, n_de={len(de)}, m_oc={m_oc:.4f}, m_de={m_de:.4f}, std_oc={oc['aest'].std():.4f}, std_de={de['aest'].std():.4f}, t={t_s:.4f} (p={p_t:.4f}), U={u_s:.1f} (p={p_u:.4f})")

# Check Power BI tables and measures
pbi_tables = sorted(glob.glob('powerbi/Visualizacion-Analisis-Desocupacion.SemanticModel/definition/tables/*.tmdl'))
print('PBI TMDL tables:', len(pbi_tables), [t.split('\\')[-1] for t in pbi_tables])
med_txt = open('powerbi/Visualizacion-Analisis-Desocupacion.SemanticModel/definition/tables/_Medidas.tmdl', encoding='utf-8').read()
print('PBI measure count:', med_txt.count('\tmeasure '))
pbi_pages = sorted(glob.glob('powerbi/Visualizacion-Analisis-Desocupacion.Report/definition/pages/*/visuals/*', recursive=True))
print('PBI visual count:', len(pbi_pages))
