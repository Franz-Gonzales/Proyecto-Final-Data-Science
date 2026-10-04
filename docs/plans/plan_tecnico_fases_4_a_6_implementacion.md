# PLAN TÉCNICO DE IMPLEMENTACIÓN ANALÍTICA (FASES 4 A 6)

**Proyecto:** *Análisis de los factores asociados a la desocupación en jóvenes de 16 a 28 años en Bolivia*  
**Programa Académico:** Diplomado en Data Science — Versión I  
**Institución:** Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX) — CEPI  
**Autor / Investigador:** Franz Reinaldo Gonzales Suyo  
**Docente Coordinador:** Ing. Marcelo Arancibia  
**Fecha de Elaboración:** Octubre 2026 | **Versión:** 1.1 (Plan Técnico de Ingeniería Actualizado)  
**Alcance Técnico:** Fases 4, 5 y 6 (CRISP-DM Fases 5 y 6: Modelado Dimensional y Despliegue en Power BI PBIP, Auditoría de Validación Cruzada Multiplataforma y Consolidación del Capítulo III en Markdown como Fuente Única de Verdad)

---

## 1. INFORMACIÓN GENERAL Y ARQUITECTURA DEL SISTEMA

### 1.1. Propósito del Documento
Este documento establece la **especificación técnica de ingeniería de software, arquitectura de modelado semántico, catálogo formal de medidas DAX ponderadas, diseño de interfaz PBIR (Power BI Enhanced Report Format), protocolo automatizado de aseguramiento de calidad (QA) y consolidación integral del documento maestro en Markdown (`docs/GonzalesSuyo_Franz_ActividadNº1.md`)** para la culminación práctica del proyecto.

Constituye la guía técnica prescriptiva que traduce las decisiones del planteamiento conceptual en código ejecutable, artefactos reproducibles y entregables académicos conformes a la normativa del CEPI. El documento `docs/GonzalesSuyo_Franz_ActividadNº1.md` servirá como la fuente única y completa para que el autor traslade de manera manual y externa el contenido a su plantilla final en Microsoft Word.

### 1.2. Pila Tecnológica (Tech Stack)
*   **Entorno de Business Intelligence y Modelado Semántico:** Microsoft Power BI Desktop (modo proyecto PBIP: TMDL + PBIR) sobre `powerbi/Visualizacion-Analisis-Desocupacion.pbip`.
*   **Protocolo de Control y Modelado MCP:** Servidor `powerbi-modeling-mcp` (operaciones sobre modelo, tablas, columnas, relaciones y medidas tabulares).
*   **Lenguajes Analíticos y de Transformación:** 
    *   Lenguaje M (Power Query) para ingestión y tipificación tabular.
    *   DAX (Data Analysis Expressions) para medidas analíticas ponderadas con factor de expansión muestral.
*   **Motor de Datos y Validación Automatizada:** Python 3.14+ (`pandas >= 2.2.0`, `numpy >= 1.26.0`, `scipy >= 1.13.0`).
*   **Estándar Documental y Redacción Académica:** Formato Markdown estructurado (`docs/GonzalesSuyo_Franz_ActividadNº1.md`) con tablas, diagramas y figuras según normas APA 7ma edición y Guía CEPI USFX 2024, optimizado para su copiado manual al procesador de texto por parte del autor.
*   **Control de Versiones y Formatos Abiertos:** TMDL (*Tabular Model Definition Language*) y PBIR (*Power BI Interactive Report JSON*) versionados limpiamente en Git.

---

## 2. ARQUITECTURA DEL FLUJO DE TRABAJO (END-TO-END PIPELINE)

El pipeline de las Fases 4 a 6 conecta de forma desacoplada y trazable el repositorio de datos procesados en Python con el reporte interactivo y el documento final de monografía:

```text
[ CAPA DE DATOS PROCESADOS ]
  data/processed/ECE_4T2025_Jovenes_PEA.csv (6.649 filas x 156 columnas, factor fact_trim_act)
       │
       ├────────────────────────────────────────────────────────────────────────┐
       ▼                                                                        ▼
[ FASE 4: INGENIERÍA POWER BI (PBIP) ]                   [ FASE 5: PROTOCOLO VALIDACIÓN QA ]
  powerbi/Visualizacion-Analisis-Desocupacion/             scratch/run_cross_validation_qa.py
       │                                                                        │
       ├─ Power Query M: Ingesta y normalización                                ├─ Auditoría línea base INE (3.7% / 8.7%)
       ├─ Modelo Semántico TMDL: Star Schema (1:N)                              ├─ Conciliación Python vs. Power BI (DAX)
       ├─ Catálogo DAX: Medidas ponderadas obligatorias                         ├─ Verificación consistencia aditiva
       └─ Reporte PBIR: 6 páginas interactivas UI/UX                            └─ outputs/reports/informe_validacion_cruzada_qa.md
               │                                                                        │
               └────────────────────────────────┬───────────────────────────────────────┘
                                                ▼
                         [ FASE 6: CONSOLIDACIÓN INTEGRAL EN MARKDOWN ]
                           docs/GonzalesSuyo_Franz_ActividadNº1.md
                                                │
                                                ├─ Sección 3.1: Presentación objetiva + Evidencia Power BI
                                                ├─ Sección 3.2: Discusión analítica (Humanizer, APA 7ma)
                                                └─ Fuente única completa y maquetada lista para traslado
                                                   manual a la plantilla oficial de Word por el autor
```

