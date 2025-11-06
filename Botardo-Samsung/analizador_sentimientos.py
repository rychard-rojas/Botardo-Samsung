"""
Módulo de Análisis de Sentimiento

Encapsula el pipeline de Hugging Face Transformers para analizar
el sentimiento de un texto dado.
"""
from transformers import pipeline
from config import SENTIMENT_MODEL

class AnalizadorSentimiento:
    """
    Una clase para cargar y utilizar un modelo de análisis de sentimiento.
    El modelo se carga una sola vez para mejorar la eficiencia.
    """
    def __init__(self):
        """Inicializa y carga el pipeline del modelo."""
        try:
            print("Cargando el modelo de análisis de sentimiento...")
            self.analizador = pipeline(
                "sentiment-analysis",
                model=SENTIMENT_MODEL
            )
            print("¡Modelo cargado con éxito! ✅")
        except Exception as e:
            print(f"Error al cargar el modelo de sentimiento: {e}")
            self.analizador = None

    def _mapear_sentimiento(self, resultado_modelo: dict) -> dict:
        """Traduce la salida del modelo a un formato más legible."""
        label = resultado_modelo['label'].lower()
        score = resultado_modelo['score']
        
        sentimiento_map = {
            '5 stars': ("Muy Positivo", "😊"),
            '4 stars': ("Positivo", "🙂"),
            '3 stars': ("Neutral", "😐"),
            '2 stars': ("Negativo", "😟"),
            '1 star': ("Muy Negativo", "😠"),
        }
        
        sentimiento, emoji = sentimiento_map.get(label, ("Desconocido", "❓"))
        
        return {
            "sentimiento": sentimiento,
            "confianza": f"{score:.2%}",
            "emoji": emoji
        }

    def analizar(self, texto: str) -> dict:
        """
        Analiza el sentimiento de una cadena de texto.

        Args:
            texto: El texto a analizar.

        Returns:
            Un diccionario con el sentimiento, confianza y un emoji.
        """
        if not self.analizador or not isinstance(texto, str) or not texto.strip():
            return {"error": "Analizador no disponible o texto inválido."}

        try:
            resultado = self.analizador(texto)
            return self._mapear_sentimiento(resultado[0])
        except Exception as e:
            return {"error": f"Error durante el análisis: {e}"}