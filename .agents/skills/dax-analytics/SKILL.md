---
name: dax-analytics
description: >-
  Catálogo y directrices para el desarrollo de medidas DAX ponderadas por factor de expansión
  (PEA, Ocupación, Desocupación, Subocupación, Cesantes, Aspirantes, Brechas de Género y Territorio)
  para el proyecto de Desocupación Juvenil en Bolivia (ECE 4T-2025).
---

# Skill: DAX Analytics & Medidas Ponderadas (ECE 4T-2025)

Esta skill compila el catálogo integral de medidas DAX diseñado para responder a los objetivos de investigación sobre la desocupación de jóvenes de 16 a 28 años en el área urbana de Bolivia, garantizando la rigurosa ponderación muestral (`fact_trim_act`).

---

## 1. Regla de Oro Metodológica en DAX

> [!CAUTION]
> En encuestas por muestreo probabilístico del INE jamás debe utilizarse `COUNTRows` o recuentos simples para evaluar volúmenes poblacionales o calcular tasas. Toda estimación poblacional debe aplicar la suma ponderada del factor de expansión trimestral:
> $$\text{Tasa de Desocupación} = \frac{\sum (\text{es\_desocupado} \times \text{peso\_trimestral})}{\sum (\text{peso\_trimestral})} \times 100$$

---

## 2. Catálogo de Medidas DAX Principales

### 2.1 Muestra Muestral (Sin Ponderar)
```dax
Muestra Jovenes PEA = 
COUNTROWS('Fact_Jovenes_PEA')
```
*Formato: Número entero `#,##0`*

### 2.2 Población PEA Juvenil Estimada
```dax
PEA Juvenil Ponderada = 
SUM('Fact_Jovenes_PEA'[peso_trimestral])
```
*Formato: Número entero `#,##0` personas*

### 2.3 Población Ocupada Juvenil
```dax
Poblacion Ocupada = 
CALCULATE(
    SUM('Fact_Jovenes_PEA'[peso_trimestral]),
    'Fact_Jovenes_PEA'[es_ocupado] = 1
)
```
*Formato: Número entero `#,##0` personas*

### 2.4 Población Desocupada Juvenil
```dax
Poblacion Desocupada = 
CALCULATE(
    SUM('Fact_Jovenes_PEA'[peso_trimestral]),
    'Fact_Jovenes_PEA'[es_desocupado] = 1
)
```
*Formato: Número entero `#,##0` personas*

### 2.5 Tasa de Desocupación Ponderada (%)
```dax
Tasa Desocupacion Ponderada = 
DIVIDE(
    [Poblacion Desocupada],
    [PEA Juvenil Ponderada],
    0
)
```
*Formato: Porcentaje `0.00%` (Meta oficial 4T-2025: 3.71%)*

### 2.6 Población Subocupada Juvenil
```dax
Poblacion Subocupada = 
CALCULATE(
    SUM('Fact_Jovenes_PEA'[peso_trimestral]),
    'Fact_Jovenes_PEA'[es_subocupado] = 1
)
```
*Formato: Número entero `#,##0` personas*

### 2.7 Tasa de Subocupación Ponderada (%)
```dax
Tasa Subocupacion Ponderada = 
DIVIDE(
    [Poblacion Subocupada],
    [Poblacion Ocupada],
    0
)
```
*Formato: Porcentaje `0.00%` (Meta oficial 4T-2025: 8.70%)*

---

## 3. Medidas de Caracterización de la Desocupación (Cesantes vs. Aspirantes)

### 3.1 Desocupados Cesantes (Con Experiencia Previa)
```dax
Desocupados Cesantes = 
CALCULATE(
    SUM('Fact_Jovenes_PEA'[peso_trimestral]),
    'Fact_Jovenes_PEA'[es_cesante] = 1
)
```

### 3.2 Desocupados Aspirantes (Búsqueda de Primer Empleo)
```dax
Desocupados Aspirantes = 
CALCULATE(
    SUM('Fact_Jovenes_PEA'[peso_trimestral]),
    'Fact_Jovenes_PEA'[es_aspirante] = 1
)
```

### 3.3 Proporción de Aspirantes (%)
```dax
Proporcion Aspirantes % = 
DIVIDE(
    [Desocupados Aspirantes],
    [Poblacion Desocupada],
    0
)
```
*Formato: Porcentaje `0.0%`*

---

## 4. Medidas de Brechas de Género

### 4.1 Tasa de Desocupación Masculina
```dax
Tasa Desocupacion Hombres = 
CALCULATE(
    [Tasa Desocupacion Ponderada],
    'Fact_Jovenes_PEA'[sexo] = "Hombre"
)
```

### 4.2 Tasa de Desocupación Femenina
```dax
Tasa Desocupacion Mujeres = 
CALCULATE(
    [Tasa Desocupacion Ponderada],
    'Fact_Jovenes_PEA'[sexo] = "Mujer"
)
```

### 4.3 Brecha de Género en Desocupación (Puntos Porcentuales)
```dax
Brecha Desocupacion Genero pp = 
[Tasa Desocupacion Mujeres] - [Tasa Desocupacion Hombres]
```
*Formato: `+0.00;-0.00;0.00` pp*

---

## 5. Medidas para Grupos Etarios y Educación

### 5.1 Tasa de Desocupación por Tramo Etario
Se obtiene colocando `Dim_GrupoEdad[grupo_edad]` o `Fact_Jovenes_PEA[grupo_edad]` en el eje visual y evaluando `[Tasa Desocupacion Ponderada]`.

### 5.2 Años de Estudio Ponderados
```dax
Promedio Anios Estudio Ponderado = 
DIVIDE(
    SUMX('Fact_Jovenes_PEA', 'Fact_Jovenes_PEA'[anios_estudio] * 'Fact_Jovenes_PEA'[peso_trimestral]),
    [PEA Juvenil Ponderada],
    0
)
```
*Formato: Decimal `0.0` años*
