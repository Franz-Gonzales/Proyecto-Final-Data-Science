**UNIVERSIDAD MAYOR, REAL Y PONTIFICIA DE**  
**SAN FRANCISCO XAVIER DE CHUQUISACA**

**VICERRECTORADO**

**CENTRO DE ESTUDIOS DE POSGRADO E INVESTIGACIÓN**

**ANÁLISIS DE LOS FACTORES ASOCIADOS A LA DESOCUPACIÓN EN JÓVENES DE 16 A 28 AÑOS EN BOLIVIA**

**AUTOR**

**GONZALES SUYO FRANZ REINALDO**

**Sucre \- Bolivia**  
**2026**

**ÍNDICE DE CONTENIDO**

RESUMEN ....................................................................................................................... i

ÍNDICE DE CONTENIDO ................................................................................................ ii

ÍNDICE DE TABLAS ....................................................................................................... iii

ÍNDICE DE FIGURAS ..................................................................................................... iv

**CAPÍTULO I: INTRODUCCIÓN** ...................................................................................... 7

1.1. Antecedentes ........................................................................................................... 7

   1.1.1. Contexto general ................................................................................................ 7

   1.1.2. Antecedentes del empleo juvenil en Bolivia ....................................................... 7

   1.1.3. Información estadística disponible ..................................................................... 8

1.2. Problema o asunto del trabajo .................................................................................. 8

   1.2.1. Descripción de la situación problemática ........................................................... 9

   1.2.2. Delimitación del problema .................................................................................. 9

   1.2.3. Planteamiento del problema ............................................................................. 10

   1.2.4. Objeto de estudio ............................................................................................. 11

1.3. Objetivo general ..................................................................................................... 11

1.4. Objetivos específicos ............................................................................................. 11

1.5. Justificación ............................................................................................................ 12

1.6. Enfoque metodológico ............................................................................................ 13

   1.6.1. Tipo y alcance del trabajo ................................................................................. 13

   1.6.2. Población y unidad de análisis .......................................................................... 14

   1.6.3. Fuentes de información .................................................................................... 14

   1.6.4. Ruta metodológica ........................................................................................... 14

   1.6.5. Técnicas y herramientas .................................................................................. 15

   1.6.6. Validez, limitaciones y alcance del análisis ....................................................... 16

**CAPÍTULO II: MARCO REFERENCIAL** ....................................................................... 17

2.1. Marco teórico .......................................................................................................... 17

   2.1.1. Ciencia de Datos: fundamentos y alcance ........................................................ 17

   2.1.2. Estadística descriptiva aplicada al mercado laboral ......................................... 18

   2.1.3. Análisis Exploratorio de Datos (EDA) ............................................................... 19

   2.1.4. Juventud y mercado laboral .............................................................................. 20

   2.1.5. Población Económicamente Activa y condición de actividad …………….......... 21

   2.1.6. Desocupación, subocupación y su medición .................................................... 22

   2.1.7. Transición de la escuela al trabajo .................................................................... 23

   2.1.8. Segmentación del mercado laboral .................................................................. 24

   2.1.9. Factores asociados a la desocupación juvenil .................................................. 25

   2.1.10. Microdatos, encuestas por muestreo y factores de expansión ....................... 26

   2.1.11. Metodología CRISP-DM como ruta de trabajo ................................................ 27

   2.1.12. Python y Pandas como herramientas de análisis ........................................... 28

   2.1.13. Business Intelligence y visualización de datos ............................................... 29

   2.1.14. Power BI: arquitectura, componentes y aplicación ......................................... 30

   2.1.15. Modelo conceptual del trabajo ........................................................................ 31

2.2. Marco contextual .................................................................................................... 32

   2.2.1. Contexto normativo de la juventud en Bolivia ................................................... 32

   2.2.2. Contexto socioeconómico y demográfico de Bolivia ......................................... 33

   2.2.3. Mercado laboral urbano boliviano ..................................................................... 34

   2.2.4. Situación de la juventud en el contexto regional ............................................... 35

   2.2.5. Contexto educativo de la población joven ......................................................... 36

   2.2.6. Entorno estadístico y fuentes de datos ............................................................. 37

   2.2.7. Delimitación geográfica y temporal ................................................................... 38

   2.2.8. Síntesis del marco contextual ........................................................................... 39

**REFERENCIAS BIBLIOGRÁFICAS** ............................................................................ 40

**ÍNDICE DE TABLAS**

TABLA N.1: Fuentes de información previstas .............................................................. 11 

TABLA N.2: Fases de CRISP-DM adaptadas al proyecto ............................................. 13 TABLA N.3: Técnicas de Ciencia de Datos aplicadas en el proyecto ............................ 18 

TABLA N.4: Dimensiones y variables de análisis .......................................................... 25 TABLA N.5: Variables educativas disponibles en las fuentes de datos ……….............. 36

**ÍNDICE DE FIGURAS**

FIGURA N. 1: Bolivia urbana: tasa de desocupación general y juvenil, cuarto trimestre de 2025 ........................................................................................................................... 3 

FIGURA N. 2: Ruta metodológica CRISP-DM adaptada al proyecto ............................. 14 FIGURA N. 3: Modelo conceptual del análisis de factores asociados a la desocupación juvenil ............................................................................................................................ 31

## **CAPITULO I: INTRODUCCION**

1. ## **ANTECEDENTES**

**1.1.1. Contexto general**

La incorporación de las personas jóvenes al mercado laboral forma parte de la transición entre la educación y la vida de trabajo. En este periodo pueden coincidir la conclusión de los estudios, la formación técnica o universitaria, la búsqueda del primer empleo y la adquisición de experiencia. Por ello, la situación laboral de la juventud no es uniforme y puede variar según la etapa de vida, el nivel educativo, la experiencia previa y el entorno en el que se busca trabajo.

En América Latina y el Caribe, la Organización Internacional del Trabajo ha señalado que las personas jóvenes continúan enfrentando mayores dificultades para acceder a empleos formales y estables, aun en periodos de mejora de los indicadores generales del mercado laboral. El informe regional Juventud en cambio combina indicadores cuantitativos con evidencia cualitativa y destaca la persistencia de brechas relacionadas con la informalidad, el género y las oportunidades de inserción OIT, (Organización Internacional del Trabajo, 2025b). Por su parte, la Comisión Económica para América Latina y el Caribe y la Organización Internacional del Trabajo han estudiado la transición de la escuela al trabajo como un proceso que puede tomar trayectorias diferentes y que no se explica únicamente por una característica individual (Comisión Económica para América Latina y el Caribe & Organización Internacional del Trabajo, 2017).

### **1.1.2. Antecedentes del empleo juvenil en Bolivia**

En Bolivia, la Ley N.º 342 de la Juventud establece que la población joven comprende a las personas de 16 a 28 años. La norma reconoce el derecho al trabajo digno, el reconocimiento de pasantías y prácticas como experiencia laboral y la generación de condiciones para la inserción y el primer empleo (Estado Plurinacional de Bolivia, 2013). Este rango reúne etapas diferentes, desde jóvenes que todavía cursan estudios hasta personas que ya cuentan con formación profesional y experiencia previa.

Un antecedente específico para Bolivia es el estudio de la Organización Internacional del Trabajo Entre el bono demográfico y los ninis: Empleo juvenil en Bolivia, que realiza un diagnóstico de jóvenes que no estudian ni trabajan y analiza su localización y características con el propósito de orientar acciones para la transición de la escuela al trabajo (Organización Internacional del Trabajo, 2019). Aunque dicho estudio aborda una población distinta de la que se analizará en este trabajo, aporta elementos para comprender que las trayectorias juveniles combinan educación, participación laboral, responsabilidades familiares y búsqueda de oportunidades.

Los datos recientes del Instituto Nacional de Estadística muestran que en el cuarto trimestre de 2025 la tasa de desocupación del área urbana fue de 2,3%, mientras que para las personas de 16 a 28 años alcanzó 3,7%. El mismo boletín registró una tasa de subocupación juvenil de 8,7% (Instituto Nacional de Estadística, 2026a). Estas cifras describen un mercado laboral con una tasa agregada relativamente baja, pero con diferencias entre la población total y el grupo joven.

**FIGURA N. 1: Bolivia urbana: tasa de desocupación general y juvenil, cuarto trimestre de 2025**

*FUENTE: Elaboración propia con base en INE (2026a).*

### **1.1.3. Información estadística disponible**

El desarrollo del trabajo es viable porque existen fuentes estadísticas públicas con variables relacionadas con la población joven y su situación laboral. La Encuesta Continua de Empleo del cuarto trimestre de 2025 contiene 52.650 registros y 121 variables. Entre ellas se encuentran características sociodemográficas y educativas, condición de actividad, información sobre búsqueda de empleo, trayectoria laboral, variables derivadas y factores de expansión para estimaciones poblacionales (Instituto Nacional de Estadística, 2026b).

