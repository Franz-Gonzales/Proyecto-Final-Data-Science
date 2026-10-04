# PLAN INTEGRAL Y PROPUESTA DE IMPLEMENTACIÓN FINAL (FASES 4 A 6)

**Proyecto:** *Análisis de los factores asociados a la desocupación en jóvenes de 16 a 28 años en Bolivia*  
**Programa Académico:** Diplomado en Data Science — Versión I  
**Institución:** Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX)  
**Unidad de Posgrado:** Centro de Estudios de Posgrado e Investigación (CEPI) — Vicerrectorado  
**Autor / Investigador:** Franz Reinaldo Gonzales Suyo  
**Docente Coordinador:** Ing. Marcelo Arancibia  
**Sede y Gestión:** Sucre - Bolivia, 2026  
**Documento Estratégico:** Propuesta de Planteamiento Conceptual y Metodológico (Cero Código Técnico)

---

## 1. RESUMEN EJECUTIVO Y PROPÓSITO DEL PLAN

El presente documento constituye la **Propuesta de Planteamiento Estratégico y Conceptual** para el desarrollo de las fases finales del proyecto de monografía (Fases 4, 5 y 6), articuladas bajo la metodología estándar CRISP-DM y las directrices académicas del CEPI de la Universidad San Francisco Xavier de Chuquisaca.

El propósito principal es establecer con máxima rigurosidad, claridad y visión analítica la ruta que permitirá culminar el proyecto con los más altos estándares profesionales de la Ciencia de Datos y la Inteligencia de Negocios (Business Intelligence), traduciendo el análisis estadístico previo en herramientas interactivas de decisión y en un reporte académico formal de alto impacto.

### 1.1. Balance de la Línea Base Alcanzada (Fases 1 a 3)
El proyecto cuenta con una base metodológica y estadística sólida, validada y reproducible:
*   **Fase 1 (Comprensión y Preparación de Microdatos):** Se procesó la base oficial de la Encuesta Continua de Empleo (ECE 4T-2025) del INE, delimitando mediante tres filtros analíticos sucesivos (área urbana, 16 a 28 años y condición de PEA) una muestra efectiva de **6.649 registros** que, calibrada mediante el factor de expansión trimestral (`peso_trimestral`), representa a **1.380.841 jóvenes** en el mercado laboral urbano.
*   **Fase 2 (Análisis Descriptivo Univariado Ponderado):** Se replicaron con precisión matemática los indicadores del Boletín Oficial del INE: Tasa de Desocupación Juvenil de **3,71%** (frente al 2,30% general urbano) y Tasa de Subocupación Juvenil de **8,70%** (115.736 jóvenes subutilizados).
*   **Fase 3 (Análisis Bivariado y Pruebas de Asociación):** Se comprobaron relaciones estadísticamente significativas mediante pruebas Chi-cuadrado y V de Cramér:
    *   *Vulnerabilidad etaria:* Pico en el tramo de 18 a 20 años con una desocupación de **4,65%** ($p = 0,0105$).
    *   *Brecha de género:* Tasa en mujeres de **4,69%** frente a **2,85%** en varones, una brecha absoluta de $+1,84$ puntos porcentuales ($p = 0,0221$).
    *   *Disparidad territorial:* Chuquisaca lidera la desocupación nacional con **5,80%**, seguida de Tarija con **4,72%** y Cochabamba con **4,71%** ($p = 0,0026$).
    *   *Paradoja del desempleo ilustrado:* Mayor escolaridad acumulada en desocupados (**13,01 años**) frente a ocupados (**12,64 años**), con significancia estadística comprobada ($p = 0,0174$).
    *   *Trayectoria de cesantía:* El **89,62%** de los jóvenes desocupados son cesantes (con empleo previo) y solo el **10,38%** son aspirantes (primer empleo).

### 1.2. Alcance y Objetivos de las Fases Finales (4 a 6)
Las tres fases que completan la investigación se estructuran de la siguiente manera:
1.  **FASE 4: Construcción del Dashboard Interactivo en Power BI (Fase 6 de CRISP-DM — Despliegue):** Diseño e implementación de un cuadro de mando analítico de 6 páginas en formato PBIP (`Visualizacion-Analisis-Desocupacion.pbip`), estructurado sobre un modelo dimensional en estrella (*Star Schema*), con un catálogo completo de medidas DAX ponderadas, paneles de KPIs, gráficos dinámicos y narrativa visual adaptada a la identidad institucional de la USFX.
2.  **FASE 5: Protocolo de Validación y Control de Calidad (Fase 5 de CRISP-DM — Evaluación):** Proceso formal de contrastación cruzada entre los resultados de Python, las medidas del modelo Power BI y las publicaciones oficiales del INE, garantizando consistencia absoluta, ausencia de distorsiones por recuentos no expandidos y reproducibilidad integral.
3.  **FASE 6: Redacción Académica y Consolidación del Capítulo III:** Actualización, estructuración y cierre del documento oficial `GonzalesSuyo_Franz_ActividadNº1.md` conforme a la Guía CEPI 2024 y normas APA 7ma edición, integrando la evidencia visual del dashboard, el análisis crítico por dimensiones, las implicaciones para políticas públicas y la matriz formal de hallazgos, aplicando criterios de redacción natural y académica libre de modismos o sesgos de inteligencia artificial.

