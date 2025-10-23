# 🧑‍💻 Manual de Usuario – MPLS Vision Bot

Este manual detalla cómo utilizar el sistema de validación automática de etiquetas de red a través de una interfaz conversacional implementada mediante un bot de Telegram.

---

## 1. Guía paso a paso para usar la interfaz

1. Abre la app de **Telegram**.
2. Busca y selecciona el bot: `@mpls_vision_bot`.
3. Presiona **Iniciar** o escribe `/start` para activar el menú.
4. Envía una **imagen clara de la etiqueta** que deseas validar.
5. Recibe un mensaje automático con:
   - Texto extraído por OCR
   - Estado de validez (válido/no válido)
   - Detalles interpretados de la estructura de la etiqueta

---

## 2. Capturas de pantalla anotadas

📸 Ejemplo de interacción con el bot:

```
[imagen de etiqueta enviada]

Bot:
**PROCESANDO IMAGEN...**
✓ Texto extraído: `UIO-Gosseal(A)-Whymper(E)(B)/FO2-PEI6B-CAF`
📦 Código detectado: ...
✅ Estado: VÁLIDO
...
```

> Las capturas completas están en `/app/assets/`.

---

## 3. Funcionalidades del sistema

| Funcionalidad             | Descripción                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| OCR automático            | Extrae texto estructurado desde imágenes                                     |
| Validación semántica      | Verifica la estructura de la etiqueta según su tipo (completa / no aplica)  |
| Comprobación de color     | Evalúa si el color del buffer pertenece al catálogo de 12 colores válidos   |
| Interfaz conversacional   | Usa comandos amigables en Telegram para guiar al usuario                    |
| Respuesta enriquecida     | Devuelve mensaje estructurado con campos extraídos y validados              |

---

## 4. Problemas comunes y soluciones (Troubleshooting)

| Problema encontrado                                | Solución sugerida                                             |
|----------------------------------------------------|----------------------------------------------------------------|
| El bot no responde                                 | Verifica conexión a internet y vuelve a enviar `/start`       |
| Imagen mal interpretada                            | Asegúrate de buena iluminación, sin movimiento                |
| Resultado “no válido” para etiqueta correcta       | Verifica formato, color y estructura esperada                 |
| Texto OCR ilegible                                 | Usa etiquetas impresas con tipografía estándar                |
| No reconoce imagen enviada desde la galería       | Usa la cámara o comprueba que el formato sea `.jpg` o `.png`  |

---

## 5. FAQ – Preguntas Frecuentes

**¿Qué etiquetas puedo validar?**  
Solo etiquetas del sistema MPLS Ecuador con formato predefinido.

**¿Qué colores son válidos?**  
12 colores válidos: ROJ, BLA, CAF, VER, NAR, AZU, ROS, VIO, GRI, NEG, CEL, AMA.

**¿Puedo usar imágenes antiguas?**  
Sí, mientras estén enfocadas y legibles.

**¿Puedo validar varias etiquetas a la vez?**  
No. El bot analiza una imagen por vez.

**¿El resultado tiene validez legal?**  
No. Es una herramienta de apoyo técnico, no de certificación oficial.

---

## 6. Contacto para soporte

📧 **Marcelo Ismael Andrade** – `0958610558`  
📧 **María Augusta Flores** – `0982704137`

---