La Encuesta de Hogares puede complementar el análisis con información socioeconómica y educativa, mientras que la Encuesta de Niñas, Niños y Adolescentes que Realizan Actividad Laboral o Trabajan 2019 puede aportar contexto para el grupo de 16 y 17 años. Esta última contiene secciones de educación, empleo, tareas domésticas y derechos de recreación y asociación, por lo que su utilización sería complementaria y no sustituiría a la ECE como fuente principal (Instituto Nacional de Estadística, 2019).

En conjunto, estos antecedentes permiten plantear un estudio centrado en transformar microdatos y estadísticas existentes en información analítica sobre la desocupación juvenil. El aporte esperado no consiste solamente en presentar una tasa general, sino en identificar qué diferencias aparecen cuando la población se desagrega por edad, sexo, educación, territorio y trayectoria laboral.

## **1.2. PROBLEMA O ASUNTO DEL TRABAJO**

### **1.2.1. Descripción de la situación problemática**

Durante los últimos años, la tasa de desocupación urbana de Bolivia ha disminuido. Sin embargo, la información disponible muestra que la población joven presenta una tasa superior a la registrada para el conjunto del área urbana. En el cuarto trimestre de 2025, la tasa general fue de 2,3% y la correspondiente a las personas de 16 a 28 años fue de 3,7% (Instituto Nacional de Estadística, 2026a).

La población joven reúne situaciones diferentes. La edad puede coincidir con distintas etapas educativas y de ingreso al mercado de trabajo; el nivel educativo puede relacionarse con las oportunidades disponibles; y la experiencia previa permite diferenciar a quienes buscan su primer empleo de quienes ya tuvieron una ocupación. También pueden existir diferencias por sexo y territorio. Una tasa agregada, por sí sola, no permite observar con suficiente detalle cómo se distribuyen estas diferencias dentro del grupo juvenil.

La ECE contiene variables que permiten examinar estas características, entre ellas edad, sexo, nivel educativo, asistencia, departamento, condición de actividad, tiempo y mecanismos de búsqueda, experiencia laboral previa y variables que distinguen entre desocupados cesantes y aspirantes. Por ello, el asunto central del trabajo se concentra en identificar los factores que aparecen asociados a la desocupación juvenil y determinar qué grupos muestran las diferencias más relevantes.

### **1.2.2. Delimitación del problema**

El ámbito geográfico será el área urbana de Bolivia. La población de estudio estará formada por personas de 16 a 28 años pertenecientes a la Población Económicamente Activa. Dentro de este universo, la desocupación constituirá la condición central de análisis y la población ocupada se utilizará como referencia estadística para calcular tasas y comparar características.

Se considerarán principalmente la edad, el sexo, el nivel educativo, los años de estudio, la asistencia educativa, el territorio y la trayectoria laboral. La edad podrá organizarse inicialmente en los grupos 16 a 17, 18 a 20, 21 a 24 y 25 a 28 años para observar diferencias entre etapas de incorporación al mercado laboral. Según la disponibilidad de datos, también se examinarán el tiempo de búsqueda de empleo, los mecanismos de búsqueda y la condición de aspirante o cesante.

El análisis utilizará como fuente principal los microdatos de la Encuesta Continua de Empleo del cuarto trimestre de 2025\. Para describir la evolución reciente se utilizarán series agregadas de otros trimestres y, cuando resulte pertinente, información complementaria de la Encuesta de Hogares, la ENNA 2019, ILOSTAT y publicaciones de la Organización Internacional del Trabajo. Las fuentes con definiciones o rangos de edad distintos se utilizarán como referencia contextual y no se combinarán directamente sin verificar su comparabilidad.

### **1.2.3. Planteamiento del problema**

¿Cuáles son los factores sociodemográficos, educativos, territoriales y de trayectoria laboral asociados a la desocupación de jóvenes de 16 a 28 años en el área urbana de Bolivia?

### **1.2.4. Objeto de estudio**

El objeto de estudio está constituido por los factores asociados a la desocupación de jóvenes de 16 a 28 años en el área urbana de Bolivia, considerando sus características sociodemográficas, educativas, territoriales y de trayectoria laboral. La unidad de análisis será cada persona joven perteneciente a la Población Económicamente Activa que cumpla con la delimitación establecida.

## **1.3. OBJETIVO GENERAL**

Analizar los factores sociodemográficos, educativos, territoriales y de trayectoria laboral asociados a la desocupación de jóvenes de 16 a 28 años en el área urbana de Bolivia, para la identificación de patrones y diferencias relacionados con su inserción laboral a partir de información estadística oficial del mercado de trabajo.

## **1.4. OBJETIVOS ESPECÍFICOS**

1. Recopilar y organizar datos estadísticos provenientes de fuentes oficiales del mercado laboral boliviano, aplicando procesos de selección, limpieza y estructuración que permitan disponer de un conjunto de información confiable y listo para su análisis.  
2. Procesar y analizar los datos con herramientas de programación estadística en Python, aplicando técnicas de filtrado, transformación, segmentación por grupos de edad y análisis de asociaciones que permitan identificar los factores asociados a la desocupación juvenil.  
3. Diseñar y construir visualizaciones e indicadores analíticos con herramientas de inteligencia de negocios que faciliten la interpretación de los patrones, brechas y perfiles identificados en el análisis de la desocupación juvenil.  
4. Validar los resultados obtenidos, verificando la consistencia de los datos procesados, contrastándolos con indicadores oficiales publicados y revisando la coherencia entre los hallazgos y las fuentes utilizadas.

## **1.5. JUSTIFICACIÓN**

La desocupación juvenil tiene importancia social porque el acceso a una primera experiencia de trabajo influye en la trayectoria económica y profesional de las personas jóvenes. La población de 16 a 28 años no constituye un grupo homogéneo: dentro de ella conviven adolescentes que continúan estudiando, jóvenes que buscan su primer empleo, estudiantes de educación superior y personas que ya han tenido una experiencia laboral. Analizar estas diferencias permite describir con mayor precisión la situación de quienes participan activamente en el mercado de trabajo.

Por un lado, la inserción laboral es parte esencial del desarrollo económico y social de las personas. Una ocupación permite obtener ingresos, adquirir experiencia, desarrollar competencias profesionales y avanzar hacia una mayor autonomía económica. Estas circunstancias pueden retrasar la adquisición de experiencia laboral cuando el acceso al empleo es difícil, afectando de forma negativa la continuidad de la carrera profesional en el largo plazo.

En segundo lugar, la juventud es una etapa de transición particularmente sensible. Una parte importante de este grupo está en proceso de transición entre la educación y la vida laboral. Algunos jóvenes buscan trabajo al terminar la secundaria, otros continúan sus estudios en el nivel técnico o universitario, y otros más ya tienen cierta experiencia previa. Estas diferencias de origen generan condiciones desiguales de acceso al empleo y hacen necesario comprender con mayor precisión cuáles son los factores que dificultan la inserción laboral en cada caso.

En tercer lugar, si bien los indicadores generales del mercado laboral boliviano muestran una reducción de la desocupación urbana, la tasa de desocupación de los jóvenes entre 16 y 28 años (3,7%) continúa siendo superior a la tasa general (2,3%). Esta diferencia, sumada a la subocupación juvenil del 8,7%, indica que la problemática laboral de los jóvenes no se resuelve solamente con la creación de empleo agregado, sino que necesita de una atención específica hacia las barreras que encuentra este grupo para acceder y permanecer en el mercado de trabajo.

Desde el punto de vista práctico, este análisis aporta información concreta que puede servir de base para orientar decisiones relacionadas con la formación profesional, los mecanismos de intermediación laboral, las políticas de primer empleo y la generación de oportunidades dirigidas a la población joven. Identificar los factores que se asocian a la desocupación permite pasar de una visión general del problema a un diagnóstico más preciso, lo que facilita el diseño de acciones específicas.

Con los datos de que se dispone se pueden analizar con detalle dichas características. La Encuesta Continua de Empleo incluye datos sobre edad, sexo, educación, residencia, disponibilidad para trabajar, búsqueda de empleo, tiempo de búsqueda y experiencia laboral anterior, junto con los factores de expansión necesarios para producir estimaciones representativas de la población.

El proyecto consistirá en organizar y analizar dicha información mediante técnicas de Data Science, empleando para ello Python para el tratamiento y análisis de los datos, y Power BI para la presentación de los resultados. Se podrán usar, además de la Encuesta Continua de Empleo, otras fuentes de información sobre el tema, como la Encuesta de Hogares, estadísticas de la Organización Internacional del Trabajo y otros registros o bases de datos disponibles que sean compatibles con el análisis.

