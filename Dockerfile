# 1) Base image (légère)
FROM python:3.13-slim

# 2) Variables Python: pas de .pyc, logs immédiats
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3) Dossier de travail
WORKDIR /app

# 4) Installer pipenv
RUN pip install --no-cache-dir pipenv

# 5) Copier les fichiers de dépendances d'abord (cache)
COPY Pipfile Pipfile.lock /app/

# 6) Installer les dépendances "runtime" dans l'environnement système du conteneur
RUN pipenv install --system --deploy

# 7) Copier le code
COPY . /app/

# Variables uniquement pour la phase de build (collectstatic a besoin des settings)
ARG SECRET_KEY=build-only-secret-key
ENV SECRET_KEY=${SECRET_KEY}

# 8 ) Gestion des fichiers statiques pour être servis par Whitenoise
RUN python manage.py collectstatic --noinput

# 8) Exposer le port (info)
EXPOSE 8000

# 9) Démarrer le serveur WSGI
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
