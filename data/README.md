# 📂 Datos del Proyecto

Este directorio contiene los datasets utilizados en el desarrollo del sistema de validación automática de etiquetas de red mediante visión computacional.

## 📁 Estructura de carpetas

```
/data/
├── raw/         → Datos originales proporcionados por la compañía de telecomunicaciones (formato Excel)
├── processed/   → Dataset procesado, limpio y etiquetado, utilizado en los notebooks y validaciones
└── README.md    → Este documento
```

---

## 🗃️ Descripción del dataset

Los datos corresponden a etiquetas físicas reales utilizadas en el despliegue de infraestructura de red MPLS. Cada registro contiene información sobre:

- Ciudad
- Nodo Concentrador
- Nodo Estándar
- Nodo Backup (si aplica)
- Ruta (tipo de recorrido)
- Código de Caja
- Color de Buffer (abreviado en 3 letras)
- Texto OCR extraído (en el dataset procesado)
- Estado de validez (etiqueta válida / no válida)

---

## 🧼 Diferencias entre versiones

| Versión         | Formato | Descripción                                                  |
|------------------|---------|--------------------------------------------------------------|
| `raw/`           | `.xlsx` | Datos originales, sin limpieza ni transformación            |
| `processed/`     | `.csv`  | Datos depurados, formateados, codificados y balanceados     |


---

## 🔒 Uso y confidencialidad

Los datos provienen de entornos reales de una empresa de telecomunicaciones. Aunque no contienen datos personales, su uso está restringido al ámbito académico del proyecto final de maestría.

- No se deben utilizar con fines comerciales sin autorización.
- No se incluyen nombres de clientes ni direcciones reales.