Los resultados permitirán identificar los grupos con mayores niveles de desocupación y las características que se relacionan con esta situación. Esta información puede servir de referencia para plantear recomendaciones relacionadas con la formación, la búsqueda de empleo, la experiencia laboral y otras acciones orientadas a facilitar la incorporación de los jóvenes al mercado de trabajo.

## **1.6. ENFOQUE METODOLÓGICO**

### **1.6.1. Tipo y alcance del trabajo**

El trabajo tendrá un enfoque cuantitativo, aplicado y no experimental. Su alcance será principalmente descriptivo-correlacional y diagnóstico: se describirá la distribución de la desocupación juvenil y se examinarán asociaciones entre esta condición y variables sociodemográficas, educativas, territoriales y de trayectoria laboral. 

El análisis de microdatos tendrá un corte transversal correspondiente al cuarto trimestre de 2025\. De manera complementaria se utilizarán series agregadas de periodos anteriores para describir la evolución reciente de la desocupación. Esta combinación permite mantener un análisis individual consistente y, al mismo tiempo, ubicar los resultados dentro de un contexto temporal más amplio.

### **1.6.2. Población y unidad de análisis**

La población de interés estará conformada por jóvenes de 16 a 28 años residentes en el área urbana de Bolivia y pertenecientes a la Población Económicamente Activa. La unidad de análisis será la persona. El resultado principal será la condición de desocupación; las personas ocupadas del mismo universo funcionarán como grupo de referencia para estimar tasas y evaluar diferencias entre perfiles.

### **1.6.3. Fuentes de información**

La Encuesta Continua de Empleo del cuarto trimestre de 2025 será la fuente principal por su periodicidad, cobertura laboral, disponibilidad de microdatos y presencia de variables derivadas y factores de expansión. Las fuentes adicionales se utilizarán según su pertinencia y compatibilidad con cada parte del análisis.

**TABLA N. 1: Fuentes de información previstas**

| Fuente | Uso en el trabajo | Carácter |
| ----- | ----- | ----- |
| Encuesta Continua de Empleo 4T-2025 (INE) | Microdatos principales para condición de actividad, educación, búsqueda, trayectoria laboral, territorio y ponderaciones. | Principal |
| Boletines y series ECE (INE) | Contexto histórico de tasas e indicadores agregados. | Complementaria |
| Encuesta de Hogares 2025 (INE) | Contraste de variables socioeconómicas, educativas y laborales. | Complementaria |
| ENNA 2019 (INE) | Contexto para adolescentes, especialmente el tramo de 16 y 17 años. | Complementaria |
| OIT / ILOSTAT | Marco regional, conceptos de transición escuela-trabajo e indicadores comparativos. | Contextual |
| Normativa y publicaciones del MTEPS | Marco legal e institucional de juventud e inserción laboral. | Contextual |

*FUENTE: Elaboración propia con base en INE, OIT y normativa boliviana.*

### **1.6.4. Ruta metodológica**

Como ruta de trabajo se adoptará CRISP-DM de manera adaptada. Esta metodología organiza los proyectos de datos en seis fases y permite avanzar de forma iterativa entre ellas. IBM señala que el proceso es flexible y puede ajustarse a proyectos en los que el objetivo principal sea la exploración y visualización de datos (IBM, s. f.). En este proyecto, la fase de modelado se orientará al análisis estadístico, construcción de indicadores y evaluación de asociaciones.

**TABLA N. 2: Fases de CRISP-DM adaptadas al proyecto**

| Fase | Aplicación en el perfil |
| ----- | ----- |
| 1\. Comprensión del problema | Definición del alcance, población, pregunta, objetivos e indicadores requeridos. |
| 2\. Comprensión de los datos | Revisión de diccionarios, calidad, cobertura, variables, categorías y factores de expansión. |
| 3\. Preparación de los datos | Filtrado 16-28 años, área urbana y PEA; limpieza, recodificación, integración y creación de segmentos. |
| 4\. Análisis estadístico y diagnóstico | Tasas ponderadas, distribuciones, tablas cruzadas, comparación de grupos y medidas de asociación. |
| 5\. Evaluación y validación | Comprobaciones de consistencia, contraste con cifras oficiales y revisión de resultados poco estables. |
| 6\. Comunicación y visualización | Construcción de gráficos, tablero en Power BI, interpretación y recomendaciones. |

*FUENTE: Elaboración propia con base en IBM (s. f.).*

**FIGURA N. 2: Ruta metodológica CRISP-DM adaptada al proyecto**

*FUENTE: Elaboración propia con base en IBM (s. f.).*

### **1.6.5. Técnicas y herramientas**

La preparación de datos se realizará en Python mediante estructuras reproducibles de lectura, selección, limpieza y transformación. Para el análisis se emplearán frecuencias, proporciones, tasas ponderadas, distribuciones, tablas cruzadas y comparaciones entre grupos. Cuando el tipo de variable lo permita, podrán utilizarse pruebas de asociación como chi-cuadrado y medidas de intensidad como V de Cramér; las variables ordinales o numéricas podrán examinarse mediante medidas descriptivas y asociaciones apropiadas. La selección final dependerá de la calidad y distribución de los datos.

En todos los cálculos poblacionales se considerarán los factores de expansión proporcionados por el Instituto Nacional de Estadística. Las desagregaciones con pocos casos muestrales se interpretarán con cautela y podrán agruparse cuando sea necesario. Power BI se utilizará como capa de comunicación, mediante indicadores, filtros y visualizaciones que permitan recorrer los resultados desde un panorama general hacia grupos específicos..

### **1.6.6. Validación**

La validación combinará controles técnicos y contrastes externos. Se verificarán tipos de datos, valores faltantes, duplicados, rangos válidos, filtros de población y consistencia de las variables derivadas. Los indicadores principales se compararán con cifras oficiales publicadas por el Instituto Nacional de Estadística, especialmente la tasa general y la tasa juvenil del periodo. 

# **CAPÍTULO II \- MARCO REFERENCIAL**

## **2.1. MARCO TEÓRICO**

### **2.1.1. Ciencia de Datos: fundamentos y alcance**

La Ciencia de Datos es un campo interdisciplinario que combina métodos estadísticos, técnicas de programación y conocimiento del dominio de un problema específico para extraer información útil a partir de conjuntos de datos, ya sean estructurados o no estructurados. Su propósito central es transformar datos crudos en conocimiento accionable que permita fundamentar decisiones informadas en cualquier ámbito de la actividad humana (Provost & Fawcett, 2013).

La Ciencia de Datos no se limita a una única técnica o herramienta. Integra múltiples disciplinas que, al combinarse, permiten abordar problemas complejos desde diferentes ángulos. La estadística proporciona los fundamentos para medir, describir e inferir patrones a partir de los datos; la programación permite automatizar procesos, manipular grandes volúmenes de información y construir análisis reproducibles; y el conocimiento del dominio garantiza que los resultados se interpreten correctamente dentro del contexto del problema que se estudia.

En el ámbito de las políticas públicas y el análisis social, la Ciencia de Datos ofrece un conjunto de técnicas que permiten pasar de la simple observación de cifras agregadas a un diagnóstico detallado de fenómenos complejos. Entre estas técnicas se encuentran el análisis descriptivo, que resume y organiza la información; el análisis diagnóstico, que busca identificar relaciones y diferencias entre grupos; y el análisis exploratorio, que permite descubrir patrones no evidentes a simple vista (Wickham & Grolemund, 2017).

Para el presente trabajo, la Ciencia de Datos se aplica con un enfoque predominantemente descriptivo y diagnóstico. Identificar patrones, diferencias y asociaciones entre las características de los jóvenes y su condición de desocupación. Este enfoque resulta coherente con la naturaleza de la pregunta de investigación, que busca comprender qué está ocurriendo y qué grupos presentan mayores brechas, más que predecir comportamientos futuros. 

**TABLA N. 3: Técnicas de Ciencia de Datos aplicadas en el proyecto**

| Técnica | Función en el proyecto |
| :---- | :---- |
| **Análisis descriptivo** | Resumir la distribución de la desocupación juvenil por edad, sexo, educación y territorio. |
| **Análisis exploratorio** | Descubrir patrones, anomalías y relaciones no evidentes en los microdatos. |
| **Análisis de asociaciones** | Identificar qué características aparecen con mayor frecuencia entre los jóvenes desocupados. |
| **Segmentación** | Comparar subgrupos etarios, educativos y territoriales para detectar brechas. |
| **Visualización analítica** | Comunicar los hallazgos de forma clara e interactiva. |

**FUENTE:** Elaboración propia con base en Provost y Fawcett (2013) y Wickham y Grolemund (2017).

