---
name: powerbi-modeling
description: >-
  Guía y procedimientos para el modelado dimensional en estrella (Star Schema),
  transformación en Power Query (Lenguaje M) y configuración de relaciones 1:N
  para el proyecto de Desocupación Juvenil en Bolivia (ECE 4T-2025).
---

# Skill: Power BI Modeling & Dimensional Architecture (ECE 4T-2025)

Esta skill proporciona las instrucciones técnicas y patrones de código necesarios para estructurar el modelo analítico de la Encuesta Continua de Empleo (ECE 4T-2025) en un modelo dimensional en estrella (Star Schema) optimizado en Power BI Desktop.

---

## 1. Arquitectura del Modelo Dimensional (Star Schema)

El modelo separa los microdatos expandidos de los jóvenes en la PEA (`Fact_Jovenes_PEA`) de las entidades de contexto y segmentación (dimensiones):

```
                        +----------------------+
                        |    Dim_GrupoEdad     |
                        | (grupo_edad, orden)  |
                        +----------+-----------+
                                   | 1
                                   | 
                                   | *
+----------------------+ 1      * +----------------------+ *      1 +----------------------+
|       Dim_Sexo       +----------+   Fact_Jovenes_PEA   +----------+  Dim_NivelEducativo  |
|  (sexo_cod, sexo)    |          | (Microdatos PEA 16-28|          |  (niv_ed_cod, nivel) |
+----------------------+          +----------+-----------+          +----------------------+
                                             | *
                                             | 
                                             | 1
                                  +----------+-----------+
                                  |   Dim_Departamento   |
                                  |  (depto_cod, nombre) |
                                  +----------------------+
```

---

## 2. Definición de Tablas del Modelo

### 2.1 Tabla de Hechos: `Fact_Jovenes_PEA`
- **Origen:** `data/processed/ECE_4T2025_Jovenes_PEA.csv` (o conexión Power Query directa).
- **Granularidad:** 1 registro por cada joven encuestado en el área urbana de Bolivia de 16 a 28 años perteneciente a la PEA ($n = 6.649$).
- **Campos Principales:**
  - `id_persona` (Clave de registro)
  - `edad` (Entero, 16 a 28)
  - `grupo_edad` (16 a 17 años, 18 a 20 años, 21 a 24 años, 25 a 28 años)
  - `sexo_cod`, `sexo`
  - `depto_cod`, `departamento`
  - `niv_ed_cod`, `nivel_educativo`
  - `anios_estudio`
  - `asistencia_cod`, `asiste_estudio`
  - `tipo_condicion_laboral` (Ocupado, Desocupado Cesante, Desocupado Aspirante)
  - `es_ocupado` (1/0)
  - `es_desocupado` (1/0)
  - `es_cesante` (1/0)
  - `es_aspirante` (1/0)
  - `es_subocupado` (1/0)
  - `peso_trimestral` (`fact_trim_act` con punto decimal, ponderador muestral)

### 2.2 Tablas Dimensionales (Creadas en DAX o Power Query)

#### Dim_GrupoEdad
```dax
Dim_GrupoEdad = DATATABLE(
    "grupo_edad", STRING,
    "Orden", INTEGER,
    {
        {"16 a 17 años", 1},
        {"18 a 20 años", 2},
        {"21 a 24 años", 3},
        {"25 a 28 años", 4}
    }
)
```
*(Configurar 'Ordenar por columna' -> `Orden`)*

#### Dim_Sexo
```dax
Dim_Sexo = DATATABLE(
    "sexo_cod", INTEGER,
    "sexo", STRING,
    {
        {1, "Hombre"},
        {2, "Mujer"}
    }
)
```

#### Dim_Departamento
```dax
Dim_Departamento = DATATABLE(
    "depto_cod", INTEGER,
    "departamento", STRING,
    "Region", STRING,
    {
        {1, "Chuquisaca", "Valles"},
        {2, "La Paz", "Altiplano"},
        {3, "Cochabamba", "Valles"},
        {4, "Oruro", "Altiplano"},
        {5, "Potosí", "Altiplano"},
        {6, "Tarija", "Valles"},
        {7, "Santa Cruz", "Llanos"},
        {8, "Beni", "Llanos"},
        {9, "Pando", "Llanos"}
    }
)
```

#### Dim_NivelEducativo
```dax
Dim_NivelEducativo = DATATABLE(
    "niv_ed_cod", INTEGER,
    "nivel_educativo", STRING,
    "Orden", INTEGER,
    {
        {1, "Sin instrucción", 1},
        {2, "Primaria", 2},
        {3, "Secundaria", 3},
        {4, "Superior No Universitario (Técnico)", 4},
        {5, "Superior Universitario", 5},
        {6, "Otros", 6}
    }
)
```

---

## 3. Relaciones del Modelo
- `Dim_GrupoEdad[grupo_edad]` $1 \rightarrow \infty$ `Fact_Jovenes_PEA[grupo_edad]` (Filtro Cruzado: Única).
- `Dim_Sexo[sexo]` $1 \rightarrow \infty$ `Fact_Jovenes_PEA[sexo]` (Filtro Cruzado: Única).
- `Dim_Departamento[departamento]` $1 \rightarrow \infty$ `Fact_Jovenes_PEA[departamento]` (Filtro Cruzado: Única).
- `Dim_NivelEducativo[nivel_educativo]` $1 \rightarrow \infty$ `Fact_Jovenes_PEA[nivel_educativo]` (Filtro Cruzado: Única).

---

## 4. Consulta Power Query M (ETL Reproducible)

```powerquery
let
    Origen = Csv.Document(File.Contents("C:\Users\franz\workspace\diplomado\Proyecto-Final-Data-Science\data\processed\ECE_4T2025_Jovenes_PEA.csv"), [Delimiter=";", Columns=135, Encoding=65001, QuoteStyle=QuoteStyle.None]),
    EncabezadosPromovidos = Table.PromoteHeaders(Origen, [PromoteAllScalars=true]),
    TipoCambiado = Table.TransformColumnTypes(EncabezadosPromovidos,{
        {"edad", Int64.Type},
        {"sexo", type text},
        {"grupo_edad", type text},
        {"departamento", type text},
        {"nivel_educativo", type text},
        {"anios_estudio", Int64.Type},
        {"asiste_estudio", type text},
        {"tipo_condicion_laboral", type text},
        {"es_ocupado", Int64.Type},
        {"es_desocupado", Int64.Type},
        {"es_cesante", Int64.Type},
        {"es_aspirante", Int64.Type},
        {"es_subocupado", Int64.Type},
        {"peso_trimestral", type number}
    })
in
    TipoCambiado
```
