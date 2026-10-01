# AGENTS.md — Directrices del Proyecto de Investigación y Desarrollo

## 1. Identificación del Proyecto y Datos Académicos

- **Título Oficial:** *Análisis de los factores asociados a la desocupación en jóvenes de 16 a 28 años en Bolivia*
- **Autor / Investigador:** Gonzales Suyo Franz Reinaldo
- **Institución:** Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX)
  - **Unidad de Posgrado:** Centro de Estudios de Posgrado e Investigación (CEPI) — Vicerrectorado
- **Programa Académico:** Diplomado en Data Science — Versión I
- **Docente / Coordinador:** Ing. Marcelo Arancibia
- **Sede y Gestión:** Sucre - Bolivia, 2026
- **Entregables Finales:**
  1. Monografía formal de posgrado (~50 páginas, formato Word según plantilla CEPI: `GonzalesSuyo_Franz_ActividadNº.docx`).
  2. Notebook reproducible (`Proyecto-Final.ipynb`).
  3. Tablero de Business Intelligence interactivo en Power BI (`.pbix`).
  4. Código modular y reproducible en Python (`src/`).

---

## 2. Propósito, Planteamiento del Problema y Objetivos

### 2.1. Planteamiento del Problema
¿Cuáles son los factores sociodemográficos, educativos, territoriales y de trayectoria laboral asociados a la desocupación de jóvenes de 16 a 28 años en el área urbana de Bolivia?

### 2.2. Delimitación y Población de Estudio
- **Ámbito Geográfico:** Área urbana de Bolivia.
- **Población Objetivo:** Personas entre 16 y 28 años cumplidos (conforme a la Ley N.º 342 de la Juventud de Bolivia) pertenecientes a la **Población Económicamente Activa (PEA)**.
- **Segmentación Etaria Oficial:**
  - `16 a 17 años`: Adolescentes en transición secundaria/laboral (bajo marco de la Ley N.º 548 y Ley N.º 1139).
  - `18 a 20 años`: Jóvenes en inserción laboral inicial o egresados de bachillerato.
  - `21 a 24 años`: Jóvenes en etapa de formación técnica o universitaria superior.
  - `25 a 28 años`: Jóvenes en consolidación profesional o inserción al empleo calificado.

### 2.3. Objetivo General
Analizar los factores sociodemográficos, educativos, territoriales y de trayectoria laboral asociados a la desocupación de jóvenes de 16 a 28 años en el área urbana de Bolivia, para la identificación de patrones y diferencias relacionados con su inserción laboral a partir de información estadística oficial del mercado de trabajo.

### 2.4. Objetivos Específicos
1. **Recopilar y organizar** datos estadísticos oficiales del mercado laboral boliviano (ECE 4T-2025, INE), aplicando procesos de selección, limpieza y estructuración.
2. **Procesar y analizar** los datos mediante Python (Pandas/SciPy/Statsmodels), aplicando técnicas de filtrado, transformación, tasas ponderadas y análisis de asociaciones ($\chi^2$, V de Cramér).
3. **Diseñar y construir** visualizaciones e indicadores interactivos en Power BI (tablero analítico de 6 páginas con medidas DAX ponderadas) que faciliten la interpretación de brechas y perfiles.
4. **Validar y contrastar** los resultados frente a los boletines oficiales publicados por el INE y la literatura laboral regional (OIT/CEPAL).

---

## 3. Arquitectura y Estructura del Repositorio

El proyecto cuenta con una estructura modular estándar para Ciencia de Datos:

