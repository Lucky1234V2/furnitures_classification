# Utiliser une image Python officielle
FROM python:3.9

# Créer un répertoire pour l'application
WORKDIR /app

COPY ./app /app
COPY ./model /model
COPY ./requirements.txt /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port 80
EXPOSE 80

# Commande pour démarrer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
