# 📘 Manual de Usuario — MPLS VisionBot

**Versión:** 1.0  
**Autores:** María Augusta Flores, Marcelo Ismael Andrade  
**Grupo:** #7 — M&M Inteligencia Artificial e Innovación  
**Institución:** UEES  
**Asignatura:** Proyecto Integrador en Inteligencia Artificial  
**Docente:** Ing. Gladys Villegas Rugel  
**Fecha:** Octubre 2025 — Guayaquil, Ecuador  

---

## 📑 Tabla de Contenidos
1. [Guía paso a paso para usar la interfaz](#guía-paso-a-paso-para-usar-la-interfaz)  
2. [Capturas de pantalla anotadas](#capturas-de-pantalla-anotadas)  
3. [Funcionalidad del Sistema](#funcionalidad-del-sistema)  
4. [Troubleshooting (problemas comunes y soluciones)](#troubleshooting)  
5. [FAQ (preguntas frecuentes)](#faq)  
6. [Soporte técnico y mantenimiento](#soporte-técnico-y-mantenimiento)  

---

## 1. Guía paso a paso para usar la interfaz

1. Abre la app de Telegram.  
2. Busca y selecciona el bot: `@mpls_vision_bot`  
3. Presiona el botón `Iniciar` o escribe `/start` para activar el menú  
4. Envía una imagen clara de la etiqueta que deseas validar  
5. Recibe una respuesta automática con:
   - Texto extraído por OCR  
   - Estado de validez (válido / no válido)  
   - Detalles estructurados interpretados de la etiqueta  

---

## 2. Capturas de pantalla anotadas

*📌 Inserta aquí las imágenes reales con anotaciones (guías visuales para el usuario)*

```markdown
![Inicio del bot](assets/start.png)
![Menú principal](assets/menu.png)
![Validación exitosa](assets/valid_success.png)
![Validación fallida](assets/valid_fail.png)
```

---

## 3. Funcionalidad del Sistema

| Funcionalidad            | Descripción                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| OCR automático           | Extrae texto estructurado desde imágenes                                   |
| Validación semántica     | Verifica la estructura de la etiqueta según su tipo (completa / no aplica) |
| Comprobación de color    | Evalúa si el color del buffer es uno de los 12 colores válidos              |
| Interfaz conversacional  | Usa comandos amigables en Telegram para guiar al usuario                   |
| Respuesta enriquecida    | Devuelve mensaje estructurado con los campos extraídos y validados         |

---

## 4. Troubleshooting

| Problema encontrado                  | Solución sugerida                                     |
|-------------------------------------|--------------------------------------------------------|
| El bot no responde                  | Verifica conexión a internet y vuelve a enviar `/start` |
| Imagen mal interpretada             | Asegúrate de buena iluminación, sin movimiento        |
| Resultado “no válido” incorrecto    | Verifica formato, color y estructura esperada         |
| Texto OCR ilegible                  | Usa etiquetas impresas con tipografía estándar        |
| No reconoce imagen desde galería    | Usa la cámara o asegúrate que sea `.jpg` o `.png`     |

---

## 5. FAQ (Preguntas Frecuentes)

**❓ Qué etiquetas puedo validar?**  
Solo etiquetas del sistema MPLS Ecuador con formato predefinido

**❓ Qué colores son válidos?**  
12 colores válidos: ROJ, BLA, CAF, VER, NAR, AZU, ROS, VIO, GRI, NEG, CEL, AMA

**❓ Puedo usar imágenes antiguas?**  
Sí, siempre que estén enfocadas y legibles

**❓ Puedo validar varias etiquetas a la vez?**  
No. El bot analiza una imagen por vez

**❓ Puedo usar el bot sin conexión a Internet?**  
No. MPLS VisionBot requiere conexión activa

**❓ El bot guarda mis fotografías?**  
No. Solo se utilizan temporalmente durante la validación

**❓ El resultado tiene validez legal?**  
No. Es una herramienta de apoyo técnico, no de certificación oficial

---

## 6. Soporte Técnico y Mantenimiento

| Nivel                        | Descripción                          | Responsable             | Contacto           |
|-----------------------------|--------------------------------------|-------------------------|--------------------|
| Nivel 1 – Soporte operativo | Guía y asistencia al usuario en campo| María Augusta Flores    | 0958610558         |
| Nivel 2 – Soporte técnico   | Mantenimiento técnico del sistema    | Marcelo Andrade         | 0982704137         |

📬 Email: [info@acclatam.lat](mailto:info@acclatam.lat)  
🌐 Web: [www.acclatam.lat/mmia](http://www.acclatam.lat/mmia)

---

📍 Quito, Ecuador