---

## 3. FASE 4: ESPECIFICACIÓN TÉCNICA DEL MODELO SEMÁNTICO EN POWER BI

### 3.1. Ingestión y Transformación en Lenguaje M (Power Query)
La tabla de hechos se cargará directamente desde el archivo consolidado de microdatos. Las tablas dimensionales se construirán garantizando claves unívocas, descripciones estandarizadas y ordenamientos personalizados.

#### A. Consulta M para Tabla de Hechos: `Fact_MercadoLaboral`
```powerquery
let
    Origen = Csv.Document(File.Contents("data/processed/ECE_4T2025_Jovenes_PEA.csv"), [Delimiter=";", Columns=156, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    EncabezadosPromovidos = Table.PromoteHeaders(Origen, [PromoteAllScalars=true]),
    ColumnasSeleccionadas = Table.SelectColumns(EncabezadosPromovidos, {
        "id_persona", "edad", "grupo_edad", "sexo", "departamento", 
        "nivel_educativo", "anios_estudio", "asiste_estudio", "tipo_condicion_laboral", 
        "tipo_hogar", "parentesco", "mecanismo_busqueda",
        "es_ocupado", "es_desocupado", "es_cesante", "es_aspirante", "es_subocupado", 
        "peso_trimestral"
    }),
    TiposCambiados = Table.TransformColumnTypes(ColumnasSeleccionadas, {
        {"id_persona", Int64.Type},
        {"edad", Int64.Type},
        {"grupo_edad", type text},
        {"sexo", type text},
        {"departamento", type text},
        {"nivel_educativo", type text},
        {"anios_estudio", Int64.Type},
        {"asiste_estudio", type text},
        {"tipo_condicion_laboral", type text},
        {"tipo_hogar", type text},
        {"parentesco", type text},
        {"mecanismo_busqueda", type text},
        {"es_ocupado", Int64.Type},
        {"es_desocupado", Int64.Type},
        {"es_cesante", Int64.Type},
        {"es_aspirante", Int64.Type},
        {"es_subocupado", Int64.Type},
        {"peso_trimestral", type number}
    })
in
    TiposCambiados
```

#### B. Tablas Dimensionales (Definidas en Power Query M / TMDL Datatables):
1.  **`Dim_GrupoEdad`:**
    *   Columnas: `grupo_edad` (Texto, PK), `OrdenEtario` (Entero, 1 a 4).
    *   Filas: `{"16 a 17 años", 1}`, `{"18 a 20 años", 2}`, `{"21 a 24 años", 3}`, `{"25 a 28 años", 4}`.
    *   Propiedad: `OrderByAttribute = OrdenEtario`.
2.  **`Dim_Sexo`:**
    *   Columnas: `sexo` (Texto, PK), `sexo_cod` (Entero: 1=Hombre, 2=Mujer).
3.  **`Dim_Departamento`:**
    *   Columnas: `departamento` (Texto, PK), `depto_cod` (Entero, 1 a 9), `RegionGeografica` (Texto: Valles, Altiplano, Llanos).
    *   Mapeo regional: Chuquisaca, Cochabamba, Tarija $\rightarrow$ *Valles*; La Paz, Oruro, Potosí $\rightarrow$ *Altiplano*; Santa Cruz, Beni, Pando $\rightarrow$ *Llanos*.
4.  **`Dim_NivelEducativo`:**
    *   Columnas: `nivel_educativo` (Texto, PK), `OrdenEducativo` (Entero, 1 a 5).
    *   Filas: `{"Sin instrucción", 1}`, `{"Primaria", 2}`, `{"Secundaria", 3}`, `{"Superior Técnico", 4}`, `{"Superior Universitario", 5}`.
    *   Propiedad: `OrderByAttribute = OrdenEducativo`.
5.  **`Dim_CondicionLaboral`:**
    *   Columnas: `tipo_condicion_laboral` (Texto, PK), `Categoria` (Texto: Ocupado / Desocupado).
    *   Filas: `{"Ocupado", "Ocupado"}`, `{"Desocupado Cesante", "Desocupado"}`, `{"Desocupado Aspirante", "Desocupado"}`.
