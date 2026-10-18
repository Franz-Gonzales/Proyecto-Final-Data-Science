/**
 * ==============================================================================
 * UNIVERSIDAD MAYOR, REAL Y PONTIFICIA DE SAN FRANCISCO XAVIER DE CHUQUISACA
 * CENTRO DE ESTUDIOS DE POSGRADO E INVESTIGACIÓN (CEPI) - VICERRECTORADO
 * PROGRAMA: Diplomado en Data Science - Versión I
 * PROYECTO: Análisis de los Factores Asociados a la Desocupación en Jóvenes de 16 a 28 Años en Bolivia (ECE 4T-2025)
 * AUTOR: Franz Reinaldo Gonzales Suyo
 * DOCENTE: Ing. Marcelo Arancibia
 * ==============================================================================
 * SCRIPT DE GENERACIÓN AUTOMÁTICA DEL FORMULARIO DE VALIDACIÓN POR JUICIO DE EXPERTOS
 * Plataforma: Google Apps Script (FormApp)
 * Entorno: Google Forms (Editor de secuencias de comandos)
 * ==============================================================================
 */

/**
 * CONFIGURACIÓN MAESTRA DEL FORMULARIO
 * Personalice aquí los enlaces y textos generales del proyecto.
 */
var CONFIG = {
  // Reemplace este enlace con el enlace público de su carpeta "Carpeta_Resultados_Proyecto" en Google Drive
  DRIVE_URL: "https://drive.google.com/drive/folders/TU_ID_DE_CARPETA_AQUI?usp=sharing",
  
  TITULO_FORMULARIO: "Validación de Resultados por Expertos: Desocupación Juvenil en Bolivia (ECE 4T-2025)",
  AUTOR: "Franz Reinaldo Gonzales Suyo",
  DOCENTE: "Ing. Marcelo Arancibia",
  INSTITUCION: "Universidad Mayor, Real y Pontificia de San Francisco Xavier de Chuquisaca (USFX)",
  UNIDAD: "Centro de Estudios de Posgrado e Investigación (CEPI) - Vicerrectorado",
  PROGRAMA: "Diplomado en Data Science (Versión I)",
  GESTION: "Sucre - Bolivia (2026)"
};

/**
 * Función principal para generar o actualizar el formulario en Google Forms.
 * Se ejecuta directamente desde el botón "Ejecutar" en el editor de Google Apps Script.
 */
function generarFormularioValidacionExpertos() {
  var form;

  // 1. Detección del formulario: activo (contenedor vinculado) o nuevo formulario
  try {
    form = FormApp.getActiveForm();
  } catch (e) {
    form = null;
  }

  if (!form) {
    form = FormApp.create(CONFIG.TITULO_FORMULARIO);
    Logger.log("[INFO]: Se ha creado un nuevo formulario: " + form.getTitle());
  } else {
    Logger.log("[INFO]: Trabajando sobre el formulario activo: " + form.getTitle());
    // Limpieza de ítems previos para asegurar una generación limpia y sin preguntas duplicadas
    limpiarItemsPrevios(form);
  }

  // 2. Configuración de Metadatos y Ajustes Globales del Formulario
  configurarAjustesGenerales(form);

  // 3. SECCIÓN 1: Identificación y Datos del Evaluador
  construirSeccionDatosEvaluador(form);

  // 4. SECCIÓN 2: Preparación de Datos y Muestreo Ponderado
  construirSeccionMuestreo(form);

  // 5. SECCIÓN 3: Indicadores y Coincidencia con Cifras Oficiales del INE
  construirSeccionIndicadoresINE(form);

  // 6. SECCIÓN 4: Análisis Estadístico y Pruebas de Hipótesis
  construirSeccionAnalisisEstadistico(form);

  // 7. SECCIÓN 5: Cuadro de Mando en Power BI Desktop
  construirSeccionPowerBI(form);

  // 8. SECCIÓN 6: Interpretación de Brechas y Hallazgos
  construirSeccionHallazgos(form);

  // 9. SECCIÓN 7: Conclusiones y Calidad General del Trabajo
  construirSeccionConclusiones(form);

  // 10. SECCIÓN 8: Evaluación Cualitativa y Dictamen Final
  construirSeccionEvaluacionFinal(form);

  // Resumen en la consola de Apps Script
  Logger.log("==============================================================================");
  Logger.log("¡FORMULARIO GENERADO CON ÉXITO!");
  Logger.log("URL de Edición (Admin): " + form.getEditUrl());
  Logger.log("URL de Publicación (para enviar a los expertos): " + form.getPublishedUrl());
  Logger.log("==============================================================================");
}