---

## 2. FASE 4: CONSTRUCCIÓN DEL DASHBOARD ANALÍTICO EN POWER BI (DESPLIEGUE CRISP-DM)

### 2.1. Propósito y Enfoque de Negocio
El dashboard en Power BI tiene como propósito principal transformar las tablas estadísticas y los microdatos tabulados en una plataforma visual interactiva orientada a la toma de decisiones basada en evidencia. 

A diferencia de una simple colección de gráficos estáticos, el tablero debe permitir que planificadores gubernamentales, directivos universitarios, investigadores sociolaborales y tomadores de decisiones exploren la desocupación juvenil desde múltiples perspectivas (demográfica, educativa, territorial y de trayectoria laboral), identifiquen los grupos de mayor vulnerabilidad y evalúen escenarios para la formulación de políticas públicas de empleo.

### 2.2. Arquitectura de Datos: Modelo Dimensional en Estrella (Star Schema)
Para asegurar máximo rendimiento en el motor tabular de Power BI (VertiPaq) y facilitar la navegación analítica, los datos procesados en Python se organizarán en una arquitectura dimensional en estrella normalizada. 

El modelo separa los registros observados de las entidades de contexto, garantizando que los filtros aplicados en cualquier dimensión se propaguen de forma natural hacia las métricas agregadas:

```text
                               +------------------------+
                               |     Dim_GrupoEdad      |
                               |  - grupo_edad (PK)     |
                               |  - OrdenEtario         |
                               +-----------+------------+
                                           | 1
                                           | 
                                           | *
+----------------------+ 1      * +--------+---------------+ *      1 +------------------------+
|       Dim_Sexo       +----------+   Fact_MercadoLaboral   +----------+   Dim_NivelEducativo   |
|  - sexo_cod (PK)     |          |  (Microdatos ECE 4T)    |          |  - niv_ed_cod (PK)     |
|  - Sexo              |          |  - id_persona (PK)      |          |  - NivelEducativo      |
+----------------------+          |  - peso_trimestral      |          |  - OrdenEducativo      |
                                  |  - banderas laborales   |          +------------------------+
+----------------------+ 1      * |  - anios_estudio        | *      1 +------------------------+
|   Dim_Departamento   +----------+                         +----------+  Dim_CondicionLaboral  |
|  - depto_cod (PK)    |          +--------+---------------+          |  - condact_cod (PK)    |
|  - Departamento      |                   | *                         |  - CondicionDetallada  |
|  - RegionGeografica  |                   |                           +------------------------+
+----------------------+                   | 1
                               +-----------+------------+
                               |        Dim_Hogar       |
                               |  - tipohogar_cod (PK)  |
                               |  - TipoHogar           |
                               +------------------------+
```

#### Entidades y Componentes del Modelo:
1.  **Tabla de Hechos (`Fact_MercadoLaboral`):**
    *   *Granularidad:* Una fila por cada persona joven encuestada (6.649 registros).
    *   *Columnas clave y atributos métricos:* Identificador de persona, factor de expansión muestral (`peso_trimestral`), indicadores binarios de condición laboral (ocupado, desocupado, subocupado por tiempo, cesante, aspirante), años de escolaridad acumulados (`anios_estudio`) y claves foráneas hacia las dimensiones.
2.  **Dimensión Grupo Etario (`Dim_GrupoEdad`):**
    *   Segmentación analítica oficial: 16-17 años (adolescentes), 18-20 años (transición bachillerato/primer empleo), 21-24 años (formación superior) y 25-28 años (consolidación laboral). Incluye columna de orden para clasificación secuencial cronológica.
3.  **Dimensión Sexo (`Dim_Sexo`):**
    *   Código oficial y etiqueta clara (Hombre / Mujer) para el análisis de brechas estructurales.
4.  **Dimensión Departamento y Territorio (`Dim_Departamento`):**
    *   Los 9 departamentos de Bolivia codificados según nomenclatura oficial del INE, complementados con la agrupación macro-regional (Valles, Altiplano, Llanos) para análisis agregado.
