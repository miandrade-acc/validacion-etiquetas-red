# 🧪 Pruebas Unitarias del Proyecto

Este directorio contiene los tests automáticos para verificar la funcionalidad del sistema de validación automática de etiquetas de red.

---

## 📂 Archivos incluidos

| Archivo                    | ¿Qué prueba?                                              |
|----------------------------|-----------------------------------------------------------|
| `test_data_processing.py` | Funciones auxiliares como `es_color_valido()`             |
| `test_model.py`           | Existencia y carga del modelo `best_model.pkl`            |
| `test_app.py`             | Que el archivo `app.py` del bot se cargue sin errores     |

---

## ✅ ¿Cómo ejecutar los tests?

### ▶️ En local

```bash
pip install pytest
pytest tests/
```

> Asegúrate de estar en la raíz del proyecto, donde está el `README.md`.

---

### ▶️ En Google Colab

1. Clona el repositorio:

```python
!git clone https://github.com/miandrade-acc/validacion-etiquetas-red.git
%cd validacion-etiquetas-red
```

2. Instala `pytest`:

```python
!pip install pytest
```

3. Añade el path del repositorio:

```python
import sys
sys.path.append('/content/validacion-etiquetas-red')
```

4. Ejecuta los tests:

```python
!pytest tests/
```

---

## ⚠️ Posibles errores comunes

| Error                                              | Solución                                                                 |
|----------------------------------------------------|--------------------------------------------------------------------------|
| `ModuleNotFoundError: No module named 'src'`       | Asegúrate de haber hecho `sys.path.append(...)` en Colab o VSCode       |
| `FileNotFoundError` al cargar modelos              | Verifica que `best_model.pkl` y `model_v1.pkl` existan en `/models/`    |

---

## 📌 Requisitos

- Python 3.8 o superior
- `pytest`
- Modelos entrenados guardados previamente (`.pkl`)

---