/**
 * Configura los ajustes de seguridad, presentación y mensajes del formulario.
 */
function configurarAjustesGenerales(form) {
  form.setTitle(CONFIG.TITULO_FORMULARIO);

  var descripcion = 
    CONFIG.INSTITUCION + "\n" +
    CONFIG.UNIDAD + "\n" +
    "Programa: " + CONFIG.PROGRAMA + "\n" +
    "Autor / Investigador: " + CONFIG.AUTOR + "\n" +
    "Docente / Coordinador: " + CONFIG.DOCENTE + "\n" +
    "Sede: " + CONFIG.GESTION + "\n\n" +
    "Estimado(a) profesional especialista:\n\n" +
    "Le invito a participar como Juez Experto en la validación técnica, metodológica y aplicada del proyecto de ciencia de datos: " +
    "\"Análisis de los factores asociados a la desocupación en jóvenes de 16 a 28 años en el área urbana de Bolivia (ECE 4T-2025)\".\n\n" +
    "El estudio procesó microdatos oficiales del Instituto Nacional de Estadística (INE) sobre una muestra depurada de 6.649 jóvenes activos, " +
    "representativa de 1.380.841 jóvenes de la PEA urbana, implementando cálculos en Python y un modelo dimensional interactivo en Power BI Desktop (6 páginas).\n\n" +
    "📁 ENLACE A LA CARPETA DE EVIDENCIAS Y RESULTADOS (GOOGLE DRIVE):\n" +
    CONFIG.DRIVE_URL + "\n" +
    "(Incluye el resumen ejecutivo en PDF, cuadernillo Jupyter, tablas CSV, figuras analíticas y capturas de pantalla de Power BI).\n\n" +
    "🔒 Uso de la información: Fines exclusivamente académicos para la monografía de posgrado. " +
    "Puede tomarse todo el tiempo necesario para revisar los recursos compartidos y registrar su valoración.";

  form.setDescription(descripcion);

  // Ajustes de Google Forms
  form.setCollectEmail(true);                    // Recopila el correo electrónico verificado
  form.setLimitOneResponsePerUser(true);         // Límite a 1 respuesta por cuenta
  form.setProgressBar(true);                     // Barra de progreso visual por secciones
  form.setAllowResponseEdits(false);             // Inmutabilidad de la respuesta tras enviar
  form.setShowLinkToRespondAgain(false);         // No mostrar enlace para otra respuesta
  form.setPublishingSummary(false);              // Resumen privado para el investigador

  // Mensaje final tras completar el formulario
  form.setConfirmationMessage(
    "Muchas gracias por su valiosa participación en el panel de evaluación experta de la Universidad San Francisco Xavier de Chuquisaca (USFX - CEPI).\n\n" +
    "Su dictamen técnico contribuye sustantivamente al rigor científico y a la validación de este proyecto en Ciencia de Datos."
  );
}

/**
 * SECCIÓN 1: Identificación del Experto Evaluador
 */
function construirSeccionDatosEvaluador(form) {
  // Nota: Al inicio del formulario se recolectan los datos de contacto
  var emailItem = form.addTextItem();
  emailItem.setTitle("1. Dirección de correo electrónico de contacto o institucional:")
    .setHelpText("Ingrese su correo electrónico para el registro oficial de su participación como juez evaluador.")
    .setRequired(true);

  // Validación de formato de correo electrónico
  var validacionEmail = FormApp.createTextValidation()
    .setHelpText("Por favor, introduzca una dirección de correo electrónico válida (ejemplo: usuario@correo.com).")
    .requireTextIsEmail()
    .build();
  emailItem.setValidation(validacionEmail);

  var nombreItem = form.addTextItem();
  nombreItem.setTitle("2. Nombre y apellidos completos:")
    .setHelpText("Ingrese su nombre completo para fines de acreditación académica en la monografía.")
    .setRequired(true);
}