5.  **Dimensión Educativa (`Dim_NivelEducativo`):**
    *   Clasificación pedagógica estandarizada (Primaria, Secundaria, Técnico, Universitario, Sin instrucción) ordenada jerárquicamente por nivel formativo.
6.  **Dimensión Condición Laboral y Trayectoria (`Dim_CondicionLaboral`):**
    *   Detalle cualitativo del estado de actividad: Ocupado, Desocupado Cesante (con experiencia laboral previa) y Desocupado Aspirante (en búsqueda de primera inserción laboral).
7.  **Dimensión Hogar y Entorno Familiar (`Dim_Hogar`):**
    *   Tipología familiar de residencia (hogar monoparental, biparental con hijos, extendido, compuesto, unipersonal) para evaluar la red de contención económica y cargas de cuidado.

### 2.3. Catálogo Conceptual de Medidas Analíticas (Lógica DAX Ponderada)
En cumplimiento de las normas estadísticas oficiales, **se prohíbe el uso de recuentos directos de filas** para reportar volúmenes poblacionales o porcentajes. El tablero implementará una tabla dedicada exclusivamente a medidas organizadas en carpetas temáticas:

#### A. Medidas de Volumen Poblacional (Expandidas con Factor de Expansión):
*   **PEA Juvenil Ponderada:** Estimación del tamaño total de la fuerza de trabajo juvenil urbana (meta oficial: 1.380.841 jóvenes).
*   **Población Ocupada Juvenil:** Número total de jóvenes urbanos insertos activamente en la producción de bienes o servicios (meta oficial: 1.329.645 jóvenes).
*   **Población Desocupada Juvenil:** Número total de jóvenes sin trabajo que realizan gestiones activas de búsqueda (meta oficial: 51.196 jóvenes).
*   **Población Subocupada por Tiempo:** Jóvenes ocupados que trabajan menos de 40 horas a la semana, desean trabajar más horas y están disponibles para hacerlo (meta oficial: 115.736 jóvenes).
*   **Desocupados Cesantes:** Volumen de jóvenes sin empleo que registran desvinculación laboral reciente (meta oficial: 45.882 personas; 89,62% del total de desocupados).
*   **Desocupados Aspirantes:** Volumen de jóvenes en búsqueda de su primera oportunidad laboral (meta oficial: 5.314 personas; 10,38% del total de desocupados).

#### B. Tasas Analíticas Clave (Porcentajes Ponderados):
*   **Tasa de Desocupación Juvenil (%):** Razón entre la población desocupada ponderada y la PEA juvenil ponderada (meta oficial: 3,71%).
*   **Tasa de Subocupación Juvenil (%):** Razón entre la población subocupada por tiempo y la población ocupada juvenil ponderada (meta oficial: 8,70%).
*   **Tasa Comparativa Urbana General (%):** Indicador de referencia nacional para personas de 14 años o más (2,30%), permitiendo calcular dinámicamente el ratio de sobreexposición juvenil (1,61 veces).
*   **Tasa de Desocupación por Sexo (Mujeres y Hombres):** Indicadores desagregados para medir la brecha absoluta (Mujeres: 4,69% vs. Varones: 2,85%).
*   **Brecha de Género en Puntos Porcentuales:** Medida calculada que resta la tasa masculina de la tasa femenina ($+1,84$ pp).

#### C. Medidas de Soporte Técnico y Calidad:
*   **Muestra Muestral Observada:** Conteo simple de encuestados efectivos ($n = 6.649$) utilizado exclusivamente como indicador de confiabilidad muestral en tarjetas secundarias o tooltips.
*   **Años de Estudio Promedio Ponderado:** Media aritmética de escolaridad expandida por el ponderador muestral, discriminando entre ocupados (12,64 años) y desocupados (13,01 años).

---

### 2.4. Arquitectura de las 6 Páginas del Tablero y Storytelling Analítico

El tablero se estructurará en **6 páginas interactivas**, diseñadas con base en una secuencia narrativa lógica que va desde la visión macroeconómica general hacia los determinantes específicos, culminando en la toma de decisiones:

