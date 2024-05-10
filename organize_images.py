import os
import shutil
import pandas as pd

# Charger le fichier CSV
csv_path = 'furniture_category_image.csv'
furniture_data = pd.read_csv(csv_path)

# Dossier racine des images
root_folder = 'furnitures'

# Créer les dossiers basés sur les noms des catégories
for _, row in furniture_data.iterrows():
    category = row['category_name'].split('/')[0].strip()  # Prendre le premier sous-groupe seulement
    image_name = row['image']

    # Créer le dossier de catégorie s'il n'existe pas
    category_path = os.path.join(root_folder, category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

    # Déplacer les images dans le dossier de catégorie
    src_path = os.path.join(root_folder, image_name)
    dst_path = os.path.join(category_path, image_name)
    if os.path.exists(src_path):
        shutil.move(src_path, dst_path)
    else:
        print(f"Image non trouvée : {src_path}")