/**
 * SECCIÓN 2: Preparación de Datos y Muestreo
 */
function construirSeccionMuestreo(form) {
  var section = form.addPageBreakItem();
  section.setTitle("SECCIÓN 2: PREPARACIÓN DE DATOS Y MUESTREO")
    .setHelpText(
      "En esta sección se evalúa el proceso de filtrado de los microdatos del INE y la calibración muestral con factor de expansión.\n\n" +
      "Escala de valoración: 1 = Totalmente en desacuerdo | 2 = En desacuerdo | 3 = Ni de acuerdo ni en desacuerdo | 4 = De acuerdo | 5 = Totalmente de acuerdo"
    );

  agregarItemEscala(
    form,
    "P1. Los criterios de delimitación muestral (residencia urbana, edad de 16 a 28 años según Ley N.º 342 y condición activa en la PEA, totalizando 6.649 registros) son adecuados y claros.",
    "Revise la Tabla N.º 1 del Resumen Ejecutivo y el Cuadernillo Jupyter."
  );

  agregarItemEscala(
    form,
    "P2. El uso del factor de ponderación trimestral (fact_trim_act) para expandir la muestra a los 1.380.841 jóvenes urbanos es correcto para evitar distorsiones estadísticas.",
    "Garantiza que ningún indicador provenga de recuentos simples no ponderados."
  );
}

/**
 * SECCIÓN 3: Indicadores y Coincidencia con Cifras Oficiales del INE
 */
function construirSeccionIndicadoresINE(form) {
  var section = form.addPageBreakItem();
  section.setTitle("SECCIÓN 3: INDICADORES Y RÉPLICA OFICIAL DEL INE")
    .setHelpText(
      "En esta sección se evalúa la consistencia de los indicadores obtenidos frente al Boletín Oficial del INE para el 4T-2025.\n\n" +
      "Escala de valoración: 1 = Totalmente en desacuerdo | 2 = En desacuerdo | 3 = Ni de acuerdo ni en desacuerdo | 4 = De acuerdo | 5 = Totalmente de acuerdo"
    );

  agregarItemEscala(
    form,
    "P3. La tasa de desocupación juvenil calculada en el proyecto (3,71%, equivalente a 51.196 jóvenes) coincide con precisión con el reporte oficial publicado por el INE (3,7%).",
    "Consulte la Tabla N.º 2 del Resumen Ejecutivo y tabla_desocupacion_macro.csv."
  );

  agregarItemEscala(
    form,
    "P4. La tasa de subocupación juvenil por tiempo (8,70%, equivalente a 115.736 jóvenes) refleja adecuadamente la subutilización laboral reportada por el INE (8,7%).",
    "Calculada sobre la población ocupada de 1.329.645 jóvenes."
  );

  agregarItemEscala(
    form,
    "P5. La comparación que demuestra que la desocupación en jóvenes (3,71%) supera en 1,61 veces a la desocupación general urbana nacional (2,30%) está claramente sustentada.",
    "Consulte la Figura N.º 1 en la carpeta de figuras compartidas."
  );
}

/**
 * SECCIÓN 4: Análisis Estadístico y Pruebas de Hipótesis
 */
