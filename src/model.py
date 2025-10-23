"""
Definición de modelos utilizados en el proyecto:
- Modelo de clasificación para etiquetas (Random Forest)
- Placeholder para OCR si se integraran modelos propios
"""

from sklearn.ensemble import RandomForestClassifier
import joblib


def crear_modelo_clasificacion(random_state=42, n_estimators=100, max_depth=None):
    """
    Crea un clasificador Random Forest con hiperparámetros definidos.
    """
    modelo = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state
    )
    return modelo


def entrenar_y_guardar_modelo(X_train, y_train, ruta_salida="model_rf.pkl"):
    """
    Entrena el modelo y guarda los pesos en disco.
    """
    modelo = crear_modelo_clasificacion()
    modelo.fit(X_train, y_train)
    joblib.dump(modelo, ruta_salida)
    return modelo


def cargar_modelo(ruta_modelo="model_rf.pkl"):
    """
    Carga un modelo previamente entrenado.
    """
    return joblib.load(ruta_modelo)


# Placeholder para modelo OCR personalizado (no utilizado en este proyecto)
def aplicar_ocr_personalizado(imagen):
    """
    Esta función no se implementa porque se usa Tesseract o EasyOCR.
    """
    raise NotImplementedError("Este proyecto usa motores OCR preentrenados.")