```text
Proyecto-Final-Data-Science/
├── AGENTS.md                                   # Guía maestra y reglas de trabajo para agentes de IA
├── requirements.txt                            # Dependencias de Python (pandas, scipy, statsmodels, etc.)
├── Proyecto-Final.ipynb                        # Notebook principal de ingestión, EDA, estadística y modelado
├── data/                                       # Almacenamiento de datos del proyecto
│   ├── raw/                                    # Microdatos originales inalterados del INE
│   │   ├── ECE_4T2025.csv                      # Microdatos ECE 4T-2025 (separador ';', latin1)
│   │   ├── ECE_4T2025.dta                      # Formato Stata
│   │   └── ECE_4T2025.sav                      # Formato SPSS
│   └── processed/                              # Microdatos procesados y listos para modelado y Power BI
│       └── ECE_4T2025_Jovenes_PEA.csv          # Universo filtrado (PEA urbana 16-28 años, n=6.649)
├── docs/                                       # Documentación académica y especificaciones
│   ├── Perfil_Trabajo_Data_Science_Desocupacion_Juvenil_Bolivia.pdf # Perfil de monografía aprobado
│   ├── Monografia_Diplomado_Data_Science.md   # Estructura de evaluación y guía metodológica CEPI
│   └── PLAN-IMPLEMENTACION-CAPÍTULO_III_ RESULTADOS.md # Plan de ejecución técnica y redacción Cap. III
├── outputs/                                    # Resultados y artefactos generados para la monografía
│   ├── figures/                                # Figuras analíticas exportadas a 300 DPI (PNG)
│   ├── tables/                                 # Tablas de frecuencias, tasas y pruebas Chi2 / Cramér (CSV)
│   └── reports/                                # Borradores y entregables formales en Word (.docx)
├── powerbi/                                    # Recursos del reporte interactivo de Business Intelligence
│   ├── measures/                               # Catálogo de medidas analíticas en DAX
│   └── dashboard_desocupacion_juvenil.pbix     # Archivo de Power BI Desktop
├── src/                                        # Código fuente modular en Python
│   ├── __init__.py
│   ├── config.py                               # Rutas, diccionarios INE, parámetros y paleta de colores
│   ├── data_processing.py                      # Pipeline de carga, filtrado, recodificación y validación
│   ├── statistical_analysis.py                 # Cálculos univariados, bivariados, Chi2 y V de Cramér
│   └── visualization.py                        # Scripts de generación de gráficos de alta resolución
└── .agents/skills/                             # Habilidades especializadas configuradas para el proyecto
    ├── dax-analytics/                          # Medidas analíticas DAX con factor de expansión
    ├── powerbi-dashboard-design/               # Arquitectura de 6 páginas y diseño visual USFX
    ├── powerbi-modeling/                       # Modelado dimensional Star Schema y consultas Power Query M
    └── project-documentation/                  # Redacción académica bajo formato CEPI y normas APA 7ma
```

---

## 4. Diccionario de Datos y Microdatos (ECE 4T-2025)

El archivo fuente `data/raw/ECE_4T2025.csv` cuenta con **52.650 registros** y **121 variables** oficiales del INE.

| Variable en ECE | Variable Procesada | Descripción y Valores | Criterio de Selección / Uso |
| :--- | :--- | :--- | :--- |
| `id_persona` | `id_persona` | Identificador único del encuestado | Clave primaria |
| `area` | `area_num` | `1` = Urbana, `2` = Rural | **Filtro obligatorio:** `area == 1` |
| `s1_03a` | `edad` | Años cumplidos (0 a 98) | **Filtro obligatorio:** `16 <= s1_03a <= 28` |
| `pea` | `pea_val` | `1` = Pertenece a la PEA, `0` = Inactivo | **Filtro obligatorio:** `pea == 1` |
| `s1_02` | `sexo` | `1` = Hombre, `2` = Mujer | Brecha de género en desocupación |
| *Calculada* | `grupo_edad` | 16-17, 18-20, 21-24, 25-28 años | Segmentación etaria analítica |
| `depto` | `departamento` | 1 al 9 (Chuquisaca a Pando) | Dimensión territorial |
| `peao` | `es_ocupado` | `1` = Ocupado, `0` = No | Denominador ocupados |
| `pead` | `es_desocupado` | `1` = Desocupado, `0` = No | **Variable objetivo (Resultado)** |
| `peadces` | `es_cesante` | `1` = Cesante (tuvo empleo previo), `0` = No | Pérdida de empleo |
| `peadasp` | `es_aspirante` | `1` = Aspirante (busca primer empleo), `0` = No | Barrera del primer empleo |
| `psubocup` | `es_subocupado`| `1` = Subocupado por tiempo, `0` = No | Subutilización de mano de obra |
| `niv_ed_g` | `nivel_educativo`| Primaria, Secundaria, Técnico, Universitario | Capital humano alcanzado |
| `aestudio` | `anios_estudio`| Años acumulados de escolaridad | Nivel formativo continuo |
| `s1_09` | `asiste_estudio`| `1` = Asiste actualmente, `2` = No | Interacción estudio-trabajo |
| `fact_trim_act`| `peso_trimestral`| Ponderador trimestral del diseño muestral | **OBLIGATORIO:** Factor de expansión |

> [!CAUTION]
> **REGLA METODOLÓGICA CRÍTICA:**  
> Jamás calcular promedios ni frecuencias simples sin el ponderador `peso_trimestral` (`fact_trim_act`).  
> Fórmula oficial: $\text{Tasa de Desocupación} = \frac{\sum (\text{es\_desocupado} \times \text{peso\_trimestral})}{\sum (\text{peso\_trimestral})} \times 100$.

---

## 5. Resultados Oficiales de Línea Base (Validación Exitosa)

El pipeline de datos (`src/data_processing.py` y `src/statistical_analysis.py`) reproduce con exactitud los datos oficiales del INE para el 4T-2025:

