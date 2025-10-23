# 🧑‍💻 Manual de Usuario – MPLS Vision Bot

Este manual detalla cómo utilizar el sistema de validación automática de etiquetas de red a través de una interfaz conversacional implementada mediante un bot de Telegram.

---

## 1. Acceso al sistema

Para acceder al bot:

1. Abre la aplicación de **Telegram**.
2. Busca el nombre del bot: `@mpls_vision_bot` (puede cambiar en producción).
3. Presiona el botón **Iniciar** o escribe `/start`.

> No se requiere registro ni permisos especiales.

---

## 2. Comandos disponibles

| Comando       | Descripción                                     |
|---------------|-------------------------------------------------|
| `/start`      | Inicia el bot, muestra el menú interactivo      |
| `/ayuda`      | Muestra instrucciones de uso                    |
| `/salir`      | Finaliza la sesión y cierra el flujo del bot    |

---

## 3. Flujo de uso

1. 📤 El usuario envía una imagen de una etiqueta física MPLS.
2. 🧠 El sistema procesa la imagen, ejecuta OCR y valida la estructura.
3. 📦 Se extraen los siguientes campos automáticamente:
   - Ciudad
   - Nodo Concentrador
   - Nodo Estándar
   - Nodo Backup (si aplica)
   - Ruta
   - Código de caja
   - Color del buffer (verificado con catálogo válido)
4. ✅ El bot responde con:
   - Texto OCR interpretado
   - Estado de validez (válido/no válido)
   - Detalles de cada campo extraído

---

## 4. Ejemplo de interacción

```plaintext
Usuario: [envía imagen de etiqueta]

Bot:
**PROCESANDO IMAGEN...**
✓ Texto extraído: `UIO-Gosseal(A)-Whymper(E)(B)/FO2-PEI6B-CAF`
📦 *Código detectado:* `UIO-Gosseal(A)-Whymper(E)(B)/FO2-PEI6B-CAF`
📁 *Tipo de ruta:* Ruta Completa
🎨 *Color buffer:* CAFÉ
✅ *Estado:* VÁLIDO

*DETALLES:*
• Ciudad: UIO
• Nodo Concentrador: Gosseal (A)
• Nodo Estándar: Whymper (E)
• Nodo Backup: Whymper (B)
• Código de Caja: FO2-PEI6B
• Color: CAFÉ
```

---

## 5. Recomendaciones de uso

- Enviar imágenes claras, bien iluminadas y sin movimiento.
- Usar etiquetas oficiales con formato definido.
- Validar manualmente si el resultado no es concluyente.
- Consultar la ayuda con `/ayuda` ante cualquier duda.

---

## 6. Limitaciones

- No reconoce etiquetas fuera del formato MPLS.
- Puede fallar con imágenes borrosas o fuera de foco.
- El resultado no tiene validez legal. Solo es una **herramienta de apoyo**.

---

## 7. Soporte

Para asistencia técnica o sugerencias de mejora, contactar a:

📧 **Marcelo Ismael Andrade** – `miandrade@ejemplo.com`  
📧 **María Augusta Flores** – `maflores@ejemplo.com`

---