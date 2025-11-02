"""
Módulo procesador_texto.py

Implementa la clase 'ProcesadorTexto', encargada de la limpieza
y normalización de texto para el análisis emocional en EduMoodBot.
"""
import re
from procesadores.procesador import Procesador

class ProcesadorTexto(Procesador):
    def __init__(self, datos: str) -> None:
        self.datos = datos

    def procesar(self) -> str:
        if not isinstance(self.datos, str):
            return "⚠️ Texto inválido para procesar."
        texto_limpio = self.procesar_texto(self.datos)
        self.datos = texto_limpio
        return texto_limpio

    def procesar_texto(self, texto: str) -> str:
        texto_limpio = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", "", texto)
        texto_limpio = re.sub(r"\s+", " ", texto_limpio).strip().lower()
        return texto_limpio