6.  **`Dim_Hogar`:**
    *   Columnas: `tipo_hogar` (Texto, PK).

### 3.2. Configuración de Relaciones en el Modelo Semántico (TMDL)
Todas las relaciones serán unidireccionales de uno a muchos (1:N) con integridad referencial activa:

| Tabla Origen (1) | Columna Origen (PK) | Tabla Destino (N) | Columna Destino (FK) | Cardinalidad | Dirección Filtro |
| :--- | :--- | :--- | :--- | :---: | :---: |
| `Dim_GrupoEdad` | `grupo_edad` | `Fact_MercadoLaboral` | `grupo_edad` | 1:N | Single (Unidireccional) |
| `Dim_Sexo` | `sexo` | `Fact_MercadoLaboral` | `sexo` | 1:N | Single (Unidireccional) |
| `Dim_Departamento` | `departamento` | `Fact_MercadoLaboral` | `departamento` | 1:N | Single (Unidireccional) |
| `Dim_NivelEducativo` | `nivel_educativo` | `Fact_MercadoLaboral` | `nivel_educativo` | 1:N | Single (Unidireccional) |
| `Dim_CondicionLaboral` | `tipo_condicion_laboral` | `Fact_MercadoLaboral` | `tipo_condicion_laboral`| 1:N | Single (Unidireccional) |
| `Dim_Hogar` | `tipo_hogar` | `Fact_MercadoLaboral` | `tipo_hogar` | 1:N | Single (Unidireccional) |

---

### 3.3. Catálogo Exhaustivo de Medidas DAX Ponderadas

Se implementará una tabla dedicada exclusivamente a medidas denominada `_Medidas`, categorizada en carpetas de visualización jerárquicas:

#### Carpeta 01: Volúmenes Poblacionales Ponderados
```dax
Muestra Jovenes PEA = 
COUNTROWS('Fact_MercadoLaboral')
// Formato: Entero #,##0 | Meta de control: 6.649 observaciones

PEA Juvenil Ponderada = 
SUM('Fact_MercadoLaboral'[peso_trimestral])
// Formato: Entero #,##0 | Meta oficial INE: 1.380.841 personas

Poblacion Ocupada = 
CALCULATE(
    SUM('Fact_MercadoLaboral'[peso_trimestral]),
    'Fact_MercadoLaboral'[es_ocupado] = 1
)
// Formato: Entero #,##0 | Meta oficial INE: 1.329.645 personas

Poblacion Desocupada = 
CALCULATE(
    SUM('Fact_MercadoLaboral'[peso_trimestral]),
    'Fact_MercadoLaboral'[es_desocupado] = 1
)
// Formato: Entero #,##0 | Meta oficial INE: 51.196 personas

Poblacion Subocupada = 
CALCULATE(
    SUM('Fact_MercadoLaboral'[peso_trimestral]),
    'Fact_MercadoLaboral'[es_subocupado] = 1
)
// Formato: Entero #,##0 | Meta oficial INE: 115.736 personas

Desocupados Cesantes = 
CALCULATE(
    SUM('Fact_MercadoLaboral'[peso_trimestral]),
    'Fact_MercadoLaboral'[es_cesante] = 1
)
// Formato: Entero #,##0 | Meta: 45.882 personas (89,62% de los desocupados)

Desocupados Aspirantes = 
CALCULATE(
    SUM('Fact_MercadoLaboral'[peso_trimestral]),
    'Fact_MercadoLaboral'[es_aspirante] = 1
)
// Formato: Entero #,##0 | Meta: 5.314 personas (10,38% de los desocupados)
```

#### Carpeta 02: Tasas Analíticas de Mercado Laboral
```dax
Tasa Desocupacion Ponderada = 
DIVIDE(
    [Poblacion Desocupada],
    [PEA Juvenil Ponderada],
    0
)
// Formato: Porcentaje 0.00% | Meta oficial INE: 3,71%

Tasa Subocupacion Ponderada = 
DIVIDE(
    [Poblacion Subocupada],
    [Poblacion Ocupada],
    0
)
// Formato: Porcentaje 0.00% | Meta oficial INE: 8,70%

Tasa Desocupacion Urbana General = 
0.0230
// Constante de control oficial: 2,30% urbana de 14 años o más

Ratio Desocupacion Juvenil vs General = 
DIVIDE(
    [Tasa Desocupacion Ponderada],
    [Tasa Desocupacion Urbana General],
    0
)
// Formato: Decimal 0.00x | Meta: 1,61 veces
```

