# Furniture Classification Project

Le but de ce projet est d'améliorer un modèle de classification d'images pour identifier des meubles à partir d'une image fournie en entrée. Le modèle actuel permet de catégoriser les meubles et de donner des informations supplémentaires comme le nom du fournisseur et l'URL d'achat.

## Finalité

### Objectif à long terme
Nous souhaitons développer un modèle multimodal capable de prendre en entrée des images, du texte, voire de l'audio, afin de trouver le nom d'un meuble, sa catégorie et son image.

#### Fonctionnalités futures :
- **Input Texte** : Permettre de donner une description approximative d'un meuble (fournisseur, marque, couleur, etc.) et de recevoir une ou plusieurs réponses avec un pourcentage de chance pour chaque meuble.
- **Input Image** : Prendre une ou plusieurs photos (avec un téléphone) et donner la catégorie du meuble, son nom, le fournisseur et l'URL d'achat si possible.

## Ressources
### [Repositorie Model](https://huggingface.co/Lucky12345/furniture_classifier_model/tree/main)


### [Datasets](https://huggingface.co/datasets/Lucky12345/furnitures_dataset)

## Lancement rapide
Pour ceux qui ne souhaitent pas entraîner le modèle eux-mêmes, un modèle pré-entraîné est disponible sur Hugging Face. Vous pouvez le télécharger
### [Télécharger le model](https://huggingface.co/Lucky12345/furniture_classifier_model/resolve/main/furniture_classifier_model.h5?download=true)
Après téléchargement, placez le fichier `furniture_classifier_model.h5` dans le dossier `model`.

## Lancement entrainement
```sh
   cd model
   python train_model.py
```




## Lancer le projet avec Docker
Construisez l'image Docker :
   ```sh
   docker-compose build
  ```
Démarrez le conteneur :
  ```sh
  docker-compose up
  ```
L'API sera disponible à l'adresse http://localhost:80. Vous pouvez accéder à l'interface web ou utiliser les endpoints de l'API pour prédire et entraîner le modèle.
