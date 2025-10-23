import joblib
import os
import pytest

def test_modelo_existente():
    assert os.path.exists("models/best_model.pkl")

def test_modelo_carga():
    modelo = joblib.load("models/best_model.pkl")
    assert hasattr(modelo, "predict")