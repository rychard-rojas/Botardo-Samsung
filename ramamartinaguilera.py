# class manejadordeimput:
#     def play(self):
#         pass


# class Texto(manejadordeimput):
#     def play(self):
#         print("reproduciendo canal de tv")

# class Audio(manejadordeimput):
#     def play(self):
#         print("reproduciendo pelicula")

# class imagen(manejadordeimput):
#     def play(self):
#         print("reproduciendo juego") 

# class algomassssssss(manejadordeimput):
#     def play(self):
#         print("reproduciendo musica") 

# (Aca pueden ir los "imports")

# INTERFAZ BASE
class ManejadorDeInput:
    def procesar(self, data):
        raise NotImplementedError("La clase hija debe implementar el método 'procesar'")

# IMPLEMENTACIONES (CLASES HIJAS)

class Texto(ManejadorDeInput):
    """Maneja mensajes de texto y analiza sentimiento."""
    
    def procesar(self, mensaje_texto):
        print(f"[TEXTO]: Procesando '{mensaje_texto}'")
        
        # Toda la función de análisis de sentimiento
        sentimiento_simulado = "Positivo 😊" # Simulación
        print(f"Sentimiento detectado: {sentimiento_simulado}")
        return f"Texto analizado. Sentimiento: {sentimiento_simulado}"

class Imagen(ManejadorDeInput):
    """Describe fotos"""
    
    def procesar(self, ruta_a_la_imagen):
        print(f"[IMAGEN]: Analizando '{ruta_a_la_imagen}'")
        
        # Se llama al que ve imagen
        descripcion_simulada = "Un gato durmiendo en un sofá." # Simulación
        print(f"Descripción generada: {descripcion_simulada}")
        return f"Descripción: {descripcion_simulada}"

class Audio(ManejadorDeInput):
    """Maneja audio y lo transcribe."""
    
    def procesar(self, ruta_al_audio):
        print(f"[AUDIO]: Transcribiendo '{ruta_al_audio}'")
        
        # función de transcripción
        transcripcion_simulada = "Hola, esto es una prueba de audio." # Simulación
        print(f"Texto transcrito: {transcripcion_simulada}")
        return f"Transcripción: {transcripcion_simulada}"


# --- 3. EL "BOT" (EL CÓDIGO QUE USA EL POLIMORFISMO) ---


#Crear una instancia de CADA manejador
manejador_de_texto = Texto()
manejador_de_imagen = Imagen()
manejador_de_audio = Audio()

# Crear el "cerebro" del bot diccionario
manejadores = {
    "texto": manejador_de_texto,
    "imagen": manejador_de_imagen,
    "audio": manejador_de_audio
}

# Simular la llegada de mensajes
mensajes_recibidos = [
    ("texto", "¡Qué buen día hace hoy!"),
    ("imagen", "ruta/real/a/tu/foto.jpg"),  # <-- CAMBIA ESTO
    ("audio", "ruta/real/a/tu/audio.mp3"), # <-- CAMBIA ESTO
    ("texto", "No me gustó el servicio.")
]

# El Bucle Polimórfico
print("--- Iniciando Bot (Simulación) ---")
for tipo, data in mensajes_recibidos:
    
    manejador = manejadores.get(tipo)
    
    if manejador:
        try:
            respuesta = manejador.procesar(data)
            print(f"Respuesta del Bot: {respuesta}\n")
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo '{data}'. Asegúrate de que la ruta sea correcta.\n")
        except Exception as e:
            print(f"Error procesando {data}: {e}\n")
    else:
        print(f"Error: No sé cómo manejar el tipo '{tipo}'\n")