# Importamos la función 'pipeline' de la biblioteca transformers
from transformers import pipeline

# 1. Creamos el pipeline de análisis de sentimiento
#    - Especificamos la tarea: "sentiment-analysis".
#    - Elegimos un modelo pre-entrenado. 'nlptown/bert-base-multilingual-uncased-sentiment'
#      es un modelo multilenguaje popular y eficiente que está disponible públicamente.
print("Cargando el modelo de análisis de sentimiento...")
analizador_sentimiento = pipeline(
    "sentiment-analysis",
    #model="pysentimiento/robertuito-sentiment-analysis"
    model="nlptown/bert-base-multilingual-uncased-sentiment" 
)
print("¡Modelo cargado con éxito! ✅")

# 2. Preparamos una lista de frases para analizar
frases_para_analizar = [
    "¡Me encantó este curso, aprendí muchísimo!",
    "El servicio al cliente fue bastante lento y poco útil.",
    "La película estuvo bien, aunque el final fue predecible.",
    "Estoy muy decepcionado con la calidad del producto.",
    "Qué día tan maravilloso para salir a caminar.",
    "No estoy seguro de si volvería a comprar en esa tienda.",
    "¡El servicio al cliente fue excepcional, resolvieron mi problema en minutos!",
    "Estoy encantado con la calidad del producto, superó todas mis expectativas.",
    "La película tiene una trama brillante y unas actuaciones memorables.",
    "¡Qué día tan maravilloso para pasear por el parque y disfrutar del sol!",
    "El nuevo álbum de la banda es una obra maestra, cada canción es increíble.",
    "El dispositivo electrónico viene con un manual de instrucciones detallado.",
    "La reunión está programada para el próximo martes a las 10 de la mañana.",
    "El informe meteorológico indica que la probabilidad de lluvia es del 30 por ciento.",
    "El coche es de color gris y tiene cuatro puertas.",
    "El documento debe ser entregado antes del final de la jornada laboral.",
    "La experiencia en el restaurante fue decepcionante, la comida estaba fría.",
    "El producto llegó dañado y no funciona correctamente.",
    "La conexión a internet ha sido inestable durante toda la semana.",
    "No estoy satisfecho con la política de devolución de la tienda.",
    "El tráfico en la ciudad es terrible, tardé dos horas en llegar a casa."
]

# 3. Usamos el pipeline para obtener el sentimiento de cada frase
print("\nAnalizando frases...")
resultados = analizador_sentimiento(frases_para_analizar)

# 4. Mostramos los resultados de una forma clara
for frase, resultado in zip(frases_para_analizar, resultados):
    sentimiento = resultado['label']
    confianza = resultado['score']
    
    # Añadimos un emoji para hacerlo más visual
    # El modelo 'nlptown/bert-base-multilingual-uncased-sentiment' devuelve etiquetas como '1 star', '2 stars', etc.
    # Acá mapeamos esas estrellas a sentimientos más generales para los emojis.
    emoji = "❓"
    if "star" in sentimiento:
        if sentimiento == '5 stars':
            emoji = "😊" # Muy positivo
        elif sentimiento == '4 stars':
            emoji = "🙂" # Positivo
        elif sentimiento == '3 stars':
            emoji = "😐" # Neutral
        elif sentimiento == '2 stars':
            emoji = "😟" # Negativo
        elif sentimiento == '1 star':
            emoji = "😠" # Muy negativo

    print(f"\nFrase: '{frase}'")
    print(f"  -> Sentimiento Detectado: {sentimiento.upper()} {emoji} (Confianza: {confianza:.2%})")