| Métrica / Indicador | Muestra ($n$) | Población Ponderada | Resultado Obtenido | Meta Oficial Boletín INE |
| :--- | :---: | :---: | :---: | :---: |
| **PEA Juvenil Urbana (16-28 años)** | 6.649 | 1.380.841 personas | 100.0% | Referencia oficial |
| **Población Ocupada Juvenil** | 6.406 | 1.329.645 personas | 96.29% | Referencia oficial |
| **Población Desocupada Juvenil** | 243 | 51.196 personas | 3.71% | **3.7%** |
| **Tasa de Subocupación Juvenil** | 567 | 115.736 personas | 8.70% | **8.7%** |
| **Desocupados Cesantes** | 215 | 45.882 personas | 89.6% de desocupados | Mayoritarios |
| **Desocupados Aspirantes** | 28 | 5.314 personas | 10.4% de desocupados | Primer empleo |

### Brechas Clave Identificadas:
- **Brecha de Género:** Hombres = 2.85% vs. Mujeres = 4.69% (Brecha de $+1.84$ pp; $\chi^2 = 5.24$, $p = 0.0221$, estadísticamente significativa).
- **Tramo Etario Crítico:** 18 a 20 años presenta la mayor tasa: **4.65%** ($\chi^2 = 11.23$, $p = 0.0105$, estadísticamente significativa).
- **Disparidad Territorial:** Chuquisaca lidera la tasa de desocupación juvenil con **5.80%**, seguido de Tarija con **4.72%** y Cochabamba con **4.71%** ($\chi^2 = 23.69$, $p = 0.0026$, estadísticamente significativa).

---

## 6. Comandos de Ejecución del Pipeline

Para reproducir todo el procesamiento y análisis desde la terminal:

```powershell
# 1. Instalar dependencias
python -m pip install -r requirements.txt

# 2. Ejecutar procesamiento y limpieza de microdatos
python -m src.data_processing

# 3. Ejecutar análisis estadístico, tablas y pruebas Chi2 / Cramér
python -m src.statistical_analysis

# 4. Generar catálogo de figuras de alta resolución (300 DPI)
python -m src.visualization
```

---

## 7. Arquitectura del Dashboard de Power BI (6 Páginas)

| Página | Título de Página | Foco Analítico |
| :---: | :--- | :--- |
| **Pág 1** | **Panorama Laboral Juvenil** | KPIs (PEA, Ocupados, Desocupados, Tasa Ponderada 3.71%, Subocupación 8.70%), distribución y filtros globales. |
| **Pág 2** | **Desocupación por Grupo Etario** | Análisis de los 4 tramos (16-17, 18-20, 21-24, 25-28), resaltando el pico en 18-20 años (4.65%). |
| **Pág 3** | **Educación y Desocupación** | Tasa por nivel educativo alcanzado (`niv_ed_g`), años de escolaridad y condición de asistencia académica. |
| **Pág 4** | **Brechas de Género y Territorio** | Brecha mujer vs. hombre (+1.84 pp) y ranking departamental (Chuquisaca 5.80%, Tarija 4.72%, eje troncal). |
| **Pág 5** | **Perfil del Joven Desocupado** | Cesantes (89.6%) vs. Aspirantes (10.4%), tiempo de búsqueda y ocupaciones anteriores. |
| **Pág 6** | **Hallazgos y Recomendaciones** | Síntesis ejecutiva, matriz de implicancias de políticas públicas e intervenciones de inserción laboral. |

---

## 8. Cronograma Académico CEPI y Fechas Límite

| Hito / Entrega | Contenido Requerido | Ponderación | Fecha Límite |
| :---: | :--- | :---: | :---: |
| **Actividad 1** | **Presentación del Capítulo III:** Resultados completos (3.1 Presentación + 3.2 Análisis crítico) con tablas, gráficos y trazabilidad CRISP-DM. | **25%** | **Domingo 04/10/2026** (23:59) |
| **Actividad 2** | **Versión corregida del Capítulo III** + Conclusiones + Recomendaciones + Referencias bibliográficas (APA) + Anexos + Resumen Ejecutivo. | **25%** | **Domingo 11/10/2026** (23:59) |
| **Actividad 3** | **Presentación final de la monografía corregida** (~50 páginas completas en formato Word: `GonzalesSuyo_Franz_Actividad3.docx`). | **50%** | **Domingo 18/10/2026** (23:59) |

---

## 9. Directrices de Calidad para los Agentes de IA

1. **Idioma y Estilo Formal:** Todo código, documentación y redacción debe realizarse en español, manteniendo redacción académica formal en tercera persona.
2. **Ponderación Inquebrantable:** Prohibido el uso de recuentos simples `COUNT` o sumas no ponderadas para métricas agregadas o porcentajes. Toda estimación debe expandirse con `peso_trimestral` (`fact_trim_act`).
3. **No Afirmar Causalidad:** El estudio es descriptivo, bivariado y diagnóstico. Las pruebas de $\chi^2$ y V de Cramér miden grado de **asociación estadística**, jamás causalidad directa.
4. **Sincronización Total:** Los números citados en el texto de la monografía deben coincidir al 100% con los cálculos generados en Python (`outputs/tables/`) y las medidas DAX de Power BI.
5. **Apego al Formato CEPI:** La plantilla de documento debe respetar los lineamientos de la Guía CEPI 2024 de la USFX.
