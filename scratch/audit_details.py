import json, pandas as pd, glob

# 1. Check notebook execution and outputs
nb = json.load(open('Proyecto-Final.ipynb', encoding='utf-8'))
print("=== NOTEBOOK CELLS EXECUTION ===")
for i, c in enumerate(nb['cells']):
    if c['cell_type'] == 'code':
        outs = c.get('outputs', [])
        errs = [o for o in outs if o.get('output_type') == 'error']
        print(f"Cell {i}: exec_count={c.get('execution_count')}, outputs={len(outs)}, errors={len(errs)}")
        for o in outs:
            if o.get('output_type') == 'stream':
                txt = ''.join(o.get('text', []))
                for line in txt.splitlines():
                    if any(k in line for k in ['1,', '3.7', '8.7', '533', '567', '13.0', '12.6', 't =', 'U =', '51,196', '115,73']):
                        print("   OUT:", line)

# 2. Check sample counts of desocupados by sexo, edad, depto from stripped processed CSV
df = pd.read_csv('data/processed/ECE_4T2025_Jovenes_PEA.csv', sep=';')
df.columns = df.columns.str.strip()
for col in df.select_dtypes(include='str').columns:
    df[col] = df[col].str.strip()

print("\n=== ACTUAL DATASET EXACT NUMBERS ===")
for dim in ['sexo', 'grupo_edad', 'departamento', 'nivel_educativo']:
    sub = df[df['es_desocupado'] == 1].groupby(dim).agg(
        n_desoc=('es_desocupado', 'sum'),
        N_desoc=('peso_trimestral', 'sum')
    )
    print(f"-- {dim} (desocupados) --")
    print(sub)

# 3. Check 12.64 vs 12.38 and 567 vs 533 in docs/
for md_path in ['docs/GonzalesSuyo_Franz_ActividadNº1.md', 'docs/Proyecto_Monografia_Data_Science_Desocupacion_Juvenil_Bolivia.docx.md']:
    txt = open(md_path, encoding='utf-8').read()
    print(f"\n=== {md_path} ===")
    for kw in ['567', '533', '12,38', '12,64', '2,22%', '2,98%', '19.645', '20.848', '38,82%', '41,4%', '40,72%', '708.200', '714.498', '0,0174', '0,0202', '36 medidas', '20 Medidas', '8,63', '4,53', 'Franz Gonzales', 'tt-Student']:
        cnt = txt.count(kw)
        if cnt > 0:
            print(f"  '{kw}': {cnt} times")
