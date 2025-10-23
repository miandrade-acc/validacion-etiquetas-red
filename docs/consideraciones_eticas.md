# ⚖️ Consideraciones Éticas del Proyecto

## 1. Análisis de sesgos

El dataset fue construido a partir de etiquetas físicas utilizadas en instalaciones reales de redes de fibra óptica. No contiene información demográfica, cultural o personal. Sin embargo, podrían existir **sesgos técnicos** relacionados con:

- Zonas urbanas mejor documentadas (más muestras)
- Variabilidad en formatos de impresión de etiquetas
- Calidad de imagen desigual (iluminación, enfoque)

Estos sesgos podrían afectar la precisión del modelo, principalmente si ciertas configuraciones (como colores o estructuras) están subrepresentadas. Aunque no hay grupos humanos perjudicados directamente, **los técnicos en campo podrían recibir respuestas erróneas si el modelo fue entrenado con ejemplos sesgados.**

---

## 2. Equidad y fairness

El modelo trata por igual todos los tipos de etiquetas y no tiene diferenciación explícita entre grupos. Aun así, se aplicaron estas acciones:

- Curado balanceado de etiquetas válidas/no válidas
- Verificación manual de muestras por tipo de ruta
- Separación explícita de estructuras “Ruta Completa” y “Ruta No Aplica”

No se utilizaron métricas específicas de fairness (como disparate impact), ya que no hay atributos sensibles. Pero sí se implementó **evaluación por tipo de ruta**, como mecanismo de control de equidad funcional.

---

## 3. Privacidad

El proyecto **no utiliza datos personales, ni geolocalización, ni imágenes de personas**. Solo se procesan etiquetas impresas que no contienen nombres, direcciones ni identificadores únicos de clientes. Las imágenes no se almacenan ni se envían a servicios externos.

📌 El sistema es compliant con principios de privacidad tipo GDPR:
- No se identifican usuarios
- No hay persistencia de datos sin consentimiento
- No se requiere login ni cookies

---

## 4. Transparencia y explicabilidad

El sistema es totalmente interpretable, pues:

- La lógica de validación se basa en reglas explícitas (estructura, colores válidos, campos definidos)
- El modelo usado (Random Forest) permite extraer la importancia de atributos
- Se documenta el pipeline completo y decisiones en los notebooks
- Las predicciones son fácilmente trazables: se muestra la estructura detectada, campos separados y motivo de validez/no validez

Técnicas como SHAP o LIME no fueron necesarias, pero podrían incorporarse en futuras versiones si se utiliza un modelo más complejo.

---

## 5. Impacto social

### Impactos positivos:
- Reducción de errores humanos en instalaciones
- Aumento de la trazabilidad operativa
- Mayor eficiencia en despliegues de red
- Profesionalización del personal técnico con herramientas IA

### Posibles impactos negativos:
- Excesiva dependencia del bot sin verificación humana
- Confusión si el modelo falla y no se explica claramente el error

Los principales beneficiarios son:
- Técnicos de campo
- Supervisores de redes
- Clientes indirectamente (por mejores instalaciones)

---

## 6. Responsabilidad

La responsabilidad recae sobre el equipo desarrollador y supervisor académico, quienes deben garantizar:

- Validación correcta del sistema antes de producción
- Actualizaciones del dataset cuando cambien los formatos de etiqueta
- Capacitación mínima al usuario final (técnico)

Se prevé una estrategia de revisión por versiones, pruebas controladas antes de despliegue real y un mecanismo de mejora continua documentado.

---

## 7. Uso dual y mal uso

Aunque el proyecto tiene fines técnicos, podría ser mal utilizado para:

- Validar documentos falsos si se adapta el OCR
- Automatizar decisiones sin control humano

⚠️ Por ello, se han tomado las siguientes salvaguardas:

- Claras advertencias de uso en el bot
- No se permite envío de texto arbitrario (solo imágenes estructuradas)
- Limitación de uso a equipos internos
- No se conecta a bases de datos empresariales

---

## 8. Limitaciones reconocidas

Este modelo **no debe usarse como sistema de validación legal ni para decisiones críticas sin supervisión humana**. No es confiable en:

- Imágenes borrosas, movidas o mal iluminadas
- Etiquetas sin estructura clara o con códigos no estandarizados
- Formatos distintos a los definidos (MPLS Ecuador)

Se recomienda siempre validar visualmente y usar el bot como **asistente de validación**, no como único criterio de decisión.