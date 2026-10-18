# RESUMEN EJECUTIVO: RESULTADOS DEL MERCADO LABORAL JUVENIL EN BOLIVIA
### Análisis de los Factores Asociados a la Desocupación en Jóvenes de 16 a 28 Años (ECE 4T-2025)

**Institución:** Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX)  
**Unidad de Posgrado:** Centro de Estudios de Posgrado e Investigación (CEPI) - Vicerrectorado  
**Programa:** Diplomado en Data Science - Versión I  
**Autor:** Franz Reinaldo Gonzales Suyo  
**Coordinador / Docente:** Ing. Marcelo Arancibia  
**Fecha y Sede:** Sucre - Bolivia, 2026  

---

## 1. INTRODUCCIÓN Y OBJETIVO DEL PROYECTO

El presente trabajo analiza los factores sociodemográficos, formativos, territoriales y de trayectoria laboral que inciden en la desocupación de los jóvenes entre 16 y 28 años en el área urbana de Bolivia. Se busca generar evidencia cuantitativa reproducible a partir de microdatos estadísticos oficiales para respaldar la toma de decisiones y el diseño de políticas públicas orientadas al empleo juvenil.

* **Población Objetivo:** Jóvenes de 16 a 28 años cumplidos (Ley N.º 342 de la Juventud de Bolivia) pertenecientes a la Población Económicamente Activa (PEA) en áreas urbanas.
* **Fuente de Datos:** Encuesta Continua de Empleo (ECE) correspondiente al cuarto trimestre de 2025 (4T-2025), relevada por el Instituto Nacional de Estadística (INE).
* **Muestra Efectiva Analizada:** 6.649 personas encuestadas (depurada de 52.650 registros brutos).
* **Población Expandida Representada:** 1.380.841 jóvenes activos en el mercado de trabajo urbano, calibrados mediante el ponderador trimestral oficial (`fact_trim_act`).

---

## 2. METODOLOGÍA Y PIPELINE DE CIENCIA DE DATOS

El proyecto se desarrolló bajo el estándar internacional **CRISP-DM** (Cross-Industry Standard Process for Data Mining) mediante herramientas de código abierto y tecnologías de Business Intelligence:

```
[Ingesta ECE 4T-2025] ──> [Filtros: Urbana + 16-28 años + PEA] ──> [Calibración con Factor Trimestral]
                                                                                │
       ┌────────────────────────────────────────────────────────────────────────┴─────────────────┐
       ▼                                                                                          ▼
[Análisis Estadístico en Python]                                               [Modelo Dimensional Power BI]
• Tasas ponderadas de desocupación y subocupación                             • Modelo Star Schema (1 Fact + 6 Dim)
• Contrastes Chi-cuadrado y V de Cramér                                       • 36 medidas analíticas en DAX
• Pruebas t de Welch y Mann-Whitney para escolaridad                          • Cuadro de mando interactivo de 6 páginas
```

1. **Ingeniería de Datos en Python:** Limpieza automatizada, validación de valores nulos, estandarización del factor de expansión a tipo coma flotante (`float64`) y derivación de variables sociolaborales clave.
2. **Estadística Inferencial Ponderada:** Todas las frecuencias, totales y proporciones fueron calculadas ponderando por el factor de expansión, replicando las fórmulas del INE y de la Organización Internacional del Trabajo (OIT).
3. **Modelado en Power BI:** Estructuración de un modelo en estrella (*Star Schema*) con una tabla de hechos central y dimensiones de Calendario, Departamento, Grupo Etario, Sexo, Nivel Educativo y Condición de Actividad.

---

## 3. PRINCIPALES INDICADORES Y RESULTADOS CLAVE

Los cálculos realizados en el proyecto replican con total exactitud las cifras del Boletín Oficial del INE para el cuarto trimestre de 2025:

| Indicador Laboral | Muestra ($n$) | Población Ponderada ($N$) | Tasa / Porcentaje | Comparativa Oficial INE |
| :--- | :---: | :---: | :---: | :---: |
| **PEA Juvenil Urbana (16-28 años)** | **6.649** | **1.380.841** | **100,00%** | Referencia oficial |
| **Población Ocupada Juvenil** | 6.406 | 1.329.645 | 96,29% | Base de ocupados |
| **Población Desocupada Juvenil** | **243** | **51.196** | **3,71%** | **3,7% (Coincidencia exacta)** |
| **Subocupación por Tiempo** | 567 | 115.736 | 8,70% | **8,7% (Coincidencia exacta)** |
| **Desempleo General Urbano (Total país)** | - | - | 2,30% | Referencia nacional |
| **Ratio Desempleo Juvenil vs. General** | - | - | **1,61 veces** | Mayor vulnerabilidad juvenil |