#### Carpeta 03: Brechas de Género y Territorio
```dax
Tasa Desocupacion Mujeres = 
CALCULATE(
    [Tasa Desocupacion Ponderada],
    'Dim_Sexo'[sexo] = "Mujer"
)
// Formato: Porcentaje 0.00% | Meta: 4,69%

Tasa Desocupacion Hombres = 
CALCULATE(
    [Tasa Desocupacion Ponderada],
    'Dim_Sexo'[sexo] = "Hombre"
)
// Formato: Porcentaje 0.00% | Meta: 2,85%

Brecha Desocupacion Genero pp = 
[Tasa Desocupacion Mujeres] - [Tasa Desocupacion Hombres]
// Formato: +0.00%;-0.00% | Meta: +1,84 puntos porcentuales

Porcentaje Mujeres Desocupadas = 
DIVIDE(
    CALCULATE([Poblacion Desocupada], 'Dim_Sexo'[sexo] = "Mujer"),
    [Poblacion Desocupada],
    0
)
// Formato: Porcentaje 0.00% | Meta: 59,10%
```

#### Carpeta 04: Educación y Capital Humano
```dax
Anios Estudio Promedio Desocupados = 
DIVIDE(
    CALCULATE(
        SUMX('Fact_MercadoLaboral', 'Fact_MercadoLaboral'[anios_estudio] * 'Fact_MercadoLaboral'[peso_trimestral]),
        'Fact_MercadoLaboral'[es_desocupado] = 1
    ),
    [Poblacion Desocupada],
    0
)
// Formato: Decimal 0.00 años | Meta: 13,01 años

Anios Estudio Promedio Ocupados = 
DIVIDE(
    CALCULATE(
        SUMX('Fact_MercadoLaboral', 'Fact_MercadoLaboral'[anios_estudio] * 'Fact_MercadoLaboral'[peso_trimestral]),
        'Fact_MercadoLaboral'[es_ocupado] = 1
    ),
    [Poblacion Ocupada],
    0
)
// Formato: Decimal 0.00 años | Meta: 12,64 años

Diferencia Escolaridad Anios = 
[Anios Estudio Promedio Desocupados] - [Anios Estudio Promedio Ocupados]
// Formato: +0.00;-0.00 | Meta: +0,37 años lectivos adicionales
```

#### Carpeta 05: Trayectoria y Búsqueda
```dax
Porcentaje Desocupados Cesantes = 
DIVIDE(
    [Desocupados Cesantes],
    [Poblacion Desocupada],
    0
)
// Formato: Porcentaje 0.00% | Meta: 89,62%

Porcentaje Desocupados Aspirantes = 
DIVIDE(
    [Desocupados Aspirantes],
    [Poblacion Desocupada],
    0
)
// Formato: Porcentaje 0.00% | Meta: 10,38%
```

---

### 3.4. Especificación Visual y Layout de las 6 Páginas (PBIR)

El archivo de reporte `powerbi/Visualizacion-Analisis-Desocupacion.Report/definition/report.json` se configurará con resolución fija de alta fidelidad 16:9 (**1280 x 720 píxeles**), aplicando la paleta oficial USFX.

#### Estructura de Visuales por Página:

