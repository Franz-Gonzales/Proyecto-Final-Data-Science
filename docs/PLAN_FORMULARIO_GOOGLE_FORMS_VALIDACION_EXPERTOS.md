# PLAN DE DISEÑO E IMPLEMENTACIÓN DEL FORMULARIO DE VALIDACIÓN POR EXPERTOS (GOOGLE FORMS)

**PROGRAMA ACADÉMICO:** Diplomado en Data Science - Versión I  
**INSTITUCIÓN:** Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX)  
**UNIDAD DE POSGRADO:** Centro de Estudios de Posgrado e Investigación (CEPI) - Vicerrectorado  
**TÍTULO DEL PROYECTO:** *Análisis de los factores asociados a la desocupación en jóvenes de 16 a 28 años en Bolivia*  
**AUTOR:** Gonzales Suyo Franz Reinaldo  
**COORDINADOR / DOCENTE:** Ing. Marcelo Arancibia  
**FECHA:** Sucre - Bolivia, 2026  

---

## 1. INTRODUCCIÓN Y OBJETIVO

En el marco del **Objetivo Específico 4** del proyecto, se establece el proceso de **validación de resultados mediante Juicio de Expertos**. 

El propósito de este formulario en Google Forms es compartir con profesionales externos dedicados al área de Ciencia de Datos, Estadística y Economía Laboral el trabajo realizado en el proyecto, permitiéndoles revisar los resultados obtenidos (figuras, tablas en CSV, cuadernillo Jupyter, capturas del reporte interactivo en Power BI y resumen metodológico) para que califiquen de manera objetiva la consistencia y calidad técnica del estudio.

---

## 2. ARQUITECTURA DE LA CARPETA EN GOOGLE DRIVE (EVIDENCIAS COMPARTIDAS)

Para que los evaluadores puedan revisar cómodamente todo el contenido del proyecto antes de contestar el formulario, se colocará en el encabezado del Google Form un enlace público de Google Drive con la siguiente estructura organizada en cinco carpetas:

```text
Carpeta_Resultados_Proyecto/
├── 01_Documentacion/
│   ├── Resumen_Ejecutivo_Metodologico.pdf         # Ficha ejecutiva de 2 páginas con los resultados clave
│   └── GonzalesSuyo_Franz_Monografia_Cap3.pdf     # Documento completo del trabajo y anexos
├── 02_Codigo_y_Cuadernillo/
│   ├── Proyecto-Final.ipynb                       # Cuadernillo Jupyter con el flujo completo ejecutado
│   ├── data_processing.py                         # Código en Python de filtrado y preparación de datos
│   ├── statistical_analysis.py                    # Código en Python de cálculos y contrastes estadísticos
│   └── visualization.py                           # Código en Python para generación de gráficos
├── 03_Tablas_de_Resultados/
│   ├── ECE_4T2025_Jovenes_PEA.csv                 # Dataset final procesado (6.649 registros)
│   ├── tabla_desocupacion_macro.csv               # Totales y tasas de la PEA, ocupados y desocupados
│   ├── tabla_pruebas_chi2_cramer.csv              # Resultados de pruebas Chi-cuadrado y V de Cramér
│   ├── tabla_comparativa_escolaridad.csv          # Medias de estudio y pruebas t-Welch y Mann-Whitney
│   └── tabla_desocupacion_departamento.csv        # Tasas de desocupación por departamento
├── 04_Figuras/
│   ├── figura_1_desocupacion_general_vs_juvenil.png
│   ├── figura_2_desocupacion_por_tramo_etario.png
│   ├── figura_3_brecha_genero.png
│   ├── figura_4_desocupacion_por_departamento.png
│   ├── figura_5_cesantes_vs_aspirantes.png
│   ├── figura_6_desocupacion_por_nivel_educativo.png
│   ├── figura_7_desocupacion_asiste_estudio.png
│   ├── figura_8_distribucion_anios_estudio.png
│   ├── figura_9_mecanismos_busqueda.png
│   └── figura_10_desocupacion_tipo_hogar.png
└── 05_Capturas_Power_BI/
    ├── pagina_1_panorama_laboral.png              # Página 1: Panorama Laboral Juvenil Urbano
    ├── pagina_2_tramo_etario.png                  # Página 2: Desocupación por Tramo Etario
    ├── pagina_3_educacion.png                     # Página 3: Capital Humano y Escolaridad
    ├── pagina_4_genero_y_departamento.png         # Página 4: Género y Disparidades Departamentales
    ├── pagina_5_perfil_desocupados.png            # Página 5: Perfil del Joven Desocupado
    └── pagina_6_politicas_publicas.png            # Página 6: Conclusiones y Propuestas de Política
```

---

## 3. ESTRUCTURA Y CONTENIDO TEXTUAL DEL FORMULARIO EN GOOGLE FORMS

A continuación se detalla la redacción literal de cada sección, los enlaces y los reactivos simplificados y directos para el formulario:

### [ENCABEZADO DEL FORMULARIO]

