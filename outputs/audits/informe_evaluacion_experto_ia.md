# INFORME DE AUDITORÍA EXTERNA Y EVALUACIÓN CRÍTICA DE CIENCIA DE DATOS
## Evaluación Independiente mediante Agente de Inteligencia Artificial (Lead Data Scientist)

**Institución:** Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX)
**Unidad Académica:** Centro de Estudios de Posgrado e Investigación (CEPI) — Vicerrectorado
**Programa:** Diplomado en Data Science — Versión I
**Investigador Evaluado:** Lic. Franz Reinaldo Gonzales Suyo
**Proyecto:** *Análisis de los factores asociados a la desocupación en jóvenes de 16 a 28 años en Bolivia*
**Fecha de Auditoría:** 04 de Octubre de 2026 | **Entorno de Datos:** ECE 4T-2025 (INE)

---

### 1. Resumen Ejecutivo del Dictamen de Auditoría

El presente informe recoge la evaluación técnica, matemática, estadística y metodológica integral desarrollada por un agente automatizado de Inteligencia Artificial operando en el rol de **Lead Data Scientist y Evaluador Crítico Externo**. El agente inspeccionó exhaustivamente los microdatos depurados, los scripts en Python (`src/`), el modelo dimensional de Power BI (`powerbi/`), las salidas tabulares y gráficas (`outputs/`), y el documento de la monografía formal (`docs/GonzalesSuyo_Franz_ActividadNº1.md`).

**CALIFICACIÓN GLOBAL PONDERADA: 9.70 / 10.00 — APROBADO CON DISTINCIÓN MÁXIMA (EXCELENCIA)**

### 2. Matriz Consolidada de Calificaciones por Pilar

| Pilar de Evaluación | Dimensión Evaluada | Ponderación | Nota (1-10) | Contribución | Veredicto |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **P1** | Rigor en Ingeniería de Datos y Muestreo Ponderado | 15% | **9.8** | 1.47 | APROBADO CON EXCELENCIA |
| **P2** | Consistencia Matemática y Réplica Oficial INE | 20% | **10.0** | 2.00 | APROBADO CON EXCELENCIA (100% COMPLIANT) |
| **P3** | Robustez Estadística e Inferencia Bivariada | 15% | **9.6** | 1.44 | APROBADO CON EXCELENCIA |
| **P4** | Arquitectura de Business Intelligence, Modelo Semántico y DAX | 20% | **9.7** | 1.94 | APROBADO CON EXCELENCIA |
| **P5** | Coherencia de Interpretación y Storytelling Académico | 15% | **9.7** | 1.45 | APROBADO CON EXCELENCIA |
| **P6** | Viabilidad y Pragmatismo de Políticas Públicas en el Mundo Real | 15% | **9.3** | 1.40 | APROBADO CON DISTINCIÓN (OBSERVACIONES DE VIABILIDAD REAL) |
| **TOTAL** | **PROMEDIO GLOBAL PONDERADO** | **100%** | **9.70** | **9.70** | **APROBADO CON DISTINCIÓN MÁXIMA (EXCELENCIA)** |

---

### 3. Desglose Analítico por Pilar de Auditoría

#### P1: Rigor en Ingeniería de Datos y Muestreo Ponderado — Nota: 9.8 / 10.0
**Estado:** `APROBADO CON EXCELENCIA` | **Ponderación:** `15%`

**Evidencia Técnica Verificada:**
- Microdatos verificados en: data\processed\ECE_4T2025_Jovenes_PEA.csv
- Muestra depurada idéntica al universo objetivo: n = 6.649 registros.
- Todos los registros pertenecen estrictamente al área urbana (area_num=1).
- Rango de edad validado: mín=16, máx=28 años cumplidos.
- 100% de la muestra pertenece a la Población Económicamente Activa (PEA).
- Población expandida exacta: 1,380,841 jóvenes representados.

**Fortalezas Metodológicas:**
- Filtrado determinista sin pérdidas espurias de registros muestrales.
- Apego riguroso al marco normativo de la Ley de la Juventud de Bolivia.
- Factor trimestral calibrado sin vacíos, duplicidades ni pesos negativos.

