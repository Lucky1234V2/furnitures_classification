import tensorflow as tf
from datasets import load_dataset

# Configuration des paramètres du modèle
batch_size = 16
img_height = 224
img_width = 224
epochs = 10

# Définir les indices des classes
class_indices = {
    'Accessoire': 0, 'Assise': 1, 'Canapé': 2, 'Cuisine': 3,
    'Déco': 4, 'Électricité': 5, 'Électroménager': 6, 'Extérieur': 7,
    'Literie': 8, 'Luminiare': 9, 'Ménage': 10, 'Rangement': 11,
    'Rideau': 12, 'SdB': 13, 'Table': 14, 'Tapis': 15
}

# Chargement du dataset
dataset = load_dataset("Lucky12345/furnitures_dataset")
train_data = dataset['train']


# Fonction de prétraitement des données
def preprocess(features):
    # S'assurer que l'image a trois canaux
    image = tf.keras.preprocessing.image.img_to_array(features['image'].convert('RGB'))
    image = tf.image.resize(image, [img_height, img_width])
    image /= 255.0
    label = tf.one_hot(features['label'], depth=len(class_indices))
    return image, label


# Conversion en TensorFlow Dataset
train_dataset = tf.data.Dataset.from_generator(
    lambda: map(preprocess, train_data),
    output_signature=(
        tf.TensorSpec(shape=(img_height, img_width, 3), dtype=tf.float32),
        tf.TensorSpec(shape=(len(class_indices),), dtype=tf.float32))
)

# Application des méthodes TensorFlow
train_dataset = train_dataset.batch(batch_size).shuffle(1024).prefetch(tf.data.experimental.AUTOTUNE)

# Définition de l'architecture du modèle CNN
model = tf.keras.models.Sequential([
    tf.keras.layers.InputLayer(input_shape=(img_height, img_width, 3)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(256, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(len(class_indices), activation='softmax')
])

# Compilation du modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entraînement du modèle
model.fit(train_dataset, epochs=epochs)

# Sauvegarde du modèle entraîné
model.save('furniture_classifier_model.h5')