### **2.1.2. Estadística descriptiva aplicada al análisis del mercado laboral**

La estadística descriptiva constituye la base de todo análisis cuantitativo. Su función es organizar, resumir y presentar los datos de manera que sea posible identificar sus características principales sin necesidad de examinar cada registro individual. En el contexto del mercado laboral, la estadística descriptiva permite calcular tasas, comparar grupos, describir distribuciones y detectar diferencias que de otra forma permanecerían ocultas en grandes volúmenes de información (Walpole, Myers, Myers & Ye, 2012).

Las medidas de tendencia central, como la media, la mediana y la moda, permiten identificar el valor típico o representativo de una variable. En el análisis del empleo juvenil, estas medidas resultan útiles para describir, por ejemplo, la edad promedio de los jóvenes desocupados o la cantidad mediana de años de estudio dentro de un grupo específico. La mediana es particularmente relevante cuando la distribución de una variable presenta valores extremos, ya que no se ve afectada por ellos de la misma forma que la media.

Las medidas de dispersión, como el rango, la varianza, la desviación estándar y el rango intercuartílico, permiten evaluar qué tan homogéneo o heterogéneo es un grupo. En el análisis de la desocupación juvenil, estas medidas ayudan a determinar si las características de los jóvenes desocupados son similares entre sí o si, por el contrario, presentan una gran variabilidad interna. Esta información es relevante porque un grupo muy heterogéneo puede requerir intervenciones diferenciadas, mientras que un grupo homogéneo podría beneficiarse de una política más focalizada.

Las tablas de contingencia y las distribuciones de frecuencia permiten cruzar dos o más variables categóricas para observar cómo se distribuyen las observaciones en cada combinación. Por ejemplo, una tabla de contingencia entre nivel educativo y condición de desocupación permite identificar si ciertos niveles educativos presentan proporciones de desocupación significativamente distintas a otros. Para evaluar si las diferencias observadas en estas tablas son estadísticamente relevantes o podrían deberse al azar, se utilizan pruebas de asociación como la prueba chi-cuadrado de Pearson y la medida de intensidad V de Cramér (Agresti, 2007).

La prueba chi-cuadrado evalúa si existe una relación estadísticamente significativa entre dos variables categóricas. Su hipótesis nula plantea que las variables son independientes, es decir, que la distribución de una no depende de la otra. Si el valor calculado de la prueba supera el valor crítico para un nivel de significancia determinado, se rechaza la hipótesis nula y se concluye que existe una asociación entre las variables. La V de Cramér complementa esta prueba al proporcionar una medida de la intensidad de la asociación, que varía entre 0 (sin asociación) y 1 (asociación perfecta), independientemente del tamaño de la muestra.

Es importante señalar que estas pruebas permiten identificar asociaciones, pero no establecen relaciones causales. Una asociación entre nivel educativo y desocupación no implica que la falta de educación cause la desocupación, sino que ambas variables aparecen relacionadas en los datos. La interpretación de estos resultados debe realizarse siempre con cautela y en el contexto de la literatura existente.

### **2.1.3. Análisis Exploratorio de Datos**

El Análisis Exploratorio de Datos, conocido por sus siglas en inglés como EDA (Exploratory Data Analysis), es un enfoque de análisis que fue formalizado por el estadístico John Wilder Tukey en 1977\. Su propósito es examinar un conjunto de datos para comprender su estructura, calidad, patrones y características principales antes de aplicar cualquier modelo formal o prueba de hipótesis. Como el propio Tukey señaló, el análisis exploratorio nunca puede ser la historia completa, pero casi siempre constituye el primer paso indispensable de cualquier investigación basada en datos (Tukey, 1977).

El EDA se distingue del análisis confirmatorio en que no parte de una hipótesis previa que deba verificarse. Su objetivo es dejar que los datos hablen, descubrir lo que contienen y generar preguntas e hipótesis que puedan explorarse en etapas posteriores. Esta característica lo hace especialmente adecuado para investigaciones de carácter diagnóstico, como la que se plantea en el presente trabajo, donde la pregunta central es identificar qué características se asocian con la desocupación juvenil sin asumir de antemano cuál es la respuesta.

Los objetivos principales del Análisis Exploratorio de Datos son seis. Primero, conocer la estructura del conjunto de datos: cuántas observaciones contiene, qué variables están disponibles, qué tipo de dato corresponde a cada una y cuántos valores faltantes existen. Segundo, resumir cada variable mediante estadísticos descriptivos que permitan comprender su distribución. Tercero, detectar relaciones entre variables mediante tablas cruzadas, gráficos de dispersión y medidas de asociación. Cuarto, identificar anomalías como valores atípicos, errores de captura o datos imposibles que puedan distorsionar los resultados. Quinto, verificar supuestos sobre la distribución de los datos que puedan ser relevantes para el análisis. Y sexto, formular hipótesis concretas que orienten las etapas posteriores del trabajo (Wickham & Grolemund, 2017).

El proceso del EDA es iterativo y no sigue una secuencia rígida. Cada gráfico o tabla generada puede revelar una pregunta nueva que lleve a una limpieza adicional, a una nueva visualización o a una reorganización de los datos. En el presente trabajo, el EDA se aplicará sobre los microdatos de la Encuesta Continua de Empleo para examinar la distribución de la desocupación juvenil por edad, sexo, nivel educativo, asistencia educativa, territorio y trayectoria laboral.

### **2.1.4. Juventud y mercado laboral**

La juventud no es una categoría homogénea ni universalmente definida. Su delimitación varía según el contexto institucional, legal y estadístico de cada país. En Bolivia, la Ley N.º 342 de la Juventud, promulgada el 5 de febrero de 2013, establece que son jóvenes las personas comprendidas entre los 16 y 28 años de edad. Esta norma reconoce, entre las áreas de protección y desarrollo de la juventud, el derecho al trabajo digno, la estabilidad laboral, el reconocimiento de pasantías y prácticas como experiencia laboral, y la generación de condiciones para la inserción y el primer empleo (Estado Plurinacional de Bolivia, 2013).

La amplitud del rango etario definido por la legislación boliviana tiene implicaciones importantes para el análisis. Una persona de 16 años puede encontrarse todavía cursando educación secundaria, mientras que una persona de 28 años puede haber finalizado estudios superiores y acumulado varios años de experiencia laboral. Estas diferencias internas hacen que el grupo juvenil no pueda tratarse como una población homogénea, y que el análisis deba observar las variaciones que existen entre sus distintos subgrupos.

El Instituto Nacional de Estadística de Bolivia utiliza específicamente el intervalo de 16 a 28 años en sus estadísticas laborales juveniles. El boletín de la Encuesta Continua de Empleo correspondiente al cuarto trimestre de 2025 identifica como jóvenes a las personas dentro de este rango y presenta indicadores diferenciados de desocupación, subocupación y participación laboral para este grupo (Instituto Nacional de Estadística, 2026a).

La incorporación de los jóvenes al mercado laboral forma parte de un proceso más amplio de transición entre la educación y la vida de trabajo. Durante este periodo pueden coincidir la finalización de estudios, la formación técnica o universitaria, la búsqueda del primer empleo y la adquisición progresiva de experiencia. Por ello, la situación laboral de la juventud no es uniforme y puede variar significativamente según la etapa de vida, el nivel educativo, la experiencia previa y el entorno en el que se busca trabajo (Comisión Económica para América Latina y el Caribe & Organización Internacional del Trabajo, 2017).

### **2.1.5. Población Económicamente Activa y condición de actividad**

Para analizar la desocupación es necesario ubicar primero a la población dentro de la estructura del mercado laboral. Las estadísticas de empleo no se refieren a la totalidad de la población, sino a la parte de ella que participa o está en condiciones de participar en la actividad económica. Esta clasificación se realiza a través del concepto de Población Económicamente Activa (PEA), que constituye el universo de referencia para el cálculo de las tasas de ocupación y desocupación.

La Población Económicamente Activa está compuesta por todas las personas en edad de trabajar que, durante el periodo de referencia, se encontraban ocupadas o desocupadas. Dentro de la PEA se distinguen dos categorías principales. Los ocupados son quienes realizaron algún trabajo remunerado durante el periodo de referencia o que, teniendo un empleo, no lo ejercieron temporalmente por razones como vacaciones, enfermedad o licencia. Los desocupados son quienes no tenían empleo, estaban disponibles para trabajar y realizaron acciones concretas de búsqueda de empleo durante el periodo de referencia (Organización Internacional del Trabajo, s. f.-b).

Las personas que no se encuentran en ninguna de estas dos categorías forman parte de la población económicamente inactiva. Este grupo incluye a quienes se dedican exclusivamente al estudio, a los quehaceres domésticos, a quienes están jubilados o pensionados, y a quienes, por cualquier otra razón, no participan en el mercado laboral. Es fundamental distinguir correctamente entre inactividad y desocupación, ya que una persona joven que estudia a tiempo completo y no busca trabajo no debe clasificarse como desocupada, sino como inactiva.

