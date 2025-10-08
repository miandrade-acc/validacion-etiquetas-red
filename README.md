![Banner del proyecto](docs/valid.png)

# 🔎 Validación Automática de Etiquetas de Red  
*Visión Computacional + Bot en Campo*

👩‍💻 **Autores:** Grupo #7 - María Augusta Flores · Marcelo Ismael Andrade  
🎓 **Programa:** Proyecto Integrador – Maestría en Inteligencia Artificial (UEES)  
👩‍🏫 **Docente:** Ing. Gladys Villegas Rugel  
📅 **Fecha:** Septiembre 2025  

---

## 📌 Descripción del Proyecto
Este repositorio acompaña al **Documento Técnico Final** del Proyecto Integrador.  
El sistema combina **visión computacional ligera** con un **bot móvil** para validar automáticamente etiquetas físicas de red (ONT, OLT, patch panels, cajas de empalme) en condiciones reales de campo.  

✨ **Beneficios esperados:**  
- 📉 Reducir ≥40% errores de inventario  
- ⚡ Validación en ≤2 segundos  
- 📝 Reportes automáticos y trazables  
- 👷‍♂️ Mayor adopción por técnicos en campo  

---

## 🎯 Objetivo SMART
- **Específico:** Desarrollar un sistema de visión computacional y bot móvil que valide etiquetas de red en campo.  
- **Medible:** Alcanzar F1 ≥ 0.85, Accuracy ≥ 90%, reducción de errores ≥ 40%, tiempo de validación ≤ 2 s.  
- **Alcanzable:** Con dataset de etiquetas, modelos OCR ligeros y despliegue en bot de campo.  
- **Relevante:** Mejora la eficiencia y confiabilidad del inventario en empresas de telecomunicaciones.  
- **Temporal:** Implementación completa en un plazo máximo de 6 semanas.  

---

## 📂 Estructura del Repositorio
```
📁 data/samples/                → Dataset final validado (`dataset_etiquetas_cajas_mpls_vfinal.csv`) y muestras de imágenes
📁 docs/mockups/                → Mockups del bot y dashboard
📄 Documento_Tecnico_Final.pdf  → Documento técnico final (versión de prueba)
📁 references/                  → Referencias y bibliografía
📁 scripts/                     → Notebooks y scripts de pruebas
📁 src/                         → Código fuente y pseudocódigo inicial
📄 LICENSE                      → Licencia MIT
📄 README.md                    → Este archivo
📄 .gitignore                   → Exclusiones de Git
📄 requerimientos.txt           → Dependencias del proyecto (Python)
```

---

## 📦 Dataset Validado

Se ha cargado el dataset final validado y balanceado para entrenamiento del modelo de clasificación binaria.

- **Archivo:** `dataset_etiquetas_cajas_mpls_vfinal.csv`
- **Ubicación:** `/data/samples/`
- **Total de registros:** 818
- **Etiquetas (`clase`):**
  - `1` → Etiqueta correcta
  - `0` → Etiqueta incorrecta (ejemplos sintéticos)
- **Tipos de ruta:**
  - `ruta_completa` → nodo estandar y nodo backup
  - `ruta_no_aplica` → solo nodo estandar (`/N/A`)

📌 Este dataset reemplaza versiones anteriores como `dataset_etiquetas_cajas_mpls.csv`, que se conservan solo por trazabilidad.

---

## 🧠 Validación y Clasificación

Cada registro ha sido evaluado según reglas de negocio:

✅ **Clase = 1 (válida):**
- Color dentro de los 12 estándares (`ROJ`, `VER`, etc.)
- Caja con formato correcto (`PC12A`, `PE03B`, etc.)
- Nodo concentrador, estandar y backup (si aplica) presentes
- Campos completos y coherentes

❌ **Clase = 0 (inválida):**
- Color inválido (`BLANCO`, `ROSA`, etc.)
- Caja mal escrita o con errores
- Nodos faltantes o mal formateados
- Registros creados como ejemplos negativos controlados

---

