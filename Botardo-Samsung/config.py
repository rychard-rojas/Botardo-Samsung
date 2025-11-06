"""
Módulo de Configuración

Carga las variables de entorno y define las constantes
utilizadas en toda la aplicación.
"""
import os
from dotenv import load_dotenv

# Carga las variables desde el archivo .env
load_dotenv()

# --- Claves de API ---
TELEGRAM_TOKEN: str = os.getenv('TELEGRAM_TOKEN', '8252725949:AAHx4rnp8fBQI8yq8YeDrHPlkK7j_Sp630E')
GROQ_API_KEY: str = os.getenv('GROQ_API_KEY', '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')

# --- Modelos ---
# Modelo de IA generativa para dar feedback
GROQ_MODEL = "llama-3.1-8b-instant"

# Modelo de Hugging Face para el análisis de sentimientos
SENTIMENT_MODEL: str = "nlptown/bert-base-multilingual-uncased-sentiment"

# --- Endpoints ---
# URL de la API de Groq compatible con OpenAI
GROQ_API_URL: str = "https://api.groq.com/openai/v1/chat/completions"

# --- Rutas ---
# Directorio para guardar archivos temporales (fotos, audios)
DOWNLOAD_DIR: str = "downloads"

# Crear el directorio si no existe
os.makedirs(DOWNLOAD_DIR, exist_ok=True)