function construirSeccionAnalisisEstadistico(form) {
  var section = form.addPageBreakItem();
  section.setTitle("SECCIÓN 4: ANÁLISIS ESTADÍSTICO Y PRUEBAS DE ASOCIACIÓN")
    .setHelpText(
      "En esta sección se evalúa la pertinencia metodológica de las pruebas estadísticas bivariadas e inferenciales.\n\n" +
      "Escala de valoración: 1 = Totalmente en desacuerdo | 2 = En desacuerdo | 3 = Ni de acuerdo ni en desacuerdo | 4 = De acuerdo | 5 = Totalmente de acuerdo"
    );

  agregarItemEscala(
    form,
    "P6. Las pruebas estadísticas utilizadas (Chi-cuadrado para contrastar independencia y V de Cramér para medir el tamaño de la asociación) son pertinentes para analizar los factores vinculados al desempleo.",
    "Consulte la matriz de contrastes en tabla_pruebas_chi2_cramer.csv."
  );

  agregarItemEscala(
    form,
    "P7. La comparación de años de estudio entre jóvenes ocupados y desocupados mediante pruebas de hipótesis (prueba t de Welch y Mann-Whitney) es metodológicamente sólida.",
    "Verifica diferencias estadísticas significativas (p < 0,05) considerando no normalidad."
  );

  agregarItemEscala(
    form,
    "P8. La interpretación de los resultados es adecuada al explicar asociaciones estadísticas sin afirmar relaciones de causalidad directa.",
    "Enfoque metodológico riguroso acorde a un diseño observacional transversal."
  );
}

/**
 * SECCIÓN 5: Cuadro de Mando en Power BI Desktop
 */
function construirSeccionPowerBI(form) {
  var section = form.addPageBreakItem();
  section.setTitle("SECCIÓN 5: CUADRO DE MANDO EN POWER BI")
    .setHelpText(
      "En esta sección se evalúa la arquitectura dimensional, medidas DAX ponderadas y visualización interactiva de 6 páginas.\n\n" +
      "Escala de valoración: 1 = Totalmente en desacuerdo | 2 = En desacuerdo | 3 = Ni de acuerdo ni en desacuerdo | 4 = De acuerdo | 5 = Totalmente de acuerdo"
    );

  agregarItemEscala(
    form,
    "P9. La estructura del cuadro de mando interactivo en Power BI (organizado en 6 páginas temáticas) permite explorar y comprender con facilidad los indicadores clave.",
    "Consulte las capturas de pantalla de las 6 páginas en la carpeta 05_Capturas_Power_BI."
  );

  agregarItemEscala(
    form,
    "P10. Los gráficos (barras, tarjetas de indicadores, gráficos de donas y tablas dinámicas) facilitan la visualización y análisis de las brechas laborales.",
    "Diseño visual estandarizado orientado a la toma de decisiones técnicas."
  );
}

/**
 * SECCIÓN 6: Interpretación de Resultados y Hallazgos
 */
function construirSeccionHallazgos(form) {
  var section = form.addPageBreakItem();
  section.setTitle("SECCIÓN 6: INTERPRETACIÓN DE RESULTADOS Y HALLAZGOS")
    .setHelpText(
      "En esta sección se evalúa la coherencia de las explicaciones ante las brechas sociodemográficas y laborales detectadas.\n\n" +
      "Escala de valoración: 1 = Totalmente en desacuerdo | 2 = En desacuerdo | 3 = Ni de acuerdo ni en desacuerdo | 4 = De acuerdo | 5 = Totalmente de acuerdo"
    );

  agregarItemEscala(
    form,
    "P11. El análisis de las principales brechas laborales (pico de desocupación de 4,65% en jóvenes de 18 a 20 años y mayor tasa en mujeres con 4,69% frente a 2,85% en hombres) es coherente con la realidad económica.",
    "Consulte las Figuras 2 y 3 y el resumen de hallazgos."
  );

  agregarItemEscala(
    form,
    "P12. El hallazgo de que el 89,62% de los jóvenes desocupados son cesantes (con trabajo anterior) y solo el 10,38% son aspirantes (primer empleo) aporta claridad sobre la inestabilidad del empleo juvenil.",
    "Desmitifica que la desocupación juvenil sea un problema exclusivo de primer acceso."
  );
}

/**
 * SECCIÓN 7: Conclusiones y Calidad General
 */
