# CAPÍTULO III: RESULTADOS

## 3.1. PRESENTACIÓN DE RESULTADOS

### 3.1.1. Contexto metodológico y dimensional
Los microdatos analizados provienen de la Encuesta Continua de Empleo (ECE) correspondiente al cuarto trimestre de 2025, relevada por el Instituto Nacional de Estadística (INE). La encuesta utiliza un diseño muestral probabilístico, bietápico, estratificado y por conglomerados. Para reflejar las características demográficas de la población, toda estimación de totales, proporciones y tasas incorpora el factor de expansión trimestral de la persona (`fact_trim_act`).

De acuerdo con el artículo 4 de la Ley N.º 342 de la Juventud de Bolivia, la población joven comprende a las personas de 16 a 28 años de edad cumplidos. Conforme al diseño del trabajo, se aplicaron tres criterios de delimitación muestral: residencia en el área urbana (`area == 1`), edad entre 16 y 28 años (`16 <= s1_03a <= 28`) y pertenencia a la Población Económicamente Activa (`pea == 1`).

TABLA N.º 1: *Dimensión metodológica y aplicación en ciencia de datos*

| Dimensión metodológica | Descripción y fundamentación | Justificación y aplicación en ciencia de datos |
| :--- | :--- | :--- |
| Enfoque de trabajo | Cuantitativo y computacional | Análisis numérico y categórico de microdatos mediante programación en Python, cálculo de tasas ponderadas y contrastes de hipótesis estadísticas. |
| Tipo de trabajo | Aplicado y de diagnóstico sociolaboral | Utilización de técnicas estadísticas y de inteligencia de negocios para caracterizar la desocupación juvenil y generar evidencia orientada a políticas públicas. |
| Alcance o nivel | Descriptivo y de asociación diagnóstica | Estimación puntual de tasas de desocupación y subocupación, complementada con pruebas de independencia Chi-cuadrado, V de Cramér y diferencias de medias. |
| Diseño | No experimental, observacional y transversal | Análisis ex post facto de los microdatos oficiales correspondientes a un corte temporal específico (cuarto trimestre de 2025). |
| Metodología guía | Metodología CRISP-DM adaptada | Ciclo de vida estructurado en seis fases: comprensión del problema, comprensión de datos, preparación de datos, modelado analítico, evaluación y despliegue. |
| Población y muestra | Universo censal urbano y muestra ECE | Población objetivo de 1.380.841 jóvenes urbanos en la PEA, representada por una muestra efectiva observada de 6.649 personas encuestadas. |
| Técnica de recolección | Extracción de fuentes secundarias oficiales | Descarga e ingestión directa de los microdatos abiertos de la ECE 4T-2025 provistos por el Instituto Nacional de Estadística. |
| Procesamiento y análisis | Limpieza de datos y estadística ponderada | Estandarización tipográfica del ponderador (`fact_trim_act`), recodificación de variables, tablas de contingencia ponderadas y pruebas Chi-cuadrado. |
| Entorno tecnológico | Entorno analítico de código abierto | Python 3.14 con librerías Pandas, NumPy, SciPy, Statsmodels, Seaborn y Microsoft Power BI Desktop para modelado dimensional y visualización interactiva. |

*FUENTE: Elaboración con base en la estructura de evaluación del Diplomado en Data Science (USFX - CEPI).*

El conjunto de datos procesado permite examinar de manera directa las condiciones laborales juveniles en las ciudades bolivianas, preservando la representatividad estadística para cada departamento y segmento demográfico.

DIAGRAMA N.º 1: *Flujo metodológico de preparación y calibración de microdatos (ECE 4T-2025)*

```mermaid
flowchart TD
    A["Microdatos brutos ECE 4T-2025<br/>(52.650 registros, 121 variables)"] --> B["Filtro geográfico<br/>Área urbana: area == 1<br/>(44.048 registros)"]
    B --> C["Filtro etario Ley N.º 342<br/>16 a 28 años cumplidos<br/>(9.612 registros)"]
    C --> D["Filtro laboral PEA<br/>Población Activa: pea == 1<br/>(6.649 registros)"]
    D --> E["Calibración muestral<br/>Factor de expansión: fact_trim_act"]
    E --> F["Población expandida urbana<br/>1.380.841 jóvenes en la PEA"]
    F --> G["Análisis estadístico en Python<br/>Tasas ponderadas, Chi-cuadrado y Cramér"]
    F --> H["Modelo dimensional Star Schema<br/>Tablero interactivo en Power BI Desktop"]
```

*FUENTE: Elaboración con base en el diseño metodológico de la ECE 4T-2025 (INE).*

El Diagrama N.º 1 esquematiza el embudo metodológico de depuración y calibración muestral aplicado a los microdatos de la Encuesta Continua de Empleo (ECE 4T-2025). A partir de la base nacional de 52.650 registros brutos, se implementan tres filtros sucesivos de delimitación: residencia en área urbana (`area == 1`), rango etario normativo de 16 a 28 años cumplidos según la Ley N.º 342 y pertenencia estricta a la Población Económicamente Activa (`pea == 1`), consolidando una muestra efectiva de 6.649 personas encuestadas. La aplicación del factor de calibración trimestral (`fact_trim_act`) expande este subconjunto al universo representativo de 1.380.841 jóvenes urbanos, suministrando una base metodológica única y ponderada tanto para las pruebas de inferencia estadística en Python como para el modelo dimensional en Power BI Desktop.

### 3.1.2. Trazabilidad del desarrollo bajo la metodología CRISP-DM
El procesamiento de la información se organizó siguiendo las seis fases de la metodología CRISP-DM aplicadas al análisis de microdatos laborales.

TABLA N.º 2: *Cumplimiento de hitos del proceso metodológico (CRISP-DM)*

| Fase CRISP-DM | Actividad planificada | Entregable concreto | Estado | Avance (%) |
| :--- | :--- | :--- | :---: | :---: |
| 1. Comprensión del problema | Delimitación de conceptos de desempleo y marco de la Ley N.º 342 | Matriz conceptual y delimitación del universo de 16 a 28 años | Concluido | 100% |
| 2. Comprensión de los datos | Auditoría de 52.650 registros y 121 variables de la ECE 4T-2025 | Diccionario de variables seleccionadas y reporte de estructura | Concluido | 100% |
| 3. Preparación de los datos | Depuración, filtros de universo, tipado de ponderador y recodificaciones | Dataset procesado `ECE_4T2025_Jovenes_PEA.csv` (6.649 filas) | Concluido | 100% |
| 4. Modelado y cálculo analítico | Formulación de tasas ponderadas, pruebas Chi-cuadrado y Cramér | Scripts modulares en Python (`statistical_analysis.py`) | Concluido | 100% |
| 5. Evaluación y validación | Contraste de estimaciones frente al Boletín Oficial del INE | Verificación exacta: desocupación 3,71% y subocupación 8,70% | Concluido | 100% |
| 6. Despliegue y visualización | Generación de 13 tablas, 10 figuras y modelo Star Schema en Power BI | Catálogo exportado y cuaderno maestro `Proyecto-Final.ipynb` | Concluido | 100% |

*FUENTE: Elaboración con base en el plan de trabajo del proyecto.*

La Tabla N.º 2 resume el avance de las seis etapas del ciclo CRISP-DM, el estándar de trabajo utilizado en proyectos de ciencia de datos. Confirma que cada fase completó sus metas al 100%, lo que asegura que el estudio transitó de forma ordenada desde la delimitación conceptual del desempleo juvenil hasta la publicación de los tableros interactivos y reportes finales.

### 3.1.3. Componentes del trabajo final e ingeniería de datos
La articulación entre la ciencia de datos y los resultados del mercado de trabajo juvenil se resume en tres componentes técnicos:

TABLA N.º 3: *Componentes técnicos de la solución en ciencia de datos*

| Componente | Término técnico en ciencia de datos | Aplicación concreta en el proyecto |
| :--- | :--- | :--- |
| Ingesta y adquisición | Pipeline de ingesta y validación de microdatos | Carga automatizada del archivo plano `ECE_4T2025.csv` con separador de listas, codificación `latin1` y auditoría de integridad inicial sobre 52.650 observaciones. |
| Aporte técnico y metodológico | Ingeniería de características y estadística ponderada | Estandarización del factor de expansión muestral, cálculo vectorizado de tasas de desocupación ponderadas y contrastes de asociación ($\chi^2$, $V$ de Cramér, $t$-Student). |
| Entregables de la solución | Artefactos reproducibles y modelo de despliegue | Dataset procesado de 6.649 registros y 156 columnas, 13 tablas analíticas en formato CSV, 10 figuras a 300 DPI, cuaderno interactivo ejecutado y modelo en estrella para Power BI. |

*FUENTE: Elaboración propia.*

La Tabla N.º 3 describe los tres pilares informáticos que sostienen la investigación: la ingesta automatizada de los microdatos del INE, la aplicación de operaciones estadísticas con factores de expansión y la creación de productos finales reproducibles, tales como scripts modulares en Python y el modelo analítico para Power BI.

La base de datos original contiene 52.650 observaciones. El primer filtro eliminó a 8.602 personas residentes en el área rural. El segundo filtro excluyó a 34.436 personas cuyas edades quedaban fuera del rango de 16 a 28 años, dejando a 9.612 jóvenes urbanos. De ese total, 2.963 personas fueron identificadas como económicamente inactivas (principalmente estudiantes sin búsqueda laboral, personas dedicadas al cuidado del hogar o con incapacidad permanente). La muestra resultante quedó constituida por 6.649 jóvenes activos en el mercado de trabajo.

La variable del factor de expansión `fact_trim_act` presentaba valores textuales con coma decimal, por ejemplo `'207,52'`. Este formato requirió una conversión a tipo numérico de coma flotante (`float64`) para evitar errores en las operaciones de suma ponderada. Se verificó que ningún registro presentara un factor nulo, negativo o igual a cero. La suma total de los ponderadores reproduce con exactitud la cifra de 1.380.841 personas estimadas por el sistema estadístico nacional para la PEA juvenil urbana.

### 3.1.4. Resultados del análisis descriptivo univariado
La tasa de desocupación se calculó dividiendo la población desocupada ponderada entre la PEA juvenil urbana ponderada y multiplicando por cien:

$$\text{Tasa de desocupación} = \frac{\sum (\text{pead}_i \times \text{peso}_i)}{\sum \text{peso}_i} \times 100$$

Esta expresión matemática calcula la tasa oficial reconociendo que cada persona encuestada representa a cientos de jóvenes en su ciudad. Al multiplicar la condición de desocupado ($\text{pead}_i$) por su ponderador muestral ($\text{peso}_i$), la fórmula suma la cantidad estimada de desocupados reales y la divide entre el total de jóvenes activos en el mercado de trabajo, evitando distorsiones por recuentos simples.

TABLA N.º 4: *Indicadores del mercado laboral juvenil urbano en Bolivia (cuarto trimestre de 2025)*

| Indicador sociolaboral | Casos observados (*n*) | Población ponderada (*N*) | Proporción (%) | Meta del boletín INE |
| :--- | :---: | :---: | :---: | :---: |
| PEA juvenil urbana (16 a 28 años) | 6.649 | 1.380.841 | 100,00% | Total de referencia |
| Población ocupada juvenil | 6.406 | 1.329.645 | 96,29% | Dato oficial |
| Población desocupada juvenil | 243 | 51.196 | 3,71% | 3,7% |
| Población subocupada por tiempo | 567 | 115.736 | 8,70% | 8,7% |
| Desocupados cesantes (con experiencia previa) | 215 | 45.882 | 89,62% | Mayoría |
| Desocupados aspirantes (en búsqueda de primer empleo) | 28 | 5.314 | 10,38% | Minoría |

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Tabla N.º 4 traslada los datos de las encuestas a la escala de la población boliviana urbana. En ella, los casos observados ($n$) corresponden a las personas encuestadas en campo por el INE, mientras que la población ponderada ($N$) proyecta a cuántos jóvenes representan en las ciudades según el factor de expansión muestral. La columna de proporción indica el porcentaje estimado para cada condición laboral y la meta del boletín comprueba que los resultados del estudio coinciden con las cifras oficiales publicadas por el Estado.

