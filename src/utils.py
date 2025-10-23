"""
Funciones auxiliares para el proyecto MPLS Vision Bot.
Incluye carga de datos, visualización básica y validaciones generales.
"""

import os
import pandas as pd


def cargar_csv(ruta):
    """
    Carga un archivo CSV y verifica existencia.
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"Archivo no encontrado: {ruta}")
    return pd.read_csv(ruta)


def resumen_dataset(df):
    """
    Imprime resumen rápido de un DataFrame.
    """
    print("📊 Dimensiones:", df.shape)
    print("\n📌 Primeras filas:")
    print(df.head())
    print("\n🔍 Valores faltantes:")
    print(df.isnull().sum())


def guardar_csv(df, ruta):
    """
    Guarda un DataFrame como CSV.
    """
    df.to_csv(ruta, index=False)
    print(f"✅ Archivo guardado en: {ruta}")


def validar_extension_imagen(nombre_archivo):
    """
    Verifica si el archivo tiene extensión válida de imagen.
    """
    return nombre_archivo.lower().endswith((".png", ".jpg", ".jpeg", ".bmp"))