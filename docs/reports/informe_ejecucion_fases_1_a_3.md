# INFORME TÉCNICO DE EJECUCIÓN Y RESULTADOS (FASES 1 A 3)
## Proyecto: Análisis de los Factores Asociados a la Desocupación en Jóvenes de 16 a 28 Años en Bolivia (ECE 4T-2025)

---

### Metadatos Académicos e Institucionales
- **Programa:** Diplomado en Data Science — Versión I
- **Institución:** Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX)
- **Unidad de Posgrado:** Centro de Estudios de Posgrado e Investigación (CEPI) — Vicerrectorado
- **Investigador / Autor:** Franz Reinaldo Gonzales Suyo
- **Docente Coordinador:** Ing. Marcelo Arancibia
- **Sede y Gestión:** Sucre - Bolivia, 2026
- **Entregable Metodológico:** Documento Técnico de Cierre de Fases 1, 2 y 3 (CRISP-DM)

---

## 1. RESUMEN EJECUTIVO

En cumplimiento del plan técnico aprobado y bajo los estándares de rigor científico del CEPI, se ejecutó integralmente la implementación de las **Fases 1 a 3** de la metodología CRISP-DM para el análisis estadístico de la desocupación juvenil urbana en Bolivia, utilizando la base oficial de microdatos de la **Encuesta Continua de Empleo (ECE) del 4to Trimestre de 2025**, provista por el Instituto Nacional de Estadística (INE).

### Hitos Técnicos Consolidados:
1. **Fase 1 (Comprensión y Preparación de Datos):** Procesamiento de la base bruta de **52.650 registros** y delimitación estricta al universo muestral juvenil urbano de la PEA (**6.649 registros**), expandido mediante el ponderador trimestral `fact_trim_act` a **1.380.841 jóvenes**.
2. **Fase 2 (Análisis Descriptivo Univariado Ponderado):** Replicación exacta y validación de los macroindicadores del Boletín Oficial del INE:
   - **Tasa de Desocupación Juvenil:** **3,71%** (Meta oficial INE: **3,7%**).
   - **Tasa de Subocupación Juvenil:** **8,70%** (Meta oficial INE: **8,7%**).
   - **Tasa General Urbana (referencia):** **2,30%** (Sobrerrepresentación juvenil: 1,6 veces la tasa general).
3. **Fase 3 (Análisis Bivariado y Contraste de Hipótesis de Asociación):**
   - **Segmentación Etaria:** Pico de desocupación en el tramo **18 a 20 años** con **4,65%** ($\chi^2 = 11,2332; p = 0,0105$, estadísticamente significativa).
   - **Brecha de Género:** Desocupación en mujeres del **4,69%** frente al **2,85%** en varones (+1,84 pp; $\chi^2 = 5,2367; p = 0,0221$, estadísticamente significativa).
   - **Heterogeneidad Territorial:** Chuquisaca encabeza la desocupación nacional con **5,80%**, seguida por Tarija (**4,72%**) y Cochabamba (**4,71%**) ($\chi^2 = 23,6920; p = 0,0026$, estadísticamente significativa).
   - **Paradoja del Desempleo Ilustrado:** Los jóvenes desocupados presentan un promedio ponderado de escolaridad mayor (**13,01 años**) que los ocupados (**12,64 años**), con diferencia estadísticamente significativa ($t = -2,39; p = 0,0174$; Mann-Whitney $U = 714.498,5; p = 0,0293$).
4. **Entregables de Código y Artefactos:**
   - Módulos modulares en Python: `src/config.py`, `src/data_processing.py`, `src/statistical_analysis.py`, `src/visualization.py`.
   - Dataset procesado y validado: `data/processed/ECE_4T2025_Jovenes_PEA.csv` (3,89 MB).
   - Catálogo de **13 tablas estadísticas** exportadas a `outputs/tables/`.
   - Catálogo de **10 figuras analíticas a 300 DPI** exportadas a `outputs/figures/`.
   - Cuaderno maestro reproducible `Proyecto-Final.ipynb` estructurado en 8 bloques CRISP-DM con **28 celdas** ejecutadas al 100%.
   - Verificación de calidad: **10/10 pruebas QA superadas exitosamente**.

---

## 2. ARQUITECTURA TÉCNICA Y TRAZABILIDAD METODOLÓGICA (CRISP-DM)

El desarrollo del proyecto se ejecutó respetando la estructura estándar de Ciencia de Datos:

