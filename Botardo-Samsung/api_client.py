"""
Módulo Cliente de Groq


Gestiona la comunicación con la API de Groq para generar respuestas empáticas y constructivas
basadas en el análisis emocional de las entradas del usuario.
"""


import requests
from typing import Dict, Any
from config import GROQ_API_KEY, GROQ_MODEL, GROQ_API_URL




def generar_feedback_ia(tipo_entrada: str, analisis: Dict[str, Any]) -> str:
    """
    Genera un feedback emocionalmente empático y constructivo utilizando la IA de Groq.


    Args:
        tipo_entrada (str): Tipo de entrada del usuario ('texto', 'imagen', 'audio').
        analisis (Dict[str, Any]): Resultados del análisis de emociones/sentimientos.


    Returns:
        str: Mensaje breve con apoyo emocional adaptado al contexto educativo.
    """
    # Validación de la API key
    if not GROQ_API_KEY or not (GROQ_API_KEY.startswith("sk-") or GROQ_API_KEY.startswith("gsk_")):
        return "⚠️ La API Key de Groq no está configurada correctamente."


    # --- Prompt refinado para EduMood ---
    prompt = f"""
Eres EduMood, un asistente virtual empático y reflexivo diseñado para brindar apoyo emocional genuino
a estudiantes de secundaria y universidad.


Un usuario ha enviado un mensaje de tipo "{tipo_entrada}".
El análisis automático de su mensaje ha arrojado los siguientes resultados: {analisis}.
(No menciones ni hagas referencia al análisis ni a sus valores técnicos.)


Tu tarea es redactar una respuesta breve (2 a 4 frases) que cumpla lo siguiente:
1. Valida las emociones del usuario de forma natural y comprensiva.
2. Usa un tono cálido, cercano y humano —como el de un mentor o compañero empático—.
3. Ofrece una sugerencia amable o una perspectiva constructiva solo si es apropiado.
4. Evita sonar artificial, excesivamente positivo o dar consejos no solicitados.
5. Habla directamente al usuario en segunda persona (tú).


Ejemplos de estilo esperado:
- "Parece que estás pasando por un momento difícil, y es totalmente válido sentirse así. A veces dar un paso atrás y respirar puede ayudar un poco."
- "Entiendo que te frustre esta situación, sobre todo si estás dando lo mejor de ti. Quizás podrías hablarlo con alguien de confianza o tomarte un pequeño descanso."
- "Se nota que esto te preocupa mucho, y es normal sentirse inseguro ante algo importante. No estás solo en eso."
- "Se nota que juegas al LOL bastante. Recuerda equilibrar el tiempo de juego con otras actividades que te hagan sentir bien."
"""


    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }


    data = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "Eres EduMood, un asistente de apoyo emocional para estudiantes."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.8,
        "max_tokens": 180
    }


    try:
        response = requests.post(GROQ_API_URL, headers=headers, json=data, timeout=20)
        response.raise_for_status()
        respuesta = response.json()["choices"][0]["message"]["content"].strip()
        return respuesta


    except requests.exceptions.HTTPError as http_err:
        return f"[Error en la API de Groq {http_err.response.status_code}: {http_err.response.text}]"
    except requests.exceptions.Timeout:
        return "[Error de conexión: La solicitud a Groq superó el tiempo de espera.]"
    except Exception as e:
        return f"[Error de conexión a Groq: {e}]"
