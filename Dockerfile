# 1) Base image (légère)
FROM python:3.13-slim

# 2) Injecte le SHA du commit (via la CI) pour l’exposer à Sentry
ARG APP_RELEASE=unknown
ENV SENTRY_RELEASE=$APP_RELEASE

# 3) Variables Python: pas de .pyc, logs immédiats
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 4) Dossier de travail
WORKDIR /app

# 5) Installer pipenv
RUN pip install --no-cache-dir pipenv

# 6) Copier les fichiers de dépendances d'abord (cache)
COPY Pipfile Pipfile.lock /app/

# 7) Installer les dépendances "runtime" dans l'environnement système du conteneur
RUN pipenv install --system --deploy

# 8) Copier le code
COPY . /app/

# 9) Collectstatic (on fournit un SECRET_KEY dummy sans le stocker dans l'image)
RUN SECRET_KEY=dummy python manage.py collectstatic --noinput

# 10) Exposer le port (info)
EXPOSE 8000

# 11) Démarrer le serveur WSGI
CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000", "--worker-class", "gthread", "--workers", "2", "--threads", "4", "--timeout", "120", "--keep-alive", "5"]