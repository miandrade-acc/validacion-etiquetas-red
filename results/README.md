# 📊 Resultados del Modelo

Este directorio contiene los resultados generados durante la etapa de evaluación del modelo, así como las evidencias visuales, métricas y reportes que respaldan el rendimiento del sistema.

---

## 📁 Estructura de la carpeta

### 📈 `figures/`
Contiene los gráficos generados automáticamente a partir de los notebooks de entrenamiento y evaluación. Entre ellos:

- Curvas de aprendizaje (train vs. validation)
- Matriz de confusión
- Importancia de características
- Comparaciones antes/después de optimización

> Formato recomendado: `.png`, `.svg`, `.jpg`

---

### 📊 `metrics/`
Contiene las métricas cuantitativas obtenidas durante la evaluación de los modelos. Por ejemplo:

- `metrics_rf.json` → Diccionario con accuracy, precision, recall, f1-score
- `confusion_matrix.csv` → Matriz de confusión exportada
- `ranking_importancia.csv` → Ranking de variables

> Formato recomendado: `.csv`, `.json`

---

### 📝 `reports/`
Reportes generados automáticamente o de forma manual que resumen los hallazgos. Ejemplos:

- `informe_modelo.pdf` → Documento formal con interpretación de resultados
- `resumen.txt` o `resumen.md` → Conclusiones principales

---

## 📌 Notas

- Todos estos resultados se generan desde los notebooks `/notebooks/04_optimizacion.ipynb` y `05_evaluacion.ipynb`
- Esta carpeta sirve como respaldo para la reproducibilidad del proyecto