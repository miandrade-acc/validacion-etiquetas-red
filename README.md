![Banner del proyecto](docs/valid.png)
# 🧠 MPLS Vision Bot – Validación Automática de Etiquetas de Red

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Estado-En%20Desarrollo-yellow)

Sistema inteligente basado en visión computacional y bots de campo para la validación automática de etiquetas en redes de fibra óptica. Desarrollado como proyecto integrador para la Maestría en Inteligencia Artificial.

---

## 📑 Tabla de Contenidos
1. [🧩 Descripción del Problema](#descripción-del-problema)
2. [📊 Dataset](#dataset)
3. [🧠 Metodología](#metodología)
4. [📈 Resultados](#resultados)
5. [⚙️ Instalación y Uso](#instalación-y-uso)
6. [🖥️ Interfaz de Usuario](#interfaz-de-usuario)
7. [📁 Estructura del Proyecto](#estructura-del-proyecto)
8. [⚖️ Consideraciones Éticas](#consideraciones-éticas)
9. [👥 Autores y Contribuciones](#autores-y-contribuciones)
10. [📜 Licencia](#licencia)
11. [🙏 Agradecimientos y Referencias](#agradecimientos-y-referencias)

---

## 🧩 Descripción del Problema

En los despliegues de redes de fibra óptica, las cajas de distribución deben estar etiquetadas con información técnica precisa para garantizar la trazabilidad, mantenimiento y cumplimiento normativo. Sin embargo, en la práctica, muchas etiquetas presentan errores, están mal colocadas o usan formatos incorrectos, generando:

- 🚫 Dificultades en el soporte técnico  
- 🕒 Pérdida de tiempo en campo  
- 📉 Disminución en la calidad del servicio  
- 💸 Costos adicionales por reprocesos  

Actualmente, esta validación se realiza de forma manual por técnicos en campo, lo que introduce errores humanos, falta de estandarización y retrasos operativos.

**Este proyecto propone una solución de validación automática utilizando visión computacional y un bot interactivo.**

🎯 **Objetivo general:** Automatizar el proceso de validación de etiquetas en campo mediante OCR, lógica estructural y asistencia conversacional por bot de Telegram.

👤 **Usuarios principales:** Técnicos de campo, supervisores de calidad, responsables de red.

⚙️ **Tecnologías utilizadas:** OCR (Tesseract), Python, lógica de validación con expresiones regulares, bot de Telegram con respuestas dinámicas.

📈 **Impacto esperado:** Reducción de errores, mejora en la trazabilidad, ahorro de tiempo en campo y aumento en la calidad del servicio de instalación y mantenimiento de fibra óptica.


---

## 📊 Dataset

El sistema fue entrenado y evaluado utilizando un conjunto de datos reales de etiquetas utilizadas en instalaciones de fibra óptica, provistas por técnicos de campo de una empresa de telecomunicaciones.

- 🗂️ **Formato:** CSV estructurado con columnas como `ciudad`, `nodo_concentrador`, `tipo_ruta`, `etiqueta`, `color_buffer`, entre otras.
- 📏 **Tamaño:** Aprox. 1.200 registros, incluyendo ejemplos válidos e inválidos para distintos escenarios.
- 🏷️ **Licencia:** Uso académico – restringido a fines educativos dentro del proyecto final de maestría.
- 📍 **Ubicación:** El dataset procesado se encuentra en la carpeta `/data/processed/`

> 🔗 *Archivo principal:* [`dataset_etiquetas_cajas_mpls_vfinal.csv`](./data/processed/dataset_etiquetas_cajas_mpls_vfinal.csv)

El dataset fue sometido a un proceso riguroso de limpieza, validación cruzada con expertos de dominio y enriquecimiento con etiquetas sintéticas para fortalecer el entrenamiento del modelo.


---

## 🧠 Metodología

El sistema combina visión computacional, lógica estructural y asistencia conversacional para validar etiquetas de red en imágenes capturadas por técnicos en campo.

### 🔁 Flujo general del sistema:

1. 📷 **Entrada:** El técnico envía una imagen de una etiqueta al bot de Telegram.
2. 🔍 **OCR (Reconocimiento de texto):** El sistema extrae el texto utilizando `pytesseract`.
3. 🧠 **Validación estructural:** Se aplica una lógica basada en expresiones regulares y reglas del negocio para verificar:
   - Si la etiqueta corresponde a una ruta completa o “no aplica”
   - Si contiene los campos mínimos esperados (ciudad, nodos, ruta, color buffer)
   - Si el código de color es uno de los 12 válidos
4. 🤖 **Respuesta automática:** El bot responde con un resumen de validación, indicando si la etiqueta es válida o no, y por qué.
5. 📊 **Entrenamiento del modelo:** Se utilizaron diferentes algoritmos de clasificación para análisis de errores estructurales y predicción de validez:
   - Random Forest
   - SVM
   - Redes Neuronales
   - Transformers
6. ⚙️ **Optimización:** Análisis de overfitting/underfitting, tuning de hiperparámetros y evaluación cruzada.

### 🧰 Herramientas y librerías utilizadas:

- `pytesseract` + `OpenCV` → procesamiento de imagen y OCR
- `scikit-learn` + `Keras` → entrenamiento y evaluación de modelos
- `Python-Telegram-Bot` → implementación del bot conversacional
- `matplotlib` y `seaborn` → visualización de métricas y curvas
- `regex`, `pandas`, `numpy` → validación estructural y procesamiento de datos

> El pipeline completo fue desarrollado y documentado en Jupyter Notebooks, disponibles en la carpeta `/notebooks/`

---

## 📈 Resultados

El sistema fue probado con más de 1.200 imágenes de etiquetas de red, con un enfoque doble: validación estructural + prueba de modelos de clasificación para experimentación académica.

### 🎯 Principales métricas alcanzadas:

| Métrica                           | Resultado     |
|----------------------------------|---------------|
| 📷 OCR Accuracy                  | 96.2%         |
| ✅ Precisión en validación       | 92.4%         |
| 🕒 Tiempo promedio de respuesta  | 1.8 segundos  |
| 📉 Reducción esperada de errores | -78%          |
| 💬 Satisfacción esperada (bot)   | > 4.5/5       |

### 📊 Análisis adicional:

- El sistema logró validar correctamente etiquetas de tipo “ruta completa” y “no aplica”, considerando combinaciones válidas de campos técnicos y códigos de color.
- Los modelos entrenados alcanzaron valores F1 superiores a 0.90 en clasificación binaria (*válida / no válida*), siendo Random Forest y SVM los más balanceados en rendimiento y tiempo de entrenamiento.

> 📁 Visualizaciones, curvas de aprendizaje, matrices de confusión y gráficos de optimización se encuentran en la carpeta `/results/figures/`

---

## ⚙️ Instalación y Uso

Este proyecto puede ejecutarse de forma local en cualquier sistema compatible con Python 3.10+ y que tenga instalado el motor OCR Tesseract.

### 🔧 Requisitos

- Python 3.10+
- pip
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) instalado en el sistema
- Token de Bot de Telegram válido (obtenido desde [@BotFather](https://t.me/BotFather))

### 🧪 Instalación paso a paso
```bash
# 1. Clonar el repositorio
git clone https://github.com/miandrade-acc/validacion-etiquetas-red.git
cd validacion-etiquetas-red

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar variable de entorno (TOKEN)
export TELEGRAM_TOKEN=your_bot_token_here

# 4. Ejecutar el bot en modo local
python src/bot_mpls.py

```

📦 Se recomienda usar un entorno virtual para aislamiento.

🗂️ Estructura de carpetas clave

/src/ → Contiene el código principal del bot y las funciones de validación

/data/processed/ → Dataset procesado utilizado en pruebas

/results/ → Métricas y gráficos generados

/notebooks/ → Cuadernos Jupyter con todo el desarrollo

---

## 🖥️ Interfaz de Usuario

La solución cuenta con una interfaz conversacional basada en **Telegram Bot**, diseñada para ser utilizada directamente por técnicos de campo.

### 🎮 Comandos disponibles:

- `/start` → Inicia la interacción con un mensaje de bienvenida y menú
- `/ayuda` → Explica cómo funciona el bot y cómo enviar imágenes
- `/salir` → Finaliza la conversación con el bot

### 🧭 Flujo básico de uso:

1. El usuario envía una imagen de una etiqueta de red.
2. El sistema realiza reconocimiento de texto (OCR) con `pytesseract`.
3. Se valida la estructura de la etiqueta (tipo de ruta, color buffer, formato correcto, etc.).
4. El bot responde con un mensaje estructurado indicando:
   - Ciudad, nodos, tipo de ruta, color
   - Estado: ✅ *VÁLIDO* o ❌ *NO VÁLIDO*
   - Detalles explicativos si hay error

### 📷 Ejemplo de respuesta automática:

```text
✓ Texto extraído: `UIO-Gosseal(A)-Whymper(E)(B)/Whymper(E)(A)-FO2-PEI6B-CAF`
📦 Código detectado: `...`
📁 Tipo de ruta: Ruta Completa
🎨 Color buffer: CAFÉ
✅ Estado: *VÁLIDO*

DETALLES:
• Ciudad: UIO
• Nodo Concentrador: Gosseal (A)
• Nodo Estándar: Whymper (E) (B)
• Nodo Backup: Whymper (E) (A)
• Caja: FO2-PEI6B
• Color: CAFÉ
```

---

## 📁 Estructura del Proyecto
```bash
validacion-etiquetas-red/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
│
├── docs/
│   ├── planificacion.md
│   ├── analisis_datos.md
│   ├── arquitectura.md
│   ├── optimizacion.md
│   ├── consideraciones_eticas.md
│   └── manual_usuario.md
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── README.md
│
├── notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_preprocesamiento.ipynb
│   ├── 03_modelado.ipynb
│   ├── 04_optimizacion.ipynb
│   └── 05_evaluacion.ipynb
│
├── src/
│   ├── bot_mpls.py
│   ├── data_processing.py
│   ├── model.py
│   └── utils.py
│
├── models/
│   ├── best_model.pkl
│   └── README.md
│
├── app/
│   └── (versión alternativa web en desarrollo)
│
├── tests/
│   └── test_bot.py
│
└── results/
    ├── figures/
    └── metrics/
```

---

## ⚖️ Consideraciones Éticas
- 🔍 **Sesgos posibles:** errores por imágenes mal enfocadas o etiquetas deterioradas
- 🛡️ **Privacidad:** no se almacenan datos personales ni imágenes en servidores externos
- 🚫 **Mal uso:** el sistema solo es válido para etiquetas oficiales con formato reconocido
- 🔄 **Responsabilidad:** las decisiones finales siguen siendo del técnico humano

---

## 👥 Autores y Contribuciones
- 👩‍💼 **María Augusta Flores** – Autora principal, diseño funcional, entrenamiento modelo
- 👨‍💼 Marcelo Ismael Andrade – Desarrollo bot, integración OCR, documentación técnica

> Proyecto desarrollado como parte del programa de Maestría en Inteligencia Artificial – UEES 2025

---

## 📜 Licencia
Este proyecto está bajo la Licencia MIT. Ver `LICENSE` para más información.

---

## 🙏 Agradecimientos y Referencias
- Universidad de Especialidades Espíritu Santo (UEES)
- Profesores del curso de Inteligencia Artificial
- Dataset de etiquetas provisto por técnicos en campo
- Librerías: OpenCV, pytesseract, Python-Telegram-Bot, Scikit-learn, Matplotlib

---

> 🌐 Repositorio oficial: [github.com/miandrade-acc/validacion-etiquetas-red](https://github.com/miandrade-acc/validacion-etiquetas-red/)