```text
+----------------------------------------------------------------------------------------------------+
|               ARQUITECTURA DE PÁGINAS DEL DASHBOARD EN POWER BI DESKTOP                            |
+----------------------------------------------------------------------------------------------------+
| Pág 1: Panorama Laboral Juvenil       -> Visión Macro, PEA, Desocupados, Tasas y Subocupación     |
| Pág 2: Vulnerabilidad Etaria          -> Transición 16-17, 18-20 (pico), 21-24, 25-28 años        |
| Pág 3: Educación y Escolaridad        -> Capital humano, paradoja del desempleo ilustrado          |
| Pág 4: Brechas de Género y Territorio -> Brecha mujer/varón (+1.84 pp) y ranking departamental    |
| Pág 5: Perfil del Joven Desocupado    -> Cesantes vs. Aspirantes, canales de búsqueda y hogares   |
| Pág 6: Síntesis y Recomendaciones     -> Matriz ejecutiva para políticas públicas de empleo        |
+----------------------------------------------------------------------------------------------------+
```

#### Especificación Detallada por Página:

#### 1. Página 1: Panorama Laboral Juvenil en Bolivia Urbana (Macroindicadores)
*   **Objetivo:** Ofrecer una visión integral y ejecutiva del estado del mercado laboral juvenil al cuarto trimestre de 2025.
*   **Panel Superior de KPIs (Tarjetas visuales con formato numérico formateado):**
    1.  *PEA Juvenil:* 1.380.841 personas (subtexto: Muestra efectiva $n = 6.649$).
    2.  *Población Ocupada:* 1.329.645 personas (96,29% de la PEA).
    3.  *Población Desocupada:* 51.196 personas (3,71% de la PEA).
    4.  *Tasa de Desocupación Juvenil:* 3,71% (con indicador de comparación frente al 2,30% general urbano).
    5.  *Tasa de Subocupación:* 8,70% (115.736 jóvenes subutilizados).
*   **Visualizaciones Principales:**
    *   *Gráfico de Donut:* Distribución porcentual de la PEA juvenil (Ocupados 96,29% vs. Desocupados 3,71%).
    *   *Gráfico de Barras Agrupadas:* Comparativa de la desocupación: Juventud urbana (3,71%) frente al Total nacional urbano (2,30%), destacando que los jóvenes duplican la incidencia de desocupación adulta.
    *   *Gráfico de Barras de Composición Interna:* Subocupación y desocupación abierta como componentes de la subutilización laboral.
*   **Filtros y Segmentadores Globales:**
    *   Menú desplegable de Departamento, Selector de Sexo (Botones) y Selector de Rango de Edad.

#### 2. Página 2: Vulnerabilidad Etaria y Transición a la Vida Laboral
*   **Objetivo:** Evidenciar cómo la desocupación golpea con diferente intensidad según el ciclo vital, identificando el punto crítico de fricción laboral.
*   **KPIs de Cabecera:**
    *   Tasa en tramo crítico (18 a 20 años): **4,65%**.
    *   Volumen de desocupados en 18 a 20 años: **13.504 jóvenes**.
    *   Diferencia respecto a la tasa nacional: $+0,94$ puntos porcentuales por encima del promedio.
*   **Visualizaciones:**
    *   *Gráfico de Columnas Clúster:* Tasa de desocupación según los 4 tramos etarios (16-17 años: 1,87%; 18-20 años: 4,65%; 21-24 años: 3,55%; 25-28 años: 3,88%).
    *   *Gráfico de Cascada o Área Apilada:* Distribución del volumen absoluto de jóvenes desocupados por tramo etario (resaltando que el grupo de 25-28 años concentra 19.988 desocupados por su mayor masa poblacional).
    *   *Panel de Texto Dinámico:* Diagnóstico de la transición bachillerato-trabajo y ausencia de experiencia laboral en el tramo 18-20 años.

#### 3. Página 3: Educación, Escolaridad y la Paradoja del Desempleo Ilustrado
*   **Objetivo:** Analizar la asociación entre el nivel educativo alcanzado, la asistencia a centros formativos y la probabilidad de encontrarse desocupado.
*   **KPIs de Cabecera:**
    *   Años promedio de escolaridad en desocupados: **13,01 años**.
    *   Años promedio de escolaridad en ocupados: **12,64 años**.
    *   Diferencia promedio de capital humano: $+0,37$ años (significancia $p = 0,0174$).
*   **Visualizaciones:**
    *   *Gráfico de Barras Horizontales:* Tasa de desocupación según máximo nivel educativo alcanzado (Sin instrucción: 2,31%, Primaria: 3,43%, Secundaria: 4,02%, Superior Universitario: 4,04%).
    *   *Gráfico de Barras Bivariado:* Tasa de desocupación según condición de asistencia escolar (Asiste: 3,54% vs. No asiste: 3,92%).
    *   *Gráfico de Densidad / Barras de Distribución:* Comparativa de la distribución de años de escolaridad acumulados entre jóvenes con y sin empleo.
    *   *Tarjeta de Interpretación Teórica:* Breve explicación del desajuste entre la oferta formativa universitaria y la demanda de perfiles en las empresas urbanas.

