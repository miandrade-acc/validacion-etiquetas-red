# Validación automática de etiquetas de red mediante visión computacional y bot en campo

**Autores:** Marcelo Ismael Andrade · María Augusta Flores  
**Programa:** Proyecto Integrador – Maestría en Inteligencia Artificial  
**Institución:** [Nombre de la Universidad]  
**Docente:** _____________________  
**Fecha:** Septiembre 2025  

---

## 📌 Descripción
Este repositorio acompaña al **Documento Técnico Final** del Proyecto Integrador.  
El objetivo es desarrollar un sistema de **visión computacional ligera** integrada con un **bot móvil**, para validar automáticamente etiquetas físicas de red (ONT, OLT, patch panels, cajas de empalme) en condiciones reales de campo.

La solución busca:
- Reducir en ≥40% los errores de inventario.
- Disminuir tiempos de validación a ≤2 segundos.
- Integrar reportes automáticos y trazables.
- Facilitar la adopción por técnicos de telecomunicaciones.

---

## 📂 Estructura del repositorio
```
src/                    # Código fuente y pseudocódigo inicial
  ocr_pipeline.py       # Pipeline OCR (pseudocódigo)
  bot_interface.py      # Interfaz del bot (pseudocódigo)
  evaluation/metrics.py # Métricas técnicas (precisión, recall, F1)

scripts/
  train.py              # Plantilla de entrenamiento

data/
  samples/              # Muestras de imágenes sintéticas (ejemplos de etiquetas)

docs/
  mockups/              # Mockups del bot y dashboard

notebooks/              # Espacio para experimentos exploratorios

references/
  IEEE_20.txt           # 20 fuentes en formato IEEE consolidadas
```

---

## ⚙️ Requisitos sugeridos
- Python 3.10+  
- Librerías:  
  ```bash
  pip install opencv-python pillow numpy pandas
  ```
- Para OCR real: integración futura con **Tesseract/CRAFT/DBNet/CRNN**.

---

## 🚀 Uso rápido
```bash
# Clonar
git clone https://github.com/<usuario>/<repositorio>.git
cd validacion-etiquetas-red

# Crear entorno (opcional)
python -m venv .venv
source .venv/bin/activate   # (Windows: .venv\Scripts\activate)

# Instalar dependencias
pip install -r requirements.txt
```

Ejemplo de uso del pipeline:
```python
from src.ocr_pipeline import run_pipeline

result = run_pipeline("data/samples/sample_1.png")
print(result)
```

---

## 📊 Métricas de éxito
- **Técnicas**: F1 ≥ 0.85, Accuracy ≥ 90%, tiempo de respuesta ≤ 2 s.  
- **Impacto**: Reducción de errores de inventario ≥ 40%.  
- **Usabilidad**: Adopción ≥ 80%, satisfacción ≥ 4/5.  

---

## 🗂️ Documentación complementaria
- 📄 [Documento Técnico Final (PDF)](enlace-pdf)  
- 🎞️ [Presentación Ejecutiva (PPT)](enlace-ppt)  

---

## ⚖️ Licencias y permisos
- **Código:** Licenciado bajo MIT (ver `LICENSE`).  
- **Datasets públicos sugeridos:** ICDAR-MLT, COCO-Text, SynthText, Total-Text (revisar condiciones).  
- **Dataset propio:** no versionado aquí; uso interno con permisos.  
- **Muestras incluidas:** sintéticas, sin datos sensibles.  

---

## 👥 Autores
- Marcelo Ismael Andrade  
- María Augusta Flores
