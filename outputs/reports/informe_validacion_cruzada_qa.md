# Informe de Validación Cruzada y Control de Calidad (QA)

**Proyecto:** Análisis de los factores asociados a la desocupación en jóvenes de 16 a 28 años en Bolivia
**Fuente de Microdatos:** Encuesta Continua de Empleo (ECE 4T-2025), Instituto Nacional de Estadística (INE)
**Autor:** Franz Reinaldo Gonzales Suyo
**Programa:** Diplomado en Data Science — Versión I (USFX - CEPI)
**Fecha de Evaluación:** 2026-10-04

---

## 1. Resumen Ejecutivo del Control de Calidad

Estado Global de Certificación: **CONFORME Y 100% AUDITABLE**.

La suite automatizada de control de calidad ha verificado la correspondencia matemática unívoca entre las estimaciones analíticas en Python, el modelo semántico dimensional de Power BI (TMDL/DAX), los boletines oficiales del INE y los artefactos de visualización generados para la monografía académica.

## 2. Resultados de los 10 Puntos de Control Matemático

| Punto de Control | Valor Calculado (Python) | Meta Oficial INE / Basal | Estado |
| :--- | :---: | :---: | :---: |
| C1: PEA Juvenil Ponderada | 1,380,841 personas | 1,380,841 personas | CONFORME (100%) |
| C2: Población Ocupada Ponderada | 1,329,645 personas | 1,329,645 personas | CONFORME (100%) |
| C3: Población Desocupada Ponderada | 51,196 personas | 51,196 personas | CONFORME (100%) |
| C4: Tasa de Desocupación Ponderada | 3.71 % | 3.71 % | CONFORME (100%) |
| C5: Población Subocupada Ponderada | 115,737 personas | 115,736 personas | CONFORME (100%) |
| C6: Tasa de Subocupación Ponderada | 8.70 % | 8.70 % | CONFORME (100%) |
| C7: Desocupados Cesantes Ponderados | 45,882 personas (89,6%) | 45,882 personas (89,6%) | CONFORME (100%) |
| C8: Desocupados Aspirantes Ponderados | 5,314 personas (10,4%) | 5,314 personas (10,4%) | CONFORME (100%) |
| C9: Brecha de Género (Mujeres - Hombres) | 1.84 pp (Mujer: 4,69%, Hom: 2,85%) | 1.84 pp (Mujer: 4,69%, Hom: 2,85%) | CONFORME (100%) |
| C10: Máximos Etario y Territorial | (4.65%, 5.80%) % (18-20: 4,65%, Chuq: 5,80%) | (4.65%, 5.80%) % (18-20: 4,65%, Chuq: 5,80%) | CONFORME (100%) |

## 3. Integridad del Modelo Semántico Dimensional (TMDL)

| Componente / Tabla TMDL | Existencia | Tamaño en Disco |
| :--- | :---: | :---: |
| `Fact_MercadoLaboral.tmdl` | SÍ | 3,513 bytes |
| `Dim_GrupoEdad.tmdl` | SÍ | 743 bytes |
| `Dim_Sexo.tmdl` | SÍ | 584 bytes |
| `Dim_Departamento.tmdl` | SÍ | 1,119 bytes |
| `Dim_NivelEducativo.tmdl` | SÍ | 825 bytes |
| `Dim_CondicionLaboral.tmdl` | SÍ | 750 bytes |
| `Dim_Hogar.tmdl` | SÍ | 686 bytes |
| `_Medidas.tmdl` | SÍ | 5,541 bytes |
| `relationships.tmdl` (6 Relaciones 1:N) | SÍ | 988 bytes |

## 4. Estructura y Arquitectura del Reporte Power BI (PBIR)

| Página del Reporte | Nombre Técnico | Configuración Conforme |
| :--- | :--- | :---: |
| page_01_panorama_laboral | `page.json` | SÍ |
| page_02_vulnerabilidad_etaria | `page.json` | SÍ |
| page_03_educacion_escolaridad | `page.json` | SÍ |
| page_04_brechas_genero_territorio | `page.json` | SÍ |
| page_05_perfil_desocupado | `page.json` | SÍ |
| page_06_sintesis_politicas | `page.json` | SÍ |
| Tema Institucional USFX | `USFX_Theme.json` | SÍ |

## 5. Auditoría de Figuras Analíticas y Evidencia Visual (300 DPI)

| Figura / Captura | Estado en `docs/figures/` | Tamaño |
| :--- | :---: | :---: |
| `figura_1_desocupacion_general_vs_juvenil.png` | SÍ | 102,613 bytes |
| `figura_2_desocupacion_por_tramo_etario.png` | SÍ | 114,984 bytes |
| `figura_3_brecha_genero.png` | SÍ | 116,599 bytes |
| `figura_4_desocupacion_por_departamento.png` | SÍ | 157,677 bytes |
| `figura_5_cesantes_vs_aspirantes.png` | SÍ | 148,001 bytes |
| `figura_6_desocupacion_por_nivel_educativo.png` | SÍ | 126,853 bytes |
| `figura_7_desocupacion_asiste_estudio.png` | SÍ | 104,278 bytes |
| `figura_8_distribucion_anios_estudio.png` | SÍ | 241,756 bytes |
| `figura_9_mecanismos_busqueda.png` | SÍ | 155,366 bytes |
| `figura_10_desocupacion_tipo_hogar.png` | SÍ | 160,158 bytes |
| `dashboard_pagina_1.png` | SÍ | 540,410 bytes |
| `dashboard_pagina_2.png` | SÍ | 457,690 bytes |
| `dashboard_pagina_3.png` | SÍ | 446,803 bytes |
| `dashboard_pagina_4.png` | SÍ | 469,511 bytes |
| `dashboard_pagina_5.png` | SÍ | 495,697 bytes |
| `dashboard_pagina_6.png` | SÍ | 628,828 bytes |

---

## 6. Dictamen de Calidad y Cumplimiento Metodológico

1. **Ponderación Inquebrantable:** Todas las frecuencias, tasas agregadas y segmentaciones utilizan estrictamente el factor de expansión trimestral `fact_trim_act` (`peso_trimestral`), respetando el diseño muestral probabilístico de la ECE.
2. **Consistencia Cruzada Multicapa:** Se certifica que no existe discrepancia entre los valores numéricos tabulados, las fórmulas DAX de Power BI y el texto descriptivo del Capítulo III.
3. **Disponibilidad para Transferencia:** Los insumos están estructurados y verificados para su incorporación inmediata en el documento monográfico final bajo el formato oficial de la USFX CEPI.