function construirSeccionConclusiones(form) {
  var section = form.addPageBreakItem();
  section.setTitle("SECCIÓN 7: CONCLUSIONES Y CALIDAD GENERAL")
    .setHelpText(
      "En esta sección se evalúa la articulación de las conclusiones y el valor agregado general del trabajo de ciencia de datos.\n\n" +
      "Escala de valoración: 1 = Totalmente en desacuerdo | 2 = En desacuerdo | 3 = Ni de acuerdo ni en desacuerdo | 4 = De acuerdo | 5 = Totalmente de acuerdo"
    );

  agregarItemEscala(
    form,
    "P13. Las conclusiones y recomendaciones del proyecto responden de forma directa y justificada a los problemas identificados en los datos.",
    "Propuestas de formación dual, redes de cuidado infantil y diversificación tecnológica."
  );

  agregarItemEscala(
    form,
    "P14. En general, el trabajo de ciencia de datos realizado demuestra rigor técnico, reproducibilidad y utilidad práctica.",
    "Valoración sintética del pipeline integral: CRISP-DM, Python, Power BI y evidencia INE."
  );
}

/**
 * SECCIÓN 8: Evaluación Cualitativa y Dictamen Final
 */
function construirSeccionEvaluacionFinal(form) {
  var section = form.addPageBreakItem();
  section.setTitle("SECCIÓN 8: EVALUACIÓN CUALITATIVA Y DICTAMEN FINAL")
    .setHelpText("Por favor, comparta su juicio técnico de síntesis y sus observaciones cualitativas para el autor:");

  // Calificación lineal de 1 a 10 puntos
  var escalaGlobal = form.addScaleItem();
  escalaGlobal.setTitle("Calificación cuantitativa global del proyecto:")
    .setHelpText("Califique el desempeño técnico, metodológico y de visualización del trabajo en una escala de 1 a 10:")
    .setBounds(1, 10)
    .setLabels("1 = Muy deficiente", "10 = Excelente / Sobresaliente")
    .setRequired(true);

  // Pregunta abierta 1: Fortalezas
  var fortalezasItem = form.addParagraphTextItem();
  fortalezasItem.setTitle("Principales fortalezas del trabajo:")
    .setHelpText("Describa los aspectos más sólidos, rigurosos o aportes destacados del proyecto.")
    .setRequired(true);

  // Pregunta abierta 2: Debilidades
  var debilidadesItem = form.addParagraphTextItem();
  debilidadesItem.setTitle("Principales debilidades o aspectos a mejorar:")
    .setHelpText("Señale limitaciones metodológicas, técnicas o aspectos analíticos que podrían profundizarse.")
    .setRequired(true);

  // Pregunta abierta 3: Sugerencias adicionales (opcional)
  var sugerenciasItem = form.addParagraphTextItem();
  sugerenciasItem.setTitle("Sugerencias y recomendaciones adicionales:")
    .setHelpText("Comentarios complementarios o líneas futuras de investigación para el autor (Opcional).")
    .setRequired(false);

  // Dictamen final de validación (Selección única)
  var dictamenItem = form.addMultipleChoiceItem();
  dictamenItem.setTitle("Dictamen final de validación por parte del experto:")
    .setHelpText("Seleccione su dictamen técnico formal sobre la validez del trabajo evaluado:")
    .setChoiceValues([
      "Aprobado con Distinción / Sobresaliente (El proyecto cumple estándares excepcionales de rigor y reproducibilidad)",
      "Aprobado Plenamente (El proyecto es metodológicamente sólido y sus resultados son válidos y consistentes)",
      "Aprobado con Observaciones Menores (Requiere ajustes formales leves que no comprometen los hallazgos)",
      "Requiere Modificaciones Sustanciales (Presenta debilidades técnicas que deben ser subsanadas)",
      "No Aprobado (Inconsistencias técnicas o metodológicas severas)"
    ])
    .setRequired(true);
}

/**
 * Función auxiliar para agregar preguntas de escala Likert (1 a 5).
 */
function agregarItemEscala(form, titulo, textoAyuda) {
  var item = form.addScaleItem();
  item.setTitle(titulo)
    .setHelpText(textoAyuda)
    .setBounds(1, 5)
    .setLabels("Totalmente en desacuerdo", "Totalmente de acuerdo")
    .setRequired(true);
  return item;
}

/**
 * Función auxiliar para limpiar de forma segura todos los ítems previos de un formulario existente.
 * Se recorre de atrás hacia adelante para evitar el desfasaje de índices.
 */
function limpiarItemsPrevios(form) {
  var items = form.getItems();
  for (var i = items.length - 1; i >= 0; i--) {
    form.deleteItem(i);
  }
}