---

## 4. BRECHAS Y FACTORES DETERMINANTES IDENTIFICADOS

### A. Vulnerabilidad por Tramo Etario
* **Pico Crítico (18 a 20 años):** Registra la mayor tasa de desocupación con **4,65%** ($\chi^2 = 11,23; p = 0,0105$). Representa la transición crítica de salida de la secundaria y el intento de inserción laboral sin experiencia previa.
* **Otros Tramos:** 16-17 años (3,16%), 21-24 años (3,67%) y 25-28 años (3,41%).

### B. Brecha Estructural de Género
* **Tasa en Mujeres:** **4,69%** (30.258 jóvenes desocupadas).
* **Tasa en Hombres:** **2,85%** (20.938 jóvenes desocupados).
* **Brecha:** **+1,84 puntos porcentuales** desfavorable a las mujeres ($\chi^2 = 5,24; p = 0,0221$). Las mujeres representan el **59,10%** del total de desocupados juveniles, situación ligada a cargas desproporcionadas de cuidado no remunerado en el hogar.

### C. Asimetrías Territoriales y Departamentales
* **Departamentos con Mayor Desocupación:** Chuquisaca encabeza el país con **5,80%**, seguido de Tarija con **4,72%** y Cochabamba con **4,71%** ($\chi^2 = 23,69; p = 0,0026$).
* **Eje y Regiones de Menor Desocupación:** Santa Cruz (3,12%), Potosí (2,81%), Oruro (3,52%), Beni (3,39%), Pando (2,41%) y La Paz (3,78%). La reducida base industrial en Chuquisaca y Tarija satura el sector servicios y la administración pública.

### D. Perfil de los Desocupados: Cesantes vs. Aspirantes
* **Cesantes (con experiencia previa):** Representan el **89,62%** de los desocupados (45.882 personas).
* **Aspirantes (en busca del primer empleo):** Representan solo el **10,38%** (5.314 personas).
* **Conclusión:** El desempleo juvenil urbano no es principalmente un problema de acceso inicial, sino de inestabilidad y pérdida de empleos precarios.

### E. Nivel Educativo y la Paradoja de la Escolaridad
* **Escolaridad Promedio:** Los jóvenes desocupados presentan un promedio de escolaridad significativamente mayor que los ocupados: **13,01 años frente a 12,38 años** (Prueba $t$ de Welch: $t = -2,39; p = 0,0174$; Mann-Whitney: $U = 714.498,5; p = 0,0293$).
* **Interpretación:** Los jóvenes con menor formación se ven obligados a ocuparse inmediatamente en empleos informales y de subsistencia, mientras que los jóvenes con mayor nivel de instrucción experimentan mayores tiempos de búsqueda al aspirar a puestos acordes a su formación.

---

## 5. ESTRUCTURA DEL CUADRO DE MANDO EN POWER BI (6 PÁGINAS)

1. **Página 1: Panorama Laboral Juvenil:** Indicadores macroeconómicos (PEA, ocupados, desocupados, subocupación) y distribución por grandes variables.
2. **Página 2: Tramo Etario:** Comparación de tasas de desocupación entre los cuatro grupos de edad y análisis de la transición educativa.
3. **Página 3: Capital Humano y Escolaridad:** Comportamiento del desempleo según nivel educativo alcanzado y condición de asistencia a centros de estudio.
4. **Página 4: Género y Territorio:** Mapa departamental de desocupación y análisis detallado de la brecha entre mujeres y varones.
5. **Página 5: Perfil del Desocupado:** Comparativa entre cesantes y aspirantes, canales de búsqueda utilizados y tiempo de desocupación.
6. **Página 6: Conclusiones y Recomendaciones:** Síntesis ejecutiva interactiva y matriz de propuestas de política pública.

---

## 6. RECOMENDACIONES ESTRATÉGICAS

1. **Programa de Empleo Temprano y Formación Dual (18-20 años):** Alianzas formativas con empresas privadas que incluyan pasantías remuneradas y periodos de prueba subvencionados.
2. **Servicios de Apoyo al Cuidado Infantil:** Centros municipales de cuidado diurno para reducir las barreras de inserción laboral en mujeres jóvenes.
3. **Impulso a Sectores Tecnológicos en Chuquisaca y Tarija:** Fomentar el desarrollo de empresas de software, servicios digitales y emprendimiento técnico para absorber la mano de obra profesional disponible.
4. **Modernización de la Intermediación Laboral:** Fortalecimiento del Servicio Público de Empleo mediante plataformas digitales accesibles y programas de reconversión de habilidades técnicas para jóvenes cesantes.

---
*Documento preparado en el marco del Diplomado en Data Science - USFX CEPI (2026).*
