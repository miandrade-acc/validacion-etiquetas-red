"""
Interfaz simple (pseudocódigo) del bot para técnicos de campo.
Expone una función que recibe una imagen, corre el pipeline OCR y devuelve feedback.
"""
from typing import Dict, Any
from .ocr_pipeline import run_pipeline

def validate_label(image_path: str) -> Dict[str, Any]:
    result = run_pipeline(image_path)
    feedback = {
        "message": "Etiqueta válida" if result["sem"]["valid"] else "Etiqueta con inconsistencias",
        "details": result
    }
    return feedback
