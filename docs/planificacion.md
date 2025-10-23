# 📌 Planificación del Proyecto

## 1. Definición del problema y objetivos

El presente proyecto tiene como objetivo resolver el problema de validación incorrecta y manual de etiquetas físicas en redes de fibra óptica MPLS, utilizando técnicas de visión computacional y automatización mediante un bot de Telegram.

### 🎯 Objetivo General
Implementar un sistema automatizado que permita validar etiquetas de cajas de red a partir de imágenes tomadas en campo, utilizando visión computacional y un bot funcional para operatividad técnica.

### ✅ Objetivos Específicos
- Extraer texto estructurado de etiquetas de red utilizando OCR.
- Validar automáticamente los códigos según criterios de color, topología y estructura.
- Desarrollar una interfaz conversacional en Telegram para validar etiquetas desde campo.
- Documentar y evaluar el sistema bajo métricas de desempeño técnico y experiencia de usuario.

## 2. Justificación de la relevancia del proyecto

El proceso actual de validación de etiquetas de red es manual, propenso a errores y poco escalable. Esto genera retrabajo, problemas de trazabilidad e inconsistencias en la implementación de rutas de fibra óptica. Automatizar este proceso representa una mejora directa en eficiencia operativa, reducción de errores humanos y trazabilidad en tiempo real. Su impacto es alto en áreas de despliegue de red, soporte técnico y aseguramiento de calidad.

## 3. Alcance del proyecto

### ✔️ Lo que incluye:
- Desarrollo de un sistema OCR para extraer información de etiquetas.
- Lógica de validación basada en estructura y códigos de color.
- Interfaz de interacción mediante bot de Telegram.
- Pruebas con imágenes reales y dataset etiquetado (~1200 registros).
- Cuadernos Jupyter con EDA, modelado y optimización.
- Repositorio estructurado con documentación y presentación.

### ❌ Lo que NO incluye:
- Despliegue en producción real con usuarios externos.
- Integración con bases de datos empresariales.
- Validación de otras tipologías de etiquetas fuera del formato MPLS definido.
- Reconocimiento de etiquetas borrosas sin delimitación visible.

## 4. Cronograma de desarrollo

| Fase                      | Entregable                      | Fecha planificada | Fecha real (si aplica) |
|---------------------------|----------------------------------|--------------------|-------------------------|
| Exploración de datos      | `01_exploracion.ipynb`           | Semana 1           | Semana 1                |
| Preprocesamiento          | `02_preprocesamiento.ipynb`      | Semana 2           | Semana 2                |
| Modelado base             | `03_modelado.ipynb`              | Semana 3           | Semana 3                |
| Optimización              | `04_optimizacion.ipynb`          | Semana 4           | Semana 4                |
| Evaluación final          | `05_evaluacion.ipynb`            | Semana 5           | Semana 5                |
| Desarrollo del bot        | `src/bot_mpls.py`                | Semana 5           | Semana 6                |
| Interfaz Telegram         | `app/telegram`                   | Semana 5-6         | Semana 6                |
| Presentación / demo       | `README.md / video demo`         | Semana 6           | Semana 6                |

## 5. Recursos necesarios

### 👤 Humanos:
- Desarrollador Python (Marcelo Ismael Andrade)
- Coordinadora técnica y académica (María Augusta Flores)
- Supervisor académico del proyecto

### 💻 Técnicos:
- Dataset etiquetado de etiquetas MPLS (1200 registros aprox.)
- Python 3.10
- Google Colab o ejecución local
- pytesseract, opencv-python, scikit-learn, python-telegram-bot
- API de Telegram
- Documentación guía del proyecto final

## 6. Riesgos identificados y mitigación

| Riesgo identificado                      | Probabilidad | Impacto | Estrategia de mitigación                     |
|------------------------------------------|--------------|---------|-----------------------------------------------|
| Calidad inconsistente del dataset        | Alta         | Alta    | Validación manual inicial y generación sintética si aplica |
| OCR falla por baja calidad de imagen     | Media        | Alta    | Filtrado, umbral adaptativo y pruebas con múltiples muestras |
| Tiempos de entrega ajustados             | Media        | Media   | Planificación con buffers semanales y entregas incrementales |
| Complejidad en lógica de validación      | Media        | Alta    | Iteraciones controladas en notebooks y uso de reglas claras |
| Errores en despliegue de bot             | Baja         | Alta    | Pruebas locales y testeo anticipado del flujo Telegram |