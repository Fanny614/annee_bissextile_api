# Image de base du conteneur
FROM python:3.12.7

LABEL authors="fanny-tutenuit"
# Définit le répertoire de travail
WORKDIR /app
# Installe poetry en local pour l'utilisateur
RUN pip install --no-cache-dir poetry==1.8.4
# Copie les fichiers poetry dans le workdir
COPY poetry.lock pyproject.toml /app/
# Installe le fichier poetry - Installe les dépedanses
RUN poetry install --no-root
# Copie l'intégralité du code du projet
COPY . /app/
# Spécifie quel port il faut utiliser
EXPOSE 8005
# Défini les variable d'environnement
ENV PYTHONUNBUFFERED=1
# Commande qui exécute le programme
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8005"]