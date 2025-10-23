# 📊 Métricas de Evaluación del Modelo

Este directorio contiene los archivos de métricas cuantitativas generados durante las fases de entrenamiento y evaluación de los modelos desarrollados en el proyecto.

---

## 📁 Archivos incluidos

| Archivo                      | Descripción                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| `metrics_rf.json`           | Diccionario con métricas globales del modelo Random Forest (accuracy, precision, recall, f1-score) |
| `classification_report.txt` | Reporte completo con desgloses por clase, extraído con `classification_report()` |
| `confusion_matrix.csv`      | Matriz de confusión en formato tabular                                     |
| `feature_importance.csv`    | Ranking de importancia de características (si se generó)                    |
| `cross_val_scores.csv`      | Resultados de validación cruzada (si se generó)                             |

---

## 📌 Notas

- Estas métricas fueron generadas principalmente desde los notebooks:
  - `04_optimizacion.ipynb`
  - `05_evaluacion.ipynb`
- Sirven para sustentar las decisiones del modelo y se refieren al dataset ubicado en `/data/processed/`.

---

## 🧪 Formatos recomendados

- `.json` → Diccionarios serializados con múltiples métricas
- `.csv` → Matrices o rankings tabulares legibles
- `.txt` → Reportes exportados directamente desde `sklearn`

---

🔁 Esta carpeta puede ser actualizada si se reentrena el modelo o se optimizan nuevos hiperparámetros.