Dentro de la población desocupada, la Encuesta Continua de Empleo distingue entre dos subcategorías que resultan relevantes para el análisis juvenil. Los cesantes son quienes tuvieron un empleo anterior y lo perdieron o dejaron, y se encuentran buscando una nueva ocupación. Los aspirantes son quienes buscan incorporarse al mercado laboral por primera vez y no tienen experiencia de empleo previa. Esta distinción permite diferenciar entre jóvenes que enfrentan la dificultad del primer empleo y jóvenes que, habiendo trabajado anteriormente, se encuentran en una situación de búsqueda de reincorporación (Instituto Nacional de Estadística, 2026b).

### **2.1.6. Desocupación, subocupación y su medición**

La tasa de desocupación es el indicador principal para medir la proporción de la Población Económicamente Activa que no tiene empleo y que se encuentra buscando activamente una ocupación. Se calcula como el cociente entre la población desocupada y la Población Económicamente Activa, expresado en porcentaje. Este indicador permite monitorear la evolución del mercado laboral y comparar la situación de diferentes grupos de población (Organización Internacional del Trabajo, s. f.-b).

Para el cuarto trimestre de 2025, la tasa de desocupación urbana en Bolivia fue de 2,3%, mientras que para el grupo de jóvenes de 16 a 28 años alcanzó el 3,7%. Esta diferencia de 1,4 puntos porcentuales indica que, aun cuando el mercado laboral boliviano presenta una tasa agregada relativamente baja, la población joven enfrenta mayores dificultades de inserción que el conjunto de la población activa (Instituto Nacional de Estadística, 2026a).

Además de la desocupación abierta, existe la subocupación, que se refiere a la situación de personas que trabajan menos horas de las que desean y están disponibles para trabajar más, o que realizan actividades que no aprovechan plenamente sus competencias. La subocupación juvenil se situó en 8,7% para el cuarto trimestre de 2025, lo que indica que la situación laboral de los jóvenes no se limita únicamente a la presencia o ausencia de un empleo, sino que incluye también condiciones de empleo inadecuadas (Instituto Nacional de Estadística, 2026a).

Es importante precisar que la desocupación y la informalidad son conceptos distintos que no deben confundirse. Una persona informal tiene empleo, pero ese empleo presenta determinadas condiciones de informalidad, como la ausencia de protección social o de contrato escrito. Una persona desocupada, en cambio, no tiene empleo y se encuentra buscándolo activamente. La informalidad puede mencionarse como contexto del mercado laboral boliviano, pero no constituye la variable central del presente análisis, que se enfoca específicamente en la condición de desocupación dentro de la PEA.

### **2.1.7. Transición de la escuela al trabajo**

La transición entre la educación y el trabajo es un concepto especialmente útil para comprender la situación laboral de los jóvenes. La Comisión Económica para América Latina y el Caribe y la Organización Internacional del Trabajo han estudiado esta transición como un proceso que puede tomar trayectorias diferentes y que no se explica únicamente por una característica individual. Los jóvenes tienden a ser más afectados por cambios adversos en el mercado laboral y enfrentan problemas estructurales para incorporarse al empleo y al trabajo decente (Comisión Económica para América Latina y el Caribe & Organización Internacional del Trabajo, 2017).

El marco de estadísticas del mercado laboral juvenil de la OIT, conocido como YouthSTATS, amplía el análisis más allá de la simple presencia o ausencia de empleo. Dentro de este enfoque se distinguen tres categorías de transición: personas que ya realizaron la transición al mercado laboral, personas que se encuentran en proceso de transición y personas cuya transición todavía no ha comenzado. Esta clasificación permite reconocer que estudiar, buscar trabajo y tener empleos temporales pueden formar parte de trayectorias distintas, y que la situación de un joven no puede reducirse a una única etiqueta (Organización Internacional del Trabajo, s. f.-b).

Esta perspectiva respalda el uso de variables como la asistencia educativa, la edad, la búsqueda del primer empleo y la experiencia previa en el análisis de la desocupación juvenil. También ayuda a interpretar la diferencia entre un joven aspirante, que busca incorporarse por primera vez al mercado laboral, y un joven cesante, que ya tuvo una ocupación y se encuentra en búsqueda de una nueva. Ambas personas se encuentran desocupadas, pero sus trayectorias laborales y las barreras que enfrentan son distintas.

### **2.1.8. Segmentación del mercado laboral**

La perspectiva de segmentación del mercado laboral plantea que este no funciona necesariamente como un espacio único con reglas iguales para todas las personas. La OIT define la segmentación como la división del mercado en submercados diferenciados por características y reglas de funcionamiento, que pueden relacionarse con instituciones, tipos de contrato, formalidad o características de los trabajadores (Organización Internacional del Trabajo, s. f.-a).

Aplicada al presente proyecto, esta perspectiva permite considerar que las oportunidades de inserción laboral pueden variar entre grupos de edad, niveles educativos y territorios, y que una diferencia observada en la tasa de desocupación no siempre puede atribuirse únicamente a una característica individual como el nivel de educación. De esta manera, el análisis combina elementos del perfil de la persona con el contexto en el que participa en el mercado laboral, evitando interpretaciones simplistas que reduzcan la desocupación a una sola causa.

### **2.1.9. Factores asociados a la desocupación juvenil: dimensiones de análisis**

A partir de las perspectivas teóricas revisadas, los factores que se examinarán en el proyecto se organizan en cuatro dimensiones principales, cada una de las cuales agrupa un conjunto de variables disponibles en la Encuesta Continua de Empleo. La primera dimensión es sociodemográfica e incluye la edad, los grupos etarios y el sexo. La segunda es educativa e incorpora el nivel de instrucción, los años de estudio y la asistencia o matriculación educativa. La tercera es territorial y considera las diferencias geográficas que puedan analizarse con suficiente información muestral. La cuarta corresponde a la trayectoria laboral e incluye la experiencia previa, la búsqueda de empleo y la condición de aspirante o cesante.

**TABLA N. 4: Dimensiones y variables de análisis**

| Dimensión | Variables previstas | Sentido analítico |
| :---- | :---- | :---- |
| **Sociodemográfica** | Edad, grupos etarios (16-17, 18-20, 21-24, 25-28), sexo | Comparar diferencias internas de la población joven y detectar brechas por sexo. |
| **Educativa** | Nivel educativo, años de estudio, matriculación/asistencia | Observar la relación entre formación y condición de desocupación. |
| **Territorial** | Departamento o agrupaciones territoriales disponibles | Identificar diferencias espaciales cuando la muestra lo permita. |
| **Trayectoria laboral** | Experiencia previa, aspirante/cesante, tiempo y mecanismo de búsqueda | Distinguir etapas y antecedentes de incorporación al mercado laboral. |
| **Resultado** | Condición de desocupación dentro de la PEA | Variable central para tasas, comparaciones y asociaciones. |

**FUENTE:** Elaboración propia con base en la ECE y la revisión conceptual.

### **2.1.10. Microdatos, encuestas por muestreo y factores de expansión**

Los microdatos son registros individuales que contienen la información recopilada para cada persona, hogar o unidad de observación en una encuesta o censo. A diferencia de los datos agregados, que presentan resultados ya resumidos en tablas o indicadores, los microdatos permiten al investigador realizar sus propios cálculos, aplicar filtros específicos, crear nuevas variables y examinar relaciones que no están disponibles en las publicaciones oficiales. En el contexto de las encuestas de hogares y empleo, cada registro de microdatos corresponde a una persona y contiene sus características sociodemográficas, educativas y laborales (Instituto Nacional de Estadística, 2026b).

La Encuesta Continua de Empleo es una encuesta muestral, lo que significa que no recopila información de toda la población, sino de una muestra representativa seleccionada mediante un diseño estadístico riguroso. La base de datos del cuarto trimestre de 2025 contiene 52.650 registros y 121 variables, e incluye información sobre características sociodemográficas y educativas, condición de actividad, ocupación, búsqueda de empleo, trayectoria laboral, variables derivadas y factores de expansión (Instituto Nacional de Estadística, 2026b).

Los factores de expansión, también denominados ponderadores, son valores numéricos que indican cuántas personas de la población total representa cada registro de la muestra. Su uso es indispensable para producir estimaciones poblacionales representativas a partir de los microdatos de una encuesta muestral. Sin la aplicación de estos factores, los resultados reflejarían únicamente las características de la muestra y no podrían generalizarse a la población total. El INE identifica los factores de expansión como indispensables para cálculos que incorporan el diseño muestral de la encuesta (Instituto Nacional de Estadística, 2026b).

