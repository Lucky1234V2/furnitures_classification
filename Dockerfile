# Utiliser une image Python officielle
FROM python:3.9

# Créer un répertoire pour l'application
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .
COPY main.py .
COPY furniture_classifier_model.h5 .
COPY index.html .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 80
EXPOSE 80

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
