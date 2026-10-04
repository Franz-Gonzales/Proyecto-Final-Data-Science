"""
Script para actualizar y enriquecer _Medidas.tmdl en el Semantic Model de Power BI.
Añade todas las medidas analíticas y alias requeridos para garantizar cero errores en Power BI Desktop.
"""

import os
import uuid

TMDL_PATH = "powerbi/Visualizacion-Analisis-Desocupacion.SemanticModel/definition/tables/_Medidas.tmdl"

NEW_MEASURES = [
    {
        "name": "Brecha Desocupacion Genero",
        "expr": "[Tasa Desocupacion Mujeres] - [Tasa Desocupacion Hombres]",
        "format": "+0.00%;-0.00%",
        "folder": "03_Brechas_Genero_Territorio",
        "tag": "a1b2c3d4-0001-4000-8000-000000000001"
    },
    {
        "name": "Tasa Desocupacion Chuquisaca",
        "expr": "CALCULATE([Tasa Desocupacion Ponderada], 'Dim_Departamento'[departamento] = \"Chuquisaca\")",
        "format": "0.00%",
        "folder": "03_Brechas_Genero_Territorio",
        "tag": "a1b2c3d4-0002-4000-8000-000000000002"
    },
    {
        "name": "Escolaridad Promedio Desocupados",
        "expr": "[Anios Estudio Promedio Desocupados]",
        "format": "0.00",
        "folder": "04_Educacion_Escolaridad",
        "tag": "a1b2c3d4-0003-4000-8000-000000000003"
    },
    {
        "name": "Escolaridad Promedio Ocupados",
        "expr": "[Anios Estudio Promedio Ocupados]",
        "format": "0.00",
        "folder": "04_Educacion_Escolaridad",
        "tag": "a1b2c3d4-0004-4000-8000-000000000004"
    },
    {
        "name": "Brecha Escolaridad Meses",
        "expr": "([Anios Estudio Promedio Desocupados] - [Anios Estudio Promedio Ocupados]) * 12",
        "format": "+0.0;-0.0",
        "folder": "04_Educacion_Escolaridad",
        "tag": "a1b2c3d4-0005-4000-8000-000000000005"
    },
    {
        "name": "Proporcion Cesantes Pct",
        "expr": "[Porcentaje Desocupados Cesantes]",
        "format": "0.00%",
        "folder": "05_Trayectoria_Busqueda",
        "tag": "a1b2c3d4-0006-4000-8000-000000000006"
    },
    {
        "name": "Proporcion Aspirantes Pct",
        "expr": "[Porcentaje Desocupados Aspirantes]",
        "format": "0.00%",
        "folder": "05_Trayectoria_Busqueda",
        "tag": "a1b2c3d4-0007-4000-8000-000000000007"
    },
    {
        "name": "Presion Total Empleo",
        "expr": "[Tasa Desocupacion Ponderada] + [Tasa Subocupacion Ponderada]",
        "format": "0.00%",
        "folder": "02_Tasas_Analiticas",
        "tag": "a1b2c3d4-0008-4000-8000-000000000008"
    },
    {
        "name": "Tasa Desocupacion 18 a 20",
        "expr": "CALCULATE([Tasa Desocupacion Ponderada], 'Dim_GrupoEdad'[grupo_edad] = \"18 a 20 años\")",
        "format": "0.00%",
        "folder": "02_Tasas_Analiticas",
        "tag": "a1b2c3d4-0009-4000-8000-000000000009"
    },
    {
        "name": "Desocupados 18 a 20 Anios",
        "expr": "CALCULATE([Poblacion Desocupada], 'Dim_GrupoEdad'[grupo_edad] = \"18 a 20 años\")",
        "format": "#,##0",
        "folder": "01_Volumenes_Poblacionales",
        "tag": "a1b2c3d4-0010-4000-8000-000000000010"
    },
    {
        "name": "Desocupados 25 a 28 Anios",
        "expr": "CALCULATE([Poblacion Desocupada], 'Dim_GrupoEdad'[grupo_edad] = \"25 a 28 años\")",
        "format": "#,##0",
        "folder": "01_Volumenes_Poblacionales",
        "tag": "a1b2c3d4-0011-4000-8000-000000000011"
    },
    {
        "name": "Mujeres Desocupadas",
        "expr": "CALCULATE([Poblacion Desocupada], 'Dim_Sexo'[sexo] = \"Mujer\")",
        "format": "#,##0",
        "folder": "01_Volumenes_Poblacionales",
        "tag": "a1b2c3d4-0012-4000-8000-000000000012"
    },
    {
        "name": "Tasa Desocupacion Secundaria",
        "expr": "CALCULATE([Tasa Desocupacion Ponderada], 'Dim_NivelEducativo'[nivel_educativo] = \"Secundaria\")",
        "format": "0.00%",
        "folder": "04_Educacion_Escolaridad",
        "tag": "a1b2c3d4-0013-4000-8000-000000000013"
    },
    {
        "name": "Tasa Desocupacion Superior Universitario",
        "expr": "CALCULATE([Tasa Desocupacion Ponderada], 'Dim_NivelEducativo'[nivel_educativo] = \"Superior Universitario\")",
        "format": "0.00%",
        "folder": "04_Educacion_Escolaridad",
        "tag": "a1b2c3d4-0014-4000-8000-000000000014"
    },
    {
        "name": "Desocupados Aspirantes 18 a 20",
        "expr": "CALCULATE([Desocupados Aspirantes], 'Dim_GrupoEdad'[grupo_edad] = \"18 a 20 años\")",
        "format": "#,##0",
        "folder": "05_Trayectoria_Busqueda",
        "tag": "a1b2c3d4-0015-4000-8000-000000000015"
    },
    {
        "name": "Porcentaje Desocupados Aspirantes 18 a 20",
        "expr": "DIVIDE([Desocupados Aspirantes 18 a 20], [Desocupados Aspirantes], 0)",
        "format": "0.00%",
        "folder": "05_Trayectoria_Busqueda",
        "tag": "a1b2c3d4-0016-4000-8000-000000000016"
    }
]

def update_tmdl():
    with open(TMDL_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Identificar la sección donde terminan las medidas (antes de "column Indice")
    split_marker = "\tcolumn Indice"
    if split_marker not in content:
        raise ValueError("No se encontró 'column Indice' en _Medidas.tmdl")
        
    parts = content.split(split_marker)
    measures_section = parts[0]
    tail_section = split_marker + parts[1]
    
    # Comprobar qué medidas ya existen para evitar duplicados
    added_count = 0
    for m in NEW_MEASURES:
        measure_header = f"measure '{m['name']}'"
        if measure_header not in measures_section:
            snippet = f"\tmeasure '{m['name']}' = {m['expr']}\n"
            snippet += f"\t\tformatString: {m['format']}\n"
            snippet += f"\t\tdisplayFolder: {m['folder']}\n"
            snippet += f"\t\tlineageTag: {m['tag']}\n\n"
            measures_section += snippet
            added_count += 1
            print(f"[+] Añadida medida: '{m['name']}'")
        else:
            print(f"[-] Ya existe medida: '{m['name']}'")
            
    updated_content = measures_section + tail_section
    with open(TMDL_PATH, "w", encoding="utf-8") as f:
        f.write(updated_content)
        
    print(f"\n[OK] _Medidas.tmdl actualizado con éxito. Medidas añadidas: {added_count}")

if __name__ == "__main__":
    update_tmdl()