#### 4. Página 4: Brechas Estructurales de Género y Disparidades Territoriales
*   **Objetivo:** Visibilizar la desventaja laboral sistemática de las mujeres jóvenes y la heterogeneidad entre regiones del país.
*   **KPIs de Cabecera:**
    *   Tasa en Mujeres: **4,69%** (30.258 desocupadas).
    *   Tasa en Varones: **2,85%** (20.938 desocupados).
    *   Brecha de Género: **+1,84 pp** (las mujeres representan el 59,10% del total de desocupados a pesar de ser minoría en la PEA).
    *   Departamento con mayor desocupación: **Chuquisaca (5,80%)**.
*   **Visualizaciones:**
    *   *Tarjeta Visual Comparativa (Kardex de Género):* Tarjeta dividida Hombre vs. Mujer con barras de participación relativa.
    *   *Gráfico de Barras Horizontales Ordenado (Ranking Departamental):* Tasas de desocupación juvenil en los 9 departamentos (Chuquisaca 5,80%, Tarija 4,72%, Cochabamba 4,71%, La Paz 3,84%, Santa Cruz 3,33%, Oruro 2,98%, Beni 2,07%, Pando 1,89%, Potosí 1,64%).
    *   *Gráfico de Barras Agrupadas 100%:* Concentración del volumen de desocupados en el Eje Troncal (La Paz, Cochabamba, Santa Cruz concentran el 78,5% del total de desocupados urbanos del país).

#### 5. Página 5: Perfil Operativo del Joven Desocupado (Cesantes, Aspirantes y Canales)
*   **Objetivo:** Caracterizar el origen del desempleo (pérdida de empleo anterior vs. barrera de entrada al primer empleo), los canales de búsqueda y la estructura familiar de contención.
*   **KPIs de Cabecera:**
    *   Desocupados Cesantes: **89,62%** (45.882 personas).
    *   Desocupados Aspirantes: **10,38%** (5.314 personas).
    *   Canal de Búsqueda Dominante: **Avisos digitales y redes sociales (38,82%)**.
*   **Visualizaciones:**
    *   *Gráfico de Donut:* Proporción de Cesantes vs. Aspirantes en la juventud urbana.
    *   *Gráfico de Columnas Agrupadas:* Aspirantes vs. Cesantes distribuidos por tramo etario (mostrando cómo los aspirantes se concentran casi en su totalidad en 16-17 y 18-20 años).
    *   *Gráfico de Barras Horizontales:* Principales canales utilizados para buscar empleo (Avisos digitales 38,82%, Presentación directa de currículum 31,62%, Otras formas 17,63%, Preguntó en lugares de trabajo 7,67%, Redes de familiares 2,28%).
    *   *Gráfico de Barras por Tipología de Hogar:* Desocupación según estructura del hogar (Monoparental 5,68%, Extendido 5,37%, Biparental con hijos 3,21%).

#### 6. Página 6: Síntesis Estratégica, Matriz de Hallazgos y Políticas Públicas
*   **Objetivo:** Sintetizar la evidencia cuantitativa en un cuadro de mando ejecutivo orientado a la formulación de recomendaciones de política laboral e intervenciones programáticas.
*   **Componentes Visuales:**
    *   *Matriz Interactiva de Hallazgos:* Tabla estructurada con 5 ejes analíticos:
        1.  *Eje Etario:* Pico en 18 a 20 años (4,65%) $\rightarrow$ Prioridad en programas de transición secundaria-trabajo y pasantías formativas remuneradas.
        2.  *Eje de Género:* Brecha de $+1,84$ pp en contra de la mujer $\rightarrow$ Servicios públicos de cuidado infantil urbano y combate a la segregación ocupacional.
        3.  *Eje Territorial:* Presión extrema en valles del sur (Chuquisaca 5,80%, Tarija 4,72%) $\rightarrow$ Diversificación productiva local, polos de economía digital y retención de talento.
        4.  *Eje Educativo:* Paradoja del desempleo ilustrado ($+0,37$ años en desocupados) $\rightarrow$ Articulación entre currículas universitarias y demanda del sector empresarial.
        5.  *Eje Trayectoria:* 9 de cada 10 desocupados son cesantes $\rightarrow$ Estabilidad en la contratación, formalización y reconversión técnica.
    *   *Tarjetas de Recomendaciones Estratégicas:* 3 bloques destacados con directrices de política pública fundamentadas directamente en los datos.

---

### 2.5. Sistema de Diseño Visual y Paleta Institucional (USFX CEPI)

