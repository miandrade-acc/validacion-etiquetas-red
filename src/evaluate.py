"""
Script de evaluación para modelo entrenado. 
Carga el modelo desde disco y calcula métricas sobre un conjunto de prueba.
"""

import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from src.model import cargar_modelo
import os

# Rutas
DATA_PATH = "data/processed/dataset_etiquetas_limpio.csv"
MODELO_PATH = "models/model_rf.pkl"

def cargar_datos():
    """
    Carga el dataset procesado.
    """
    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(f"Dataset no encontrado en: {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)
    return df

def preparar_datos(df):
    """
    Prepara los datos para evaluación.
    """
    y = df["etiqueta_valida"]
    X = df.drop(columns=["etiqueta_valida"])
    return X, y

def main():
    df = cargar_datos()
    X, y = preparar_datos(df)

    modelo = cargar_modelo(MODELO_PATH)
    y_pred = modelo.predict(X)

    print("=== MATRIZ DE CONFUSIÓN ===")
    print(confusion_matrix(y, y_pred))

    print("\n=== REPORTE DE CLASIFICACIÓN ===")
    print(classification_report(y, y_pred))

if __name__ == "__main__":
    main()