# 🧪 Optimización de Hiperparámetros

## 1. Proceso de optimización

Durante el Workshop de la Semana 5 se implementó un análisis sistemático de hiperparámetros utilizando técnicas de validación cruzada y curvas de sensibilidad para evitar overfitting o underfitting.

Se utilizó `GridSearchCV` y análisis manual con `validation_curve` y `learning_curve` sobre un clasificador Random Forest entrenado con los atributos extraídos de las etiquetas validadas.

## 2. Hiperparámetros explorados

Los principales hiperparámetros ajustados fueron:

| Parámetro         | Rangos evaluados                 |
|------------------|----------------------------------|
| `n_estimators`   | [10, 50, 100, 200]               |
| `max_depth`      | [None, 10, 20, 30]               |
| `min_samples_split` | [2, 5, 10]                    |
| `criterion`      | ['gini', 'entropy']              |
| `bootstrap`      | [True, False]                    |

La métrica optimizada fue el `accuracy` con validación cruzada de 5 folds.

## 3. Resultados del análisis de sensibilidad

- Se observó que valores mayores a 100 en `n_estimators` no aportaban mejora significativa.
- Un `max_depth=20` ofrecía buen balance entre precisión y generalización.
- El `min_samples_split=2` mostró el mejor rendimiento sin sobreajuste.

## 4. Partial Dependence Plots (PDP)

> Se generaron gráficos de dependencia parcial con `sklearn.inspection.plot_partial_dependence`, disponibles en `/results/figures/pdp/`.

Estos mostraron cómo cada hiperparámetro afectaba la probabilidad de una predicción correcta, confirmando que `max_depth` y `n_estimators` tenían mayor impacto.

## 5. Ranking de importancia de hiperparámetros

Según la validación cruzada y feature importance del modelo entrenado, el ranking fue:

1. `max_depth`
2. `n_estimators`
3. `min_samples_split`
4. `criterion`
5. `bootstrap`

## 6. Análisis de interacciones

Se identificó interacción significativa entre:

- `max_depth` y `n_estimators`: profundidad alta con pocos árboles causaba overfitting.
- `min_samples_split` y `bootstrap`: configuraciones rígidas reducían recall en clases minoritarias.

## 7. Configuración final seleccionada

```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=20,
    min_samples_split=2,
    criterion='gini',
    bootstrap=True,
    random_state=42
)
```

Esta configuración balancea precisión, interpretabilidad y eficiencia computacional.

## 8. Comparación antes / después

| Métrica         | Baseline RF       | Después de Optimización |
|-----------------|-------------------|--------------------------|
| Accuracy        | 0.82              | 0.88                     |
| Precision       | 0.80              | 0.87                     |
| Recall          | 0.81              | 0.88                     |
| F1-score        | 0.80              | 0.88                     |

> Las métricas mejoraron significativamente después de la optimización de hiperparámetros, con especial impacto en recall y balance general.

---

Todos los resultados están documentados en el cuaderno `04_optimizacion.ipynb`.