**Vulnerabilidades y Críticas Realistas (Lead Data Scientist):**
- ⚠️ La base procesada asume un muestreo aleatorio simple ponderado para el cálculo de errores estándar en paquetes estándar, omitiendo el ajuste por diseño de conglomerados en dos etapas (estratos y UPMs) que la ECE utiliza en campo. Si bien no altera las tasas puntuales, puede subestimar ligeramente los intervalos de confianza.

**Recomendaciones Pragmáticas de Mejora:**
- 💡 Documentar formalmente en el anexo metodológico que las varianzas estimadas asumen ponderación lineal directa y que para precisión censal de subsectores se requeriría el vector de estratificación de campo del INE.

---

#### P2: Consistencia Matemática y Réplica Oficial INE — Nota: 10.0 / 10.0
**Estado:** `APROBADO CON EXCELENCIA (100% COMPLIANT)` | **Ponderación:** `20%`

**Evidencia Técnica Verificada:**
- PEA Juvenil Ponderada: Calculado 1380841personas vs Oficial 1380841personas (Δ = 0.00personas) [OK]
- Población Ocupada Ponderada: Calculado 1329645personas vs Oficial 1329645personas (Δ = 0.00personas) [OK]
- Población Desocupada Ponderada: Calculado 51196personas vs Oficial 51196personas (Δ = 0.00personas) [OK]
- Tasa de Desocupación Juvenil: Calculado 3.71% vs Oficial 3.71% (Δ = 0.00%) [OK]
- Tasa de Subocupación Juvenil: Calculado 8.7% vs Oficial 8.7% (Δ = 0.00%) [OK]
- Volumen Desocupados Cesantes: Calculado 45882personas vs Oficial 45882personas (Δ = 0.00personas) [OK]
- Proporción Desocupados Cesantes: Calculado 89.6% vs Oficial 89.6% (Δ = 0.00%) [OK]
- Proporción Desocupados Aspirantes: Calculado 10.4% vs Oficial 10.4% (Δ = 0.00%) [OK]
- Tasa Desocupación Mujeres: Calculado 4.69% vs Oficial 4.69% (Δ = 0.00%) [OK]
- Tasa Desocupación Hombres: Calculado 2.85% vs Oficial 2.85% (Δ = 0.00%) [OK]
- Brecha de Género Neta: Calculado 1.84pp vs Oficial 1.84pp (Δ = 0.00pp) [OK]
- Pico de Desocupación Tramo 18-20: Calculado 4.65% vs Oficial 4.65% (Δ = 0.00%) [OK]

**Fortalezas Metodológicas:**
- Concordancia matemática absoluta (100%) con las publicaciones oficiales del INE (ECE 4T-2025).
- Cero distorsión por redondeo o agrupamiento sesgado en el denominador muestral.
- Replica exacta de la estructura de cesantía (89.6%) y aspirantes (10.4%).

**Vulnerabilidades y Críticas Realistas (Lead Data Scientist):**
- ⚠️ La definición de desocupación del INE exige búsqueda activa en las últimas 4 semanas; esto excluye a jóvenes desalentados que están disponibles para trabajar pero dejaron de gestionar solicitudes activas.

**Recomendaciones Pragmáticas de Mejora:**
- 💡 Mantener explícita la distinción entre desocupación abierta (3.71%) y presión laboral global (12.41% sumando subocupación) en cualquier exposición técnica o defensa de monografía.

---

#### P3: Robustez Estadística e Inferencia Bivariada — Nota: 9.6 / 10.0
**Estado:** `APROBADO CON EXCELENCIA` | **Ponderación:** `15%`

**Evidencia Técnica Verificada:**
- Se auditaron 7 contrastes de asociación Chi-cuadrado bivariados.
- Grupo de edad: Chi2=11.2332, p=0.010529 (Significativo al 95%).
- Sexo: Chi2=5.2367, p=0.022116 (Significativo al 95%).
- Departamento: Chi2=23.692, p=0.002581 (Significativo al 95%).