```text
Proyecto-Final-Data-Science/
├── Proyecto-Final.ipynb                        # Cuaderno maestro CRISP-DM con salidas persistidas
├── data/
│   ├── raw/ECE_4T2025.csv                      # Microdatos originales inalterados (52.650 filas x 121 vars)
│   └── processed/ECE_4T2025_Jovenes_PEA.csv    # Microdatos limpios y filtrados (6.649 filas x 156 vars)
├── outputs/
│   ├── figures/                                # Catálogo de 10 figuras a 300 DPI (PNG)
│   ├── tables/                                 # 13 tablas estadísticas oficiales (CSV delimitado por ;)
│   └── reports/                                # Informe técnico de ejecución (Markdown)
├── src/
│   ├── config.py                               # Configuración de rutas, diccionarios y paleta USFX
│   ├── data_processing.py                      # Pipeline ETL y validación matemática
│   ├── statistical_analysis.py                 # Motor de tasas ponderadas, Chi2, Cramér y t-test
│   └── visualization.py                        # Generador de gráficos de alta resolución (300 DPI)
└── scratch/
    ├── build_master_notebook.py                # Script de compilación y ejecución headless del notebook
    └── run_qa_checks.py                        # Suite de validación de 10 aserciones de consistencia
```

---

## 3. DETALLE DE RESULTADOS OBTENIDOS POR FASE

### 3.1. Fase 1: Ingesta, Filtrado y Curaduría de Microdatos

1. **Fuente de Microdatos:** Archivo `ECE_4T2025.csv` con separador de listas `;` y codificación `latin1`.
2. **Criterios de Delimitación Muestral:**
   - **Área Geográfica:** `area == 1` (Bolivia urbana).
   - **Rango Etario (Ley N.º 342):** `16 <= s1_03a <= 28` años cumplidos.
   - **Condición Económica:** `pea == 1` (Pertenencia a la Población Económicamente Activa).
3. **Tratamiento del Factor de Expansión:** La variable `fact_trim_act` poseía coma decimal como separador textual (`"207,52"`). Se realizó la conversión estricta a tipo `float64` (`207.52`), validando que ningún factor sea nulo o menor o igual a cero.
4. **Dimensiones Validadas:**
   - Registros de la encuesta cruda: **52.650 encuestados**.
   - Muestra efectiva analizada ($n$): **6.649 jóvenes**.
   - Población juvenil urbana expandida ($N$): **1.380.841 habitantes**.

---

### 3.2. Fase 2: Análisis Descriptivo Univariado Ponderado

Toda estimación se calculó aplicando de manera inquebrantable el ponderador trimestral del diseño muestral estratificado y por conglomerados de la ECE:

$$\text{Tasa Ponderada (\%)} = \frac{\sum_{i=1}^n (\text{Target}_i \times \text{Ponderador}_i)}{\sum_{i=1}^n \text{Ponderador}_i} \times 100$$

#### TABLA 1: Balance Macro de Población y Tasas Ponderadas (Línea Base INE)
*Archivo exportado:* `outputs/tables/tabla_desocupacion_macro.csv`

| Indicador Sociolaboral | Casos Muestra ($n$) | Población Expandida ($N$) | Tasa / Proporción (%) | Meta Oficial Boletín INE |
| :--- | :---: | :---: | :---: | :---: |
| **PEA Juvenil Urbana (16-28 años)** | 6.649 | 1.380.841 | 100,00% | Universo de referencia |
| **Población Ocupada Juvenil** | 6.406 | 1.329.645 | 96,29% | Línea base oficial |
| **Población Desocupada Juvenil** | 243 | 51.196 | **3,71%** | **3,7%** |
| **Tasa de Subocupación Juvenil** | 567 | 115.736 | **8,70%** | **8,7%** |
| **Desocupados Cesantes (Con experiencia)** | 215 | 45.882 | 89,62% | Mayoritarios |
| **Desocupados Aspirantes (Primer empleo)** | 28 | 5.314 | 10,38% | Minoritarios |

> **Validación:** El modelo algorítmico replica con absoluta precisión las estimaciones publicadas por el INE para el 4T-2025.

---

### 3.3. Fase 3: Análisis Bivariado y Contraste de Hipótesis de Asociación

Se aplicaron pruebas de **Independencia Chi-cuadrado de Pearson ($\chi^2$)** con un nivel de significancia $\alpha = 0,05$ y el cálculo del coeficiente de tamaño del efecto **V de Cramér ($V$)**:

