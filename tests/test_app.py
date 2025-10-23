import importlib.util

def test_app_carga():
    spec = importlib.util.spec_from_file_location("app", "app/app.py")
    app_module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(app_module)
        assert True
    except Exception:
        assert False, "Error al cargar app.py"