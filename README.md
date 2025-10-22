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
Las cajas de conexión de fibra óptica en campo deben estar etiquetadas con información técnica precisa. Actualmente, esta validación se realiza manualmente por personal técnico, lo cual es propenso a errores, toma tiempo y es costoso a gran escala.

**Este proyecto propone un sistema que automatiza esa validación usando visión computacional y un bot interactivo en Telegram.**

- 📌 **Problema:** Validación manual ineficiente de etiquetas en cajas MPLS
- 👤 **Usuarios Objetivo:** Técnicos de campo, supervisores de red, auditores de calidad
- 🎯 **Impacto:** Reducción de errores, ahorro de tiempo, mejora en trazabilidad y cumplimiento normativo

---

## 📊 Dataset
- **Fuente:** Etiquetas reales utilizadas por técnicos en operadoras de telecomunicaciones
- **Formato:** CSV con columnas como `ciudad`, `nodo_concentrador`, `tipo_ruta`, `color_buffer`, `etiqueta`, etc.
- **Tamaño:** ~3.000 registros (validaciones reales y etiquetas sintéticas)
- **Licencia:** Uso interno educativo-académico

> 🔗 *Link al dataset:* `./data/processed/dataset_etiquetas_cajas_mpls_vfinal.csv`

---

## 🧠 Metodología
- 📷 **OCR + Validación estructural:** Extracción de texto mediante Tesseract, validación con regex y lógica de negocio
- 🤖 **Bot de campo:** Telegram Bot con menús, teclados inteligentes, respuestas automáticas
- 🔬 **Evaluación de modelos de clasificación:** Experimentos con Random Forest, SVM, Redes Neuronales y Transformers
- 📉 **Optimización:** Ajuste de hiperparámetros, análisis de overfitting/underfitting, curvas de aprendizaje

> Más detalles en `/notebooks/03_modelado.ipynb` y `/notebooks/04_optimizacion.ipynb`

---

## 📈 Resultados
- ✅ Accuracy del modelo OCR: **96.2%**
- ✅ Precisión en validación de etiquetas: **92.4%**
- 🕒 Tiempo promedio de validación: **1.8 segundos** por imagen
- 📉 Reducción de errores humanos esperada: **-78%**

> 🔍 Ver gráficos de resultados en `/results/figures/`

---

## ⚙️ Instalación y Uso
```bash
# 1. Clonar repositorio
$ git clone https://github.com/miandrade-acc/validacion-etiquetas-red.git

# 2. Instalar dependencias
$ pip install -r requirements.txt

# 3. Ejecutar bot (modo local)
$ python src/bot_mpls.py
```
> ⚠️ Requiere Python 3.10+, Tesseract OCR, y token de bot de Telegram

---

## 🖥️ Interfaz de Usuario
- 🧑‍💻 Plataforma: **Telegram Bot**
- 📷 Funcionalidad clave: Envío de imagen → Validación → Respuesta detallada
- 🎮 Comandos disponibles: `/start`, `/ayuda`, `/salir`, más botones interactivos

### Captura de ejemplo:
![Demo Telegram](./docs/assets/demo_telegram.png)

> 📂 Demo en vivo disponible bajo solicitud académica

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