**Título:**  
`Validación de Resultados por Expertos: Desocupación Juvenil en Bolivia (ECE 4T-2025)`

**Descripción:**  
> **Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX)**  
> **Centro de Estudios de Posgrado e Investigación (CEPI) - Vicerrectorado**  
> **Programa:** Diplomado en Data Science (Versión I)  
> **Autor / Investigador:** Franz Reinaldo Gonzales Suyo  
> **Docente / Coordinador:** Ing. Marcelo Arancibia  
> **Sede:** Sucre - Bolivia (2026)  
>
> Estimado(a) profesional:  
>
> Le invito a participar en la validación técnica y metodológica del proyecto de ciencia de datos titulado: *"Análisis de los factores asociados a la desocupación en jóvenes de 16 a 28 años en el área urbana de Bolivia (ECE 4T-2025)"*.  
>
> El estudio analiza microdatos oficiales del Instituto Nacional de Estadística (INE) sobre una muestra depurada de **6.649 jóvenes activos**, representativa de **1.380.841 jóvenes** de la PEA urbana, utilizando **Python** para el análisis estadístico y **Power BI** para la visualización interactiva mediante un modelo Star Schema de 6 páginas.
>
> 📁 **ENLACE A LA CARPETA DE EVIDENCIAS Y RESULTADOS (GOOGLE DRIVE):**  
> `[Insertar aquí el enlace público de la carpeta en Google Drive]`  
> *(Encontrará el resumen ejecutivo en PDF, el cuadernillo Jupyter, tablas en formato CSV, figuras analíticas y las capturas del cuadro de mando en Power BI).*  
> 🔒 **Uso de la información:** Fines exclusivamente académicos para la monografía de posgrado. Puede tomarse todo el tiempo necesario para revisar las evidencias y emitir su valoración.  

---

### SECCIÓN 1: DATOS DEL EVALUADOR

*Por favor, complete sus datos básicos:*

1. **Dirección de correo electrónico:**  
   *[Texto de respuesta corta - Obligatorio]*  
   *(Se solicita para el registro de participación del evaluador).*

2. **Nombre y apellidos completos:**  
   *[Texto de respuesta corta - Obligatorio]*  

---

### INSTRUCCIÓN PARA LAS PREGUNTAS DE VALORACIÓN

> **Escala de Valoración:**  
> Valore las siguientes afirmaciones según su criterio profesional marcando una sola opción del 1 al 5:  
> **1 = Totalmente en desacuerdo**  
> **2 = En desacuerdo**  
> **3 = Ni de acuerdo ni en desacuerdo**  
> **4 = De acuerdo**  
> **5 = Totalmente de acuerdo**  

---

### SECCIÓN 2: PREPARACIÓN DE DATOS Y MUESTREO

* **P1.** Los criterios para delimitar la población de estudio (área urbana, edad de 16 a 28 años según la Ley N.º 342 y condición activa en la PEA, totalizando 6.649 registros) son adecuados y claros.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

* **P2.** El uso del factor de ponderación trimestral (`fact_trim_act`) para expandir la muestra a los 1.380.841 jóvenes urbanos es correcto para evitar distorsiones estadísticas.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

---

### SECCIÓN 3: INDICADORES Y RÉPLICA OFICIAL DEL INE

* **P3.** La tasa de desocupación juvenil calculada en el proyecto (3,71%, equivalente a 51.196 jóvenes) coincide con precisión con el reporte oficial publicado por el INE (3,7%).  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

* **P4.** La tasa de subocupación juvenil por tiempo (8,70%, equivalente a 115.736 jóvenes) refleja adecuadamente la subutilización laboral reportada por el INE (8,7%).  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

* **P5.** La comparación que demuestra que la desocupación en jóvenes (3,71%) supera en 1,61 veces a la desocupación general urbana nacional (2,30%) está claramente sustentada.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

---

### SECCIÓN 4: ANÁLISIS ESTADÍSTICO Y PRUEBAS DE ASOCIACIÓN

* **P6.** Las pruebas estadísticas utilizadas (Chi-cuadrado para contrastar independencia y V de Cramér para medir el tamaño de la asociación) son pertinentes para analizar los factores vinculados al desempleo.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

* **P7.** La comparación de años de estudio entre jóvenes ocupados y desocupados mediante pruebas de hipótesis (prueba t y Mann-Whitney) es metodológicamente sólida.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

* **P8.** La interpretación de los resultados es adecuada al explicar asociaciones estadísticas sin afirmar relaciones de causalidad directa.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

---

### SECCIÓN 5: CUADRO DE MANDO EN POWER BI

* **P9.** La estructura del cuadro de mando interactivo en Power BI (organizado en 6 páginas temáticas) permite explorar y comprender con facilidad los indicadores clave.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

* **P10.** Los gráficos y tarjetas de indicadores utilizados facilitan la visualización y análisis de las brechas laborales.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

---

### SECCIÓN 6: INTERPRETACIÓN DE RESULTADOS Y HALLAZGOS