```text
====================================================================================================
PÁGINA 1: PANORAMA LABORAL JUVENIL (BOLIVIA URBANA 4T-2025)
====================================================================================================
[ Cabecera Superior: Título Institucional USFX + Menú Segmentador Departamento + Sexo ]
----------------------------------------------------------------------------------------------------
[ KPI 1: PEA Juvenil ] [ KPI 2: Ocupados ] [ KPI 3: Desocupados ] [ KPI 4: Tasa 3.71% ] [ KPI 5: Subocup. 8.70% ]
(1.380.841 pers.)     (1.329.645 pers.)    (51.196 pers.)       (General Urb: 2.30%)    (115.736 pers.)
----------------------------------------------------------------------------------------------------
[ Visual 1: Donut Chart ]           [ Visual 2: Columnas Clúster ]          [ Visual 3: Tarjeta Resumen ]
Distribución PEA Juvenil            Comparativa Tasa Desocupación           Juventud urbana registra una
- Ocupados: 96,29% (Verde)          - Juventud Urbana: 3,71% (Rojo)         presión de desempleo 1,61x
- Desocupados: 3,71% (Rojo)         - General Urbano:  2,30% (Azul)         superior al promedio adulto.
====================================================================================================

====================================================================================================
PÁGINA 2: VULNERABILIDAD ETARIA Y TRANSICIÓN LABORAL
====================================================================================================
[ Cabecera: Título + KPI Destacado: Tasa 18 a 20 años: 4,65% (+0,94 pp sobre el promedio nacional) ]
----------------------------------------------------------------------------------------------------
[ Visual 1: Gráfico de Columnas Clúster ]               [ Visual 2: Gráfico de Barras Horizontales ]
Tasa de Desocupación por Tramo Etario                   Volumen de Población Desocupada por Edad
- 16 a 17 años: 1,87% (Bajo)                           - 25 a 28 años: 19.988 jóvenes (Mayor masa)
- 18 a 20 años: 4,65% (PICO CRÍTICO - Rojo Carmesí)    - 21 a 24 años: 14.713 jóvenes
- 21 a 24 años: 3,55% (Azul)                           - 18 a 20 años: 13.504 jóvenes
- 25 a 28 años: 3,88% (Azul)                           - 16 a 17 años:  2.991 jóvenes
----------------------------------------------------------------------------------------------------
[ Visual 3: Matriz Resumen de Asociación Etaria (Chi-cuadrado = 11,23; p = 0,0105; V = 0,0411) ]
====================================================================================================

====================================================================================================
PÁGINA 3: EDUCACIÓN, ESCOLARIDAD Y DESEMPLEO ILUSTRADO
====================================================================================================
[ Cabecera: Título + KPI 1: Escolaridad Desocupados 13,01 años | KPI 2: Ocupados 12,64 años (+0,37) ]
----------------------------------------------------------------------------------------------------
[ Visual 1: Gráfico de Barras Horizontales ]            [ Visual 2: Barras Bivariadas ]
Tasa de Desocupación según Nivel Educativo              Tasa Desocupación según Asistencia Escolar
- Sin instrucción: 2,31%                               - No asiste a centros: 3,92%
- Primaria:        3,43%                               - Asiste activamente:  3,54%
- Secundaria:      4,02%                               (Diferencia no significativa: p = 0,2166)
- Superior Técnico:4,00%                               ---------------------------------------------
- Superior Univ.:  4,04%                               [ Visual 3: Callout Explicativo ]
(Relación positiva: a mayor instrucción formal,         El desempleo ilustrado refleja descalce
mayor fricción de colocación calificada).              entre perfil profesional y oferta laboral.
====================================================================================================

====================================================================================================
PÁGINA 4: BRECHAS ESTRUCTURALES DE GÉNERO Y TERRITORIO
====================================================================================================
[ Cabecera: Título + Kardex de Género: Mujeres 4,69% vs. Varones 2,85% | Brecha: +1,84 pp ]
----------------------------------------------------------------------------------------------------
[ Visual 1: Gráfico de Barras Horizontales Ordenadas (Ranking Departamental) ]
Tasa de Desocupación Juvenil por Departamento:
- Chuquisaca: 5,80% (MÁXIMO NACIONAL - Rojo)            - Oruro:      2,98%
- Tarija:     4,72% (Rojo)                              - Beni:       2,07%
- Cochabamba: 4,71% (Rojo)                              - Pando:      1,89%
- La Paz:     3,84%                                     - Potosí:     1,64% (MÍNIMO NACIONAL)
- Santa Cruz: 3,33%
----------------------------------------------------------------------------------------------------
[ Visual 2: Donut Chart ]                               [ Visual 3: Barras Agrupadas Eje Troncal ]
Distribución por Sexo de los Desocupados:               Concentración Absoluta: LP, CB y SC reúnen el
- Mujeres: 59,10% (30.258 personas)                     78,5% de todos los jóvenes desocupados urbanos
- Varones: 40,90% (20.938 personas)                     (40.169 desocupados).
====================================================================================================

====================================================================================================
PÁGINA 5: PERFIL OPERATIVO DEL DESOCUPADO (CESANTES VS. ASPIRANTES Y BÚSQUEDA)
====================================================================================================
[ Cabecera: Título + KPI 1: Cesantes 89,62% (45.882) | KPI 2: Aspirantes 10,38% (5.314) ]
----------------------------------------------------------------------------------------------------
[ Visual 1: Gráfico de Donut ]                          [ Visual 2: Columnas Clúster por Edad ]
Composición Interna del Desempleo:                      Distribución Aspirante/Cesante por Tramo:
- Cesantes:   89,62% (Naranja)                          - Aspirantes se concentran al 85% en menores
- Aspirantes: 10,38% (Púrpura)                            de 21 años (primer empleo).
----------------------------------------------------------------------------------------------------
[ Visual 3: Gráfico de Barras Horizontales ]            [ Visual 4: Barras por Tipo de Hogar ]
Mecanismos Principales de Búsqueda de Empleo:           Tasa de Desocupación según Estructura Hogar:
- Avisos digitales e internet: 38,82%                   - Hogar Monoparental: 5,68% (Alta carga)
- Presentación directa de CV:  31,62%                   - Hogar Extendido:    5,37%
- Redes familiares y amigos:    2,28%                   - Hogar Biparental:   3,21%
====================================================================================================

====================================================================================================
PÁGINA 6: SÍNTESIS ESTRATÉGICA Y MATRIZ DE POLÍTICAS PÚBLICAS
====================================================================================================
[ Cabecera: Título Ejecutivo + Botón de Exportación / Navegación ]
----------------------------------------------------------------------------------------------------
[ Visual 1: Matriz Analítica de Hallazgos para Tomadores de Decisión ]
----------------------------------------------------------------------------------------------------
Eje Crítico      Métrica Clave                 Implicancia Operativa de Política Pública
----------------------------------------------------------------------------------------------------
Edad             18-20 años: 4,65%             Programas de primer empleo y pasantías formativas.
Género           Brecha +1,84 pp (59,1% mujeres) Guarderías públicas urbanas y corresponsabilidad.
Territorio       Chuquisaca 5,80%, Tarija 4,72%Polos digitales y diversificación productiva local.
Educación        Desempleo ilustrado (+0,37 a) Articulación oferta universitaria / sector privado.
Trayectoria      89,6% Cesantes                Protección contractual y reconversión técnica.
----------------------------------------------------------------------------------------------------
[ Visual 2: 3 Tarjetas de Recomendaciones Estratégicas Clave para el Estado y Academia ]
====================================================================================================
```

