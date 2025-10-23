# 🧠 Modelos Entrenados

Este directorio contiene las versiones entrenadas del modelo de clasificación supervisada para validar etiquetas OCR en redes MPLS.

---

## 📄 Archivos incluidos

| Archivo             | Descripción                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `model_v1.pkl`      | Primer modelo entrenado (Random Forest baseline sin optimización)           |
| `best_model.pkl`    | Mejor modelo final tras análisis de sensibilidad y validación cruzada       |
| `README.md`         | Este documento                                                             |

---

## 🧪 Criterios de selección del modelo final

El modelo `best_model.pkl` fue elegido con base en los siguientes criterios:

- Alto rendimiento en métricas de evaluación (`accuracy`, `precision`, `recall`, `f1-score`)
- Evaluación con datos balanceados y validación cruzada (5-fold)
- Análisis de sensibilidad de hiperparámetros (`n_estimators`, `max_depth`)
- Robustez ante casos límite de etiquetas mal formateadas

---

## 📊 Métricas del modelo final

| Métrica      | Valor aproximado |
|--------------|------------------|
| Accuracy     | 0.88             |
| Precision    | 0.87             |
| Recall       | 0.88             |
| F1-score     | 0.88             |

> Las métricas completas están documentadas en los notebooks `04_optimizacion.ipynb` y `05_evaluacion.ipynb`.

---

## ⚠️ Notas

- Los modelos fueron serializados usando `joblib`.
- Pueden cargarse desde cualquier script con:  
```python
from src.model import cargar_modelo  
modelo = cargar_modelo("models/best_model.pkl")
```