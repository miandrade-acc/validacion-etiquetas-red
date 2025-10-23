"""
Módulo de procesamiento de datos para etiquetas MPLS.

Incluye funciones de validación de estructura, codificación de colores, 
y separación de campos de una etiqueta OCR.
"""

VALID_COLORS = {
    "ROJ", "BLA", "CAF", "VER", "NAR", "AZU",
    "ROS", "VIO", "GRI", "NEG", "CEL", "AMA"
}


def es_color_valido(codigo_color):
    """
    Verifica si el código de color está entre los colores válidos.
    """
    return codigo_color.upper() in VALID_COLORS


def obtener_tipo_ruta(texto):
    """
    Determina el tipo de ruta: 'Ruta Completa' o 'Ruta No Aplica'.
    Ruta completa incluye nodo estándar y nodo backup.
    """
    if "/" in texto and "-" in texto:
        return "Ruta Completa"
    return "Ruta No Aplica"


def extraer_campos(etiqueta):
    """
    Extrae los campos clave de una etiqueta formateada.
    """
    partes = etiqueta.strip().split("-")
    campos = {
        "ciudad": partes[0] if len(partes) > 0 else "",
        "nodo_concentrador": partes[1] if len(partes) > 1 else "",
        "nodo_estandar": partes[2] if len(partes) > 2 else "",
        "nodo_backup": partes[3] if len(partes) > 3 else "",
        "codigo_caja": partes[-2] if len(partes) > 4 else "",
        "color_buffer": partes[-1] if len(partes) > 5 else ""
    }
    return campos


def validar_estructura(etiqueta):
    """
    Realiza validación general de estructura y color.
    """
    campos = extraer_campos(etiqueta)
    valido = es_color_valido(campos["color_buffer"])
    return valido, campos