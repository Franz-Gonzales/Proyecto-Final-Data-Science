---
name: project-documentation
description: >-
  Procedimientos, directrices y plantillas para la redacción académica y formal de la monografía
  de posgrado (USFX CEPI), estructuración del Capítulo III (3.1 Presentación y 3.2 Análisis)
  y normas APA 7ma edición.
---

# Skill: Project Documentation & Redacción Académica CEPI (USFX)

Esta skill guía la redacción, estructuración y control de calidad metodológico del documento final de monografía del Diplomado en Data Science (USFX - CEPI), asegurando estricto apego al formato institucional de posgrado.

---

## 1. Identificación y Formato de Entrega

- **Título del Trabajo:** *Análisis de los factores asociados a la desocupación en jóvenes de 16 a 28 años en Bolivia*
- **Autor:** Gonzales Suyo Franz Reinaldo
- **Docente:** Ing. Marcelo Arancibia
- **Institución:** Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca — CEPI
- **Formato del archivo:** Microsoft Word (`.docx`).
- **Nomenclatura oficial:** `GonzalesSuyo_Franz_ActividadNº.docx` (Ejemplo: `GonzalesSuyo_Franz_Actividad1.docx`).
- **Extensión estimada:** ~50 páginas (desde Capítulo I hasta Recomendaciones inclusive).

---

## 2. Estructura Oficial de la Monografía (CEPI 2024)

```text
╭────────────────────────────────────────────────────────╮
│  PORTADA OFICIAL CEPI                                  │
│  RESUMEN / ABSTRACT (Palabras clave)                   │
│  ÍNDICES (Contenido, Tablas, Figuras)                  │
│                                                        │
│  CAPÍTULO I: INTRODUCCIÓN                              │
│     1.1. Antecedentes                                  │
│     1.2. Problema o asunto del trabajo                 │
│     1.3. Objetivo general                              │
│     1.4. Objetivos específicos                         │
│     1.5. Justificación                                 │
│     1.6. Enfoque Metodológico                          │
│                                                        │
│  CAPÍTULO II: MARCO REFERENCIAL                        │
│     2.1. Marco Teórico                                 │
│     2.2. Marco Contextual                              │
│                                                        │
│  CAPÍTULO III: RESULTADOS                              │
│     3.1. Presentación de resultados (Datos objetivos)  │
│     3.2. Análisis de Resultados (Interpretación)       │
│                                                        │
│  CONCLUSIONES Y RECOMENDACIONES                        │
│  REFERENCIAS BIBLIOGRÁFICAS (Normas APA 7ma ed.)       │
│  ANEXOS (Código Python, fichas técnicas, DAX)          │
╰────────────────────────────────────────────────────────╯
```

---

## 3. Estructura Obligatoria del Capítulo III (Hito Actividad 1)

El Capítulo III debe estructurarse obligatoriamente en dos grandes subsecciones:

### 3.1. Presentación de Resultados (Datos Objetivos, sin interpretación)
1. **Contexto metodológico:** Tabla de dimensión metodológica (enfoque cuantitativo, corte transversal 4T-2025, fuente ECE INE, factor de expansión, universo urbano 16-28 años, entorno Python y Power BI).
2. **Trazabilidad del desarrollo (CRISP-DM aplicado):** Evidencia del flujo de datos en 6 fases.
3. **Descripción del procesamiento de datos:** Registros iniciales (52.650) vs. muestra final (6.649) y población estimada (1.380.841).
4. **Resultados del análisis descriptivo:** Tablas y gráficos de tasas ponderadas por edad, sexo, educación y departamento.
5. **Resultados del análisis bivariado y de asociaciones:** Tablas de contingencia y resultados formales de $\chi^2$ de Pearson y V de Cramér.
6. **Dashboard en Power BI:** Capturas de alta resolución de las 6 páginas del tablero.

### 3.2. Análisis de Resultados (Interpretación Crítica)
1. **Interpretación por dimensión:** Discusión de los hallazgos en dimensión etaria, de género, educativa, territorial y de trayectoria previa.
2. **Implicaciones prácticas y de políticas públicas:** Recomendaciones de inserción laboral basadas en evidencia.
3. **Limitaciones encontradas:** Corte transversal, sesgos muestrales en ciudades intermedias, representatividad.
4. **Tabla consolidada de hallazgos:** Eje | Hallazgo Cuantitativo | Métrica Clave | Implicancia.

---

## 4. Estilo de Redacción y Formato APA 7ma Edición

- **Voz y Tono:** Tercera persona o voz impersonal (*"se analizó", "los datos evidencian", "se observa"*).
- **Tablas:** Encabezado superior con numeración formal (`TABLA N.º X: Título descriptivo en cursiva`). Notas al pie con la fuente (`FUENTE: Elaboración propia con base en microdatos de la ECE 4T-2025 (INE).`).
- **Figuras:** Gráficos limpios con título superior, etiquetas claras y fuente inferior.
- **Rigor Matemático:** Todos los porcentajes y poblaciones deben concordar estrictamente entre el código Python, el dashboard de Power BI y el texto de la monografía.
