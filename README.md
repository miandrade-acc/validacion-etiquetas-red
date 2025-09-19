# 🔎 Validación Automática de Etiquetas de Red  
*Visión Computacional + Bot en Campo*

👩‍💻 **Autores:** María Augusta Flores · Marcelo Ismael Andrade  
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
- **Temporal:** Implementación completa en un plazo máximo de 16 semanas.  

---

## 📂 Estructura del Repositorio
📁 data/samples/ → Muestras de imágenes sintéticas
📁 docs/mockups/ → Mockups del bot y dashboard
📁 references/ → Referencias y bibliografía
📁 scripts/ → Notebooks y scripts de pruebas
📁 src/ → Código fuente y pseudocódigo inicial
📄 LICENSE → Licencia MIT
📄 README.md → Este archivo
📄 .gitignore → Exclusiones de Git

yaml
Copiar código

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
pip install -r requirements.txt
Requisitos mínimos:
🐍 Python 3.10+
📦 Librerías: OpenCV, Pillow, NumPy, Pandas
🔮 OCR real: futura integración con Tesseract / CRAFT / DBNet / CRNN

🚀 Ejemplo de Uso
python
Copiar código
from src.ocr_pipeline import run_pipeline

result = run_pipeline("data/samples/sample_1.png")
print(result)
📊 Salida esperada:

bash
Copiar código
{'text': 'OLT-1234', 'confidence': 0.92}
📊 Métricas de Éxito
🧪 Técnicas → F1 ≥ 0.85 · Accuracy ≥ 90% · Tiempo ≤ 2 s

💰 Impacto → Reducción de errores ≥ 40%

👥 Usabilidad → Adopción ≥ 80% · Satisfacción ≥ 4/5

📄 Documentación
📕 Documento Técnico Final

⚖️ Licencia y Datasets
📜 Código bajo MIT (ver LICENSE)

🌐 Datasets recomendados: ICDAR-MLT, COCO-Text, SynthText, Total-Text

🔒 Dataset propio: uso interno, no versionado

🧪 Samples incluidos: sintéticos, sin datos sensibles

👥 Autores
👩‍💻 María Augusta Flores
👨‍💻 Marcelo Ismael Andrade
