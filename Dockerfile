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

# 8) Collectstatic (on fournit un SECRET_KEY dummy sans le stocker dans l'image)
RUN SECRET_KEY=dummy python manage.py collectstatic --noinput

# 9) Exposer le port (info)
EXPOSE 8000

# 10) Démarrer le serveur WSGI
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]
