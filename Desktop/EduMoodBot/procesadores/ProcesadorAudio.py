# procesadores/ProcesasdorAudio.py
import speech_recognition as sr
from procesadores.procesador_base import Procesador
from pydub import AudioSegment # <-- Importar pydub
import os # <-- Importar os para manejar rutas

class ProcesadorAudio(Procesador):
    def __init__(self, ruta_audio: str):
        """
        Inicializa el procesador con la ruta al archivo de audio.
        """
        super().__init__(ruta_audio)
        self.recognizer = sr.Recognizer()

    def procesar(self) -> str:
        """
        Convierte el audio a WAV, lo transcribe a texto y devuelve el resultado.
        """
        # Paso 1: Convertir .ogg a .wav
        try:
            # Cargamos el archivo de audio original (.ogg)
            audio = AudioSegment.from_file(self.datos, format="ogg")
            
            # Definimos la nueva ruta para el archivo .wav
            ruta_wav = self.datos.replace(".ogg", ".wav")
            
            # Exportamos el audio a formato WAV
            audio.export(ruta_wav, format="wav")
            
        except Exception as e:
            return f"⚠️ Error al convertir el audio con pydub: {e}. Asegúrate de que 'ffmpeg' esté instalado y accesible en el PATH del sistema."

        # Paso 2: Transcribir el archivo .wav
        try:
            with sr.AudioFile(ruta_wav) as source:
                audio_data = self.recognizer.record(source)
                texto_transcrito = self.recognizer.recognize_google(audio_data, language='es-ES')
            
            # (Opcional) Limpiar los archivos temporales
            os.remove(ruta_wav)
            
            return texto_transcrito
        except sr.UnknownValueError:
            os.remove(ruta_wav) # Limpiar incluso si falla
            return "⚠️ No pude entender lo que dijiste en el audio."
        except sr.RequestError as e:
            os.remove(ruta_wav) # Limpiar incluso si falla
            return f"⚠️ Error con el servicio de reconocimiento de voz; {e}"
        except Exception as e:
            if os.path.exists(ruta_wav):
                os.remove(ruta_wav)
            return f"⚠️ Error inesperado al procesar el archivo WAV: {e}"