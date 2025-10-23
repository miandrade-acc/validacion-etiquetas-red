{
  "cells": [
    {
      "cell_type": "markdown",
      "id": "b6e2ef4e",
      "metadata": {
        "id": "b6e2ef4e"
      },
      "source": [
        "# 🤖 MPLS Vision Bot\n",
        "\n",
        "Este cuaderno permite ejecutar en Google Colab un bot de Telegram para validar automáticamente etiquetas de red enviadas como fotos por técnicos de campo.\n",
        "\n",
        "### Incluye:\n",
        "- OCR con EasyOCR\n",
        "- Validación estructural (Ruta Completa o No Aplica)\n",
        "- Mensajes detallados (válidos / inválidos)\n",
        "- Menú interactivo persistente\n",
        "- Preparado para Google Colab"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "4b914074",
      "metadata": {
        "id": "4b914074"
      },
      "source": [
        "## 🔧 Instalación de librerías"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "id": "ee1f06d0",
      "metadata": {
        "id": "ee1f06d0"
      },
      "outputs": [],
      "source": [
        "!pip install python-telegram-bot --quiet\n",
        "!pip install easyocr opencv-python-headless nest_asyncio --quiet"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "144ba925",
      "metadata": {
        "id": "144ba925"
      },
      "source": [
        "## 🔐 Token del bot"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "id": "89cad407",
      "metadata": {
        "id": "89cad407"
      },
      "outputs": [],
      "source": [
        "TOKEN = '8243499597:AAHhpezJxk8wFzkzZFzCEwer5eE1BEDSlyM'"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "f67badd8",
      "metadata": {
        "id": "f67badd8"
      },
      "source": [
        "## 🧠 Clase MPLSVisionValidator"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "id": "abbbabec",
      "metadata": {
        "id": "abbbabec"
      },
      "outputs": [],
      "source": [
        "VALID_COLORS = {\n",
        "    \"ROJ\": \"ROJO\", \"BLA\": \"BLANCO\", \"CAF\": \"CAFÉ\", \"VER\": \"VERDE\", \"NAR\": \"NARANJA\",\n",
        "    \"AZU\": \"AZUL\", \"ROS\": \"ROSADO\", \"VIO\": \"VIOLETA\", \"GRI\": \"GRIS\", \"NEG\": \"NEGRO\",\n",
        "    \"CEL\": \"CELESTE\", \"AMA\": \"AMARILLO\"\n",
        "}\n",
        "\n",
        "\n",
        "class MPLSVisionValidator:\n",
        "\n",
        "    def parse_and_validate(self, raw_text: str) -> dict:\n",
        "        import re\n",
        "        result = {\"valid\": False, \"error\": \"\", \"type\": \"Desconocido\"}\n",
        "\n",
        "        try:\n",
        "            text = raw_text.strip().replace(\"\\n\", \"\").replace(\"\\r\", \"\").replace(\"—\", \"-\").replace(\"–\", \"-\").replace(\"／\", \"/\")\n",
        "\n",
        "            # REGEX para Ruta No Aplica\n",
        "            match_na = re.match(r\"^(.*?)-(.+?)-(.+?)/N/A-(.+?)-(.+?)-(.+?)$\", text, re.IGNORECASE)\n",
        "            if match_na:\n",
        "                ciudad, concentrador, estandar, ruta, caja, color = match_na.groups()\n",
        "                result.update({\n",
        "                    \"type\": \"Ruta No Aplica\",\n",
        "                    \"city\": ciudad,\n",
        "                    \"node_concentrator\": concentrador,\n",
        "                    \"node_standard\": estandar,\n",
        "                    \"route\": ruta,\n",
        "                    \"box_code\": caja,\n",
        "                    \"color\": color.upper(),\n",
        "                    \"color_name\": VALID_COLORS.get(color.upper(), \"Desconocido\"),\n",
        "                    \"emoji\": \"📁\"\n",
        "                })\n",
        "            else:\n",
        "                # REGEX para Ruta Completa\n",
        "                match_rc = re.match(r\"^(.*?)-(.+?)-(.+?)/(.+?)-(.+?)-(.+?)-(.+?)$\", text, re.IGNORECASE)\n",
        "                if not match_rc:\n",
        "                    result[\"error\"] = \"No coincide con ninguna estructura reconocida de etiqueta.\"\n",
        "                    return result\n",
        "                ciudad, concentrador, estandar, backup, ruta, caja, color = match_rc.groups()\n",
        "                result.update({\n",
        "                    \"type\": \"Ruta Completa\",\n",
        "                    \"city\": ciudad,\n",
        "                    \"node_concentrator\": concentrador,\n",
        "                    \"node_standard\": estandar,\n",
        "                    \"node_backup\": backup,\n",
        "                    \"route\": ruta,\n",
        "                    \"box_code\": caja,\n",
        "                    \"color\": color.upper(),\n",
        "                    \"color_name\": VALID_COLORS.get(color.upper(), \"Desconocido\"),\n",
        "                    \"emoji\": \"📦\"\n",
        "                })\n",
        "\n",
        "            if result[\"color\"] not in VALID_COLORS:\n",
        "                result[\"error\"] = f\"Color inválido: {result['color']}.\"\n",
        "                return result\n",
        "\n",
        "            result[\"valid\"] = True\n",
        "            return result\n",
        "\n",
        "        except Exception as e:\n",
        "            result[\"error\"] = f\"Error al procesar la etiqueta: {str(e)}\"\n",
        "            return result\n",
        "\n",
        "    def format_response(self, data: dict, ocr_text: str, confidence: float = None) -> str:\n",
        "        from datetime import datetime\n",
        "        now = datetime.now().strftime(\"%H:%M\")\n",
        "        lines = []\n",
        "\n",
        "        if data.get(\"valid\"):\n",
        "            lines.append(\"PROCESANDO IMAGEN...\")\n",
        "            lines.append(f\"✓ Texto extraído: {ocr_text}\")\n",
        "            lines.append(f\"{data['emoji']} Código detectado: {ocr_text}\")\n",
        "            lines.append(f\"📁 Tipo de ruta: {data['type']}\")\n",
        "            lines.append(f\"🎨 Color buffer: {data['color_name'].upper()}\")\n",
        "            lines.append(\"✅ Estado: VÁLIDO\")\n",
        "            lines.append(\"\")\n",
        "            lines.append(\"DETALLES:\")\n",
        "            lines.append(f\"• Ciudad: {data['city']}\")\n",
        "            lines.append(f\"• Nodo Concentrador: {data['node_concentrator']}\")\n",
        "            lines.append(f\"• Nodo Estándar: {data['node_standard']}\")\n",
        "            if data.get(\"node_backup\"):\n",
        "                lines.append(f\"• Nodo Backup: {data['node_backup']}\")\n",
        "            lines.append(f\"• Ruta: {data['route']}\")\n",
        "            lines.append(f\"• Caja/Código: {data['box_code']}\")\n",
        "            lines.append(f\"• Color: {data['color']} ({data['color_name']})\")\n",
        "        else:\n",
        "            lines.append(\"PROCESANDO IMAGEN...\")\n",
        "            lines.append(f\"✓ Texto extraído: {ocr_text}\")\n",
        "            lines.append(f\"❌ Código detectado: {ocr_text}\")\n",
        "            lines.append(f\"📁 Tipo de ruta: {data.get('type', 'No identificado')}\")\n",
        "            lines.append(\"❌ Estado: INVÁLIDO\")\n",
        "            lines.append(\"\")\n",
        "            lines.append(\"ERROR:\")\n",
        "            lines.append(data[\"error\"])\n",
        "            lines.append(\"\")\n",
        "            lines.append(\"RECOMENDACIONES:\")\n",
        "            lines.append(\"• Verifica la etiqueta físicamente.\")\n",
        "            lines.append(\"• Reintenta con mejor iluminación.\")\n",
        "            lines.append(\"• Colores válidos: ROJ, BLA, CAF, VER, NAR, AZU, ROS, VIO, GRI, NEG, CEL, AMA\")\n",
        "\n",
        "        lines.append(f\"🕒 {now} - @mpls_vision_bot\")\n",
        "        if confidence:\n",
        "            lines.append(f\"📊 Confianza OCR: {int(confidence * 100)}%\")\n",
        "\n",
        "        return \"\\n\".join(lines)"
      ]
    },
    {
      "cell_type": "markdown",
      "id": "704fa391",
      "metadata": {
        "id": "704fa391"
      },
      "source": [
        "## ▶️ Inicio del bot Telegram"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "id": "86780ba1",
      "metadata": {
        "id": "86780ba1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "aae03ddc-e7fe-4dad-a39b-e63c8cfbafdb"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:easyocr.easyocr:Using CPU. Note: This module is much faster with a GPU.\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "🤖 Bot ejecutándose. Esperando imágenes y comandos...\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Queue at 0x79f1b628cf50 maxsize=0 _getters[1]>"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "import nest_asyncio\n",
        "nest_asyncio.apply()\n",
        "\n",
        "from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove\n",
        "from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes\n",
        "import cv2\n",
        "import numpy as np\n",
        "import easyocr\n",
        "\n",
        "# Inicializar OCR y validador\n",
        "validator = MPLSVisionValidator()\n",
        "reader = easyocr.Reader(['es'], gpu=False)\n",
        "\n",
        "# Función para crear el menú principal\n",
        "def get_main_menu():\n",
        "    return ReplyKeyboardMarkup(\n",
        "        [[\"📷 Enviar Imagen\"], [\"ℹ️ Ayuda\", \"❌ Salir\"]],\n",
        "        resize_keyboard=True,\n",
        "        one_time_keyboard=False\n",
        "    )\n",
        "\n",
        "# Comando /start\n",
        "async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):\n",
        "    bienvenida = (\n",
        "        \"👋 *¡Hola! Bienvenido/a al MPLS Vision Bot*\\n\\n\"\n",
        "        \"📷 Envíame una imagen de una etiqueta MPLS y validaré automáticamente:\\n\"\n",
        "        \"• Tipo de ruta (Completa o No Aplica)\\n\"\n",
        "        \"• Estado (VÁLIDO o INVÁLIDO)\\n\"\n",
        "        \"• Recomendaciones técnicas\\n\\n\"\n",
        "        \"🚀 Usa el menú para interactuar con el bot o simplemente envía tu imagen.\"\n",
        "    )\n",
        "\n",
        "    await update.message.reply_text(\n",
        "        bienvenida,\n",
        "        parse_mode=\"Markdown\",\n",
        "        reply_markup=get_main_menu()\n",
        "    )\n",
        "\n",
        "# Comando /ayuda\n",
        "async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):\n",
        "    texto = (\n",
        "        \"ℹ️ *¿Cómo funciona este bot?*\\n\\n\"\n",
        "        \"1. Envía una imagen clara de la etiqueta\\n\"\n",
        "        \"2. Extraigo y valido el texto usando OCR\\n\"\n",
        "        \"3. Te indico si la etiqueta es válida y por qué\\n\\n\"\n",
        "        \"✅ Puedes enviar tantas imágenes como quieras\\n\"\n",
        "        \"❌ Usa el botón Salir para terminar la conversación\"\n",
        "    )\n",
        "\n",
        "    await update.message.reply_text(\n",
        "        texto,\n",
        "        parse_mode=\"Markdown\",\n",
        "        reply_markup=get_main_menu()\n",
        "    )\n",
        "\n",
        "# Comando /salir\n",
        "async def salir(update: Update, context: ContextTypes.DEFAULT_TYPE):\n",
        "    despedida = \"👋 *¡Gracias por usar el MPLS Vision Bot!*\\n\\nHasta la próxima.\"\n",
        "    await update.message.reply_text(\n",
        "        despedida,\n",
        "        parse_mode=\"Markdown\",\n",
        "        reply_markup=ReplyKeyboardRemove()\n",
        "    )\n",
        "\n",
        "# Procesar imagen\n",
        "async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):\n",
        "    try:\n",
        "        # Mensaje de procesamiento\n",
        "        processing_msg = await update.message.reply_text(\"⏳ *Procesando imagen...*\", parse_mode=\"Markdown\")\n",
        "\n",
        "        photo = update.message.photo[-1]\n",
        "        photo_file = await photo.get_file()\n",
        "        img_bytes = await photo_file.download_as_bytearray()\n",
        "        img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)\n",
        "        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)\n",
        "\n",
        "        results = reader.readtext(img_rgb)\n",
        "        ocr_text = ' '.join([text for (_, text, _) in results]).strip()\n",
        "        confidence = sum([conf for (_, _, conf) in results]) / len(results) if results else 0\n",
        "\n",
        "        result = validator.parse_and_validate(ocr_text)\n",
        "        response_raw = validator.format_response(result, ocr_text, confidence)\n",
        "\n",
        "        # Eliminar mensaje de procesamiento\n",
        "        await processing_msg.delete()\n",
        "\n",
        "        # Enviar resultado\n",
        "        await update.message.reply_text(response_raw)\n",
        "\n",
        "        # Preguntar si desea validar otra\n",
        "        teclado = ReplyKeyboardMarkup(\n",
        "            [[\"✅ Sí\", \"❌ No\"]],\n",
        "            resize_keyboard=True,\n",
        "            one_time_keyboard=True\n",
        "        )\n",
        "        await update.message.reply_text(\n",
        "            \"¿Deseas validar otra imagen?\",\n",
        "            reply_markup=teclado\n",
        "        )\n",
        "\n",
        "    except Exception as e:\n",
        "        error_msg = f\"❌ *Error al procesar la imagen:*\\n\\n`{str(e)}`\"\n",
        "        await update.message.reply_text(error_msg, parse_mode=\"Markdown\")\n",
        "\n",
        "# Manejar respuesta del teclado personalizado\n",
        "async def manejar_respuesta(update: Update, context: ContextTypes.DEFAULT_TYPE):\n",
        "    texto = update.message.text\n",
        "\n",
        "    if texto == \"✅ Sí\":\n",
        "        await update.message.reply_text(\n",
        "            \"Perfecto 👌 Puedes enviarme la siguiente imagen.\",\n",
        "            reply_markup=get_main_menu()\n",
        "        )\n",
        "    elif texto == \"❌ No\":\n",
        "        await salir(update, context)\n",
        "    elif texto == \"📷 Enviar Imagen\":\n",
        "        await update.message.reply_text(\n",
        "            \"📸 *Perfecto!*\\n\\nEnvía la imagen de la etiqueta MPLS que deseas validar.\",\n",
        "            parse_mode=\"Markdown\"\n",
        "        )\n",
        "    elif texto == \"ℹ️ Ayuda\":\n",
        "        await ayuda(update, context)\n",
        "    elif texto == \"❌ Salir\":\n",
        "        await salir(update, context)\n",
        "\n",
        "# Construir app y agregar handlers\n",
        "app = ApplicationBuilder().token(TOKEN).build()\n",
        "app.add_handler(CommandHandler(\"start\", start))\n",
        "app.add_handler(CommandHandler(\"ayuda\", ayuda))\n",
        "app.add_handler(CommandHandler(\"salir\", salir))\n",
        "app.add_handler(MessageHandler(filters.PHOTO, handle_photo))\n",
        "app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), manejar_respuesta))\n",
        "\n",
        "await app.initialize()\n",
        "await app.start()\n",
        "print(\"🤖 Bot ejecutándose. Esperando imágenes y comandos...\")\n",
        "await app.updater.start_polling()"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}
