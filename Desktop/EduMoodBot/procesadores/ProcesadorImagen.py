# procesadores/ProcesadorImagen.py
from transformers import pipeline
from procesadores.procesador_base import Procesador

class ProcesadorImagen(Procesador):
    def __init__(self, datos: str) -> None:
        """
        Inicializa el procesador de imagen.
        
        Args:
            datos: La ruta al archivo de imagen.
        """
        super().__init__(datos)
        try:
            # Usamos un modelo pre-entrenado para clasificación de imágenes.
            # Este modelo identifica objetos, no emociones directamente, pero sirve como ejemplo funcional.
            print("Cargando modelo de clasificación de imágenes...")
            self.clasificador = pipeline("image-classification", model="google/vit-base-patch16-224")
            print("Modelo de imagen cargado. ✅")
        except Exception as e:
            print(f"Error al cargar el modelo de imagen: {e} ❌")
            self.clasificador = None

    def procesar(self) -> dict:
        """
        Clasifica el contenido de una imagen y devuelve los resultados.
        """
        if not self.clasificador:
            return {"error": "El modelo de análisis de imagen no está disponible."}
        
        if not isinstance(self.datos, str):
            return {"error": "⚠️ Ruta de imagen inválida."}
        
        try:
            # El clasificador devuelve una lista de diccionarios con 'label' y 'score'
            predicciones = self.clasificador(self.datos)
            # Formateamos el resultado para que sea más legible
            resultado = {
                "descripcion_probable": predicciones[0]['label'],
                "confianza": f"{predicciones[0]['score']:.2%}",
                "contenido_detectado": [f"{p['label']} ({p['score']:.1%})" for p in predicciones[:3]]
            }
            return resultado
        except Exception as e:
            return {"error": f"⚠️ No se pudo procesar la imagen: {e}"}