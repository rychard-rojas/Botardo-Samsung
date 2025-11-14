"""
Módulo procesador.py

Define la clase base abstracta 'Procesador', utilizada como superclase
para los procesadores de texto, imagen y audio en el sistema EduMoodBot.
"""
from abc import ABC, abstractmethod
from typing import Any

class Procesador(ABC):
    def __init__(self, datos: Any = None) -> None:
        self.datos = datos

    @abstractmethod
    def procesar(self) -> Any:
        pass