Para asegurar una presentación estética de alto nivel que cause impacto visual y transmita seriedad académica, el diseño del tablero respetará estrictamente las pautas de estilo de la Universidad San Francisco Xavier:

*   **Paleta de Colores Curada:**
    *   *Azul Institucional Primario (`#0f2c59`):* Fondos de cabecera, títulos principales, barras maestras y tarjetas primarias.
    *   *Rojo Carmesí USFX (`#8b0000` / `#d9534f`):* Indicadores de desocupación, puntos de alerta, brecha desfavorable de género y tramo etario crítico.
    *   *Dorado / Ocre USFX (`#c59b27`):* Acentos visuales, líneas de promedio nacional, bordes de selección activa y resaltados.
    *   *Verde Ocupación (`#2e7d32`):* Indicadores de población ocupada y métricas de absorción favorable.
    *   *Púrpura / Amatista (`#8e44ad`):* Segmento de desocupados aspirantes (primer empleo).
    *   *Naranja Ámbar (`#e67e22`):* Segmento de desocupados cesantes (pérdida de empleo).
    *   *Fondo del Lienzo (`#f8f9fa`):* Gris tenue fuera del blanco puro, reduciendo el contraste agresivo y la fatiga visual.
*   **Tipografía y Jerarquía:**
    *   Familia tipográfica: *Segoe UI* o *Inter*.
    *   Títulos de página: 18 a 20 pt, Negrita, color azul institucional.
    *   Cifras de KPIs: 24 a 28 pt, Seminegrita.
    *   Etiquetas de datos y categorías: 9 a 10 pt, color gris oscuro neutro (`#333333`).
*   **UI/UX e Interacción:**
    *   Panel de navegación lateral estandarizado en todas las páginas con iconos claros para cambiar de vista.
    *   Sincronización de segmentadores entre páginas para mantener el contexto del usuario durante la navegación.
    *   Tooltips (información sobre herramientas) contextuales con tamaño de muestra ($n$) y porcentaje relativo.

---

## 3. FASE 5: PROTOCOLO DE VALIDACIÓN Y CONTROL DE CALIDAD (EVALUACIÓN CRISP-DM)

### 3.1. Propósito de la Validación
La fase de validación no es una simple revisión superficial, sino una auditoría metodológica rigurosa. Su objetivo es certificar que las cifras calculadas en Python, visualizadas en Power BI y citadas en el texto de la monografía provienen de una única fuente de verdad, no sufren distorsiones por recuentos no expandidos y coinciden de manera irrefutable con los datos oficiales publicados por el Instituto Nacional de Estadística.

### 3.2. Dimensiones y Pruebas de Validación Formal

#### A. Validación Externa (Línea Base Oficial INE)
*   **Prueba 1: Tasa de Desocupación Juvenil:**
    *   *Cálculo en el modelo:* $\text{Desocupados Ponderados} / \text{PEA Ponderada} = 51.196 / 1.380.841 = 3,71\%$.
    *   *Referencia oficial Boletín ECE 4T-2025:* **3,7%**. Coincidencia total.
*   **Prueba 2: Tasa de Subocupación Juvenil:**
    *   *Cálculo en el modelo:* $\text{Subocupados Ponderados} / \text{Ocupados Ponderados} = 115.736 / 1.329.645 = 8,70\%$.
    *   *Referencia oficial Boletín ECE 4T-2025:* **8,7%**. Coincidencia total.
*   **Prueba 3: Tasa de Desocupación Urbana General:**
    *   *Cálculo de control:* 2,30% sobre el total de 14 años o más. Coincidencia total.

#### B. Validación Cruzada Multiplataforma (Python vs. Power BI)
Se ejecutará una matriz de conciliación punto a punto para verificar que el motor DAX de Power BI reproduzca con discrepancia cero ($0,00\%$) los resultados generados por los scripts de Python:
*   Conciliación de totales poblacionales ponderados (PEA, Ocupados, Desocupados, Cesantes, Aspirantes).
*   Conciliación de las tasas desagregadas por los 4 tramos etarios.
*   Conciliación de las tasas de desocupación por sexo y cálculo de la brecha.
*   Conciliación del ranking de los 9 departamentos.
*   Conciliación de las medias de escolaridad acumulada.