$$V = \sqrt{\frac{\chi^2}{N \times \min(r - 1, c - 1)}}$$

#### TABLA 2: Matriz Sintética de Pruebas de Hipótesis de Asociación Bivariada
*Archivo exportado:* `outputs/tables/tabla_pruebas_chi2_cramer.csv`

| Dimensión Evaluada | Variable ECE | Muestra ($n$) | $\chi^2$ Pearson | Grados Lib. | $p$-valor | $V$ Cramér | Interpretación / Decisión |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Tramo Etario** | `grupo_edad` | 6.649 | 11,2332 | 3 | **0,01053** | 0,0411 | **Asociación Significativa** (Rechaza $H_0$) |
| **Sexo / Género** | `sexo` | 6.649 | 5,2367 | 1 | **0,02212** | 0,0281 | **Asociación Significativa** (Rechaza $H_0$) |
| **Departamento** | `departamento`| 6.649 | 23,6920 | 8 | **0,00258** | 0,0597 | **Asociación Significativa** (Rechaza $H_0$) |
| **Tipología de Hogar** | `tipo_hogar` | 6.649 | 17,4287 | 6 | **0,00783** | 0,0512 | **Asociación Significativa** (Rechaza $H_0$) |
| **Parentesco con Jefe** | `parentesco` | 6.649 | 17,2553 | 7 | **0,01584** | 0,0509 | **Asociación Significativa** (Rechaza $H_0$) |
| **Nivel Educativo** | `nivel_educativo`| 6.649 | 3,6356 | 4 | 0,45759 | 0,0234 | No significativa bivariada agregada |
| **Asistencia Educativa** | `asiste_estudio`| 6.649 | 1,5264 | 1 | 0,21666 | 0,0152 | No significativa bivariada agregada |

---

### 3.4. Desagregaciones Analíticas Clave

#### A. Segmentación Etaria
- **16 a 17 años:** Muestra $n=774$, PEA ponderada 159.899, Desocupados 2.991, **Tasa = 1,87%**.
- **18 a 20 años:** Muestra $n=1.377$, PEA ponderada 290.670, Desocupados 13.504, **Tasa = 4,65%** (Pico de máxima vulnerabilidad).
- **21 a 24 años:** Muestra $n=2.039$, PEA ponderada 414.829, Desocupados 14.713, **Tasa = 3,55%**.
- **25 a 28 años:** Muestra $n=2.459$, PEA ponderada 515.443, Desocupados 19.988, **Tasa = 3,88%**.

#### B. Brecha de Género
- **Varones:** Muestra $n=3.393$, PEA ponderada 735.643, Desocupados 20.938, **Tasa = 2,85%**.
- **Mujeres:** Muestra $n=3.256$, PEA ponderada 645.198, Desocupados 30.258, **Tasa = 4,69%**.
- **Brecha de Género:** **+1,84 puntos porcentuales** en perjuicio de las mujeres jóvenes. Aunque representan el 46,7% de la PEA juvenil, absorben el **59,1% del total de personas desocupadas**.

#### C. Ranking Departamental
1. **Chuquisaca:** **5,80%** (PEA: 62.899 hab.; Desocupados: 3.648 hab.) — *Región de mayor desocupación*.
2. **Tarija:** **4,72%** (PEA: 57.856 hab.; Desocupados: 2.728 hab.).
3. **Cochabamba:** **4,71%** (PEA: 251.505 hab.; Desocupados: 11.840 hab.).
4. **La Paz:** **3,84%** (PEA: 338.688 hab.; Desocupados: 13.016 hab.).
5. **Santa Cruz:** **3,33%** (PEA: 459.615 hab.; Desocupados: 15.313 hab.).
6. **Oruro:** **2,98%** (PEA: 67.935 hab.; Desocupados: 2.027 hab.).
7. **Beni:** **2,07%** (PEA: 60.886 hab.; Desocupados: 1.259 hab.).
8. **Pando:** **1,89%** (PEA: 11.079 hab.; Desocupados: 210 hab.).
9. **Potosí:** **1,64%** (PEA: 70.378 hab.; Desocupados: 1.155 hab.).

#### D. Análisis Educativo y "Paradoja del Desempleo Ilustrado"
- **Tasa por Nivel de Instrucción:**
  - Sin instrucción: **2,31%**
  - Primaria: **3,43%**
  - Secundaria: **4,02%**
  - Superior Universitario: **4,04%**
