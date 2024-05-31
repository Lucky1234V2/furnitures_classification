from fastapi import FastAPI, UploadFile, File, Form
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from fastapi.responses import HTMLResponse
import io

# Charger le modèle
model = tf.keras.models.load_model('model/furniture_classifier_model.h5')

# Créer un dictionnaire des classes basé sur les dossiers
class_indices = {
    'Accessoire': 0,
    'Assise': 1,
    'Cuisine': 3,
    'Canapé': 2,
    'Déco': 4,
    'Électricité': 5,
    'Électroménager': 6,
    'Extérieur': 7,
    'Literie': 8,
    'Luminiare': 9,
    'Ménage': 10,
    'Rangement': 11,
    'Rideau': 12,
    'SdB': 13,
    'Table': 14,
    'Tapis': 15
}
index_to_class = {v: k for k, v in class_indices.items()}
num_classes = len(class_indices)

# Initialiser l'application FastAPI
app = FastAPI()


@app.get("/")
async def read_index():
    with open("app/statics/index.html", "r") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)


# Route de prédiction
@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    try:
        img = image.load_img(io.BytesIO(contents), target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        predictions = model.predict(img_array)
        predicted_class = index_to_class[np.argmax(predictions[0])]
    except Exception as e:
        return {'error': str(e)}

    return {'prediction': predicted_class}


# Route d'entraînement
@app.post('/train')
async def train(file: UploadFile = File(...), category: str = Form(...)):
    if category not in class_indices:
        return {'error': 'Invalid category'}

    category_index = class_indices[category]
    contents = await file.read()

    try:
        # Charger et prétraiter l'image
        img = image.load_img(io.BytesIO(contents), target_size=(224, 224))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # Créer les labels pour la catégorie
        labels = np.zeros((1, num_classes))
        labels[0, category_index] = 1

        # Recompiler le modèle
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        # Réentraînement
        model.fit(img_array, labels, epochs=1, verbose=0)
        model.save('model/furniture_classifier_model.h5')
        return {'status': 'Model trained successfully'}
    except Exception as e:
        return {'error': str(e)}