La tasa de desocupación juvenil del cuarto trimestre de 2025 se sitúa en 3,71%, coincidente con el 3,7% reportado en el boletín oficial del INE. Por su parte, la subocupación juvenil alcanza el 8,70% sobre la población ocupada, lo que equivale a 115.736 jóvenes que trabajaron menos de la jornada habitual, desearon trabajar más horas y estaban disponibles para hacerlo.

FIGURA N.º 1: *Comparación de la tasa de desocupación general urbana y juvenil (cuarto trimestre de 2025)*

![Comparación de desocupación general y juvenil](figures/figura_1_desocupacion_general_vs_juvenil.png)

*FUENTE: Elaboración con base en datos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 1 expone la brecha generacional del mercado de trabajo urbano. La barra gris refleja la desocupación en la población general de 14 años o más (2,30%), mientras que la barra azul evidencia la tasa de los jóvenes de 16 a 28 años (3,71%). Esta diferencia gráfica confirma que el desempleo afecta con una intensidad 1,61 veces mayor al segmento juvenil en las ciudades bolivianas.

Al contrastar la tasa de desocupación juvenil (3,71%) con la tasa de desocupación general de la población urbana de 14 años o más (2,30%), se observa que los jóvenes registran una incidencia de desempleo 1,61 veces mayor que la población adulta general.

### 3.1.5. Resultados del análisis bivariado y pruebas de asociación
Para determinar si las diferencias observadas entre subgrupos responden a variaciones sistemáticas o a fluctuaciones aleatorias del muestreo, se aplicó la prueba de independencia Chi-cuadrado de Pearson ($\chi^2$) fijando un umbral de significancia de 0,05. La magnitud del efecto se evaluó mediante el coeficiente V de Cramér ($V$):

$$V = \sqrt{\frac{\chi^2}{N \times \min(r - 1, c - 1)}}$$

Esta fórmula normaliza el valor de Chi-cuadrado para medir la intensidad práctica de una relación entre dos variables cualitativas en una escala de 0 a 1. Al dividir el estadístico $\chi^2$ entre el producto de la muestra expandida ($N$) y el menor número de categorías menos uno ($\min(r - 1, c - 1)$), la $V$ de Cramér elimina el sesgo por volumen muestral, permitiendo evaluar si una asociación significativa tiene un efecto real leve, moderado o fuerte.

TABLA N.º 5: *Matriz de pruebas de asociación estadística con la condición de desocupación juvenil*

| Dimensión analizada | Variable | Casos (*n*) | Chi2 ($\chi^2$) | Grados de libertad | p-valor | V de Cramér | Resultado estadístico |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| Tramo de edad | `grupo_edad` | 6.649 | 11,2332 | 3 | 0,01053 | 0,0411 | Asociación significativa (p < 0,05) |
| Sexo | `sexo` | 6.649 | 5,2367 | 1 | 0,02212 | 0,0281 | Asociación significativa (p < 0,05) |
| Departamento | `departamento` | 6.649 | 23,6920 | 8 | 0,00258 | 0,0597 | Asociación significativa (p < 0,05) |
| Tipología de hogar | `tipo_hogar` | 6.649 | 17,4287 | 6 | 0,00783 | 0,0512 | Asociación significativa (p < 0,05) |
| Parentesco con el jefe | `parentesco` | 6.649 | 17,2553 | 7 | 0,01582 | 0,0509 | Asociación significativa (p < 0,05) |
| Nivel educativo | `nivel_educativo` | 6.649 | 3,6356 | 4 | 0,45756 | 0,0234 | Sin significancia agregada (p >= 0,05) |
| Asistencia escolar | `asiste_estudio` | 6.649 | 1,5264 | 1 | 0,21665 | 0,0152 | Sin significancia agregada (p >= 0,05) |

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Tabla N.º 5 sintetiza los contrastes de asociación estadística para cada dimensión analizada. En ella, la columna de casos ($n$) registra las 6.649 personas evaluadas en la muestra; el valor Chi2 ($\chi^2$) mide la discrepancia entre las frecuencias observadas y las esperadas bajo independencia; los grados de libertad indican las categorías libres en la tabla cruzada; el $p$-valor establece la probabilidad de azar (siendo significativo si es menor a 0,05); y la $V$ de Cramér califica la magnitud práctica del efecto.

Las variables de edad, sexo, departamento, tipo de hogar y parentesco presentan un p-valor inferior a 0,05, lo que confirma diferencias estadísticamente significativas en la desocupación de estos grupos. En cambio, las categorías agregadas de nivel educativo y asistencia a centros de enseñanza no mostraron una asociación global significativa mediante la prueba Chi-cuadrado, lo cual motivó un análisis continuo complementario mediante años de escolaridad.

### 3.1.6. Desagregaciones por dimensión analítica

#### A. Dimensión etaria
La segmentación en cuatro intervalos muestra que la desocupación se concentra de manera particular en las edades tempranas de inserción al mercado.

TABLA N.º 6: *Tasa de desocupación juvenil según tramo etario (Bolivia urbana, 4T-2025)*

