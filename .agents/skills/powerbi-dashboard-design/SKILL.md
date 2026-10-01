---
name: powerbi-dashboard-design
description: >-
  Guía de diseño visual, UI/UX, arquitectura de 6 páginas, selección de gráficos y
  storytelling analítico en Power BI para el proyecto de Desocupación Juvenil en Bolivia (ECE 4T-2025).
---

# Skill: Power BI Dashboard Design & Storytelling (Desocupación Juvenil Bolivia)

Esta skill establece la arquitectura de visualización, wireframes, componentes de navegación y paleta de colores oficial para la construcción del reporte interactivo de 6 páginas en Power BI Desktop.

---

## 1. Arquitectura de las 6 Páginas del Tablero

```text
+---------------------------------------------------------------------------------------------------+
|               ESTRUCTURA DEL DASHBOARD ANALÍTICO — DESOCUPACIÓN JUVENIL EN BOLIVIA                |
+---------------------------------------------------------------------------------------------------+
|  [Pág 1] Panorama Laboral Juvenil       -> Indicadores Macro, PEA, Desocupados, Tasa y Subocupación|
|  [Pág 2] Desocupación por Grupo Etario  -> Transición por tramos (16-17, 18-20, 21-24, 25-28)      |
|  [Pág 3] Educación y Desocupación       -> Nivel educativo, años de estudio y asistencia          |
|  [Pág 4] Brechas de Género y Territorio -> Brecha Mujer vs. Hombre y distribución departamental   |
|  [Pág 5] Perfil del Joven Desocupado    -> Caracterización Cesantes vs. Aspirantes (Primer Empleo) |
|  [Pág 6] Hallazgos y Recomendaciones    -> Matriz estratégica para políticas de inserción laboral  |
+---------------------------------------------------------------------------------------------------+
```

---

## 2. Paleta de Colores y Estilo Visual (USFX CEPI)

- **Azul Primario (Institucional USFX):** `#0f2c59` (Encabezados, tarjetas maestras, barras principales).
- **Rojo Carmesí (Alerta Desocupación / USFX):** `#8b0000` o `#d9534f` (Indicadores de desocupados, brechas negativas).
- **Dorado / Ocre (Acento USFX):** `#c59b27` (Líneas de tendencia, KPIs destacados).
- **Verde Ocupación:** `#2e7d32` (Población ocupada).
- **Púrpura / Lila (Aspirantes):** `#8e44ad` (Primer empleo).
- **Naranja (Cesantes):** `#e67e22` (Pérdida de empleo).
- **Fondo General del Canvas:** `#f8f9fa` (Gris tenue, reduce fatiga visual y da acabado limpio).
- **Tipografía:** Segoe UI o Inter (Títulos en Negrita 16-20pt, KPIs 24-28pt, Textos 10-11pt).

---

## 3. Especificación Detallada por Página

### 3.1 Página 1: Panorama Laboral Juvenil (Bolivia Urbana 4T-2025)
- **Fila Superior de KPIs (Cards):**
  1. `[PEA Juvenil Ponderada]` (1.38M personas | Subtexto: 6.649 encuestados)
  2. `[Poblacion Ocupada]` (1.33M personas | 96.29%)
  3. `[Poblacion Desocupada]` (51.2K personas | 3.71%)
  4. `[Tasa Desocupacion Ponderada]` (3.71% | Comparativo: Urbana general 2.3%)
  5. `[Tasa Subocupacion Ponderada]` (8.70% | Presión laboral cualitativa)
- **Visualizaciones:**
  - *Gráfico de Donut / Barra 100%:* Distribución de la PEA juvenil (Ocupados vs. Desocupados).
  - *Gráfico de Barras Agrupadas:* Comparativa de Tasa de Desocupación: Juvenil (3.71%) vs. Total Urbano (2.30%).
  - *Segmentadores Laterales:* Departamento, Sexo y Rango de Edad.

### 3.2 Página 2: Desocupación por Grupo Etario (Transición a la Vida Laboral)
- **Propósito:** Evidenciar cómo la desocupación golpea con mayor intensidad al egresar de secundaria (18 a 20 años).
- **Visualizaciones:**
  - *Gráfico de Columnas Clúster:* Tasa de desocupación por tramo etario (16-17: 1.87% | 18-20: 4.65% | 21-24: 3.55% | 25-28: 3.88%).
  - *Gráfico de Área Apilada / Barras:* Volumen absoluto de desocupados por tramo etario.
  - *Tarjeta Dinámica:* Tramo con mayor vulnerabilidad relativa (18-20 años).

### 3.3 Página 3: Educación y Desocupación (Capital Humano)
- **Propósito:** Analizar la relación entre el nivel educativo alcanzado y la inserción laboral.
- **Visualizaciones:**
  - *Gráfico de Barras Horizontales:* Tasa de desocupación según Nivel Educativo (Primaria, Secundaria, Técnico, Universitario).
  - *Gráfico de Dispersión / Boxplot conceptual:* Años de estudio vs. Tasa de desocupación.
  - *Matriz:* Cruce de Nivel Educativo $\times$ Tramo Etario.

### 3.4 Página 4: Brechas de Género y Territorio
- **Propósito:** Mostrar la doble disparidad que enfrentan las mujeres jóvenes y las diferencias entre ciudades intermedias y el eje central.
- **Visualizaciones:**
  - *Tarjeta KPI Comparativa:* Tasa Desocupación Mujeres (4.69%) vs. Hombres (2.85%) $\rightarrow$ Brecha de $+1.84$ pp.
  - *Mapa de Formas / Gráfico de Barras Horizontales:* Tasa por departamento (Chuquisaca 5.80%, Tarija 4.72%, Cochabamba 4.71%, La Paz 3.84%, Santa Cruz 3.33%, etc.).

### 3.5 Página 5: Perfil del Joven Desocupado (Cesantes vs. Aspirantes)
- **Propósito:** Caracterizar a quienes perdieron un empleo previo frente a quienes buscan por primera vez.
- **Visualizaciones:**
  - *Donut Chart:* Proporción Cesantes (89.6%) vs. Aspirantes (10.4%).
  - *Gráfico de Columnas Clúster:* Distribución de Aspirantes vs. Cesantes por Grupo Etario.
  - *Tabla Detallada:* Principales ramas y ocupaciones de inserción previa.

### 3.6 Página 6: Hallazgos y Recomendaciones Estratégicas
- **Propósito:** Síntesis ejecutiva de hallazgos estadísticos y propuesta de valor para políticas públicas.
- **Visualizaciones:**
  - *Matriz de Hallazgos:* Eje | Métrica Clave | Implicancia de Política Pública.
  - *Tarjetas de Recomendaciones:*
    1. Programa de inserción y primer empleo focalizado en jóvenes de 18 a 20 años.
    2. Políticas activas con enfoque de género para reducir la brecha de 1.84 pp.
    3. Fortalecimiento de la intermediación laboral en departamentos de alta presión (Chuquisaca, Tarija).