* **P11.** El análisis de las principales brechas laborales (pico de desocupación de 4,65% en jóvenes de 18 a 20 años y mayor tasa en mujeres con 4,69% frente a 2,85% en hombres) es coherente con la realidad económica.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

* **P12.** El hallazgo de que el 89,62% de los jóvenes desocupados son cesantes (con trabajo anterior) y solo el 10,38% son aspirantes (primer empleo) aporta claridad sobre la inestabilidad del empleo juvenil.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

---

### SECCIÓN 7: CONCLUSIONES Y CALIDAD GENERAL

* **P13.** Las conclusiones y recomendaciones del proyecto responden de forma directa y justificada a los problemas identificados en los datos.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

* **P14.** En general, el trabajo de ciencia de datos realizado demuestra rigor técnico, reproducibilidad y utilidad práctica.  
  `[ ] 1   [ ] 2   [ ] 3   [ ] 4   [ ] 5`

---

### SECCIÓN 8: PREGUNTAS ABIERTAS Y DICTAMEN FINAL

*Por favor, comparta sus valoraciones cualitativas sobre el trabajo:*

1. **Principales fortalezas del trabajo:**  
   *[Texto de párrafo largo - Obligatorio]*  
   *(Aspectos más sólidos, rigurosos o destacados del proyecto).*

2. **Principales debilidades o aspectos a mejorar:**  
   *[Texto de párrafo largo - Obligatorio]*  
   *(Limitaciones o sugerencias técnicas para profundizar).*

3. **Sugerencias adicionales:**  
   *[Texto de párrafo largo - Opcional]*  
   *(Recomendaciones complementarias para el autor).*

4. **Dictamen de validación:**  
   *[Selección única - Obligatorio]*  
   - [ ] **Aprobado con Distinción / Sobresaliente** (Cumple estándares excelentes de rigor y calidad técnica).  
   - [ ] **Aprobado Plenamente** (El trabajo es sólido y sus resultados son válidos y consistentes).  
   - [ ] **Aprobado con Observaciones Menores** (Requiere ajustes leves de redacción o formato).  
   - [ ] **Requiere Modificaciones Sustanciales** (Presenta debilidades que deben corregirse).  
   - [ ] **No Aprobado** (Inconsistencia técnica o metodológica severa).  

---

## 4. GUÍA DE CONFIGURACIÓN RÁPIDA EN GOOGLE FORMS

1. **Crear Formulario:** Abrir Google Forms y pegar el título y la descripción con el enlace a Google Drive.
2. **Ajustes en Configuración:**
   - Activar: *Recopilar direcciones de correo electrónico* (para el control de evaluadores).
   - Activar: *Limitar a 1 respuesta* (para evitar respuestas duplicadas).
   - Activar: *Mostrar barra de progreso* en la pestaña de presentación.
3. **Crear Secciones:** Dividir el formulario en las 8 secciones indicadas para que la navegación sea ágil y organizada.
4. **Respuestas:** Vincular el formulario a una hoja de cálculo (Google Sheets) para exportar los resultados en formato CSV/Excel al finalizar la consulta.

---

## 5. PROCESAMIENTO ESTADÍSTICO DE RESULTADOS (SCRIPT EN PYTHON)

Una vez que los evaluadores completen el formulario, se descargará el archivo CSV de respuestas y se procesará mediante el módulo [`src/audit/expert_validation_analysis.py`](file:///c:/Users/franz/workspace/diplomado/Proyecto-Final-Data-Science/src/audit/expert_validation_analysis.py), el cual calcula:

* **Promedio y Desviación Estándar** de cada dimensión.
* **Coeficiente V de Aiken ($V$):** Mide el grado de acuerdo entre evaluadores para cada reactivo (valores $V \ge 0,80$ confirman validez y consenso estadístico).
* **Alfa de Cronbach ($\alpha$):** Evalúa la consistencia interna general de las respuestas.

### Plantilla de la Tabla de Resultados para la Monografía:

| Área Evaluada | N.º Ítems | Promedio Likert (1-5) | V de Aiken ($V$) | Desviación Estándar | Nivel de Validación |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Preparación de Datos y Muestreo** | 2 | *4,80* | *0,95* | *0,40* | Validación Excelente |
| **Indicadores y Réplica INE** | 3 | *4,90* | *0,97* | *0,30* | Validación Máxima |
| **Análisis Estadístico y Pruebas** | 3 | *4,75* | *0,94* | *0,45* | Validación Excelente |
| **Cuadro de Mando en Power BI** | 2 | *4,85* | *0,96* | *0,35* | Validación Excelente |
| **Interpretación y Hallazgos** | 2 | *4,80* | *0,95* | *0,40* | Validación Excelente |
| **Conclusiones y Calidad General** | 2 | *4,70* | *0,92* | *0,48* | Validación Fuerte |
| **PROMEDIO GLOBAL DEL PANEL** | **14** | **4,80 / 5,00** | **0,95** | **0,40** | **APROBADO CON DISTINCIÓN** |

---
*Fin del documento de planificación para Google Forms.*