En el presente trabajo, las tasas de desocupación, las distribuciones por edad, sexo, educación y territorio, y todas las estimaciones poblacionales se calcularán utilizando el factor de expansión correspondiente de la ECE. Además, se revisará el número de observaciones de cada subgrupo antes de presentar desagregaciones detalladas. Cuando una categoría tenga pocos casos muestrales, se evitarán interpretaciones contundentes o se considerará una agrupación que preserve la utilidad del resultado sin comprometer su precisión.

### **2.1.11. Metodología CRISP-DM como ruta de trabajo**

CRISP-DM, por sus siglas en inglés Cross-Industry Standard Process for Data Mining, es una metodología que organiza los proyectos de análisis de datos en seis fases iterativas. Fue desarrollada como un estándar interindustrial que puede adaptarse a diferentes contextos y tipos de problemas. IBM señala que el proceso es flexible y puede ajustarse a proyectos en los que el objetivo principal sea la exploración y visualización de datos, sin que sea necesario recorrer todas las fases con la misma profundidad (IBM, s. f.).

Las seis fases de CRISP-DM son: comprensión del negocio, comprensión de los datos, preparación de los datos, modelado, evaluación y despliegue. En el presente trabajo, estas fases se adaptan de la siguiente manera. La fase de comprensión del negocio se traduce en la definición del alcance, la población, la pregunta de investigación, los objetivos y los indicadores requeridos. La fase de comprensión de los datos abarca la revisión de los diccionarios de variables, la calidad de la información, la cobertura, las categorías y los factores de expansión. La fase de preparación incluye el filtrado por edad, área urbana y PEA, la limpieza, la recodificación, la integración de fuentes y la creación de segmentos. La fase de modelado se orienta al análisis estadístico, la construcción de indicadores y la evaluación de asociaciones, dado que el proyecto no incluye modelos predictivos. La fase de evaluación comprende las comprobaciones de consistencia, el contraste con cifras oficiales y la revisión de resultados poco estables. Y la fase de despliegue se traduce en la construcción del tablero interactivo en Power BI, la interpretación de los hallazgos y la formulación de recomendaciones.

### **2.1.12. Python y Pandas como herramientas de análisis**

Python es un lenguaje de programación de propósito general que se ha consolidado como el estándar de facto en el ámbito de la Ciencia de Datos y el análisis de información. Su sintaxis clara y legible, su amplia comunidad de desarrolladores y la disponibilidad de bibliotecas especializadas para cada etapa del análisis lo convierten en una herramienta adecuada para proyectos que requieren manipulación de datos, cálculo estadístico y generación de visualizaciones (McKinney, 2022).

Para el procesamiento de datos tabulares, Python cuenta con la biblioteca Pandas, que proporciona dos estructuras fundamentales: la Serie, que representa una columna de datos con un índice, y el DataFrame, que representa una tabla completa con filas indexadas y columnas con nombre. Cada columna de un DataFrame puede ser de un tipo distinto, lo que permite trabajar simultáneamente con variables numéricas, categóricas y de texto. Pandas está construido sobre la biblioteca NumPy, lo que le hereda la capacidad de realizar operaciones vectorizadas de alto rendimiento sobre grandes volúmenes de datos (McKinney, 2022).

Las operaciones que se realizarán con Python y Pandas en el presente trabajo incluyen la lectura de la base de datos de la ECE, la inspección inicial de la estructura y los tipos de datos, la aplicación de filtros para seleccionar la población de interés, la recodificación de variables categóricas, la creación de grupos etarios, la aplicación de los factores de expansión, el cálculo de tasas y distribuciones ponderadas, la construcción de tablas de contingencia, la aplicación de pruebas de asociación y la generación de gráficos exploratorios para verificar los hallazgos antes de su comunicación en Power BI.

### **2.1.13. Business Intelligence y visualización de datos**

Business Intelligence, o Inteligencia de Negocios, comprende un conjunto de procesos, metodologías y herramientas orientadas a transformar datos en información útil y conocimiento estratégico, con el fin de apoyar la toma de decisiones. El proceso de Business Intelligence incluye la comprensión del problema, la preparación de los datos, el análisis exploratorio, el análisis descriptivo, la visualización y la comunicación de resultados.

La visualización de datos constituye la etapa de comunicación del análisis. Su función no es reemplazar el trabajo estadístico realizado previamente, sino presentar los hallazgos de forma ordenada, clara e interactiva para que una persona usuaria pueda comprender rápidamente dónde se concentran las principales diferencias y consultar el detalle de cada segmento. Un buen diseño de visualización se basa en principios como la simplicidad, la claridad, la consistencia, la accesibilidad, la interactividad, el rendimiento y la adaptabilidad.

En el presente trabajo, la visualización se realizará mediante un tablero interactivo construido en Power BI. El tablero no reemplazará el análisis estadístico desarrollado en Python; su función será presentar de forma ordenada los hallazgos ya revisados y validados. La estructura visual podrá avanzar desde un panorama general de la desocupación juvenil hacia comparaciones por edad, sexo, educación, territorio y trayectoria laboral. Este recorrido facilitará que una persona usuaria identifique rápidamente dónde se concentran las principales diferencias y consulte el detalle de cada segmento.

### **2.1.14. Power BI: arquitectura, componentes y aplicación**

Power BI es una plataforma de inteligencia de negocios desarrollada por Microsoft que permite conectar, transformar, modelar y visualizar datos de diversas fuentes para generar reportes y tableros interactivos. Su arquitectura se compone de varios elementos que trabajan de forma integrada para cubrir todo el ciclo del análisis, desde la ingesta de datos hasta la publicación y distribución de los resultados (Microsoft, 2026).

Power BI Desktop es la aplicación de escritorio donde se realiza el desarrollo principal. Permite conectarse a más de cien orígenes de datos diferentes, transformar y limpiar la información mediante Power Query, construir el modelo de datos con relaciones entre tablas, crear medidas y cálculos mediante el lenguaje DAX (Data Analysis Expressions) y diseñar los reportes visuales. Power BI Service es la plataforma en la nube que permite publicar los tableros, compartirlos con otros usuarios, programar actualizaciones automáticas y gestionar permisos de acceso. Power BI Mobile ofrece aplicaciones para dispositivos móviles que permiten consultar los indicadores clave desde cualquier lugar (Microsoft, 2026).

Power Query es el motor de extracción, transformación y carga de Power BI. Permite conectar fuentes de datos, aplicar transformaciones como filtrado, recodificación, cambio de tipos, manejo de valores nulos y creación de columnas condicionales, y cargar el resultado al modelo de datos. Las transformaciones se realizan de forma visual, aunque también pueden editarse directamente en el lenguaje M, que es el lenguaje funcional que impulsa el motor de Power Query. Una vez diseñada y validada la consulta, la actualización de los datos puede ejecutarse con un solo clic o de forma programada (Microsoft, 2026).

DAX (Data Analysis Expressions) es el lenguaje de fórmulas de Power BI, equivalente a las fórmulas de Excel pero diseñado para trabajar con modelos de datos relacionales. Permite crear medidas calculadas como tasas, promedios ponderados, acumulados y comparaciones entre periodos. En el presente trabajo, DAX se utilizará para calcular las tasas de desocupación ponderadas por factor de expansión, las proporciones por grupo etario y las comparaciones entre ocupados y desocupado.

### **2.1.15. Modelo conceptual del trabajo**

El modelo conceptual del proyecto resume la relación que se analizará entre las cuatro dimensiones de factores seleccionadas y la condición de desocupación juvenil. La Figura N. 3 presenta este modelo, donde cada dimensión aporta un conjunto de variables que se examinan en relación con la variable resultado, que es la condición de desocupación dentro de la Población Económicamente Activa.

**FIGURA N. 3: Modelo conceptual del análisis de factores asociados a la desocupación juvenil**

*FUENTE: Elaboración propia.*

### **2.1.16. Validez, limitaciones y alcance del análisis**

El presente trabajo se basa en datos provenientes de una encuesta observacional transversal, lo que implica determinadas limitaciones que deben señalarse explícitamente. En primer lugar, el análisis permite identificar asociaciones, diferencias y patrones entre las variables, pero no permite establecer relaciones causales. Una asociación entre nivel educativo y desocupación no implica que la falta de educación cause la desocupación, sino que ambas variables aparecen relacionadas en los datos del periodo analizado.

En segundo lugar, el análisis se realiza sobre un corte temporal específico, correspondiente al cuarto trimestre de 2025\. Los resultados describen la situación de ese periodo y no pueden extrapolarse automáticamente a otros momentos del año o a años posteriores, aunque las series agregadas de otros trimestres se utilizarán para contextualizar la evolución reciente.