## ⚙️ Instalación
```bash
# Clonar repositorio
git clone https://github.com/miandrade-acc/validacion-etiquetas-red.git
cd validacion-etiquetas-red

# (Opcional) Crear entorno virtual
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Instalar dependencias
pip install -r requerimientos.txt
```

**Requisitos mínimos:**  
🐍 Python 3.10+  
📦 Librerías: OpenCV, Pillow, NumPy, Pandas  
🔮 OCR real: futura integración con **Tesseract / CRAFT / DBNet / CRNN**  

---

## 🚀 Ejemplo de Uso
```python
from src.ocr_pipeline import run_pipeline

result = run_pipeline("data/samples/sample_1.png")
print(result)
```

📊 **Salida esperada:**
```bash
{'text': 'OLT-1234', 'confidence': 0.92}
```

---

## 📊 Métricas de Éxito
- 🧪 **Técnicas** → F1 ≥ 0.85 · Accuracy ≥ 90% · Tiempo ≤ 2 s  
- 💰 **Impacto** → Reducción de errores ≥ 40%  
- 👥 **Usabilidad** → Adopción ≥ 80% · Satisfacción ≥ 4/5  

---

## 📄 Documentación
### 📌 Semana 1 – Análisis Exploratorio y Dataset
- 📕 [Documento Técnico Final](docs/Documento_Tecnico_Final.pdf)
- 📊 [Notebook EDA: Análisis de etiquetas MPLS](scripts/EDA_CajasMPLS_Etiquetas_G7.ipynb)
- 📁 [Dataset Validado – MPLS](data/samples/dataset_etiquetas_cajas_mpls_vfinal.csv)
### 📌 Semana 2 – Preparación y Preprocesamiento de Datos
- 🧠 [Informe Comparativo de Algoritmos IA](docs/algoritmos/Analisis_Comparativo_Algoritmos_G7.pdf)
- 🧪 [Proyecto Final – Fase de Preparación y Preprocesamiento de Datos](scripts/Proyecto_Final_Procesamiento_Datos.ipynb)
- 📘 [Informe Técnico – Preparación y Preprocesamiento](docs/Preparacion_Procesamiento_Datos_G7.pdf)
- 📊 [Presentación Ejecutiva – Preparación de Datos](docs/Presentacion_Preparacion_Procesamiento_Datos_G7.pptx)
### 📌 Semana 3 – Diagnóstico de Overfitting / Underfitting
- 📘 [Cuaderno – Análisis y diagnóstico](./scripts/overfitting_analysis.ipynb)
- 📄 [Informe Técnico – Diagnóstico de Modelo](./docs/diagnostic_report.pdf)
### 📌 Semana 4 – Ética, Impacto Social y Responsabilidad
- 📄 [Detección de Riesgos Éticos – Grupo 7](docs/Deteccion_Riesgos_Eticos_IA_Grupo_7.pdf)  
- 📘 [Workshop – Impacto Social y Responsabilidad en Proyecto de IA (Documento Principal)](./Documentos/Workshop_Impacto%20Social%20y%20Responsabilidad%20en%20Proyecto%20de%20IA_G7.docx)  
- 📊 [Presentación Workshop – Impacto Social y Responsabilidad G7](./Documentos/Presentacion_Workshop_Impacto%20Social%20y%20Responsabilidad%20en%20Proyecto%20de%20IA_G7.ppt)



---

## ⚖️ Licencia y Datasets
- 📜 Este proyecto está bajo licencia **MIT**.  
  👉 Esto significa que el código puede ser usado, modificado y distribuido libremente, siempre y cuando se mantenga el aviso de copyright y la licencia original.  
  *(El texto completo de la licencia está disponible en `LICENSE`, en inglés).*  

- 🌐 Datasets recomendados: ICDAR-MLT, COCO-Text, SynthText, Total-Text  
- 🔒 Dataset propio: uso interno, no versionado  
- 🧪 Samples incluidos: sintéticos, sin datos sensibles  

---

## 👥 Autores
👩‍💻 María Augusta Flores  
👨‍💻 Marcelo Ismael Andrade  
