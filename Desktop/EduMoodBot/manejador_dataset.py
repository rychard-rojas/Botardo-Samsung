# manejador_dataset.py
import json
from thefuzz import process
from typing import List, Dict, Optional

class ManejadorDataset:
    def __init__(self, ruta_archivo: str):
        """
        Inicializa el manejador cargando los datos desde un archivo JSON.
        """
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                self.datos: List[Dict[str, str]] = json.load(f)
            # Extraemos solo las preguntas para la búsqueda
            self.preguntas: List[str] = [item['pregunta'] for item in self.datos]
            print("Dataset cargado correctamente. ✅")
        except Exception as e:
            self.datos = []
            self.preguntas = []
            print(f"Error al cargar el dataset: {e} ❌")

    def encontrar_respuesta(self, consulta_usuario: str, umbral: int = 75) -> Optional[str]:
        """
        Busca la pregunta más similar en el dataset y devuelve su respuesta
        si la similitud supera un umbral.

        Args:
            consulta_usuario: La pregunta del usuario.
            umbral: El porcentaje de similitud mínimo (0-100) para considerar una coincidencia.

        Returns:
            La respuesta correspondiente o None si no hay una buena coincidencia.
        """
        if not self.preguntas:
            return None

        # process.extractOne devuelve una tupla: (pregunta_encontrada, similitud)
        mejor_coincidencia = process.extractOne(consulta_usuario, self.preguntas)
        
        if mejor_coincidencia and mejor_coincidencia[1] >= umbral:
            pregunta_coincidente = mejor_coincidencia[0]
            # Buscamos la respuesta correspondiente a la pregunta encontrada
            for item in self.datos:
                if item['pregunta'] == pregunta_coincidente:
                    return item['respuesta']
        
        return None