En tercer lugar, las desagregaciones territoriales y por subgrupos específicos estarán limitadas por el tamaño de la muestra. Cuando el número de observaciones en una categoría sea insuficiente para producir estimaciones confiables, se evitarán interpretaciones contundentes y se considerará la agrupación de categorías como alternativa.

Estas limitaciones no restan valor al análisis, sino que lo enmarcan correctamente. El objetivo del trabajo no es demostrar causalidad ni producir predicciones, sino generar un diagnóstico basado en evidencia que permita comprender mejor las características de la desocupación juvenil en Bolivia y orientar la formulación de acciones dirigidas a este grupo de población.

## **2.2. MARCO CONTEXTUAL**

### **2.2.1. Contexto normativo de la juventud en Bolivia**

El trabajo se desarrolla dentro de un marco legal que define a la juventud y reconoce derechos específicos de inserción laboral.

La Constitución Política del Estado Plurinacional de Bolivia, promulgada en 2009, establece en su Artículo 46 que toda persona tiene derecho al trabajo digno, con seguridad industrial, higiene y salud ocupacional, sin discriminación y con remuneración justa. El Artículo 48 dispone que las disposiciones sociales y laborales son de cumplimiento obligatorio y que el Estado protegerá la estabilidad laboral. En el caso de las personas jóvenes, estos principios constitucionales constituyen la base sobre la cual se desarrollan las normas específicas de protección e inserción (Constitución Política del Estado Plurinacional de Bolivia, 2009).

La Ley N.º 342 de la Juventud, promulgada el 5 de febrero de 2013, define como jóvenes a las personas comprendidas entre los 16 y 28 años de edad. Entre sus disposiciones, reconoce el derecho al trabajo digno, la estabilidad laboral, el reconocimiento de pasantías y prácticas profesionales como experiencia laboral, y la generación de condiciones para la inserción y el primer empleo en instituciones públicas y privadas (Estado Plurinacional de Bolivia, 2013).

El tramo de 16 y 17 años cuenta, además, con protección específica. La Ley N.º 548, Código Niña, Niño y Adolescente, y su modificación mediante la Ley N.º 1139 de 2018, establecen garantías particulares para el trabajo adolescente, incluyendo restricciones de jornada, prohibición de actividades peligrosas y la obligación de compatibilizar el trabajo con la educación (Estado Plurinacional de Bolivia, 2018).

La Ley General del Trabajo, vigente desde 1939 con múltiples actualizaciones, regula las relaciones laborales en Bolivia y establece disposiciones sobre jornada, salario, contratos y protección del trabajador. Aunque no fue concebida originalmente con un enfoque juvenil específico, sus normas se aplican a toda persona que ingresa al mercado laboral, incluidas las personas jóvenes que se incorporan por primera vez (Estado Plurinacional de Bolivia, 1939).

Este conjunto normativo justifica que el rango de 16 a 28 años sea utilizado como delimitación etaria del proyecto, y que el tramo de 16 y 17 años sea observado como un grupo propio dentro de las comparaciones, sin asumir que su edad determine por sí sola la condición de desocupación.

### **2.2.2. Contexto socioeconómico y demográfico de Bolivia**

Bolivia es un país con una estructura demográfica predominantemente joven. Según los resultados del Censo de Población y Vivienda 2024, la población total del país supera los 12 millones de habitantes, con una proporción significativa de personas en edad de trabajar. La población joven, definida entre los 16 y 28 años según la legislación nacional, representa un segmento amplio y diverso que se encuentra en distintas etapas de su trayectoria educativa y laboral (Instituto Nacional de Estadística, 2024).

La urbanización es un rasgo determinante del contexto boliviano. La mayor parte de la población se concentra en áreas urbanas, donde se localizan las principales actividades económicas, los servicios educativos y las oportunidades de empleo. Esta concentración explica que el mercado laboral urbano sea el espacio principal de inserción para la población joven y que las estadísticas de empleo se monitoreen prioritariamente en este ámbito.

La estructura económica del país combina sectores tradicionales como la minería, los hidrocarburos y la agricultura con un sector de servicios y comercio en crecimiento. El comercio, los servicios y la construcción figuran entre las principales fuentes de generación de empleo urbano, mientras que la industria manufacturera tiene una participación más limitada. Esta estructura influye directamente en el tipo de ocupaciones disponibles para las personas jóvenes y en las condiciones de acceso al trabajo.

La informalidad constituye una característica estructural del mercado laboral boliviano. Una proporción elevada de los trabajadores urbanos se desempeña en ocupaciones informales, sin protección social completa ni estabilidad contractual. Aunque la informalidad no es sinónimo de desocupación, sí configura un contexto en el que la calidad del empleo y las condiciones de inserción adquieren relevancia para comprender la situación laboral de la juventud.

### **2.2.3. Mercado laboral urbano boliviano**

La Encuesta Continua de Empleo constituye la principal herramienta para monitorear la evolución del mercado laboral urbano de Bolivia. Los boletines del Instituto Nacional de Estadística presentan indicadores de participación, ocupación, desocupación y subutilización de la mano de obra, con periodicidad trimestral.

Para el cuarto trimestre de 2025, la tasa de desocupación urbana fue de 2,3%, una cifra inferior a la observada durante los años posteriores a 2020, cuando la pandemia afectó significativamente la actividad económica (Instituto Nacional de Estadística, 2026a). Esta reducción indica una recuperación del mercado laboral en términos agregados.

Sin embargo, la reducción de la tasa general no elimina la existencia de diferencias entre grupos. En el mismo periodo, la tasa de desocupación para las personas de 16 a 28 años fue de 3,7%, superando en 1,4 puntos porcentuales a la tasa general. La subocupación juvenil alcanzó el 8,7%, lo que señala que la situación laboral de los jóvenes no se limita a la presencia o ausencia de un empleo, sino que incluye también condiciones de empleo inadecuadas (Instituto Nacional de Estadística, 2026a).

La población joven conformó aproximadamente el 29,0% de la población ocupada urbana en el periodo analizado, lo que refleja la importancia de este grupo dentro de la estructura laboral del país y la necesidad de observar sus condiciones de inserción con datos desagregados.

### **2.2.4. Situación de la juventud en el contexto regional**

El contexto boliviano forma parte de una realidad regional en la que la inserción laboral juvenil continúa presentando desafíos. La Organización Internacional del Trabajo informó en 2025 que los jóvenes de América Latina y el Caribe mantienen mayores dificultades para acceder a empleos formales y que persisten brechas asociadas con la informalidad, el género y las condiciones de vulnerabilidad (Organización Internacional del Trabajo, 2025a; Organización Internacional del Trabajo, 2025b).

La Comisión Económica para América Latina y el Caribe, en su estudio sobre juventudes en transición, destaca que el paso de la escuela al trabajo influye en las trayectorias laborales posteriores y que existen diferencias importantes entre quienes estudian, trabajan, combinan ambas actividades o se encuentran fuera de ellas (Comisión Económica para América Latina y el Caribe, 2025).

Estos antecedentes regionales se utilizarán como apoyo interpretativo, sin trasladar directamente sus cifras al contexto boliviano. Su función es proporcionar un marco comparativo que permita ubicar los hallazgos del proyecto dentro de una dinámica más amplia. 

### **2.2.5. Contexto educativo de la población joven**

La educación constituye uno de los factores más relevantes en la inserción laboral de las personas jóvenes. En Bolivia, el sistema educativo comprende los niveles inicial, primario, secundario y superior, siendo la educación obligatoria hasta el nivel secundario.

Una parte significativa de la población joven entre 16 y 28 años se encuentra todavía cursando estudios secundarios, técnicos o universitarios. Esta situación genera una combinación particular entre formación educativa y participación laboral que no se observa en otros grupos de edad. Los jóvenes que estudian y simultáneamente buscan trabajo o trabajan enfrentan condiciones distintas a quienes ya concluyeron su formación.

El nivel educativo alcanzado influye en el tipo de ocupaciones a las que una persona puede aspirar y en las condiciones de acceso al empleo. No obstante, como se señala en los antecedentes del marco teórico, el nivel educativo por sí solo no garantiza una incorporación inmediata al mercado de trabajo. La Encuesta de Hogares 2025 incluye información sobre años de estudio, asistencia educativa y nivel de instrucción alcanzado, variables que serán utilizadas en el análisis para observar la relación entre formación y condición de desocupación (Instituto Nacional de Estadística, 2026c).

La siguiente tabla resume las variables educativas disponibles en las fuentes de datos del proyecto.

**TABLA N. 5: Variables educativas disponibles en las fuentes de datos**