#### C. Validación de Integridad Relacional y Ponderadores
*   *Prueba de integridad 1:N:* Verificar que ninguna fila de la tabla de hechos quede huérfana al cruzarse con las dimensiones (evitando la generación de la fila en blanco en Power BI).
*   *Prueba de consistencia aditiva:* Verificar que:
    $$\text{Población Ocupada} + \text{Población Desocupada} = \text{PEA Juvenil Ponderada}$$
    $$1.329.645 + 51.196 = 1.380.841 \quad \text{(Diferencia: 0 personas)}$$
    $$\text{Desocupados Cesantes} + \text{Desocupados Aspirantes} = \text{Total Desocupados}$$
    $$45.882 + 5.314 = 51.196 \quad \text{(Diferencia: 0 personas)}$$

#### D. Protocolo de Aceptación Técnica QA
Se consolidará una lista de chequeo formal de 10 puntos de control que debe arrojar estado "Aprobado" en su totalidad antes de considerar concluida la fase.

---

## 4. FASE 6: REDACCIÓN ACADÉMICA Y CONSOLIDACIÓN DEL CAPÍTULO III

### 4.1. Propósito y Lineamientos de Redacción
El objetivo final de esta fase es consolidar los hallazgos en el documento maestro `docs/GonzalesSuyo_Franz_ActividadNº1.md`, el cual constituye el núcleo del Capítulo III (Resultados y Análisis Crítico) requerido por el CEPI para la Actividad N.º 1 del diplomado.

La redacción debe apegarse estrictamente a las siguientes pautas de calidad:
*   **Estilo formal y académico:** Redacción rigurosa en tercera persona, objetiva, precisa y basada en evidencia empírica.
*   **Enfoque de asociación diagnóstica:** Mantener la claridad de que las pruebas estadísticas ($\chi^2$, V de Cramér, diferencias de medias) identifican factores asociados y patrones de vulnerabilidad, evitando terminología causal no fundamentada en modelos econométricos longitudinales o experimentales.
*   **Aplicación del Skill Humanizer:** Redacción orgánica, fluida y natural, libre de clichés de inteligencia artificial (evitar fórmulas del tipo "no solo X sino también Y", adjetivos inflados, palabras de venta, guiones largos excesivos y párrafos vacíos).
*   **Sincronización Total de Cifras:** Todas las tablas, textos y gráficos deben citar exactamente las mismas cifras validadas en las Fases 1 a 5.

### 4.2. Estructura y Contenidos de la Entrega Final

El Capítulo III quedará articulado en dos grandes apartados conforme a la normativa del CEPI:

```text
CAPÍTULO III: RESULTADOS Y DISCUSIÓN

3.1. PRESENTACIÓN DE RESULTADOS (Evidencia objetiva y descriptiva)
     3.1.1. Caracterización del diseño metodológico y muestra efectiva
            - Tabla de dimensión metodológica (enfoque, alcance, diseño, CRISP-DM)
            - DIAGRAMA N.º 1 en Mermaid (Flujo de calibración de 52.650 a 6.649)
     3.1.2. Trazabilidad del desarrollo bajo la metodología CRISP-DM
            - Matriz de cumplimiento de las 6 fases de CRISP-DM
     3.1.3. Componentes del trabajo final e ingeniería de datos
            - Tabla de componentes técnicos y arquitectura de datos
     3.1.4. Resultados descriptivos univariados y línea base oficial del INE
            - Tabla de macroindicadores y Figura 1 (Comparativa nacional vs. juvenil)
     3.1.5. Resultados del análisis bivariado y pruebas de asociación
            - Tabla de pruebas Chi-cuadrado de Pearson y coeficientes V de Cramér
     3.1.6. Desagregaciones por dimensión analítica
            - A. Dimensión etaria (Tabla y Figura por tramo de edad)
            - B. Dimensión de género (Tabla y Figura de brecha hombre/mujer)
            - C. Dimensión territorial y departamental (Tabla y Figura del ranking)
            - D. Dimensión educativa y escolaridad (Tablas y Figuras de capital humano)
            - E. Dinámica previa y canales de búsqueda (Cesantes vs. Aspirantes)
     3.1.7. Arquitectura del modelo dimensional para Power BI
            - DIAGRAMA N.º 2 en Mermaid (Esquema en estrella)
     3.1.8. Evidencia del Cuadro de Mando Interactivo (Dashboard en Power BI)
            - Fichas analíticas y capturas de alta definición de las 6 páginas del tablero

3.2. ANÁLISIS DE RESULTADOS (Interpretación crítica y discusión)
     3.2.1. Interpretación de la vulnerabilidad etaria en la inserción laboral inicial
     3.2.2. La brecha estructural de género en el mercado laboral juvenil
     3.2.3. Disparidades territoriales y concentración de la desocupación urbana
     3.2.4. La paradoja del desempleo ilustrado y el desajuste de cualificaciones
     3.2.5. Dinámica de cesantía y canales de intermediación laboral
     3.2.6. Articulación de los resultados con los objetivos específicos del trabajo
     3.2.7. Implicaciones prácticas para políticas públicas e implicaciones metodológicas
     3.2.8. Limitaciones del alcance analítico
     3.2.9. Matriz sintética consolidada de hallazgos del mercado laboral juvenil
```

