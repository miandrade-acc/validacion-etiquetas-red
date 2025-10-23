import pytest
from src import data_processing

def test_es_color_valido():
    assert data_processing.es_color_valido("CAF") is True
    assert data_processing.es_color_valido("XYZ") is False

def test_obtener_tipo_ruta():
    assert data_processing.obtener_tipo_ruta("Nodo-A/Nodo-B") == "Ruta Completa"
    assert data_processing.obtener_tipo_ruta("Nodo-A-Nodo-B") == "Ruta No Aplica"

def test_extraer_campos():
    etiqueta = "UIO-GOS-WHY-BCK-FO2-PEI6B-CAF"
    campos = data_processing.extraer_campos(etiqueta)
    assert campos["ciudad"] == "UIO"
    assert campos["color_buffer"] == "CAF"