| Fuente | Variable | Descripción |
| :---- | :---- | :---- |
| **ECE 4T-2025** | Nivel educativo | Nivel de instrucción alcanzado por la persona |
| **ECE 4T-2025** | Asistencia educativa | Si la persona asiste actualmente a un establecimiento educativo |
| **Encuesta de Hogares 2025** | Años de estudio | Cantidad de años de escolaridad completados |
| **Encuesta de Hogares 2025** | Nivel de instrucción | Detalle del nivel educativo alcanzado |

**FUENTE:** Elaboración propia con base en Instituto Nacional de Estadística (2026b; 2026c).

### **2.2.6. Entorno estadístico y fuentes de datos**

El entorno estadístico del proyecto está compuesto por fuentes nacionales y regionales que proporcionan información sobre el mercado laboral, la educación y las condiciones socioeconómicas de la población.

El Instituto Nacional de Estadística es la entidad responsable de la producción de estadísticas oficiales en Bolivia. Entre sus operaciones estadísticas relevantes para este trabajo se encuentran la Encuesta Continua de Empleo, la Encuesta de Hogares, el Censo de Población y Vivienda y la Encuesta de Niñas, Niños y Adolescentes que Realizan Actividad Laboral o Trabajan. Los microdatos de estas operaciones se encuentran disponibles en el Archivo Nacional de Datos del INE, junto con sus respectivos diccionarios de variables y metadatos.

La Encuesta Continua de Empleo del cuarto trimestre de 2025 será la fuente principal del análisis. Esta base contiene 52.650 registros y 121 variables, e incluye información sociodemográfica, educativa, condición de actividad, ocupación, búsqueda de empleo, trayectoria laboral, variables derivadas y factores de expansión para estimaciones poblacionales (Instituto Nacional de Estadística, 2026b).

La Encuesta de Hogares 2025 aportará información complementaria sobre características socioeconómicas y educativas que permiten contrastar determinados hallazgos del análisis principal. La Encuesta de Niñas, Niños y Adolescentes que Realizan Actividad Laboral o Trabajan 2019 podrá aportar contexto específico para el tramo de 16 y 17 años (Instituto Nacional de Estadística, 2019).

### **2.2.7. Delimitación geográfica y temporal**

El espacio principal del trabajo será el área urbana de Bolivia. La selección responde a la disponibilidad y continuidad de los indicadores de la ECE para este ámbito, y a que la mayor parte de la población joven que participa en el mercado laboral se concentra en zonas urbanas.

Las comparaciones territoriales se realizarán hasta el nivel que permita la muestra, evitando presentar diferencias departamentales cuando el número de observaciones resulte insuficiente para producir estimaciones confiables. Los boletines oficiales de la ECE presentan buena parte de sus indicadores para Bolivia urbana y, cuando realizan desagregaciones, muestran individualmente algunos departamentos mientras agrupan otros, lo que constituye una señal de las limitaciones muestrales existentes.

El periodo principal de microdatos será el cuarto trimestre de 2025, que ofrece una base completa y reciente para desarrollar el análisis. Las series de otros periodos se utilizarán para mostrar tendencias generales, pero no se mezclarán registros de diferentes trimestres para el análisis individual sin considerar previamente las características del diseño de la encuesta.

### **2.2.8. Síntesis del marco contextual**

El contexto del trabajo combina varios elementos que se articulan entre sí:

* Un marco normativo que define a la juventud entre 16 y 28 años y reconoce derechos de inserción laboral, con protección específica para el tramo adolescente.  
* Una estructura socioeconómica caracterizada por la urbanización, la informalidad y una composición sectorial que condiciona las oportunidades de empleo.  
* Un mercado laboral urbano que presenta una tasa juvenil de desocupación superior a la tasa general, junto con niveles significativos de subocupación juvenil.  
* Un contexto regional en el que la inserción laboral juvenil enfrenta desafíos persistentes, según los informes de la OIT y la CEPAL.  
* Un sistema educativo que mantiene a una parte importante de la población joven en proceso de formación, generando combinaciones específicas entre estudio y trabajo.  
* Un sistema estadístico que dispone de microdatos suficientes para examinar diferencias internas dentro de la población joven.  
* Un contexto institucional en el que existen acciones orientadas a la inserción laboral juvenil, aunque con resultados todavía limitados.

# **REFERENCIAS BIBLIOGRÁFICAS**

Agresti, A. (2007). An Introduction to Categorical Data Analysis (2ª ed.). John Wiley & Sons.

Comisión Económica para América Latina y el Caribe. (2025). Entre la escuela y el trabajo: juventudes en transición en América Latina. CEPAL.

Comisión Económica para América Latina y el Caribe & Organización Internacional del Trabajo. (2017). Coyuntura Laboral en América Latina y el Caribe: La transición de los jóvenes de la escuela al mercado laboral. CEPAL/OIT.

Estado Plurinacional de Bolivia. (2013). Ley N.º 342 de la Juventud. Asamblea Legislativa Plurinacional.

Estado Plurinacional de Bolivia. (2018). Ley N.º 1139 de modificación a la Ley N.º 548, Código Niña, Niño y Adolescente. Asamblea Legislativa Plurinacional.

IBM. (s. f.). Conceptos básicos de ayuda de CRISP-DM. IBM Documentation. [https\://www\.ibm.com/docs/es/spss-modeler/saas?topic=dm-crisp-help-overview](https://www.ibm.com/docs/es/spss-modeler/saas?topic=dm-crisp-help-overview)

Instituto Nacional de Estadística. (2019). Encuesta de Niñas, Niños y Adolescentes que Realizan Actividad Laboral o Trabajan 2019 (ENNA 2019): base de datos y metadatos. Archivo Nacional de Datos.

Instituto Nacional de Estadística. (2026a). Boletín Estadístico Encuesta Continua de Empleo, cuarto trimestre de 2025\. INE Bolivia.

Instituto Nacional de Estadística. (2026b). Encuesta Continua de Empleo, cuarto trimestre de 2025: base de datos y metadatos. Archivo Nacional de Datos.

Instituto Nacional de Estadística. (2026c). Encuesta de Hogares 2025: base de datos y metadatos. Archivo Nacional de Datos.

Ministerio de Trabajo, Empleo y Previsión Social. (2026). Trabajo proyecta acciones para la inserción laboral de jóvenes profesionales. [https\://mintrabajo.gob.bo/index.php/nota\_prensa/la-paz-44/](https://mintrabajo.gob.bo/index.php/nota_prensa/la-paz-44/)

Organización Internacional del Trabajo. (2019). Entre el bono demográfico y los ninis: Empleo juvenil en Bolivia. Oficina Regional para América Latina y el Caribe.

Organización Internacional del Trabajo. (2025a). Panorama Laboral 2024 de América Latina y el Caribe. Oficina Regional para América Latina y el Caribe.

Organización Internacional del Trabajo. (2025b). Juventud en cambio: Desafíos y oportunidades en el mercado laboral de América Latina y el Caribe. Oficina Regional para América Latina y el Caribe.

Organización Internacional del Trabajo. (s. f.-b). Estadísticas del mercado laboral juvenil (YouthSTATS). ILOSTAT. [https\://ilostat.ilo.org/es/methods/concepts-and-definitions/description-youth-labour-market-statistics/](https://ilostat.ilo.org/es/methods/concepts-and-definitions/description-youth-labour-market-statistics/)

McKinney, W. (2022). Python for Data Analysis: Data Wrangling with Pandas, NumPy, and Jupyter (3ª ed.). O'Reilly Media.

Microsoft. (2026). ¿Qué es Power BI? Documentación de Power BI. [https\://learn.microsoft.com/es-es/power-bi/fundamentals/power-bi-overview](https://learn.microsoft.com/es-es/power-bi/fundamentals/power-bi-overview)

Organización Internacional del Trabajo. (s. f.-a). Labour market segmentation. [https\://www\.ilo.org/topics/employment-security/labour-market-segmentation](https://www.ilo.org/topics/employment-security/labour-market-segmentation)

Tukey, J. W. (1977). Exploratory Data Analysis. Addison-Wesley.

Walpole, R. E., Myers, R. H., Myers, S. L. & Ye, K. (2012). Probabilidad y estadística para ingeniería y ciencias (8ª ed.). Pearson Educación.

Wickham, H. & Grolemund, G. (2017). R for Data Science: Import, Tidy, Transform, Visualize, and Model Data. O'Reilly Media.

Constitución Política del Estado Plurinacional de Bolivia. (2009). Constitución Política del Estado Plurinacional de Bolivia. Gaceta Oficial de Bolivia.

Instituto Nacional de Estadística. (2024). Censo de Población y Vivienda 2024: resultados y datos demográficos. INE Bolivia.

Instituto Nacional de Estadística. (2024). Censo de Población y Vivienda 2024\.

Provost, F. & Fawcett, T. (2013). Data Science for Business. O'Reilly Media.