- **Contraste de Años de Estudio (Escolaridad Acumulada):**
  - Jóvenes Ocupados: Media ponderada = **12,64 años**.
  - Jóvenes Desocupados: Media ponderada = **13,01 años** (+0,37 años de formación).
  - Prueba $t$ de Student: $t = -2,39; p = 0,0174$ (Diferencia significativa al 5%).
  - Prueba Mann-Whitney $U$: $U = 714.498,5; p = 0,0293$ (Diferencia significativa al 5%).
- **Diagnóstico Económico:** En el área urbana boliviana, una mayor acumulación educativa no inmuniza al joven frente al desempleo abierto; por el contrario, los jóvenes con más educación prolongan su tiempo de búsqueda hacia empleos profesionales calificados y formales, mientras que los jóvenes con menor instrucción se ven obligados a autoemplearse rápidamente en actividades precarias e informales de subsistencia.

#### E. Estructura y Mecanismos de Búsqueda de Empleo
- **Historial Laboral:** **89,6% Cesantes** (pérdida o fin de empleo) vs. **10,4% Aspirantes** (primer empleo).
- **Canales de Búsqueda Utilizados:**
  1. Avisos por prensa, internet o redes sociales: **38,8%**
  2. Presentación directa de solicitudes o currículum vitae: **31,6%**
  3. Otra forma de búsqueda: **17,6%**
  4. Preguntó directamente en lugares de trabajo: **7,7%**
  5. Consultó a amigos o parientes: **2,3%**
  6. Gestiones para negocio por cuenta propia: **1,1%**
  7. No aplica / No declaró: **0,9%**

---

## 4. INVENTARIO DE ARTEFACTOS Y ARCHIVOS GENERADOS

### 4.1. Catálogo de Tablas Estadísticas (`outputs/tables/`)
1. `tabla_desocupacion_macro.csv`: Macroindicadores de línea base INE.
2. `tabla_desocupacion_grupo_edad.csv`: Indicadores por los 4 tramos etarios.
3. `tabla_desocupacion_sexo.csv`: Indicadores de brecha de género.
4. `tabla_desocupacion_departamento.csv`: Indicadores por los 9 departamentos.
5. `tabla_desocupacion_nivel_educativo.csv`: Tasas según nivel de instrucción.
6. `tabla_desocupacion_asiste_estudio.csv`: Tasas según asistencia escolar.
7. `tabla_desocupacion_tipo_condicion_laboral.csv`: Cesantes vs Aspirantes.
8. `tabla_desocupacion_tipo_hogar.csv`: Tasas según tipología familiar.
9. `tabla_desocupacion_parentesco.csv`: Tasas según posición intrahogar.
10. `tabla_desocupados_cesantes_por_ocupacion.csv`: Grupos ocupacionales previos.
11. `tabla_desocupados_mecanismo_busqueda.csv`: Métodos de búsqueda de empleo.
12. `tabla_comparativa_escolaridad.csv`: Comparativa paramétrica y no paramétrica de escolaridad.
13. `tabla_pruebas_chi2_cramer.csv`: Matriz consolidada de contrastes de independencia $\chi^2$ y V de Cramér.

### 4.2. Catálogo de Figuras Editoriales a 300 DPI (`outputs/figures/`)
1. `figura_1_desocupacion_general_vs_juvenil.png`: Comparación general (2,30%) vs juvenil (3,71%).
2. `figura_2_desocupacion_por_tramo_etario.png`: Barras por tramo etario con resalte en 18-20 años.
3. `figura_3_brecha_genero.png`: Brecha gráfica de género con anotación formal (+1,84 pp).
4. `figura_4_desocupacion_por_departamento.png`: Ranking horizontal de los 9 departamentos y promedio nacional.
5. `figura_5_cesantes_vs_aspirantes.png`: Gráfico tipo dona de historial laboral (89,6% vs 10,4%).
6. `figura_6_desocupacion_por_nivel_educativo.png`: Barras de tasas según nivel de instrucción formal.
7. `figura_7_desocupacion_asiste_estudio.png`: Barras según asistencia o no asistencia educativa.
8. `figura_8_distribucion_anios_estudio.png`: Panel dual Boxplot + KDE ponderado de años de escolaridad.
9. `figura_9_mecanismos_busqueda.png`: Barras horizontales de canales de intermediación laboral.
10. `figura_10_desocupacion_tipo_hogar.png`: Barras por estructura tipológica familiar.