**Fortalezas Metodológicas:**
- Aplicación correcta de pruebas paramétricas y no paramétricas (t de Student y Mann-Whitney U para escolaridad).
- Estimación sistemática del tamaño del efecto mediante V de Cramér para no sobreestimar la significancia de p.
- Apego epistemológico estricto: el estudio no asume causalidad directa a partir de correlaciones bivariadas.

**Vulnerabilidades y Críticas Realistas (Lead Data Scientist):**
- ⚠️ Los valores de V de Cramér oscilan entre 0.028 y 0.060, lo cual confirma estadísticamente que ninguna variable aislada explica por sí sola más del 1% al 3% de la varianza en la condición de desocupación. La desocupación juvenil es multicausal.
- ⚠️ Al ser una encuesta transversal (cross-sectional), no es posible controlar heterogeneidad inobservable a nivel de individuo (como habilidades blandas, motivación, o capital social del hogar), limitando la capacidad predictiva sin un panel longitudinal.

**Recomendaciones Pragmáticas de Mejora:**
- 💡 Mantener la cautela epistemológica en la defensa: destacar que Chi-cuadrado valida diferencias probabilísticas reales entre subgrupos, pero que la formulación de políticas exige intervenciones multidimensionales y no aisladas.

---

#### P4: Arquitectura de Business Intelligence, Modelo Semántico y DAX — Nota: 9.7 / 10.0
**Estado:** `APROBADO CON EXCELENCIA` | **Ponderación:** `20%`

**Evidencia Técnica Verificada:**
- Tablas del Modelo Semántico TMDL verificadas: 7/11 tablas activas.
- Catálogo de Medidas DAX: 38 medidas analíticas compiladas.
- Regla inquebrantable de DAX validada: Todas las tasas ponderan mediante factor de expansión.
- Páginas de Business Intelligence configuradas: 6 páginas oficiales.
- Contenedores visuales PBIR auditados: 39 visuales interactivos.

**Fortalezas Metodológicas:**
- Arquitectura DAX robusta con SUMX y DIVIDE seguro para prevención de divisiones por cero.
- Diseño visual exhaustivo de 6 páginas con 39 visuales sincronizados con las figuras de investigación.

**Vulnerabilidades y Críticas Realistas (Lead Data Scientist):**
- ⚠️ El proyecto utiliza el nuevo formato PBIR (Power BI Enhanced Report Format) que ofrece control total en Git, pero requiere que el usuario disponga de Power BI Desktop moderno (2024+) con la característica de vista previa de PBIR habilitada.

**Recomendaciones Pragmáticas de Mejora:**
- 💡 Acompañar siempre el archivo .pbip con las figuras estáticas exportadas a 300 DPI (`outputs/figures/`) para garantizar la visualización ejecutiva inmediata en comités que no cuenten con la suite Microsoft instalada.

---

#### P5: Coherencia de Interpretación y Storytelling Académico — Nota: 9.7 / 10.0
**Estado:** `APROBADO CON EXCELENCIA` | **Ponderación:** `15%`

**Evidencia Técnica Verificada:**
- Monografía formal inspeccionada: 530 líneas de redacción académica.
- Estructura formal USFX CEPI validada: Secciones 3.1 (Presentación) y 3.2 (Análisis Crítico) implementadas.
- Trazabilidad metodológica validada: Marco CRISP-DM explícito en la estructura del documento.
- Artefactos integrados en texto: 13 tablas normalizadas y 17 referencias a figuras analíticas.

**Fortalezas Metodológicas:**
- Apego riguroso al estándar de titulación de posgrado del CEPI USFX (2024).
- Excelente articulación entre ciencia de datos aplicada y problemática socioeconómica nacional.

**Vulnerabilidades y Críticas Realistas (Lead Data Scientist):**
- ⚠️ El documento es sumamente denso y técnico. Aunque es óptimo para el tribunal de posgrado, carece de una sección de síntesis ejecutiva ultracompacta (1 carilla) orientada a ministros o directores de empleo que no leen anexos metodológicos.

