"""
Módulo procesador_texto.py

Implementa la clase 'ProcesadorTexto', encargada de la limpieza
y normalización de texto para el análisis emocional.
"""
import re
from typing import Union
from procesadores.procesador_base import Procesador
class ProcesadorTexto(Procesador):
    """Procesa y limpia una cadena de texto."""

    def __init__(self, datos: str) -> None:
        """Inicializa el procesador con el texto de entrada."""
        super().__init__(datos)

    def procesar(self) -> str:
        """
        Ejecuta el pipeline de procesamiento de texto.

        Returns:
            El texto limpio y normalizado, o un mensaje de error.
        """
        if not isinstance(self.datos, str):
            return "⚠️ Texto inválido para procesar."
        
        texto_limpio = self._limpiar_texto(self.datos)
        return texto_limpio

    def _limpiar_texto(self, texto: str) -> str:
        """
        Realiza la limpieza: elimina caracteres no alfabéticos,
        normaliza espacios y convierte a minúsculas.
        """
        # Elimina todo lo que no sea letra o espacio
        texto_limpio = re.sub(r"[^a-zA-ZáéíóúÁÉÍÓÚñÑ\s]", "", texto)
        # Reemplaza múltiples espacios por uno solo y elimina espacios al inicio/final
        texto_limpio = re.sub(r"\s+", " ", texto_limpio).strip().lower()
        return texto_limpio