### 4.3. Cuaderno Maestro Ejecutado (`Proyecto-Final.ipynb`)
- **Total Celdas:** 28 celdas (15 Markdown + 13 Código Python).
- **Ejecución Automatizada:** Procesado íntegramente mediante `nbclient` en Python 3.14.7.
- **Salidas Persistidas:** Todas las celdas cuentan con sus outputs embebidos, tablas formateadas y gráficos interactivos visibles.

---

## 5. AUDITORÍA DE CALIDAD Y ASERCIONES CIENTÍFICAS (QA)

| Código | Dimensión Auditada | Expresión Matemática / Aserción | Resultado Obtenido | Estado |
| :---: | :--- | :--- | :---: | :---: |
| **QA-01** | Cobertura Muestral | $n = \text{len}(df) == 6.649$ | $6.649$ encuestados | **SUPERADO** |
| **QA-02** | Expansión Poblacional | $N = \sum \text{peso\_trimestral} == 1.380.841$ | $1.380.841$ habitantes | **SUPERADO** |
| **QA-03** | Tasa Desocupación | $\text{Tasa} = (\sum \text{pead} \cdot w / \sum w) \times 100 \approx 3,7\%$ | **3,71%** | **SUPERADO** |
| **QA-04** | Tasa Subocupación | $\text{Suboc} = (\sum \text{psub} \cdot w / \sum \text{peao} \cdot w) \times 100 \approx 8,7\%$ | **8,70%** | **SUPERADO** |
| **QA-05** | Consistencia Aditiva | $\text{Ocupados} + \text{Desocupados} = \text{PEA}$ | $1.329.645 + 51.196 = 1.380.841$ | **SUPERADO** |
| **QA-06** | Consistencia Desocupación | $\text{Cesantes} + \text{Aspirantes} = \text{Desocupados}$ | $45.882 + 5.314 = 51.196$ | **SUPERADO** |
| **QA-07** | Inferencia de Género | $\chi^2(\text{sexo}) > 3,841 \land p < 0,05$ | $\chi^2 = 5,2367; p = 0,0221$ | **SUPERADO** |
| **QA-08** | Inferencia Etaria | $\chi^2(\text{edad}) > 7,815 \land p < 0,05$ | $\chi^2 = 11,2332; p = 0,0105$ | **SUPERADO** |
| **QA-09** | Inferencia Territorial | $\chi^2(\text{depto}) > 15,507 \land p < 0,05$ | $\chi^2 = 23,6920; p = 0,0026$ | **SUPERADO** |
| **QA-10** | Paradoja Educativa | $\bar{X}_{\text{desoc}} > \bar{X}_{\text{ocup}} \land p_{\text{t-test}} < 0,05$ | $13,01 > 12,64; p = 0,0174$ | **SUPERADO** |

---

## 6. PREPARACIÓN Y TRANSICIÓN HACIA LA FASE 4 (POWER BI)

Con la culminación rigurosa de las Fases 1 a 3, el proyecto cuenta con los insumos óptimos para la construcción del reporte de Business Intelligence en **Power BI**:

1. **Dataset Limpio:** `data/processed/ECE_4T2025_Jovenes_PEA.csv` contiene 156 columnas (claves primarias, indicadores booleanos, diccionarios textuales descriptivos y el ponderador muestral).
2. **Modelo Dimensional Star Schema Definido:**
   - Tabla de Hechos: `Fact_MercadoLaboralJuvenil` (6.649 filas).
   - Tablas de Dimensiones: `Dim_Tiempo`, `Dim_Geografia`, `Dim_Demografia`, `Dim_Educacion`, `Dim_CondicionLaboral`, `Dim_Hogar`.
3. **Catálogo de Medidas DAX Ponderadas:** Diseñadas para operar con `SUMX` y `DIVIDE` sobre `peso_trimestral` (garantizando consistencia total con los cálculos de Python).
4. **Arquitectura del Dashboard (6 Páginas):**
   - Página 1: Panorama Laboral Juvenil
   - Página 2: Desocupación por Tramo Etario
   - Página 3: Educación y Desocupación
   - Página 4: Brechas de Género y Territorio
   - Página 5: Perfil del Joven Desocupado
   - Página 6: Hallazgos y Recomendaciones

---

*Firma del Investigador:*  
**Franz Reinaldo Gonzales Suyo**  
Postgraduante — Diplomado en Data Science  
Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca  
Sucre, Bolivia — 2026