---

## 4. FASE 5: ESPECIFICACIÓN TÉCNICA DEL PROTOCOLO DE VALIDACIÓN (QA AUTOMATIZADO)

### 4.1. Script de Auditoría de Validación Cruzada: `scratch/run_cross_validation_qa.py`
Se implementará un script de verificación automatizada que someterá el modelo semántico y las tablas maestras a una auditoría estricta de 10 puntos de control matemático.

#### Estructura del Script de Validación:
```python
"""
scratch/run_cross_validation_qa.py
Auditoría técnica de consistencia y conciliación multiplataforma.
"""
import pandas as pd
import numpy as np

def auditar_linea_base_ine():
    df = pd.read_csv("data/processed/ECE_4T2025_Jovenes_PEA.csv", sep=";")
    w = df["peso_trimestral"]
    
    # 1. PEA total ponderada
    pea_pond = w.sum()
    assert abs(pea_pond - 1380841.0) < 1.0, f"Error en PEA: {pea_pond}"
    
    # 2. Ocupados y Desocupados
    ocup_pond = (df["es_ocupado"] * w).sum()
    desocup_pond = (df["es_desocupado"] * w).sum()
    assert abs((ocup_pond + desocup_pond) - pea_pond) < 1e-4, "Inconsistencia aditiva Ocup+Desocup!=PEA"
    
    # 3. Tasa de desocupación
    tasa_desocup = (desocup_pond / pea_pond) * 100.0
    assert round(tasa_desocup, 2) == 3.71, f"Tasa difiere: {tasa_desocup}"
    
    # 4. Tasa de subocupación
    subocup_pond = (df["es_subocupado"] * w).sum()
    tasa_subocup = (subocup_pond / ocup_pond) * 100.0
    assert round(tasa_subocup, 2) == 8.70, f"Subocupación difiere: {tasa_subocup}"
    
    # 5. Desocupados cesantes vs aspirantes
    cesantes_pond = (df["es_cesante"] * w).sum()
    aspirantes_pond = (df["es_aspirante"] * w).sum()
    assert abs((cesantes_pond + aspirantes_pond) - desocup_pond) < 1e-4, "Cesantes+Aspirantes!=Desocupados"
    assert round((cesantes_pond / desocup_pond) * 100, 2) == 89.62, "Error % cesantes"
    assert round((aspirantes_pond / desocup_pond) * 100, 2) == 10.38, "Error % aspirantes"

    # 6. Brecha de género
    tasa_mujeres = (df[df["sexo"] == "Mujer"]["es_desocupado"] * df[df["sexo"] == "Mujer"]["peso_trimestral"]).sum() / df[df["sexo"] == "Mujer"]["peso_trimestral"].sum() * 100
    tasa_hombres = (df[df["sexo"] == "Hombre"]["es_desocupado"] * df[df["sexo"] == "Hombre"]["peso_trimestral"]).sum() / df[df["sexo"] == "Hombre"]["peso_trimestral"].sum() * 100
    assert round(tasa_mujeres, 2) == 4.69, f"Tasa mujeres: {tasa_mujeres}"
    assert round(tasa_hombres, 2) == 2.85, f"Tasa hombres: {tasa_hombres}"
    assert round(tasa_mujeres - tasa_hombres, 2) == 1.84, "Brecha no coincide"

    # 7. Pico etario
    tasa_18_20 = (df[df["grupo_edad"] == "18 a 20 años"]["es_desocupado"] * df[df["grupo_edad"] == "18 a 20 años"]["peso_trimestral"]).sum() / df[df["grupo_edad"] == "18 a 20 años"]["peso_trimestral"].sum() * 100
    assert round(tasa_18_20, 2) == 4.65, f"Tasa 18-20: {tasa_18_20}"

    # 8. Departamentos extremos
    tasa_chuq = (df[df["departamento"] == "Chuquisaca"]["es_desocupado"] * df[df["departamento"] == "Chuquisaca"]["peso_trimestral"]).sum() / df[df["departamento"] == "Chuquisaca"]["peso_trimestral"].sum() * 100
    tasa_pot = (df[df["departamento"] == "Potosí"]["es_desocupado"] * df[df["departamento"] == "Potosí"]["peso_trimestral"]).sum() / df[df["departamento"] == "Potosí"]["peso_trimestral"].sum() * 100
    assert round(tasa_chuq, 2) == 5.80, f"Chuquisaca: {tasa_chuq}"
    assert round(tasa_pot, 2) == 1.64, f"Potosí: {tasa_pot}"

    # 9. Años de escolaridad ponderados
    media_desocup = (df[df["es_desocupado"] == 1]["anios_estudio"] * df[df["es_desocupado"] == 1]["peso_trimestral"]).sum() / desocup_pond
    media_ocup = (df[df["es_ocupado"] == 1]["anios_estudio"] * df[df["es_ocupado"] == 1]["peso_trimestral"]).sum() / ocup_pond
    assert round(media_desocup, 2) == 13.01, f"Media desocup: {media_desocup}"
    assert round(media_ocup, 2) == 12.64, f"Media ocup: {media_ocup}"
    
    # 10. Integridad relacional (claves nulas)
    assert df["id_persona"].nunique() == 6649, "Llaves duplicadas en dataset"
    print(">>> 10/10 PRUEBAS QA SUPERADAS EXITOSAMENTE CON DISCREPANCIA CERO.")

if __name__ == "__main__":
    auditar_linea_base_ine()
```