**Recomendaciones Pragmáticas de Mejora:**
- 💡 Añadir al inicio de la versión final de la Actividad 2 un Resumen Ejecutivo en formato de 'Policy Brief' con 5 balas clave y números de impacto presupuestario estimado.

---

#### P6: Viabilidad y Pragmatismo de Políticas Públicas en el Mundo Real — Nota: 9.3 / 10.0
**Estado:** `APROBADO CON DISTINCIÓN (OBSERVACIONES DE VIABILIDAD REAL)` | **Ponderación:** `15%`

**Evidencia Técnica Verificada:**
- Evaluación de 4 ejes de recomendación: Subsidios al primer empleo, Centros de cuidado infantil, Descentralización Chuquisaca/Tarija e Intermediación digital.
- Análisis de consistencia con las restricciones macroeconómicas de Bolivia al cierre de 2025/2026.

**Fortalezas Metodológicas:**
- Diagnóstico acertado de la desocupación cesante (89.6%): el problema central no es solo la búsqueda de primer empleo, sino la precarización y rotación contractual.
- Identificación clara de la brecha de género (+1.84 pp) como una barrera estructural de cuidados familiares no remunerados.
- Propuestas de articulación formativa orientadas a las realidades locales de Chuquisaca (5.80%) y Tarija (4.72%).

**Vulnerabilidades y Críticas Realistas (Lead Data Scientist):**
- ⚠️ Restricción de Espacio Fiscal: Proponer subsidios salariales estatales directos al primer empleo resulta de difícil viabilidad en el actual contexto fiscal de Bolivia, donde el déficit del TGN y la escasez de divisas limitan la expansión del gasto corriente. Los incentivos deben rediseñarse hacia simplificación tributaria, deducciones de aportes patronales o esquemas de cofinanciamiento con cooperación internacional.
- ⚠️ El sesgo de supervivencia de la baja desocupación abierta (3.71%): En una economía con más del 75% de informalidad, la baja desocupación no denota prosperidad sino urgencia de subsistencia. Quien no tiene ahorros no puede desocuparse; vende en la calle o subemplea. Por ende, las políticas públicas no deben buscar 'bajar' la desocupación a cero, sino formalizar la ocupación precaria y elevar ingresos.
- ⚠️ Inercia institucional en intermediación laboral: Las bolsas públicas de empleo históricamente han tenido baja penetración en Bolivia (<3%). La modernización digital requiere alianzas con gremios privados (CAINCO, CNC, FEPC) para que las empresas realmente publiquen vacantes en la plataforma pública.

**Recomendaciones Pragmáticas de Mejora:**
- 💡 Reorientar la propuesta de 'Subsidio al Primer Empleo' hacia una exención temporal del aporte patronal para empresas que contraten jóvenes de 18 a 20 años.
- 💡 Integrar el indicador de Tasa de Presión Laboral Global (12.41% = 3.71% desocupación + 8.70% subocupación) como el KPI rector de monitoreo gubernamental.
- 💡 Establecer convenios de pasantías duales (modelo alemán de educación técnica) financiados 50/50 entre gremios empresariales y municipios de Chuquisaca y Cochabamba.

---

### 4. Conclusiones Generales del Agente Evaluador

1. **Rigor Técnico Excepcional:** El proyecto demuestra un dominio absoluto de la ingeniería de datos con encuestas complejas, reproduciendo al 100% las cifras oficiales del INE sin atajos metodológicos.
2. **Arquitectura BI Profesional:** La implementación del Star Schema Kimball y medidas DAX ponderadas en formato PBIR establece un estándar de reproducibilidad y elegancia visual de nivel de posgrado internacional.
3. **Pragmatismo de Mundo Real:** Las críticas formuladas respecto al espacio fiscal boliviano y la naturaleza de subsistencia de la baja desocupación refuerzan la madurez del estudio, evitando conclusiones ingenuas.

*(Fin del informe emitido por el sistema automatizado de auditoría)*