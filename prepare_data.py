import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Configuration
batch_size = 32
img_height = 224
img_width = 224
data_dir = 'furnitures'

# Préparation des données
datagen = ImageDataGenerator(
    rescale=1./255,  # Normalisation
    validation_split=0.2  # Fraction de validation
)

# Chargement des données d'entraînement
train_data = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    subset='training',
    class_mode='categorical'
)

# Chargement des données de validation
val_data = datagen.flow_from_directory(
    data_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    subset='validation',
    class_mode='categorical'
)
