import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

img_size = 150
CLASSES = ["David Martinez", "Rebbeca", "Lucy"]

model = load_model("mood_model.h5")

def getclass(image_path: str):
    try:
        img = Image.open(image_path).convert("RGB")
        img = img.resize((img_size, img_size)) # Corrected variable name from IMG_SIZE to img_size
        arr = np.expand_dims(np.asarray(img) / 255.0, axis=0)


        if isinstance(model.input_shape, list) and len(model.input_shape) == 2: # Corrected 'imput_shape' to 'input_shape'
            preds = model.predict([arr, arr], verbose=0)[0]
        else:
            preds = model.predict(arr, verbose=0)[0]

        idx = np.argmax(preds)
        clase = CLASSES[idx]
        conf = preds[idx]

        return f"prediccion: {clase} ({conf*100:.1f}%)" # Corrected f-string formatting

    except Exception as e:
        return f"error en prediccion: {str(e)}"