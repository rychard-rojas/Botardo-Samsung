# main.py
import os
import telebot
from typing import Any

# --- Módulos del Proyecto ---
import config
from manejador_dataset import ManejadorDataset # <-- NUEVO
from procesadores.ProcesadorTexto import ProcesadorTexto
from procesadores.ProcesadorImagen import ProcesadorImagen
from procesadores.ProcesadorAudio import ProcesadorAudio
from analizador_sentimientos import AnalizadorSentimiento
from api_client import generar_feedback_ia

# --- Inicialización de Componentes ---
# Validamos que los tokens existan antes de inicializar
if not config.TELEGRAM_TOKEN or not config.GROQ_API_KEY:
    raise ValueError("Los tokens de TELEGRAM_TOKEN y GROQ_API_KEY deben estar definidos en el archivo .env")

bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
analizador_sentimiento = AnalizadorSentimiento()
manejador_qa = ManejadorDataset('dataset.json') # <-- NUEVO
procesador_imagen = ProcesadorImagen(None) # Inicializamos el modelo de imagen una sola vez para eficiencia

print("EduMoodBot iniciado. Esperando mensajes...")

# --- Manejadores de Comandos ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Maneja los comandos /start y /help."""
    welcome_text = (
        "¡Hola! Soy EduMood Bot. 😊\n"
        "Puedes preguntarme sobre mí o mis creadores.\n"
        "También puedes enviarme un mensaje de texto, una nota de voz o una imagen "
        "y analizaré el sentimiento o contenido para darte un feedback constructivo. ¡Estoy aquí para escucharte!"
    )
    bot.reply_to(message, welcome_text)

# --- Manejadores de Contenido ---
# En main.py

@bot.message_handler(content_types=['text'])
def handle_text(message):
    """Maneja los mensajes de texto."""
    bot.send_chat_action(message.chat.id, 'typing')
    texto_usuario = message.text
    
    # 1. Intentar responder desde el dataset con un umbral más alto
    # Un umbral de 85-90 es bueno para evitar falsos positivos.
    respuesta_qa = manejador_qa.encontrar_respuesta(texto_usuario, umbral=0.70)
    
    if respuesta_qa:
        bot.reply_to(message, respuesta_qa, parse_mode='Markdown')
        return

    # 2. Si es una pregunta (termina en '?') y no se encontró respuesta, informar al usuario.
    if texto_usuario.strip().endswith('?'):
        respuesta_fuera_de_scope = (
            "Lo siento, esa pregunta está fuera de mi base de conocimientos actual. 🤖\n"
            "Recuerda que puedo responder preguntas sobre mí y mis creadores, "
            "o analizar el sentimiento de frases, audios e imágenes."
        )
        bot.reply_to(message, respuesta_fuera_de_scope)
        return

    # 3. Si no es una pregunta y no hubo coincidencia, proceder con el análisis de sentimiento.
    procesador_texto = ProcesadorTexto(texto_usuario)
    texto_limpio = procesador_texto.procesar()

    if "⚠️" in texto_limpio:
        bot.reply_to(message, texto_limpio)
        return

    analisis = analizador_sentimiento.analizar(texto_limpio)
    
    if "error" in analisis:
        bot.reply_to(message, analisis["error"])
        return

    feedback = generar_feedback_ia('texto', analisis)
    bot.reply_to(message, feedback)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    """Maneja los mensajes con imágenes."""
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        # Descargamos la foto de mayor resolución
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        nombre_archivo = f"photo_{message.message_id}.jpg"
        ruta_imagen = os.path.join(config.DOWNLOAD_DIR, nombre_archivo)
        with open(ruta_imagen, 'wb') as f:
            f.write(downloaded_file)

        # Usamos el procesador de imagen (ya inicializado)
        procesador_imagen.datos = ruta_imagen
        resultado_analisis = procesador_imagen.procesar()

        if "error" in resultado_analisis:
            bot.reply_to(message, resultado_analisis["error"])
            return
        
        feedback = generar_feedback_ia('imagen', resultado_analisis)
        bot.reply_to(message, feedback)

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error al procesar la imagen: {e}")

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    """Maneja las notas de voz."""
    bot.send_chat_action(message.chat.id, 'typing')
    try:
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        nombre_archivo = f"audio_{message.message_id}.ogg"
        ruta_audio = os.path.join(config.DOWNLOAD_DIR, nombre_archivo)
        with open(ruta_audio, 'wb') as f:
            f.write(downloaded_file)

        # 1. Transcribir el audio a texto
        procesador_audio = ProcesadorAudio(ruta_audio)
        texto_transcrito = procesador_audio.procesar()

        if "⚠️" in texto_transcrito:
            bot.reply_to(message, texto_transcrito)
            return
        
        bot.reply_to(message, f"Texto transcrito: \"_{texto_transcrito}_\"", parse_mode='Markdown')
        bot.send_chat_action(message.chat.id, 'typing')

        # 2. Analizar el sentimiento del texto transcrito
        analisis = analizador_sentimiento.analizar(texto_transcrito)

        if "error" in analisis:
            bot.reply_to(message, analisis["error"])
            return

        # 3. Generar feedback
        feedback = generar_feedback_ia('audio', analisis)
        bot.reply_to(message, feedback)

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error al procesar el audio: {e}")

# --- Bucle Principal ---
if __name__ == "__main__":
    print("Iniciando el bot...")
    bot.infinity_polling(timeout=20, long_polling_timeout=30)