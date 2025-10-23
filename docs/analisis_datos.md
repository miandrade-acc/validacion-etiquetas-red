# 📊 Análisis Exploratorio de Datos (EDA)

## 1. Descripción del dataset

El dataset utilizado contiene aproximadamente 1200 registros, cada uno correspondiente a una etiqueta física de red del sistema MPLS. Cada etiqueta representa una combinación de:

- Ciudad
- Nodo Concentrador
- Nodo Estándar
- Nodo Backup (si aplica)
- Ruta (Completa o No Aplica)
- Código de caja
- Color del buffer (abreviado en 3 letras, ej. ROJ, VER, CAF)

El dataset fue generado a partir de imágenes reales procesadas y anotadas manualmente para extraer los campos válidos y validar la consistencia del OCR.

## 2. Estadísticas descriptivas

- Total de registros: ~1200
- Tipos de ruta: ~70% "Ruta Completa", ~30% "Ruta No Aplica"
- Colores más frecuentes: VER, ROJ, AZU, BLA
- Longitud promedio del texto extraído por OCR: 65 caracteres
- Cantidad de combinaciones únicas de ruta: +150
- Etiquetas válidas vs inválidas (después de validación lógica): ~85% válidas

## 3. Visualizaciones destacadas del EDA

> Se incluyen a continuación los principales gráficos generados en `01_exploracion.ipynb`:

- 📌 Distribución de colores de buffer (`color_buffer`)
- 📌 Frecuencia de tipos de ruta (`tipo_ruta`)
- 📌 Cantidad de etiquetas válidas/inválidas por tipo
- 📌 Longitud del texto OCR vs validez
- 📌 Mapa de calor de correlaciones entre atributos numéricos
- 📌 Diagrama de dispersión: posición en etiqueta vs errores de OCR

Todos los gráficos están disponibles en la carpeta `/results/figures/eda/`.

## 4. Patrones identificados y hallazgos

- Los errores de OCR se concentran en colores oscuros o imágenes con poca luz.
- Existen correlaciones entre estructura de nodo y tipo de validez.
- Las etiquetas que no incluyen nodo backup tienden a ser “Ruta No Aplica”.
- Se detectaron outliers por etiquetas con más de 100 caracteres, usualmente mal escaneadas.
- El 10% de las etiquetas contenía errores tipográficos que fueron corregidos en el preprocesamiento.

## 5. Decisiones de preprocesamiento

Las siguientes acciones fueron tomadas con base en el análisis:

- Conversión a mayúsculas de todo el texto OCR.
- Eliminación de caracteres especiales innecesarios (`~`, `#`, `=`, etc.).
- Separación de campos usando patrones RegEx basados en guiones y abreviaciones.
- Clasificación binaria del tipo de ruta (Ruta Completa / No Aplica).
- Validación contra listado de colores permitidos (12 códigos estándar).
- Validación lógica de estructura según tipo de ruta.

## 6. Manejo de datos faltantes o desbalanceados

- Se imputaron campos faltantes solo si se pudo inferir con certeza a partir del contexto (por ejemplo, nodo backup ausente implica “No Aplica”).
- No se utilizó sobremuestreo, ya que el desbalance era menor al 30%.
- Los casos no válidos se mantuvieron como clase separada para evaluación del modelo.

> Todas las decisiones fueron implementadas en el cuaderno `02_preprocesamiento.ipynb`.