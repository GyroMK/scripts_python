import tensorflow as tf
from PIL import Image
import numpy as np
import requests
from io import BytesIO

MODEL_PATH = "deepbooru_model.h5"

class DeepbooruTagger:
    def __init__(self):
        self.model = tf.keras.models.load_model(MODEL_PATH)

    def get_tags(self, image_url):
        """Descarga la imagen, la procesa y obtiene tags con Deepbooru."""
        response = requests.get(image_url)
        if response.status_code != 200:
            return []

        img = Image.open(BytesIO(response.content)).resize((299, 299))
        img_array = np.array(img) / 255.0
        img_array = img_array.reshape((1, 299, 299, 3))

        predictions = self.model.predict(img_array)[0]
        tags = [f"tag_{i}" for i, p in enumerate(predictions) if p > 0.5]  # Simulación de tags

        return tags
