"""
Entrenamiento del modelo de clasificación a partir del dataset procesado.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.model import entrenar_y_guardar_modelo
import os

# Ruta al dataset procesado
DATA_PATH = "data/processed/dataset_etiquetas_limpio.csv"  # Ajustar si el nombre es distinto
MODELO_PATH = "models/model_rf.pkl"

def cargar_datos():
    """
    Carga el dataset procesado desde CSV.
    """
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset no encontrado en: {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)
    return df

def preparar_datos(df):
    """
    Prepara los datos para entrenamiento (X, y).
    """
    # Suponemos que el dataset tiene columna 'etiqueta_valida' como target
    # y el resto de atributos ya codificados
    y = df["etiqueta_valida"]
    X = df.drop(columns=["etiqueta_valida"])
    return train_test_split(X, y, test_size=0.2, random_state=42)

def main():
    df = cargar_datos()
    X_train, X_test, y_train, y_test = preparar_datos(df)

    modelo = entrenar_y_guardar_modelo(X_train, y_train, ruta_salida=MODELO_PATH)

    # Evaluación rápida
    y_pred = modelo.predict(X_test)
    reporte = classification_report(y_test, y_pred)

    print("=== MÉTRICAS DEL MODELO ===")
    print(reporte)

if __name__ == "__main__":
    main()