### 4.3. Consolidación de `docs/GonzalesSuyo_Franz_ActividadNº1.md` como Fuente Única para Traslado Manual a Word
*   Toda la evidencia estadística, tablas formales, diagramas conceptuales y análisis crítico se estructuran de forma definitiva en el archivo maestro Markdown `docs/GonzalesSuyo_Franz_ActividadNº1.md`.
*   A partir de este documento consolidado, el autor trasladará de manera manual el contenido a la plantilla oficial Word del CEPI (`GonzalesSuyo_Franz_Actividad1.docx`).
*   Para facilitar dicho traspaso, el archivo Markdown mantiene estricta correspondencia con los niveles de titulación, formato de tablas bajo normas APA 7ma edición y rutas directas a las figuras y capturas en alta resolución (`docs/figures/`).

---

## 5. CRONOGRAMA DE EJECUCIÓN Y PLAN DE ACCIÓN PARA EL CIERRE

Para implementar las Fases 4, 5 y 6 de forma ordenada, sistemática y verificable, se establece la siguiente secuencia de actividades operativas:

| Hito / Paso | Actividad Principal | Descripción del Entregable | Estado Previsto |
| :---: | :--- | :--- | :---: |
| **Paso 4.1** | **Estructuración del Modelo Semántico en Power BI** | Configuración de tablas, relaciones 1:N y columnas en `powerbi/Visualizacion-Analisis-Desocupacion.SemanticModel`. | Pendiente de aprobación |
| **Paso 4.2** | **Implementación del Catálogo de Medidas DAX** | Creación de las medidas ponderadas de volumen, tasas y brechas en el modelo tabular. | Pendiente de aprobación |
| **Paso 4.3** | **Construcción de las 6 Páginas del Reporte PBIR** | Maquetación visual, tarjetas de KPI, gráficos y segmentadores en `Visualizacion-Analisis-Desocupacion.Report`. | Pendiente de aprobación |
| **Paso 4.4** | **Revisión de Estilo Visual y UI/UX** | Aplicación de la paleta USFX, tipografía, tooltips y navegación interactiva. | Pendiente de aprobación |
| **Paso 5.1** | **Auditoría de Validación Cruzada (Python vs. Power BI)** | Ejecución de pruebas de consistencia numérica y discrepancia cero entre plataformas. | Pendiente de aprobación |
| **Paso 5.2** | **Emisión del Informe de Validación QA** | Documento técnico formal de verificación de línea base del INE y consistencia interna. | Pendiente de aprobación |
| **Paso 6.1** | **Actualización de la Sección 3.1.8 en el Documento Maestro** | Incorporación de la evidencia visual, fichas técnicas y descripción de las 6 páginas de Power BI en `GonzalesSuyo_Franz_ActividadNº1.md`. | Pendiente de aprobación |
| **Paso 6.2** | **Revisión de Estilo Académico (Humanizer)** | Auditoría de prosa, eliminación de sesgos automatizados y pulido de la discusión crítica en la Sección 3.2. | Pendiente de aprobación |
| **Paso 6.3** | **Cierre y Auditoría Integral de `docs/GonzalesSuyo_Franz_ActividadNº1.md`** | Verificación de maquetación en Markdown lista para copiado manual a Word por el autor. | Pendiente de aprobación |

---

## 6. CRITERIOS DE ACEPTACIÓN PARA LA APROBACIÓN DEL PLAN

Para dar por concluida satisfactoriamente la implementación total del proyecto, se evaluarán los siguientes criterios de calidad:

1.  **Cero Discrepancia Numérica:** Toda cifra presentada en el dashboard de Power BI debe coincidir exactamente con las tablas exportadas en Python y el texto de la monografía.
2.  **Rigor Muestral Inquebrantable:** Todas las métricas del dashboard deben estar estrictamente ponderadas por el factor de expansión trimestral.
3.  **Interactividad Completa del Tablero:** Las 6 páginas del reporte deben ser completamente funcionales, responsivas ante los filtros y con una navegación fluida.
4.  **Alineación Curricular Estricta:** El contenido debe responder de forma directa a los cuatro objetivos específicos aprobados en el perfil de monografía.
5.  **Excelencia en la Redacción:** El Capítulo III debe exhibir un tono formal, analítico y profesional, sin marcas de escritura de IA y con estricto formato CEPI USFX.