### 4.2. Generación del Informe Técnico de Validación: `outputs/reports/informe_validacion_cruzada_qa.md`
El resultado de la ejecución del script generará un reporte formal en Markdown donde se plasmará la matriz de conciliación punto a punto con marca de tiempo, hash de los datos y confirmación de cero error numérico.

---

## 5. FASE 6: ESPECIFICACIÓN TÉCNICA DE REDACCIÓN Y COMPILACIÓN DOCUMENTAL

### 5.1. Actualización y Enriquecimiento de `docs/GonzalesSuyo_Franz_ActividadNº1.md`
El archivo actual contiene la estructura base aprobada del Capítulo III. Se realizarán las siguientes adiciones técnicas:
1.  **Incorporación de la Sección 3.1.8:** *Evidencia del Cuadro de Mando Interactivo (Dashboard en Power BI)*:
    *   Explicación de la arquitectura de 6 páginas.
    *   Ficha técnica de diseño, interacción y navegación.
    *   Inserción formal de capturas en alta resolución generadas desde Power BI Desktop.
2.  **Auditoría de Estilo y Prosa Académica (Humanizer):**
    *   Verificación de que no existan construcciones típicas de IA (*"no solo es crucial sino también vital"*, *"en resumen/en conclusión"* forzados en cada párrafo, etc.).
    *   Mantenimiento estricto del enfoque descriptivo y diagnóstico sin afirmaciones de causalidad directa.
3.  **Consolidación de la Matriz de Implicancias para Políticas Públicas:**
    *   Articulación de los 5 hallazgos estadísticos con intervenciones prácticas viables en Bolivia.

---

### 5.2. Estructuración y Preparación de `docs/GonzalesSuyo_Franz_ActividadNº1.md` como Fuente Única para Traslado Manual a Word

Para garantizar que el documento maestro en Markdown sea la fuente definitiva y completa, toda la redacción, tablas estadísticas, diagramas conceptuales y referencias de figuras se consolidarán directamente en `docs/GonzalesSuyo_Franz_ActividadNº1.md`. 

El autor trasladará de manera manual el contenido estructurado de este archivo a su plantilla oficial en Microsoft Word (`GonzalesSuyo_Franz_Actividad1.docx`). Para facilitar y asegurar un copiado manual impecable, el archivo Markdown cumplirá con las siguientes normas:

#### Estándares de Estructuración para Copiado Manual:
*   **Jerarquía de Títulos y Secciones:** Numeración estricta 3.1, 3.1.1 a 3.1.8 y 3.2, 3.2.1 a 3.2.9 idéntica a la plantilla CEPI.
*   **Tablas Académicas (Formato APA 7ma Edición):**
    *   Encabezado superior formal: `TABLA N.º X: *Título descriptivo en cursiva*`.
    *   Estructura tabular limpia y compacta, fácil de seleccionar y pegar en Word respetando bordes horizontales.
    *   Pie de tabla estandarizado: `*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*`.
