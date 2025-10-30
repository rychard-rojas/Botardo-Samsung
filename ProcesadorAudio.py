# ProcesadorAudio.py
import numpy as np
import librosa
from procesador import Procesador

class ProcesadorAudio(Procesador):
    def procesar(self):
        return self.procesar_audio(self.datos)

    def procesar_audio(self, archivo_audio: str):
        try:
            y, sr = librosa.load(archivo_audio)
            return self.analizar_tono_voz(y, sr)
        except Exception as e:
            print(f"Error al procesar audio: {e}")
            return None

    def analizar_tono_voz(self, y, sr):
        pitch = librosa.pitch_tuning(librosa.yin(y, sr=sr))
        energy = np.mean(librosa.feature.rms(y=y))
        return {
            "emocion_detectada": "tristeza",
            "tono": float(pitch),
            "intensidad": float(energy)
        }