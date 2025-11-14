# manejador_dataset.py
import json
from sentence_transformers import SentenceTransformer, util
import torch
from typing import List, Dict, Optional

class ManejadorDataset:
    def __init__(self, ruta_archivo: str):
        """
        Inicializa el manejador, carga los datos y pre-calcula los embeddings
        de las preguntas del dataset para una búsqueda semántica eficiente.
        """
        try:
            # Usamos un modelo multilingüe ligero y potente.
            print("Cargando modelo de embeddings semánticos...")
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
            print("Modelo de embeddings cargado. ✅")
            
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                self.datos: List[Dict[str, str]] = json.load(f)
            
            self.preguntas: List[str] = [item['pregunta'] for item in self.datos]
            
            # Pre-calcular los embeddings del dataset (¡esto es clave para la eficiencia!)
            print("Pre-calculando embeddings del dataset...")
            self.embeddings_dataset = self.model.encode(self.preguntas, convert_to_tensor=True)
            print("Embeddings calculados y listos. ✅")

        except Exception as e:
            self.datos = []
            self.preguntas = []
            self.embeddings_dataset = None
            print(f"Error crítico durante la inicialización del ManejadorDataset: {e} ❌")

    def encontrar_respuesta(self, consulta_usuario: str, umbral: float = 0.70) -> Optional[str]:
        """
        Busca la pregunta más similar semánticamente usando embeddings y similitud de coseno.

        Args:
            consulta_usuario: La pregunta del usuario.
            umbral: El score de similitud mínimo (0.0 a 1.0) para una coincidencia.

        Returns:
            La respuesta correspondiente o None.
        """
        if self.embeddings_dataset is None:
            return None

        # 1. Codificar la pregunta del usuario en un embedding
        embedding_usuario = self.model.encode(consulta_usuario, convert_to_tensor=True)

        # 2. Calcular la similitud de coseno entre el embedding del usuario y todos los del dataset
        # util.cos_sim nos devuelve una matriz de scores
        scores_coseno = util.cos_sim(embedding_usuario, self.embeddings_dataset)[0]

        # 3. Encontrar el score más alto y su índice
        mejor_score, mejor_indice = torch.max(scores_coseno, dim=0)

        # 4. Si el mejor score supera nuestro umbral, encontramos una coincidencia
        if mejor_score.item() > umbral:
            # Usamos el índice para encontrar la pregunta y respuesta originales
            pregunta_coincidente = self.preguntas[mejor_indice]
            for item in self.datos:
                if item['pregunta'] == pregunta_coincidente:
                    return item['respuesta']
        
        return None