*   **Figuras y Gráficos:**
    *   Rótulo superior formal: `FIGURA N.º X: *Título descriptivo en cursiva*`.
    *   Ruta local directa de las imágenes en alta resolución (`docs/figures/figura_X.png`) para permitir arrastrar o insertar directamente en Word sin pérdida de calidad.
    *   Pie inferior con indicación obligatoria de la fuente.
*   **Diagramas Conceptuales y Metodológicos:**
    *   Códigos nativos Mermaid (`flowchart TD`) y sus respectivas versiones exportadas en PNG de alta resolución en `docs/figures/` para que el autor pueda optar por pegar la imagen gráfica directamente en Word.

---

## 6. MATRIZ DE TAREAS Y DEPENDENCIAS TÉCNICAS (WBS)

```text
+-------------------------------------------------------------------------------------------------------+
| MATRIZ DE DESGLOSE DE TRABAJO (WBS) — FASES 4 A 6                                                     |
+-------------------------------------------------------------------------------------------------------+
| Código | Tarea Técnica                                | Dependencia | Artefacto Generado / Entregable |
+--------+----------------------------------------------+-------------+---------------------------------+
| T4.1   | Generar script M de carga y tipificado       | Fases 1-3   | Fact_MercadoLaboral en TMDL     |
| T4.2   | Crear definiciones TMDL de las 6 dimensiones | T4.1        | Dim_*.tmdl en SemanticModel     |
| T4.3   | Configurar relaciones 1:N unidireccionales    | T4.2        | relationships.tmdl en PBIP      |
| T4.4   | Compilar catálogo de 20 medidas DAX en TMDL  | T4.3        | _Medidas.tmdl con carpetas      |
| T4.5   | Maquetar las 6 páginas interactivas en PBIR  | T4.4        | pages/ en .Report definition    |
| T4.6   | Aplicar paleta cromática USFX y navegación   | T4.5        | Visualizacion-Analisis.pbip     |
+--------+----------------------------------------------+-------------+---------------------------------+
| T5.1   | Crear script scratch/run_cross_validation.py | T4.4        | Script de auditoría QA          |
| T5.2   | Ejecutar conciliación Python vs. Power BI    | T5.1        | Log de 10 pruebas matemáticas   |
| T5.3   | Generar informe formal de validación cruzada | T5.2        | outputs/reports/informe_qa.md   |
+--------+----------------------------------------------+-------------+---------------------------------+
| T6.1   | Incorporar Sección 3.1.8 en documento .md    | T4.6, T5.3  | Evidencia Power BI en .md       |
| T6.2   | Exportar capturas del Dashboard en alta res. | T4.6        | docs/figures/dashboard_*.png    |
| T6.3   | Aplicar revisión de estilo con Humanizer     | T6.1        | Prosa académica natural sin IA  |
| T6.4   | Auditoría integral y cierre del Cap. III .md | T6.2, T6.3  | docs/GonzalesSuyo_Franz_Activida|
|        |                                              |             | dNº1.md 100% listo para Word    |
+-------------------------------------------------------------------------------------------------------+
```

---

## 7. CRITERIOS DE ACEPTACIÓN TÉCNICA Y CONDICIONES DE CIERRE

Para declarar completado con éxito el 100% del proyecto de monografía, se verificarán obligatoriamente las siguientes condiciones de parada (*Definition of Done*):

1.  **Consistencia Numérica Cero Error:** Todas las cifras calculadas en DAX deben concordar al milímetro con las tablas exportadas en `outputs/tables/` y citadas en el documento de texto.
2.  **Validez Muestral:** Cero utilización de funciones `COUNT` o sumas directas de filas para tasas o totales poblacionales; todo el modelo opera bajo el factor de expansión trimestral `peso_trimestral`.
3.  **Integridad Estructural PBIP:** El proyecto `Visualizacion-Analisis-Desocupacion.pbip` debe abrirse sin advertencias de dependencias rotas, tablas huérfanas ni errores de sintaxis en DAX.
4.  **Alineación Académica CEPI en Markdown:** El documento `docs/GonzalesSuyo_Franz_ActividadNº1.md` debe estar 100% completo, estructurado según la Guía CEPI 2024 (secciones 3.1 y 3.2, tablas y figuras bajo normas APA 7ma edición), listo para el traslado manual a la plantilla Word por el autor.
5.  **Auditabilidad y Reproducibilidad:** Cualquier evaluador debe poder regenerar todo el pipeline ejecutando los scripts correspondientes desde la raíz del repositorio.
