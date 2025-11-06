"""
EduMoodBot - Bot de Telegram para Análisis Emocional

Este bot utiliza un enfoque modular para procesar texto, imágenes y audio,
analizar el sentimiento/emoción y proporcionar feedback utilizando IA generativa.
"""
import os
import telebot
from typing import Any

# --- Módulos del Proyecto ---
import config
from procesadores.ProcesadorTexto import ProcesadorTexto
from procesadores.ProcesadorImagen import ProcesadorImagen
from procesadores.ProcesadorAudio import ProcesadorAudio
from procesadores.procesador_base import Procesador
from analizador_sentimientos import AnalizadorSentimiento
from api_client import generar_feedback_ia

# --- Inicialización de Componentes ---
bot = telebot.TeleBot(config.TELEGRAM_TOKEN)
analizador_emocional = AnalizadorSentimiento()
print("EduMoodBot iniciado. Esperando mensajes...")

def manejar_entrada(message: Any, procesador_clase: type, tipo_entrada: str, datos: Any) -> None:
    """Procesa cualquier tipo de entrada usando polimorfismo."""
    bot.send_chat_action(message.chat.id, 'typing')
    procesador: Procesador = procesador_clase(datos)
    resultado_procesado = procesador.procesar()

    if isinstance(resultado_procesado, dict) and "error" in resultado_procesado:
        bot.reply_to(message, resultado_procesado["error"])
        return

    analisis = (
        analizador_emocional.analizar(resultado_procesado)
        if tipo_entrada == 'texto'
        else resultado_procesado
    )

    feedback = generar_feedback_ia(tipo_entrada, analisis)
    bot.reply_to(message, feedback)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """Maneja los comandos /start y /help."""
    welcome_text = (
        "¡Hola! Soy EduMood Bot. 😊\n"
        "Puedes enviarme un mensaje de texto, una nota de voz o una imagen "
        "y te daré un feedback constructivo. ¡Estoy aquí para escucharte!"
    )
    bot.reply_to(message, welcome_text)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    """Maneja los mensajes de texto."""
    manejar_entrada(message, ProcesadorTexto, 'texto', message.text)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    """Maneja los mensajes con imágenes."""
    file_path = "simulated_path/photo.jpg"  # Simulación
    manejar_entrada(message, ProcesadorImagen, 'imagen', file_path)

@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    """Maneja las notas de voz reales."""
    try:
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        nombre_archivo = f"audio_{message.message_id}.ogg"
        ruta_audio = os.path.join(config.DOWNLOAD_DIR, nombre_archivo)
        with open(ruta_audio, 'wb') as f:
            f.write(downloaded_file)

        manejar_entrada(message, ProcesadorAudio, 'audio', ruta_audio)

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error al procesar el audio: {e}")

if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
    