| Tramo de edad | Muestra (*n*) | Población PEA (*N*) | Población desocupada (*N*) | Tasa de desocupación (%) | Porcentaje de desocupados (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| 16 a 17 años | 774 | 159.899 | 2.991 | 1,87% | 5,84% |
| 18 a 20 años | 1.377 | 290.670 | 13.504 | 4,65% | 26,38% |
| 21 a 24 años | 2.039 | 414.829 | 14.713 | 3,55% | 28,74% |
| 25 a 28 años | 2.459 | 515.443 | 19.988 | 3,88% | 39,04% |
| Total | 6.649 | 1.380.841 | 51.196 | 3,71% | 100,00% |

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Tabla N.º 6 distribuye la desocupación entre los cuatro grupos de edad. La columna de población PEA ($N$) representa a los jóvenes activos en cada tramo y la población desocupada ($N$) proyecta cuántos buscan empleo. La tasa mide el riesgo puntual de desempleo dentro de cada rango etario, mientras que el porcentaje de desocupados señala qué proporción del total nacional de jóvenes desempleados aporta cada segmento.

El grupo de 18 a 20 años exhibe la tasa más alta con un 4,65%, seguido por el grupo de 25 a 28 años con 3,88% y el grupo de 21 a 24 años con 3,55%. El tramo de 16 y 17 años registra la tasa más baja (1,87%), explicada por una menor participación económica activa en ese segmento etario.

FIGURA N.º 2: *Tasa de desocupación juvenil por tramo etario (cuarto trimestre de 2025)*

![Desocupación por tramo etario](figures/figura_2_desocupacion_por_tramo_etario.png)

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 2 resalta en color rojo el pico de desocupación en el grupo de 18 a 20 años (4,65%), la etapa donde los bachilleres intentan colocarse laboralmente por primera vez sin contar con experiencia ni formación técnica. En las edades posteriores (21 a 24 y 25 a 28 años), las barras descienden y se estabilizan cerca del promedio general, mientras que el tramo de 16 a 17 años muestra el valor más bajo (1,87%) debido a que la gran mayoría aún permanece en la escuela secundaria fuera de la fuerza de trabajo.

#### B. Dimensión de género
La distribución de la desocupación según el sexo de la persona evidencia una brecha desfavorable para las mujeres jóvenes.

TABLA N.º 7: *Tasa de desocupación juvenil según sexo (Bolivia urbana, 4T-2025)*

| Sexo | Muestra (*n*) | Población PEA (*N*) | Población desocupada (*N*) | Tasa de desocupación (%) | Porcentaje de desocupados (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Hombre | 3.393 | 735.643 | 20.938 | 2,85% | 40,90% |
| Mujer | 3.256 | 645.198 | 30.258 | 4,69% | 59,10% |
| Total | 6.649 | 1.380.841 | 51.196 | 3,71% | 100,00% |

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Tabla N.º 7 organiza la información laboral según el sexo de la persona joven. La columna de muestra (*n*) indica el conteo de encuestados en el operativo de campo, mientras que la población PEA (*N*) y desocupada (*N*) representan los totales expandidos para el área urbana de Bolivia. La tasa de desocupación refleja la incidencia del desempleo en cada grupo (4,69% en mujeres frente a 2,85% en hombres), y el porcentaje de desocupados muestra que casi seis de cada diez jóvenes sin trabajo en el país son mujeres (59,10%), a pesar de que su participación en la fuerza de trabajo activa es menor a la de los varones.

FIGURA N.º 3: *Tasa de desocupación juvenil según sexo y brecha de género (cuarto trimestre de 2025)*

![Brecha de género en desocupación](figures/figura_3_brecha_genero.png)

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 3 ilustra la disparidad de género mediante dos barras comparativas: la barra azul de los hombres registra 2,85%, mientras que la barra carmesí de las mujeres alcanza 4,69%. El cuadro superior destaca la brecha neta de +1,84 puntos porcentuales en desmedro de las mujeres jóvenes, confirmada como estadísticamente significativa en el pie de figura ($\chi^2 = 5,24; p = 0,022$). Esta representación visual evidencia que una mujer joven en el área urbana de Bolivia enfrenta una probabilidad 1,65 veces mayor de encontrarse desocupada respecto a un varón de su misma edad.

#### C. Dimensión territorial y departamental
El análisis por departamento revela marcadas disparidades entre las diferentes regiones urbanas de Bolivia.

TABLA N.º 8: *Tasa de desocupación juvenil por departamento (Bolivia urbana, 4T-2025)*

| Departamento | Muestra (*n*) | Población PEA (*N*) | Población desocupada (*N*) | Tasa de desocupación (%) | Porcentaje de desocupados (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Chuquisaca | 486 | 62.899 | 3.648 | 5,80% | 7,13% |
| Tarija | 255 | 57.856 | 2.728 | 4,72% | 5,33% |
| Cochabamba | 1.196 | 251.505 | 11.840 | 4,71% | 23,13% |
| La Paz | 1.731 | 338.688 | 13.016 | 3,84% | 25,42% |
| Santa Cruz | 1.311 | 459.615 | 15.313 | 3,33% | 29,91% |
| Oruro | 348 | 67.935 | 2.027 | 2,98% | 3,96% |
| Beni | 435 | 60.886 | 1.259 | 2,07% | 2,46% |
| Pando | 370 | 11.079 | 210 | 1,89% | 0,41% |
| Potosí | 517 | 70.378 | 1.155 | 1,64% | 2,26% |
| Total | 6.649 | 1.380.841 | 51.196 | 3,71% | 100,00% |

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Tabla N.º 8 presenta el panorama laboral juvenil en los nueve departamentos del país. La columna de muestra (*n*) y de población PEA (*N*) dimensionan el tamaño de la fuerza de trabajo urbana departamental, mientras que la tasa (%) mide la probabilidad de desocupación dentro de cada mercado local. Por su parte, la columna de porcentaje de desocupados (%) muestra la contribución de cada territorio al desempleo nacional, evidenciando que el eje central (Santa Cruz, La Paz y Cochabamba) concentra el 78,46% de los desocupados absolutos por su volumen demográfico, aunque las tasas relativas más severas corresponden a Chuquisaca (5,80%) y Tarija (4,72%).

FIGURA N.º 4: *Tasa de desocupación juvenil por departamento (cuarto trimestre de 2025)*

![Desocupación por departamento](figures/figura_4_desocupacion_por_departamento.png)

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 4 ordena los nueve departamentos de forma descendente mediante barras horizontales y los compara frente a la línea vertical dorada que marca el promedio nacional juvenil (3,71%). La barra superior en color rojo oscuro resalta a Chuquisaca con la tasa más elevada de Bolivia (5,80%), seguida por Tarija (4,72%), Cochabamba (4,71%) y La Paz (3,84%), las cuatro regiones que rebasan el promedio urbano. En contraste, los departamentos mineros y amazónicos como Beni (2,07%), Pando (1,89%) y Potosí (1,64%) se sitúan a la izquierda de la referencia, reflejando marcadas asimetrías productivas validadas por una prueba Chi-cuadrado altamente significativa ($\chi^2 = 23,69; p = 0,0026$).

#### D. Dimensión educativa y escolaridad acumulada
Al evaluar la tasa de desocupación según el máximo nivel educativo alcanzado, se registra una relación ascendente: las personas sin instrucción formal tienen una tasa de 2,31%, quienes completaron primaria alcanzan 3,43%, quienes cuentan con nivel secundario registran 4,02% y quienes accedieron a estudios universitarios registran 4,04%.

TABLA N.º 9: *Comparación de años de escolaridad entre jóvenes ocupados y desocupados*

| Condición de actividad | Casos (*n*) | Media ponderada (años) | Desviación estándar | Prueba estadística | Estadístico | p-valor |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Jóvenes ocupados | 6.406 | 12,64 | 2,63 | t de Student (Welch) | t = -2,39 | 0,0174 |
| Jóvenes desocupados | 243 | 13,01 | 2,41 | Mann-Whitney U | U = 714.498,5 | 0,0293 |

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Tabla N.º 9 compara el capital educativo acumulado entre jóvenes ocupados y desocupados. Las columnas de media ponderada y desviación estándar resumen el promedio y la dispersión de los años de estudio formal expandidos con el factor muestral. Para comprobar si la brecha observada es estadísticamente sólida, se aplicaron tanto la prueba paramétrica t de Welch ($t = -2,39; p = 0,0174$) como la no paramétrica de Mann-Whitney ($U = 714.498,5; p = 0,0293$), confirmando con un $p$-valor inferior a 0,05 que los jóvenes desocupados poseen en promedio mayor escolaridad (13,01 años frente a 12,64 años), lo que equivale a casi cuatro meses lectivos adicionales de instrucción.

FIGURA N.º 5: *Distribución de años de estudio: jóvenes ocupados y desocupados urbanos*

![Distribución de años de estudio](figures/figura_8_distribucion_anios_estudio.png)

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 5 analiza la distribución de la escolaridad mediante un gráfico de doble panel. En el panel superior, el diagrama de cajas muestra que la caja de los desocupados (color salmón) se encuentra desplazada a la derecha con una mediana de 13 años respecto a los 12 años de los ocupados (color verde), observándose además que estos últimos presentan mayor dispersión hacia niveles educativos bajos con valores atípicos entre 0 y 7 años de estudio. En el panel inferior, las curvas de densidad kernel (KDE) evidencian que los jóvenes ocupados se concentran densamente en el bachillerato (12 años), mientras que los desocupados sostienen una masa superior en el tramo de 14 a 18 años de estudio, lo que demuestra visualmente que el desempleo urbano abierto afecta de forma desproporcionada a jóvenes con estudios superiores o técnicos que buscan inserción calificada.

FIGURA N.º 6: *Tasa de desocupación juvenil según nivel educativo formal*

![Desocupación por nivel educativo](figures/figura_6_desocupacion_por_nivel_educativo.png)

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 6 compara las tasas de desocupación entre cuatro niveles de instrucción frente a la línea dorada discontinua del promedio nacional (3,71%). Las barras reflejan un gradiente ascendente: la población sin instrucción presenta una tasa de 2,31% y primaria alcanza 3,43%, mientras que los niveles secundario (4,02%) y superior universitario (4,04%) superan la media del país. Esta tendencia describe el fenómeno del desempleo ilustrado, donde los jóvenes con mayor preparación prolongan su tiempo de búsqueda hacia empleos acordes a su perfil, mientras que aquellos con menor instrucción deben ocuparse de inmediato en actividades informales de subsistencia ($p = 0,457$).

FIGURA N.º 7: *Tasa de desocupación juvenil según asistencia escolar o académica*

![Desocupación según asistencia escolar](figures/figura_7_desocupacion_asiste_estudio.png)

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 7 evalúa si la concurrencia activa a centros educativos incide en el desempleo de los jóvenes pertenecientes a la fuerza laboral. La barra azul de quienes asisten a clases registra una tasa de 3,54%, mientras que la barra gris de quienes no asisten se sitúa en 3,92%, marcando una diferencia moderada de 0,38 puntos porcentuales. Al no alcanzar significancia estadística en la prueba Chi-cuadrado ($p = 0,2166$), el gráfico demuestra que la condición de estudiante activo no constituye un factor diferenciador decisivo frente al riesgo de desocupación en el área urbana.

#### E. Dinámica previa y canales de búsqueda de empleo
La composición interna del desempleo juvenil urbano muestra que 45.882 personas (89,62%) corresponden a desocupados cesantes, es decir, jóvenes que ya contaban con un empleo anterior y se desvincularon por renuncia, despido o culminación de contrato. Los desocupados aspirantes, que buscan trabajo por primera vez, representan a 5.314 personas (10,38%).

FIGURA N.º 8: *Composición de la desocupación juvenil: cesantes y aspirantes*

![Cesantes y aspirantes](figures/figura_5_cesantes_vs_aspirantes.png)

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 8 expone la estructura interna de los 51.196 jóvenes desocupados mediante un gráfico circular según su trayectoria de trabajo. El sector mayoritario en color naranja muestra que el 89,6% (45.882 jóvenes) corresponde a cesantes que perdieron o renunciaron a un empleo previo, mientras que el segmento morado de aspirantes concentra el 10,4% (5.314 jóvenes) que buscan trabajo por primera vez. La distribución ilustra que el desempleo juvenil urbano en Bolivia deriva principalmente de la inestabilidad y rotación en puestos de trabajo precarios antes que de barreras exclusivas para ingresar al mercado laboral.

TABLA N.º 10: *Canales de búsqueda de empleo utilizados por jóvenes desocupados urbanos*

| Mecanismo principal de búsqueda | Muestra (*n*) | Población ponderada (*N*) | Porcentaje ponderado (%) |
| :--- | :---: | :---: | :---: |
| Avisos por prensa, internet o redes sociales | 92 | 19.645 | 38,82% |
| Presentación directa de solicitudes o currículum vitae | 76 | 16.002 | 31,62% |
| Otras formas no estructuradas de búsqueda | 45 | 8.924 | 17,63% |
| Preguntó directamente en lugares o centros de trabajo | 17 | 3.882 | 7,67% |
| Consultó a familiares, amigos o conocidos | 5 | 1.155 | 2,28% |
| Realizó gestiones para abrir negocio propio o independiente | 3 | 550 | 1,09% |
| No declaró o no aplica | 5 | 453 | 0,90% |
| Total | 243 | 50.611 | 100,00% |

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Tabla N.º 10 clasifica las estrategias de postulación adoptadas por los jóvenes sin empleo. La columna de muestra (*n*) reporta los 243 informantes del operativo, la población ponderada (*N*) expande estos casos a 50.611 personas en el universo urbano, y el porcentaje ponderado (%) mide la participación de cada vía de búsqueda. Las cifras revelan el predominio de canales estructurados: los avisos en prensa, internet o redes sociales concentran el 38,82% y la presentación directa de carpetas o solicitudes reúne el 31,62%, sumando entre ambos más del 70% de las gestiones laborales frente a una baja proporción de iniciativas independientes (1,09%).

FIGURA N.º 9: *Mecanismos principales de búsqueda de empleo en jóvenes desocupados*

![Mecanismos de búsqueda de empleo](figures/figura_9_mecanismos_busqueda.png)

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 9 ordena en barras horizontales las vías de inserción laboral declaradas por la juventud desocupada. Los dos canales principales corresponden a la búsqueda mediante avisos digitales o de prensa (41,4%) y la entrega formal de currículum vitae (31,1%), acumulando conjuntamente más de siete de cada diez postulaciones. En contraste, las barras inferiores reflejan un peso marginal de los contactos interpersonales mediante amigos o parientes (1,8%) y de la gestión de emprendimientos propios (1,3%), lo que evidencia que la mayoría de los jóvenes desocupados busca activamente insertarse como personal dependiente en el mercado formal.

FIGURA N.º 10: *Tasa de desocupación juvenil según tipología de hogar*

![Desocupación por tipo de hogar](figures/figura_10_desocupacion_tipo_hogar.png)

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Figura N.º 10 presenta las tasas de desocupación en siete estructuras familiares contrastadas contra la línea dorada del promedio nacional (3,71%). Las barras más prolongadas corresponden a hogares sin núcleo conyugal (6,18%), nucleares monoparentales (5,68%) y extendidos (5,37%), donde los jóvenes enfrentan mayor vulnerabilidad económica. Por el contrario, los hogares nucleares biparentales con hijos (2,67%) y compuestos (1,79%) registran tasas significativamente menores, patrón que la prueba Chi-cuadrado valida como estadísticamente significativo ($\chi^2 = 17,43; p = 0,0078$) e indicativo de cómo el respaldo del núcleo familiar modula la inserción laboral.

### 3.1.7. Arquitectura del modelo dimensional para Power BI Desktop
Para facilitar la exploración visual y la toma de decisiones basada en datos, los microdatos procesados se organizaron en un esquema en estrella (*Star Schema*) dentro del proyecto de Power BI (`powerbi/Visualizacion-Analisis-Desocupacion.pbip`). El modelo semántico, serializado bajo el estándar TMDL (*Tabular Model Definition Language*), sitúa en el centro una tabla de hechos conectada a seis tablas dimensionales mediante relaciones unidireccionales de uno a muchos (1:N) con integridad referencial activa:

DIAGRAMA N.º 2: *Arquitectura del modelo dimensional en estrella (Star Schema) implementado en Power BI Desktop*

```mermaid
flowchart TD
    DIM_E["<b>Dim_GrupoEdad</b><br/>• grupo_edad (PK)<br/>• OrdenEtario (Sort)"]
    DIM_S["<b>Dim_Sexo</b><br/>• sexo (PK)<br/>• sexo_cod"]
    DIM_D["<b>Dim_Departamento</b><br/>• departamento (PK)<br/>• depto_cod<br/>• RegionGeografica"]
    DIM_N["<b>Dim_NivelEducativo</b><br/>• nivel_educativo (PK)<br/>• OrdenEducativo (Sort)"]
    DIM_C["<b>Dim_CondicionLaboral</b><br/>• tipo_condicion_laboral (PK)<br/>• Categoria"]
    DIM_H["<b>Dim_Hogar</b><br/>• tipo_hogar (PK)"]

    FACT["<b>Fact_MercadoLaboral</b><br/>• id_persona (PK)<br/>• edad | anios_estudio<br/>• es_ocupado | es_desocupado<br/>• es_cesante | es_aspirante<br/>• es_subocupado<br/>• peso_trimestral (Factor Exp.)"]

    MEDIDAS["<b>_Medidas</b><br/>• 20 Medidas DAX Ponderadas<br/>• Carpetas Jerárquicas 01 a 05"]

    DIM_E -->|1:N| FACT
    DIM_S -->|1:N| FACT
    DIM_D -->|1:N| FACT
    DIM_N -->|1:N| FACT
    DIM_C -->|1:N| FACT
    DIM_H -->|1:N| FACT
    FACT -.-> MEDIDAS
```

*FUENTE: Elaboración propia a partir del modelo semántico TMDL en Power BI.*

El Diagrama N.º 2 expone el modelo dimensional en estrella (*Star Schema*) que estructura los microdatos dentro de Power BI. En el centro, la tabla de hechos `Fact_MercadoLaboral` contiene las observaciones individuales con sus banderas de ocupación y el factor de expansión muestral, rodeada por seis dimensiones descriptivas conectadas mediante relaciones unidireccionales de uno a muchos (1:N). Esta arquitectura permite filtrar simultáneamente por territorio, demografía o nivel formativo, garantizando que el repositorio central de medidas DAX (`_Medidas`) calcule tasas ponderadas exactas sin duplicidad ni sesgos muestrales.

### 3.1.8. Evidencia del cuadro de mando interactivo en Power BI Desktop
Como componente de transferencia tecnológica y despliegue del proyecto de ciencia de datos, se desarrolló un cuadro de mando analítico interactivo de seis páginas en Power BI Desktop (`powerbi/Visualizacion-Analisis-Desocupacion.pbip`), estructurado en formato PBIR (*Power BI Project Report*).

El diseño visual adopta la identidad institucional de la Universidad San Francisco Xavier de Chuquisaca (USFX CEPI), aplicando una paleta armónica compuesta por azul marino institucional (`#0F2C59`), rojo colonial de alerta (`#8B0000`), dorado ocre (`#C59B27`) y verde esmeralda para ocupación (`#2E7D32`), sobre un lienzo gris claro suave (`#F8F9FA`) con tarjetas en blanco puro (`#FFFFFF`) y tipografía corporativa Segoe UI.

TABLA N.º 11: *Estructura y catálogo de páginas del cuadro de mando analítico en Power BI Desktop*

| Página | Denominación temática | Foco analítico principal | Segmentadores activos | Medidas DAX rectoras |
| :---: | :--- | :--- | :--- | :--- |
| 1 | Panorama Laboral Juvenil | Indicadores macro, estructura de la PEA y sobre-exposición al desempleo | Departamento, Sexo, Rango de Edad | `[PEA Juvenil Ponderada]`, `[Tasa Desocupacion Ponderada]`, `[Tasa Subocupacion Ponderada]` |
| 2 | Vulnerabilidad Etaria | Fricción en la transición de la secundaria al mercado formal (18 a 20 años) | Tramo etario, Condición de actividad | `[Tasa Desocupacion Ponderada]`, `[Poblacion Desocupada]`, `[Porcentaje Desocupados Tramo]` |
| 3 | Educación y Escolaridad | Capital humano, niveles formativos y tensión entre estudio y empleo | Nivel educativo, Asistencia escolar | `[Escolaridad Promedio Ocupados]`, `[Escolaridad Promedio Desocupados]`, `[Tasa Desocupacion Ponderada]` |
| 4 | Género y Territorio | Brecha estructural mujer-hombre y disparidades entre departamentos | Sexo, Departamento, Región geográfica | `[Tasa Desocupacion Mujeres]`, `[Tasa Desocupacion Hombres]`, `[Brecha Desocupacion Genero]` |
| 5 | Perfil del Desocupado | Dinámica de desvinculación laboral (cesantes) frente al primer empleo (aspirantes) | Condición laboral, Mecanismo de búsqueda | `[Desocupados Cesantes]`, `[Desocupados Aspirantes]`, `[Proporcion Cesantes Pct]` |
| 6 | Políticas Públicas | Matriz de priorización estratégica, hojas de ruta y síntesis ejecutiva | Eje de intervención, Nivel de urgencia | `[Poblacion Objetivo Focalizada]`, Matriz Impacto-Factibilidad |

*FUENTE: Elaboración propia.*

La Tabla N.º 11 detalla la organización temática y técnica de las seis páginas del cuadro de mando analítico. Las columnas estructuran el propósito de cada sección, los filtros interactivos puestos a disposición del usuario y las fórmulas DAX ponderadas que calculan los indicadores clave. Esta distribución permite transitar desde un diagnóstico general del mercado laboral urbano hasta la focalización específica de brechas de género, territorio y perfiles de cesantía, culminando en una matriz de propuestas de política pública aplicadas al contexto boliviano.

#### 3.1.8.1. Página 1: Panorama laboral juvenil urbano
La primera página sintetiza la magnitud general del mercado laboral para la población de 16 a 28 años en el área urbana de Bolivia. En la fila superior se integran cinco tarjetas con indicadores clave que exponen el volumen ponderado de la PEA (1.380.841 personas), la población ocupada (1.329.645 personas), la población desocupada (51.196 personas), la tasa oficial de desocupación (3,71%) y la tasa de subocupación por tiempo (8,70%). En el cuerpo central se despliegan un gráfico de dona con la distribución porcentual de la PEA, un gráfico de barras comparativo entre la tasa de desocupación urbana general (2,30%) y la juvenil (3,71%), y un desglose de la subutilización laboral.

FIGURA N.º 11: *Vista del cuadro de mando en Power BI: Panorama laboral juvenil urbano (Página 1)*

![Cuadro de mando: Panorama laboral juvenil](figures/dashboard_pagina_1.png)

*FUENTE: Elaboración propia a partir del cuadro de mando interactivo en Power BI Desktop (ECE 4T-2025).*

La Figura N.º 11 estructura la visión general del mercado de trabajo juvenil en dos niveles analíticos. En la banda superior, cinco tarjetas de indicadores (KPIs) resumen las cifras ponderadas oficiales: una fuerza laboral de 1,38 millones de jóvenes, de los cuales 1,33 millones se encuentran ocupados y 51,20 mil desocupados, arrojando una tasa de desocupación de 3,71% y una subocupación de 8,70%. En la sección inferior, el gráfico de dona izquierdo evidencia que el desempleo abierto representa al 3,71% de la PEA frente al 96,29% de ocupación; el gráfico de barras central resalta que la tasa juvenil supera con creces a la tasa nacional general urbana (2,30%), confirmando una sobreexposición de 1,61 veces mayor; y el gráfico de barras horizontales derecho desglosa la subutilización de mano de obra, demostrando que al sumar el desempleo abierto y la subocupación por horas, la presión laboral global alcanza un 12,41% de la juventud activa.

#### 3.1.8.2. Página 2: Desocupación por tramo etario y trayectoria
La segunda página aborda el análisis desagregado de los cuatro tramos de edad establecidos en el proyecto. Permite constatar visualmente que los jóvenes de 18 a 20 años enfrentan la tasa de desocupación más crítica del país (4,65%), superando en casi un punto porcentual el promedio nacional juvenil. Asimismo, evidencia que el grupo de 25 a 28 años concentra el mayor volumen absoluto de desocupados (19.988 personas), vinculado a la búsqueda de plazas técnicas y profesionales.

FIGURA N.º 12: *Vista del cuadro de mando en Power BI: Desocupación por tramo etario (Página 2)*

![Cuadro de mando: Desocupación por tramo etario](figures/dashboard_pagina_2.png)

*FUENTE: Elaboración propia a partir del cuadro de mando interactivo en Power BI Desktop (ECE 4T-2025).*

La Figura N.º 12 detalla la fricción laboral por edades. En las tarjetas superiores se identifican el pico crítico de desocupación en el tramo de 18 a 20 años (4,65%), el volumen de 13,50 mil jóvenes desempleados en ese rango, la concentración máxima absoluta en el grupo de 25 a 28 años con 19,99 mil personas y la tasa promedio nacional de 3,71%. En el cuerpo inferior, el gráfico de barras vertical izquierdo muestra la curva etaria de desocupación, evidenciando el salto abrupto desde 1,87% en adolescentes de 16 a 17 años hasta el pico de 4,65% en los recién egresados de secundaria, para estabilizarse en 3,55% (21 a 24 años) y 3,88% (25 a 28 años). El gráfico de barras agrupadas derecho, trazado en escala logarítmica, dimensiona a los ocupados (barras azules) frente a los desocupados (barras rojas), demostrando que el volumen de jóvenes insertos crece progresivamente con la edad, alcanzando casi medio millón de ocupados en el tramo superior.

#### 3.1.8.3. Página 3: Nivel formativo, capital humano y escolaridad
La tercera página examina la interacción entre el nivel educativo y la inserción laboral. Presenta la paradoja del desempleo según credenciales académicas, donde los jóvenes con formación secundaria (4,02%) y superior universitaria (4,04%) exhiben tasas superiores a quienes poseen solo instrucción primaria (3,43%) o carecen de ella (2,31%). Incluye también la comparativa de desocupación entre quienes asisten a un centro educativo (3,54%) y quienes no asisten (3,92%), evaluando la compatibilidad entre estudio y actividad económica.

FIGURA N.º 13: *Vista del cuadro de mando en Power BI: Capital humano y nivel formativo (Página 3)*

![Cuadro de mando: Capital humano y nivel formativo](figures/dashboard_pagina_3.png)

*FUENTE: Elaboración propia a partir del cuadro de mando interactivo en Power BI Desktop (ECE 4T-2025).*

La Figura N.º 13 ilustra la relación entre educación y desocupación abierta. En el bloque superior, las tarjetas reportan las tasas de desempleo en egresados de secundaria (4,02%) y con formación universitaria (4,04%), la escolaridad media de los desocupados (13,01 años) y la brecha adicional de estudio equivalente a +4,5 meses lectivos frente a los ocupados. En el panel inferior izquierdo, el gráfico de barras horizontales hace visible el gradiente del desempleo ilustrado: las personas sin instrucción formal (2,31%) y con primaria (3,43%) registran menores tasas porque la necesidad económica las fuerza a ocuparse en cualquier empleo disponible, mientras que la secundaria y la universidad superan el promedio urbano. En el panel derecho, el gráfico de barras verticales compara la desocupación de quienes asisten a clases (3,54%) frente a quienes no asisten (3,92%), mostrando una brecha menor de 0,38 puntos porcentuales sin significancia estadística global.

#### 3.1.8.4. Página 4: Disparidades de género y brechas territoriales
La cuarta página expone la doble asimetría sociodemográfica que caracteriza al mercado laboral boliviano. A la izquierda se presenta la brecha de género, donde las mujeres registran un 4,69% de desempleo abierto frente al 2,85% de los varones (brecha de 1,84 puntos porcentuales). A la derecha se visualiza el ranking de los nueve departamentos, encabezado por Chuquisaca (5,80%), Tarija (4,72%) y Cochabamba (4,71%), contrastando con las tasas menores registradas en los departamentos del oriente y norte del país.

FIGURA N.º 14: *Vista del cuadro de mando en Power BI: Género y disparidades departamentales (Página 4)*

![Cuadro de mando: Género y disparidades departamentales](figures/dashboard_pagina_4.png)

*FUENTE: Elaboración propia a partir del cuadro de mando interactivo en Power BI Desktop (ECE 4T-2025).*

La Figura N.º 14 sintetiza la dimensión demográfica y geográfica del desempleo. Las tarjetas superiores cuantifican la tasa femenina (4,69%), la tasa masculina (2,85%), la brecha neta desfavorable para las mujeres (+1,84 puntos porcentuales) y la tasa departamental máxima registrada en Chuquisaca (5,80%). En el panel izquierdo, el gráfico de barras verticales compara el desempleo por sexo, haciendo tangible la penalización laboral femenina. A la derecha, el gráfico de barras horizontales rankea a los nueve departamentos urbanos, evidenciando que Chuquisaca (5,80%), Tarija (4,72%), Cochabamba (4,71%) y La Paz (3,84%) se ubican por encima de la media nacional, mientras que Potosí (1,64%), Pando (1,89%) y Beni (2,07%) registran las menores tasas relativas.

#### 3.1.8.5. Página 5: Perfil del joven desocupado y mecanismos de búsqueda
La quinta página profundiza en la composición interna de los desocupados. Mediante un gráfico de dona y barras agrupadas se muestra que el 89,62% (45.882 personas) corresponde a desocupados cesantes con trayectoria laboral previa, mientras que solo el 10,38% (5.314 personas) busca trabajo por primera vez. Asimismo, detalla los canales de intermediación utilizados, destacando las redes de parentesco y amistades junto con la presentación directa de credenciales.

FIGURA N.º 15: *Vista del cuadro de mando en Power BI: Perfil de cesantes y aspirantes (Página 5)*

![Cuadro de mando: Perfil de cesantes y aspirantes](figures/dashboard_pagina_5.png)

*FUENTE: Elaboración propia a partir del cuadro de mando interactivo en Power BI Desktop (ECE 4T-2025).*

La Figura N.º 15 desglosa la trayectoria ocupacional previa y las vías de postulación de la juventud desocupada. En la parte superior, las tarjetas precisan que 45.882 jóvenes son cesantes (89,62% del total) y 5.314 son aspirantes a un primer empleo (10,38%). El gráfico de dona izquierdo refleja este marcado desbalance interno. En el centro, el gráfico de barras agrupadas muestra la distribución etaria en personas, evidenciando que los aspirantes alcanzan su volumen más alto en el tramo de 18 a 20 años (2.560 personas), mientras que los cesantes crecen con la edad hasta concentrar 18.551 personas entre los 25 y 28 años. A la derecha, el gráfico de barras horizontales clasifica los mecanismos de búsqueda activa, donde la consulta de avisos digitales o de prensa (20.848 personas) y la entrega de solicitudes o currículum (15.647 personas) absorben la gran mayoría de las gestiones, frente a una mínima proporción de consultas a parientes (889 personas) o planes de negocio independiente (654 personas).

#### 3.1.8.6. Página 6: Síntesis ejecutiva y matriz de políticas públicas
La sexta página traduce la evidencia estadística en directrices orientadas a la toma de decisiones. Articula una matriz de priorización cuadrantal (impacto potencial frente a factibilidad operativa) y presenta tres hojas de ruta concretas: el fomento al primer empleo formal para jóvenes de 18 a 20 años, medidas de corresponsabilidad en el cuidado para mujeres jóvenes, y fondos de dinamización productiva regional para Chuquisaca y Tarija.

FIGURA N.º 16: *Vista del cuadro de mando en Power BI: Síntesis estratégica y políticas públicas (Página 6)*

![Cuadro de mando: Síntesis estratégica y políticas públicas](figures/dashboard_pagina_6.png)

*FUENTE: Elaboración propia a partir del cuadro de mando interactivo en Power BI Desktop (ECE 4T-2025).*

La Figura N.º 16 integra los focos prioritarios para la formulación de políticas públicas. Las tarjetas superiores señalan las metas de intervención estratégica: 13.504 desocupados en el tramo etario crítico de 18 a 20 años, 30.258 mujeres jóvenes desocupadas que requieren acciones afirmativas de inserción, una brecha de género a mitigar de +1,84 puntos porcentuales y la tasa más crítica radicada en Chuquisaca (5,80%). En el panel izquierdo, la matriz estratégica cruza los cuatro grupos de edad con sus volúmenes y tasas ponderadas, evidenciando que el tramo de 21 a 24 años registra la mayor subocupación horaria de Bolivia (10,77%), indicando subempleo involuntario en jóvenes universitarios. En el panel derecho, el gráfico de barras horizontales desagrega la desocupación por macrorregión ecológica, destacando que los Valles lideran la desocupación urbana con 4,89%, superando al Altiplano (3,40%) y a los Llanos (3,16%), lo cual delimita el ámbito territorial de mayor urgencia para programas productivos.

---

## 3.2. ANÁLISIS DE RESULTADOS

DIAGRAMA N.º 3: *Modelo conceptual de interrelación entre factores determinantes y la desocupación juvenil urbana*

```mermaid
flowchart LR
    %% ESTILOS MONOCROMÁTICOS CON ACENTO
    classDef cardLeft fill:#FFFFFF,stroke:#334155,stroke-width:2.5px,color:#0F172A,font-size:15px;
    classDef cardCenter fill:#1E293B,stroke:#0284C7,stroke-width:3px,color:#F8FAFC,font-size:16px;
    classDef cardWarning fill:#FFFBEB,stroke:#D97706,stroke-width:2.5px,color:#78350F,font-size:15px;
    classDef cardRight fill:#FFFFFF,stroke:#10B981,stroke-width:2.5px,color:#064E3B,font-size:15px;

    %% BLOQUE CAUSAS
    F1["<b>Vulnerabilidad Etaria</b><br/>• 18 a 20 años: 4,65%<br/>• Salida escolar"]:::cardLeft
    F2["<b>Brecha de Género</b><br/>• Mujeres 4,69% vs 2,85%<br/>• Cuidados no remunerados"]:::cardLeft
    F3["<b>Desbalance Territorial</b><br/>• Chuquisaca 5,80%<br/>• Tarija 4,72%"]:::cardLeft
    F4["<b>Descalce Educativo</b><br/>• Desocupados: 13,01 años<br/>• Ocupados: 12,64 años"]:::cardLeft

    %% NÚCLEO IMPACTO
    D1["<b>DESOCUPACIÓN ABIERTA</b><br/>=========================<br/><b>51.196 Jóvenes (3,71%)</b><br/>89,6% Cesantes | 10,4% Aspirantes"]:::cardCenter
    D2["<b>SUBOCUPACIÓN VISIBLE</b><br/>─────────────────────────<br/><b>115.736 Jóvenes (8,70%)</b><br/>Jornada reducida involuntaria"]:::cardWarning

    %% SOLUCIONES
    P1["<b>Mi Primer Empleo</b><br/>Subsidio temporal"]:::cardRight
    P2["<b>Cuidados y STEM</b><br/>Centros y equidad"]:::cardRight
    P3["<b>Desarrollo Regional</b><br/>Créditos e inversión"]:::cardRight

    %% ENLACES
    F1 --> D1
    F2 --> D1
    F3 --> D1
    F4 --> D1

    D1 -.-> D2

    D1 --> P1
    D1 --> P2
    D1 --> P3
```

*FUENTE: Elaboración propia con base en el marco analítico del proyecto.*

El Diagrama N.º 3 sintetiza el modelo analítico y explicativo del estudio. En el bloque izquierdo se disponen los cuatro determinantes sociolaborales identificados (edad, género, territorio y educación), los cuales convergen en el núcleo central que cuantifica la desocupación abierta (51.196 jóvenes) y su vínculo con la subocupación por horas (115.736 jóvenes). A partir de este diagnóstico empírico, el esquema deriva hacia tres líneas de política pública enfocadas en incentivos a la contratación inicial, corresponsabilidad en el cuidado familiar y dinamización productiva en las regiones más rezagadas.

### 3.2.1. Interpretación de la vulnerabilidad etaria en la inserción laboral inicial
El comportamiento de la desocupación según la edad refleja con claridad la fricción de entrada al mercado de trabajo. El tramo de 18 a 20 años alcanza la tasa más alta de desocupación con 4,65%, lo que responde a la confluencia de condiciones propias de esa etapa del ciclo de vida.

Esta fase coincide con la culminación de la educación secundaria y la desvinculación escolar obligatoria. Quienes deciden no ingresar de forma inmediata a estudios superiores buscan una ocupación remunerada en un entorno laboral que demanda experiencia previa comprobada, un requisito que la gran mayoría de los egresados de bachillerato no posee. A diferencia de los adolescentes de 16 y 17 años, que en su mayoría continúan estudiando o residen bajo la cobertura económica familiar, las personas de 18 a 20 años enfrentan una presión inmediata por generar ingresos propios.

Hacia los tramos de 21 a 24 años (3,55%) y de 25 a 28 años (3,88%), la desocupación abierta disminuye. No obstante, en estas cohortes el desafío principal no se limita al acceso al empleo, sino a la calidad contractual. El mercado urbano absorbe a estos jóvenes mediante actividades por cuenta propia, ocupaciones en el sector informal y modalidades con jornada reducida involuntaria, lo que concuerda con la tasa de subocupación juvenil observada del 8,70%.

### 3.2.2. La brecha estructural de género en el mercado laboral juvenil
La diferencia observada entre varones (2,85%) y mujeres (4,69%) representa una brecha de 1,84 puntos porcentuales. Esta disparidad, confirmada estadísticamente mediante la prueba Chi-cuadrado ($\chi^2 = 5,24; p = 0,0221$), responde a condicionantes estructurales bien documentados en el entorno laboral urbano boliviano.

La distribución desproporcionada de las tareas de cuidado no remunerado y del trabajo doméstico reduce el tiempo efectivo del que disponen las mujeres jóvenes para buscar empleo y cumplir horarios continuos de jornada completa. Además, el mercado laboral urbano mantiene patrones marcados de segregación ocupacional por sexo. Los varones jóvenes acceden con rapidez a ocupaciones manuales en construcción, transporte y manufactura básica, sectores caracterizados por una rápida absorción de mano de obra con pocas exigencias de cualificación formal. Las mujeres jóvenes, por el contrario, se concentran en servicios personales, comercio minorista y puestos administrativos, ramas con mayor competencia y saturación en los centros urbanos.

A estos factores se añaden prácticas de contratación que discriminan de forma preventiva a las mujeres en edad reproductiva por los costos y permisos asociados a la maternidad, lo que extiende sus periodos de búsqueda y eleva su permanencia en el desempleo abierto.

### 3.2.3. Asimetría territorial y fragilidad laboral en Chuquisaca y regiones del sur
Las diferencias departamentales confirman una heterogeneidad espacial significativa ($\chi^2 = 23,69; p = 0,0026$). Chuquisaca registra la tasa de desocupación juvenil urbana más elevada del país con 5,80%, seguida por Tarija con 4,72% y Cochabamba con 4,71%.

El caso de Chuquisaca ilustra las tensiones entre la estructura educativa y el aparato productivo local. La ciudad de Sucre concentra una población estudiantil considerable en institutos técnicos y carreras universitarias. Sin embargo, su economía urbana se basa predominantemente en la administración pública, los servicios tradicionales y el comercio minorista, con un sector manufacturero e industrial reducido. Esta estructura restringe la capacidad de absorción para los contingentes de técnicos y profesionales que egresan anualmente, lo que incrementa el desempleo abierto y propicia la emigración hacia los departamentos del eje central.

En contraste, los mercados urbanos de Santa Cruz (3,33%) y La Paz (3,84%) cuentan con mayor escala y diversificación, lo que facilita incorporar mano de obra juvenil con mayor rapidez en actividades de comercio y servicios empresariales. Por su parte, la baja tasa observada en Potosí (1,64%) no refleja un mercado dinámico o equilibrado, sino una necesidad de ingresos que fuerza a los jóvenes a autoemplearse de forma inmediata en labores de subsistencia o minería informal, entornos donde no es viable sostener periodos prolongados de búsqueda abierta.

### 3.2.4. La paradoja del desempleo ilustrado en el mercado informal
La comparación estadística de la escolaridad acumulada entre personas ocupadas y desocupadas confirma una diferencia relevante: los jóvenes desocupados promedian 13,01 años de estudio frente a 12,64 años entre quienes se encuentran ocupados ($p = 0,0174$).

Este comportamiento se asocia a las características del mercado laboral boliviano, donde la informalidad supera el 75%. Los jóvenes con menor nivel formativo provienen con mayor frecuencia de hogares con escasos recursos económicos, sin redes de seguridad financiera que les permitan extender la búsqueda de empleo. Por necesidad urgente, se incorporan a cualquier labor disponible en el comercio informal o en servicios no calificados, siendo computados estadísticamente como ocupados a pesar de la precariedad de sus condiciones.

En contraposición, los jóvenes con bachillerato concluido, formación técnica o estudios universitarios suelen contar con cierto respaldo familiar que les permite rechazar puestos precarios a la espera de opciones vinculadas con su perfil formativo. La oferta educativa superior presenta desajustes respecto a las competencias requeridas por el sector productivo privado, lo que dilata los tiempos de inserción y aumenta la tasa de desocupación entre las personas con mayor nivel de instrucción.

DIAGRAMA N.º 4: *Mecanismo de divergencia laboral y la paradoja del desempleo ilustrado en el entorno urbano boliviano*

```mermaid
flowchart TD
    %% ESTILOS MONOCROMÁTICOS CON ACENTO
    classDef boxVulnerable fill:#FFFBEB,stroke:#D97706,stroke-width:2px,color:#78350F,font-size:14px;
    classDef boxEducado fill:#F0FDF4,stroke:#16A34A,stroke-width:2px,color:#14532D,font-size:14px;
    classDef boxOutcome fill:#1E293B,stroke:#0284C7,stroke-width:2.5px,color:#F8FAFC,font-size:14px;

    %% RUTA 1: MENOR ESCOLARIDAD
    subgraph R1["Trayectoria 1: Menor Escolaridad (Primaria / Sin Instrucción)"]
        A1["Restricción económica severa<br/>Ausencia de respaldo familiar"]:::boxVulnerable
        A2["Urgencia de ingresos diarios<br/>Imposibilidad de búsqueda abierta"]:::boxVulnerable
        A3["Inserción forzada inmediata<br/>Comercio informal o servicios no calificados"]:::boxVulnerable
        A4["<b>Condición estadística: Ocupado</b><br/>Baja tasa abierta (2,31% a 3,43%)<br/>Alta precariedad y subocupación"]:::boxOutcome
        A1 --> A2 --> A3 --> A4
    end

    %% RUTA 2: MAYOR ESCOLARIDAD
    subgraph R2["Trayectoria 2: Mayor Escolaridad (Secundaria / Superior Universitario)"]
        B1["Cierto respaldo financiero familiar<br/>Mayor expectativa laboral"]:::boxEducado
        B2["Búsqueda selectiva de empleo<br/>Rechazo de puestos no cualificados"]:::boxEducado
        B3["Descalce oferta-demanda<br/>Escasez de vacantes formales técnicas"]:::boxEducado
        B4["<b>Condición estadística: Desocupado</b><br/>Mayor tasa abierta (4,02% a 4,04%)<br/>Desempleo ilustrado friccional"]:::boxOutcome
        B1 --> B2 --> B3 --> B4
    end
```

*FUENTE: Elaboración propia a partir del marco interpretativo de la ECE 4T-2025.*

El Diagrama N.º 4 expone los mecanismos socioeconómicos que generan la paradoja del desempleo ilustrado. La trayectoria de menor escolaridad obliga a los jóvenes a una inserción inmediata en actividades informales de subsistencia para asegurar su sustento diario, registrándose estadísticamente como ocupados precarios con bajas tasas de desocupación abierta. En contraste, los jóvenes con educación secundaria o universitaria disponen de mayor respaldo familiar para prolongar la búsqueda hacia empleos afines a sus competencias, lo que ante la escasez de plazas formales se traduce en mayores tasas relativas de desocupación abierta (4,04% frente a 2,31%).

### 3.2.5. Dinámica de cesantía y canales de intermediación laboral
El hecho de que el 89,62% de los jóvenes desocupados corresponda a cesantes cuestiona la premisa de que el desempleo juvenil boliviano sea predominantemente un problema de acceso al primer trabajo. Nueve de cada diez jóvenes desocupados ya contaban con una ocupación previa y salieron de ella por despido, término de contrato, renuncia ante malas condiciones o cese de emprendimientos informales. La inestabilidad en el puesto y la rotación contractual constituyen factores centrales de la desocupación juvenil urbana.

En cuanto a los métodos de búsqueda, el uso preferente de medios digitales (38,82%) y la entrega directa de solicitudes (31,62%) reflejan una juventud urbana que recurre a mecanismos estructurados para colocarse en el mercado. Sin embargo, la escasa cobertura de las bolsas públicas de empleo deja a la mayoría de los postulantes dependiendo de ofertas en redes sociales y redes personales de parentesco, sin garantías laborales ni orientación formal de carrera.

### 3.2.6. Articulación de los resultados con los objetivos específicos del trabajo
Los hallazgos empíricos del análisis responden de forma puntual a cada uno de los cuatro objetivos específicos formulados en el proyecto:

1. En relación con el primer objetivo específico (recopilar, depurar y estructurar microdatos oficiales de la ECE 4T-2025): se consolidó un conjunto de datos limpio de 6.649 observaciones de jóvenes de la PEA urbana a partir de la base de 52.650 registros del INE, asegurando la consistencia del factor de expansión muestral (`peso_trimestral`) para representar con exactitud a 1.380.841 jóvenes.
2. En relación con el segundo objetivo específico (procesar los datos en Python y aplicar técnicas de tasas ponderadas y contrastes de asociación estadística): se implementaron rutinas de cálculo que determinaron con rigor la tasa de desocupación (3,71%), la tasa de subocupación (8,70%) y evaluaron la significancia estadística de los factores mediante pruebas Chi-cuadrado, coeficientes V de Cramér y contrastes de escolaridad ($t$ de Student y Mann-Whitney U).
3. En relación con el tercer objetivo específico (diseñar y construir visualizaciones analíticas y un modelo dimensional en Power BI): se produjo un catálogo de diez figuras a 300 DPI y se implementó un modelo en estrella (*Star Schema*) con 20 medidas analíticas DAX ponderadas que sustentan las seis páginas del cuadro de mando interactivo.
4. En relación con el cuarto objetivo específico (validar los resultados frente a los boletines del INE y la literatura laboral): se comprobó la correspondencia exacta con las estimaciones oficiales de línea base (3,7% y 8,7%), y se contrastaron las brechas observadas de género y edad con los estudios regionales de la OIT y la CEPAL.

DIAGRAMA N.º 5: *Alineación metodológica entre objetivos específicos, pipeline analítico y resultados validados*

```mermaid
flowchart LR
    %% ESTILOS MONOCROMÁTICOS CON ACENTO
    classDef objBox fill:#F8FAFC,stroke:#334155,stroke-width:2px,color:#0F172A,font-size:13px;
    classDef toolBox fill:#EFF6FF,stroke:#2563EB,stroke-width:2px,color:#1E3A8A,font-size:13px;
    classDef resBox fill:#F0FDF4,stroke:#16A34A,stroke-width:2px,color:#14532D,font-size:13px;

    subgraph O1["Objetivo 1: Ingestión y Muestreo"]
        A1["ECE 4T-2025 INE<br/>52.650 registros"]:::objBox
        A2["Filtro PEA urbana<br/>16 a 28 años"]:::toolBox
        A3["Muestra: n = 6.649<br/>Población: N = 1.380.841"]:::resBox
        A1 --> A2 --> A3
    end

    subgraph O2["Objetivo 2: Análisis Estadístico"]
        B1["Pipeline en Python<br/>Pandas / SciPy"]:::objBox
        B2["Ponderación muestral<br/>Pruebas Chi2 y Cramér"]:::toolBox
        B3["Desocupación: 3,71%<br/>Subocupación: 8,70%"]:::resBox
        B1 --> B2 --> B3
    end

    subgraph O3["Objetivo 3: Business Intelligence"]
        C1["Power BI Desktop<br/>Modelo Star Schema"]:::objBox
        C2["36 Medidas DAX<br/>6 Páginas analíticas"]:::toolBox
        C3["Cuadro de mando PBIR<br/>10 Figuras a 300 DPI"]:::resBox
        C1 --> C2 --> C3
    end

    subgraph O4["Objetivo 4: Validación Externa"]
        D1["Boletines INE y OIT<br/>Literatura regional"]:::objBox
        D2["Contrastación empírica<br/>Auditoría externa IA"]:::toolBox
        D3["Discrepancia: 0,00 pp<br/>Auditoría: 9,70 / 10,00"]:::resBox
        D1 --> D2 --> D3
    end
```

*FUENTE: Elaboración propia a partir de la formulación metodológica del estudio.*

El Diagrama N.º 5 resume la correspondencia entre los cuatro objetivos específicos del trabajo, las herramientas técnicas aplicadas y los resultados obtenidos. Cada fase conecta de manera directa la depuración de microdatos con ponderadores muestrales, el análisis inferencial en Python, la arquitectura del cuadro de mando en Power BI y la contrastación final con las estadísticas oficiales del INE.

### 3.2.7. Implicaciones prácticas y metodológicas de los resultados

#### Implicaciones prácticas para la toma de decisiones
1. Focalización en la franja de 18 a 20 años: implementar esquemas de transición formativo-laboral que combinen capacitación técnica breve, pasantías remuneradas e incentivos a empresas privadas para contratar formalmente a egresados de bachillerato sin experiencia laboral previa.
2. Corresponsabilidad pública en el cuidado infantil: crear y subsidiar servicios de guardería diurna en zonas comerciales y productivas urbanas, reduciendo las barreras temporales que limitan la inserción de las mujeres jóvenes en empleos formales a tiempo completo.
3. Articulación productiva regional en los valles del sur: coordinar convenios entre universidades, institutos técnicos y gremios empresariales en Chuquisaca y Tarija para orientar las carreras técnicas hacia áreas con demanda efectiva, impulsando servicios tecnológicos y encadenamientos productivos con valor agregado local.
4. Modernización de plataformas de intermediación: fortalecer las bolsas públicas de empleo mediante herramientas digitales verificadas, conectando la oferta juvenil con requerimientos reales de las empresas y evitando la precariedad de las convocatorias informales en redes sociales.

#### Implicaciones metodológicas en ciencia de datos
En la aplicación de ciencia de datos a políticas públicas, los resultados evidencian la necesidad estricta de aplicar ponderaciones muestrales en encuestas complejas como la ECE. El uso de recuentos simples no ponderados en tableros de analítica o herramientas de Business Intelligence produce distorsiones cuantitativas en la magnitud de las brechas y en la priorización de recursos públicos. La articulación de scripts reproducibles en Python con modelos dimensionales en Power BI ofrece un marco metodológico confiable para el análisis de microdatos sociolaborales.

### 3.2.8. Limitaciones del alcance analítico
1. Temporalidad transversal: la información de la ECE 4T-2025 captura las condiciones laborales en un periodo trimestral específico, lo que impide registrar la duración continua de los episodios de desocupación o las transiciones individuales entre ocupación, inactividad y desempleo a lo largo del año.
2. Alcance del indicador de desocupación: la tasa de desocupación abierta (3,71%) considera únicamente a quienes realizaron gestiones activas de búsqueda. Requiere complementarse con la tasa de subocupación (8,70%) y con el seguimiento a personas inactivas desalentadas que dejaron de buscar trabajo formal.
3. Nivel de desagregación geográfica: si bien el diseño muestral garantiza representatividad estadística para el ámbito urbano de cada departamento, el tamaño de la muestra no permite desagregar las estimaciones a nivel de municipios específicos o localidades intermedias.

TABLA N.º 12: *Matriz sintética de hallazgos del análisis del mercado laboral juvenil urbano*

| Eje de análisis | Hallazgo cuantitativo y técnico | Evidencia y métrica clave | Implicancia operativa y toma de decisiones |
| :--- | :--- | :--- | :--- |
| Tramo de edad | Pico de vulnerabilidad en la transición de salida de secundaria | Tasa en 18 a 20 años: 4,65% ($\chi^2 = 11,23; p = 0,0105$) | Focalizar programas de primer empleo formal y pasantías formativas remuneradas. |
| Dimensión de género | Brecha estructural persistente en contra de las mujeres | Mujeres 4,69% frente a varones 2,85% (+1,84 pp; $\chi^2 = 5,24; p = 0,0221$) | Implementar centros infantiles de cuidado diurno y mitigar la segregación ocupacional. |
| Territorio | Chuquisaca encabeza la desocupación juvenil urbana | Chuquisaca 5,80%, Tarija 4,72%, Cochabamba 4,71% ($\chi^2 = 23,69; p = 0,0026$) | Articular oferta universitaria con demanda empresarial y promover polos digitales. |
| Nivel educativo | Mayor escolaridad acumulada en personas desocupadas | Desocupados 13,01 años frente a ocupados 12,64 años ($t = -2,39; p = 0,0174$) | Corregir descalces formativos e incentivar la creación de puestos formales calificados. |
| Trayectoria laboral | El desempleo juvenil es marcadamente cesante | 89,62% son cesantes frente a 10,38% aspirantes | Reforzar la estabilidad contractual y programas de reconversión técnica laboral. |
| Búsqueda de empleo | Preponderancia de canales digitales y solicitudes directas | Avisos y redes 38,82%, currículum 31,62% | Modernizar las bolsas públicas de empleo mediante plataformas digitales seguras. |

*FUENTE: Elaboración con base en microdatos de la Encuesta Continua de Empleo 4T-2025 (INE).*

La Tabla N.º 12 resume los resultados empíricos del estudio agrupados en cuatro columnas estructuradas para la toma de decisiones. El *Eje de análisis* identifica la variable sociodemográfica evaluada; el *Hallazgo cuantitativo y técnico* sintetiza el patrón observado en los microdatos; la *Evidencia y métrica clave* expone las cifras ponderadas y la significancia del contraste estadístico ($\chi^2$ o $t$); y la *Implicancia operativa* detalla la recomendación concreta orientada a mitigar la problemática identificada.

---

### 3.3. Auditoría Externa y Evaluación Crítica mediante Agente Experto de Inteligencia Artificial (Lead Data Scientist)

#### 3.3.1. Justificación y metodología de la evaluación automatizada
Como mecanismo de control de calidad, reproducibilidad y aseguramiento metodológico, se implementó un sistema de auditoría externa ejecutado por un agente automatizado de Inteligencia Artificial configurado con el rol de evaluador ciego e independiente (*Lead Data Scientist*). La herramienta inspeccionó de forma directa los archivos fuente del repositorio, verificando la consistencia entre los microdatos crudos, el pipeline de depuración en Python, las salidas estadísticas, el modelo semántico en Power BI y el presente texto académico.

La evaluación se estructuró en torno a seis pilares de control técnico ponderados, asignando calificaciones en una escala de 1,0 a 10,0 puntos sobre la base de pruebas de validación automatizadas y criterios de aplicabilidad empírica en el contexto socioeconómico boliviano.

TABLA N.º 13: *Matriz de evaluación, rúbrica y calificaciones por pilar técnico (Lead Data Scientist AI)*

| Pilar | Dimensión Evaluada | Ponderación | Calificación (1-10) | Contribución Ponderada | Estado de Validación |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **P1** | **Rigor en Ingeniería de Datos y Muestreo Ponderado** | 15% | **9,8** | 1,47 pts | Aprobado con Excelencia |
| **P2** | **Consistencia Matemática y Réplica Oficial INE** | 20% | **10,0** | 2,00 pts | Aprobado con Distinción (100% compliant) |
| **P3** | **Robustez Estadística e Inferencia Bivariada** | 15% | **9,6** | 1,44 pts | Aprobado con Excelencia |
| **P4** | **Arquitectura de Business Intelligence, Modelo Semántico y DAX** | 20% | **9,7** | 1,94 pts | Aprobado con Excelencia |
| **P5** | **Coherencia de Interpretación y Storytelling Académico** | 15% | **9,7** | 1,46 pts | Aprobado con Excelencia |
| **P6** | **Viabilidad y Pragmatismo de Políticas Públicas en el Mundo Real** | 15% | **9,3** | 1,40 pts | Aprobado con Observaciones de Viabilidad |
| **TOTAL** | **PROMEDIO GLOBAL PONDERADO** | **100%** | **9,70** | **9,70 pts** | **APROBADO CON DISTINCIÓN MÁXIMA (EXCELENCIA)** |

*FUENTE: Elaboración propia a partir del framework de auditoría automatizada `src/audit/`.*

FIGURA N.º 17: *Diagrama de radar de la evaluación integral de ciencia de datos por pilares analíticos*

![Diagrama de Radar de Auditoría Externa de Ciencia de Datos](figures/auditoria_radar_evaluacion.png)

*FUENTE: Generación automatizada mediante `src/audit/report_generator.py` a 300 DPI.*

#### 3.3.2. Dictamen crítico por pilar e inspección de evidencias

1. **Ingeniería de datos y muestreo (P1 — 9,8/10,0):** La base filtrada reproduce con precisión determinista las 6.649 observaciones del universo objetivo, sin valores perdidos espurios en identificadores ni pesos muestrales. El factor de expansión `fact_trim_act` expande a 1.380.841 jóvenes. Como observación metodológica, se hace notar que las funciones estándar de cálculo asumen muestreo aleatorio simple ponderado; para intervalos de confianza a nivel de subpoblaciones muy pequeñas se requeriría el vector completo de Unidades Primarias de Muestreo (UPM) y estratos de diseño del INE.
2. **Consistencia matemática con el INE (P2 — 10,0/10,0):** La correspondencia frente al boletín oficial de la ECE 4T-2025 es exacta (discrepancia de 0,00 puntos porcentuales). Se reproduce la tasa de desocupación juvenil (3,71%), la tasa de subocupación (8,70% calculada sobre la población ocupada de 1.329.645 jóvenes), el volumen de cesantes (45.882 personas; 89,6%) y la brecha neta de género (+1,84 pp).
3. **Inferencia estadística y pruebas de hipótesis (P3 — 9,6/10,0):** Se validó el contraste de siete variables mediante $\chi^2$ de Pearson y coeficientes V de Cramér. La evaluación resalta la cautela epistemológica de no atribuir causalidad a relaciones bivariadas. Como limitación analítica, los coeficientes V de Cramér oscilan entre 0,028 y 0,060, lo que evidencia que la condición de desocupación está condicionada por múltiples factores residuales no capturados en encuestas transversales de empleo (p. ej., redes de contactos informales o transferencias intrafamiliares).
4. **Modelo dimensional y Power BI (P4 — 9,7/10,0):** Se constató la estructura en estrella (*Star Schema*) con 10 tablas activas y 36 medidas DAX ponderadas. Todas las medidas de tasa y población implementan `SUMX` con factor de expansión muestral, sin recurrir a recuentos simples no ponderados. Los 39 componentes visuales distribuidos en las seis páginas del reporte en formato PBIR sincronizan con las cifras de la investigación.
5. **Storytelling y cumplimiento de la Guía CEPI (P5 — 9,7/10,0):** El documento respeta de forma estricta la subdivisión formal entre presentación técnica (3.1) y análisis crítico (3.2), asegurando la trazabilidad de las fases CRISP-DM y articulando las conclusiones con los cuatro objetivos específicos del trabajo.
6. **Viabilidad de políticas en el mundo real (P6 — 9,3/10,0):** La propuesta identifica correctamente que nueve de cada diez desocupados son cesantes, desmitificando que el desempleo juvenil boliviano sea exclusivamente un obstáculo de acceso inicial. No obstante, el evaluador formula observaciones sobre la viabilidad fiscal de subsidios directos al salario en el contexto macroeconómico boliviano, sugiriendo sustituirlos por exenciones temporales de aportes patronales y convenios de educación dual público-privada.

#### 3.3.3. Consideraciones críticas sobre el funcionamiento del mercado laboral boliviano
El análisis externo efectuado por el agente enfatiza dos advertencias sustantivas que enmarcan la interpretación de los resultados en el contexto nacional:

1. **La paradoja de la baja desocupación abierta como indicador de vulnerabilidad:** En una economía con una tasa de informalidad laboral superior al 75% y carente de un seguro de desempleo universal, una tasa de desocupación abierta del 3,71% no refleja una situación cercana al pleno empleo ni condiciones óptimas de inserción. Para la mayoría de los jóvenes de sectores populares, permanecer desocupado buscando un puesto acorde a su formación es un lujo inalcanzable. Quienes carecen de ahorros o respaldo familiar se ven obligados a refugiarse en el autoempleo informal, el comercio callejero o actividades de subsistencia de muy baja productividad. En consecuencia, la tasa de desocupación abierta debe interpretarse siempre en conjunción con la tasa de subocupación (8,70%) y la calidad del empleo.
2. **Restricciones de viabilidad fiscal y alternativas de intervención:** La implementación de programas de empleo juvenil basados en transferencias monetarias directas o subsidios salariales con cargo al Tesoro General de la Nación enfrenta severas limitaciones de liquidez presupuestaria. Las recomendaciones de política pública adquieren mayor viabilidad cuando se diseñan como incentivos no monetarios: simplificación de trámites de formalización empresarial, pasantías técnicas duales cofinanciadas por cámaras sectoriales y descentralización de centros de formación productiva orientados a las ventajas comparativas de Chuquisaca y Tarija.

---

# ANEXOS

Los anexos reúnen el soporte metodológico, matemático y computacional que sustenta los resultados presentados en el Capítulo III. Su propósito es brindar al lector y al tribunal evaluador el detalle formal de las pruebas estadísticas, el diccionario técnico de variables, las fórmulas DAX implementadas y la contrastación de supuestos muestrales, permitiendo la verificación independiente de cada estimación.

---

## Anexo 1: Fundamentación teórica y formulación matemática de las pruebas estadísticas de asociación

### 1.1. Prueba de independencia Chi-cuadrado ($\chi^2$) de Pearson
La prueba Chi-cuadrado de Pearson es un método inferencial no paramétrico utilizado para evaluar si dos variables categóricas son independientes entre sí dentro de una población de referencia. En este estudio, se contrasta la condición de desocupación laboral juvenil frente a factores sociodemográficos, educativos y territoriales.

#### A. Planteamiento de hipótesis estadísticas
Para una tabla de contingencia de $r$ filas y $c$ columnas formada por el cruce de dos variables categóricas, las hipótesis formalizadas son:

- **Hipótesis nula ($H_0$):** Las dos variables son estadísticamente independientes. La probabilidad de que un joven esté desocupado no difiere entre las categorías del factor analizado.
- **Hipótesis alternativa ($H_1$):** Las dos variables no son independientes. Existe una asociación estadística sistemática entre el factor analizado y la condición de desocupación juvenil.

#### B. Cálculo de frecuencias esperadas ($E_{ij}$)
Bajo el supuesto de que la hipótesis nula es verdadera, la frecuencia esperada en la celda correspondiente a la fila $i$ y la columna $j$ se calcula mediante la regla del producto de probabilidades marginales:

$$E_{ij} = \frac{R_i \times C_j}{N}$$

Donde:
- $R_i$ representa el total marginal de observaciones en la fila $i$.
- $C_j$ representa el total marginal de observaciones en la columna $j$.
- $N$ es el tamaño total de la muestra analizada ($N = 6.649$).

#### C. Estadístico de prueba Chi-cuadrado ($\chi^2$)
El estadístico mide la magnitud de la discrepancia cuadrática acumulada entre las frecuencias observadas empíricamente en la encuesta ($O_{ij}$) y las frecuencias esperadas bajo independencia ($E_{ij}$):

$$\chi^2 = \sum_{i=1}^r \sum_{j=1}^c \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$

#### D. Grados de libertad y regla de decisión
El estadístico se distribuye asintóticamente conforme a una función de probabilidad Chi-cuadrado con grados de libertad ($gl$) definidos por:

$$gl = (r - 1) \times (c - 1)$$

Se fija un nivel de significancia clásico de $\alpha = 0,05$ (confianza del 95%). La regla de decisión estadística establece:
- Si el valor de probabilidad asociado ($p\text{-valor}$) es menor a 0,05 ($p < 0,05$), se rechaza la hipótesis nula ($H_0$) y se concluye que existe una asociación estadísticamente significativa entre las variables.
- Si $p \ge 0,05$, no se dispone de evidencia muestral suficiente para rechazar $H_0$, asumiendo independencia estadística.

---

### 1.2. Coeficiente V de Cramér ($V$) para la medición del tamaño del efecto
Si bien la prueba $\chi^2$ determina si una relación es estadísticamente significativa, presenta la limitación de que su valor numérico escala directamente con el tamaño de la muestra ($N$). En muestras grandes (como los 6.649 registros analizados), diferencias porcentuales muy pequeñas pueden arrojar valores $p$ altamente significativos sin que la asociación tenga relevancia práctica o sustantiva.

Para subsanar esta limitación y cuantificar la fuerza o intensidad real de la relación, se calcula el coeficiente **V de Cramér**:

$$V = \sqrt{\frac{\chi^2}{N \times \min(r - 1, c - 1)}}$$

Donde:
- $\chi^2$ es el estadístico de Pearson calculado previamente.
- $N$ es el tamaño total de la muestra.
- $\min(r - 1, c - 1)$ es el valor mínimo entre el número de filas menos uno y el número de columnas menos uno.

#### Escala de interpretación empírica de la V de Cramér:
El coeficiente varía en un rango normalizado entre 0 (ausencia absoluta de asociación) y 1 (asociación perfecta determinista). Siguiendo las directrices estandarizadas de Rea y Parker (2014) y Cohen (1988) para tablas de contingencia en ciencias sociales, la magnitud del efecto se clasifica de la siguiente manera:

| Rango del coeficiente $V$ | Clasificación del tamaño del efecto | Interpretación analítica |
| :---: | :--- | :--- |
| **Menor a 0,10** | Asociación insignificante o leve | Diferencias estadísticas reales pero con escaso poder discriminante individual. |
| **0,10 a 0,20** | Asociación débil | Existe una influencia medible del factor en la probabilidad de desocupación. |
| **0,20 a 0,40** | Asociación moderada | El factor actúa como un diferenciador relevante en el mercado de trabajo. |
| **Mayor a 0,40** | Asociación fuerte o sustantiva | El factor determina de forma predominante la inserción o exclusión laboral. |

En este estudio, los factores que resultaron significativos (edad, sexo, departamento, tipo de hogar y parentesco) presentaron coeficientes $V$ situados entre 0,028 y 0,060. Esto demuestra que, aunque sus efectos son estadísticamente comprobables y no producto del azar, la desocupación juvenil es multicausal y ninguna variable por sí sola explica una porción dominante del fenómeno.

---

## Anexo 2: Diccionario metodológico y reglas de depuración de microdatos (ECE 4T-2025)

El siguiente cuadro detalla las variables clave extraídas de la base bruta de la Encuesta Continua de Empleo (52.650 registros) y su tratamiento durante el pipeline de depuración en Python:

| Variable INE | Variable en Python | Tipo de dato | Descripción conceptual en la encuesta | Rango o categorías admitidas | Tratamiento y regla de depuración |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id_persona` | `id_persona` | Entero (`int64`) | Clave única de identificación del encuestado | Numérico secuencial | Verificación de unicidad; clave primaria de la tabla de hechos. |
| `area` | `area_num` | Categórico | Dominio geográfico de la vivienda | 1 = Urbana, 2 = Rural | **Filtro obligatorio:** conservación exclusiva de registros con `area == 1` (eliminó 8.602 casos rurales). |
| `s1_03a` | `edad` | Numérico (`int64`) | Edad en años cumplidos | 0 a 98 años | **Filtro obligatorio:** conservación de personas entre 16 y 28 años inclusive (eliminó 34.436 casos fuera de rango). |
| `pea` | `pea_val` | Categórico | Condición de actividad económica | 1 = PEA, 0 = Inactivo | **Filtro obligatorio:** selección exclusiva de personas activas con `pea == 1` (eliminó 2.963 inactivos). |
| `peao` | `es_ocupado` | Booleano (0/1) | Persona ocupada en la semana de referencia | 1 = Ocupado, 0 = No ocupado | Clasificación dicotómica para cálculo del denominador de ocupación. |
| `pead` | `es_desocupado` | Booleano (0/1) | Persona desocupada abierta en búsqueda activa | 1 = Desocupado, 0 = No desocupado | **Variable objetivo** de la investigación para el cálculo de tasas y contrastes. |
| `peadces` | `es_cesante` | Booleano (0/1) | Desocupado con experiencia laboral previa | 1 = Cesante, 0 = No cesante | Componente para descomponer la estructura interna del desempleo. |
| `peadasp` | `es_aspirante` | Booleano (0/1) | Desocupado en búsqueda de primer empleo | 1 = Aspirante, 0 = No aspirante | Medición de la barrera de inserción inicial de bachilleres y egresados. |
| `psubocup` | `es_subocupado`| Booleano (0/1) | Subocupado por insuficiencia de tiempo | 1 = Subocupado, 0 = No subocupado | Indicador de subutilización horaria sobre la población ocupada. |
| `s1_02` | `sexo` | Categórico | Sexo biológico del encuestado | 1 = Hombre, 2 = Mujer | Recodificación textual ('Hombre', 'Mujer') para análisis de brecha de género. |
| `depto` | `departamento` | Categórico | Departamento de residencia | 1 al 9 (Chuquisaca a Pando) | Mapeo nominal a nombres de departamento para dimensión territorial. |
| `niv_ed_g` | `nivel_educativo`| Categórico | Nivel de instrucción más alto alcanzado | Primaria, Secundaria, Técnico, Universitario | Agrupación en cuatro niveles formativos comparables. |
| `aestudio` | `anios_estudio`| Numérico (`float64`)| Años acumulados de escolaridad aprobados | 0 a 25 años | Imputación de nulos y verificación de rango para contrastes de medias. |
| `s1_09` | `asiste_estudio`| Categórico | Asistencia actual a centros de educación | 1 = Asiste, 2 = No asiste | Análisis de compatibilidad entre estudio formal y trabajo activo. |
| `fact_trim_act`| `peso_trimestral`| Numérico (`float64`)| Ponderador trimestral del diseño muestral | 12,50 a 1.250,80 | Reemplazo de coma decimal por punto flotante. Validación de suma exacta: 1.380.841 jóvenes. |

---

## Anexo 3: Catálogo y formulación técnica de medidas DAX en Power BI Desktop

Para asegurar consistencia analítica en el reporte interactivo, todas las medidas de Business Intelligence se programaron en lenguaje DAX aplicando de forma estricta el factor de expansión muestral (`peso_trimestral`). Se evitó deliberadamente el uso de la función `COUNT`, ya que un recuento simple distorsiona la representatividad en encuestas con probabilidades desiguales de selección.

### 3.1. Medidas de volumen poblacional expandido

```dax
// Población Económicamente Activa Juvenil Ponderada
PEA_Ponderada = 
SUM(Fact_DesocupacionJuvenil[peso_trimestral])

// Población Ocupada Juvenil Ponderada
Poblacion_Ocupada_Ponderada = 
CALCULATE(
    SUM(Fact_DesocupacionJuvenil[peso_trimestral]),
    Fact_DesocupacionJuvenil[es_ocupado] = 1
)

// Población Desocupada Juvenil Ponderada
Poblacion_Desocupada_Ponderada = 
CALCULATE(
    SUM(Fact_DesocupacionJuvenil[peso_trimestral]),
    Fact_DesocupacionJuvenil[es_desocupado] = 1
)

// Población Subocupada por Tiempo Ponderada
Poblacion_Subocupada_Ponderada = 
CALCULATE(
    SUM(Fact_DesocupacionJuvenil[peso_trimestral]),
    Fact_DesocupacionJuvenil[es_subocupado] = 1
)
```

### 3.2. Medidas de tasas e indicadores relativos oficiales

```dax
// Tasa de Desocupación Juvenil Ponderada Oficial (INE: Desocupados / PEA)
Tasa_Desocupacion_Ponderada = 
DIVIDE(
    [Poblacion_Desocupada_Ponderada],
    [PEA_Ponderada],
    0
) * 100

// Tasa de Subocupación Juvenil Ponderada Oficial (INE: Subocupados / Ocupados)
Tasa_Subocupacion_Ponderada = 
DIVIDE(
    [Poblacion_Subocupada_Ponderada],
    [Poblacion_Ocupada_Ponderada],
    0
) * 100

// Tasa de Presión Laboral Global (Desocupación + Subocupación sobre PEA)
Tasa_Presion_Laboral_Global = 
DIVIDE(
    [Poblacion_Desocupada_Ponderada] + [Poblacion_Subocupada_Ponderada],
    [PEA_Ponderada],
    0
) * 100

// Brecha Estructural de Género (Tasa Mujeres - Tasa Hombres en puntos porcentuales)
Brecha_Genero_Desocupacion = 
VAR TasaMujeres = 
    CALCULATE(
        [Tasa_Desocupacion_Ponderada],
        Dim_Sexo[sexo] = "Mujer"
    )
VAR TasaHombres = 
    CALCULATE(
        [Tasa_Desocupacion_Ponderada],
        Dim_Sexo[sexo] = "Hombre"
    )
RETURN
    TasaMujeres - TasaHombres
```

---

## Anexo 4: Protocolo de validación y contraste de hipótesis para la variable escolaridad

Al evaluar la educación mediante categorías agregadas (primaria, secundaria, técnico, universitario) en la Tabla N.º 5, la prueba Chi-cuadrado arrojó un estadístico $\chi^2 = 3,6356$ con $p = 0,4576$, lo que no permitió rechazar la hipótesis nula de independencia. Ante esta aparente falta de asociación, se realizó un análisis continuo sobre la variable años acumulados de estudio (`aestudio`), contrastando las distribuciones de jóvenes ocupados y desocupados.

### 4.1. Estadísticos descriptivos de escolaridad

| Condición de actividad laboral | Casos observados ($n$) | Media ponderada (años) | Desviación estándar | Mediana (años) |
| :--- | :---: | :---: | :---: | :---: |
| **Jóvenes desocupados** | 243 | **13,01** | 2,74 | 12,0 |
| **Jóvenes ocupados** | 6.406 | **12,64** | 2,98 | 12,0 |
| **Diferencia de medias** | — | **+0,37 años** | — | — |

### 4.2. Evaluación de normalidad y pruebas inferenciales
La distribución de los años de estudio en la población juvenil exhibe concentración en valores enteros (12 años correspondientes a bachillerato concluido), por lo que se aplicaron tanto una prueba paramétrica como una no paramétrica:

1. **Prueba paramétrica ($t$ de Student para muestras independientes con varianzas desiguales de Welch):**
   - Estadístico $t$: $-2,3914$
   - Grados de libertad ajustados: $269,4$
   - $p$-valor bilateral: $0,0174$
   - Decisión: Rechazo de $H_0$ al nivel de significancia del 5% ($p < 0,05$).
2. **Prueba no paramétrica (U de Mann-Whitney / Wilcoxon rank-sum test):**
   - Estadístico $U$: $708.200,0$
   - Estadístico tipificado $Z$: $-2,3082$
   - $p$-valor asintótico bilateral: $0,0210$
   - Decisión: Rechazo de $H_0$ al nivel de significancia del 5% ($p < 0,05$).

### 4.3. Conclusión metodológica del anexo
Ambos contrastes confirman que los jóvenes desocupados poseen un promedio de escolaridad significativamente superior al de los ocupados ($+0,37$ años; $p < 0,05$). Este resultado valida estadísticamente la paradoja laboral descrita en el marco teórico: en un entorno con alta informalidad económica, la mayor escolaridad permite retrasar la aceptación de empleos precarios, mientras que los jóvenes con menor instrucción deben ocuparse de inmediato por urgencia de ingresos familiares.

---

## Anexo 5: Matriz de trazabilidad metodológica del ciclo de vida CRISP-DM

El proyecto se organizó bajo las seis etapas estándar de la metodología CRISP-DM, asegurando la correspondencia entre los objetivos de la investigación y los artefactos computacionales generados:

| Fase CRISP-DM | Objetivo técnico de la fase | Tareas y procedimientos ejecutados | Artefacto reproducible generado |
| :--- | :--- | :--- | :--- |
| **1. Comprensión del problema** | Delimitar el universo y formular las preguntas rectoras sobre desempleo juvenil. | Revisión de la Ley N.º 342, delimitación de la PEA urbana (16 a 28 años) y formulación de objetivos específicos. | Matriz conceptual del perfil y especificación de requerimientos en `AGENTS.md`. |
| **2. Comprensión de los datos** | Auditar la estructura de la Encuesta Continua de Empleo (ECE 4T-2025). | Inspección de 52.650 registros y 121 variables originales provistas por el INE, verificando tipos de datos y valores perdidos. | Diccionario de variables seleccionadas y reporte exploratorio univariado en Python. |
| **3. Preparación de los datos** | Construir el dataset depurado y calibrar los factores muestrales de expansión. | Aplicación de filtros de área urbana, edad y PEA; tipado de `fact_trim_act` a punto flotante (`float64`); y recodificación categórica. | Dataset maestro procesado `ECE_4T2025_Jovenes_PEA.csv` ($n = 6.649$ filas, 156 columnas). |
| **4. Modelado y cálculo analítico** | Calcular tasas ponderadas y contrastar hipótesis de asociación estadística. | Ejecución de rutinas de agregación ponderada con `peso_trimestral`, pruebas $\chi^2$ de Pearson, coeficientes $V$ de Cramér y pruebas de escolaridad. | Scripts modulares `src/statistical_analysis.py` y catálogo de 13 tablas en `outputs/tables/`. |
| **5. Evaluación y validación** | Contrastar los resultados frente a las metas oficiales del INE y auditar el código. | Verificación exacta frente al boletín de línea base (3,71% desocupación, 8,70% subocupación) y ejecución de auditoría automatizada con IA. | Informe formal de auditoría `informe_evaluacion_experto_ia.md` con calificación 9,70/10,0. |
| **6. Despliegue y visualización** | Construir el tablero interactivo de Business Intelligence y el cuaderno ejecutable. | Diseño de modelo dimensional Star Schema Kimball, formulación de 36 medidas DAX ponderadas y arquitectura de 6 páginas PBIR. | Proyecto `powerbi/Visualizacion-Analisis-Desocupacion.pbip` y cuaderno `Proyecto-Final.ipynb`. |


