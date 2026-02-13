# Orange County Lettings

![Django](https://img.shields.io/badge/Django-4.x-092E20)
![Docker Image](https://img.shields.io/badge/docker%20hub-nzt48dev%2Foc--lettings-blue)
![Render](https://img.shields.io/badge/deployed%20on-Render-46E3B7)
[![CI](https://github.com/NZT48DEV/Projet_13_OC_Lettings/actions/workflows/ci.yml/badge.svg)](https://github.com/NZT48DEV/Projet_13_OC_Lettings/actions/workflows/ci.yml)


Application web Django permettant de gérer des locations immobilières et
des profils utilisateurs.

------------------------------------------------------------------------

# 🏗️ Architecture & Stack Technique

-   **Backend** : Django
-   **Base de données** : SQLite (développement)
-   **Serveur WSGI** : Gunicorn
-   **Fichiers statiques** : WhiteNoise
-   **Conteneurisation** : Docker
-   **CI/CD** : GitHub Actions
-   **Registry** : Docker Hub
-   **Production** : Render
-   **Monitoring** : Sentry

------------------------------------------------------------------------

# ⚙️ Installation (Développement Local)

## Prérequis

-   Python 3.10+
-   Pipenv

## Installation

``` bash
git clone https://github.com/NZT48DEV/Projet_13_OC_Lettings
pipenv install
pipenv shell
```

------------------------------------------------------------------------

# 🔐 Configuration des variables d'environnement

Les variables doivent être définies dans un fichier `.env` à la racine
du projet (non versionné).\
Un fichier `.env.example` est fourni comme modèle de configuration.

## Variables obligatoires (développement)

``` env
DEBUG=True
SECRET_KEY=votre-cle-secrete-django
ALLOWED_HOSTS=localhost,127.0.0.1
LOG_LEVEL=INFO
EVENT_LEVEL=WARNING
ENABLE_DEMO_ROUTES=true
```

### Génération d'une SECRET_KEY sécurisée

``` bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

------------------------------------------------------------------------

## Variables Sentry (optionnelles en développement)

``` env
SENTRY_DSN=your_sentry_dsn_here
SENTRY_ENVIRONMENT=development
SENTRY_RELEASE=oc-lettings-dev
ATTACH_STACKTRACE=true
SENTRY_TRACES_SAMPLE_RATE=0.0
SENTRY_PROFILES_SAMPLE_RATE=0.0
SEND_DEFAULT_PII=false
```

------------------------------------------------------------------------

# ▶️ Lancement en développement

``` bash
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

Application accessible sur :

http://127.0.0.1:8000/

------------------------------------------------------------------------

# 🐳 Exécution locale avec Docker (commande unique)

## Prérequis

-   Docker
-   Make
-   Fichier `.env` configuré

### ⚠️ Utilisateurs Windows

La commande `make` n'est pas installée par défaut sur Windows.

Si vous utilisez Git Bash ou PowerShell, vous devez installer **GNU Make**.

Méthode recommandée via Chocolatey :

```bash
choco install make
```

Redémarrer ensuite le terminal puis vérifier :

```bash
make --version
```

Alternative recommandée : utiliser **WSL (Windows Subsystem for Linux)** et installer make via :

```bash
sudo apt install make
```

------------------------------------------------------------------------

## Lancer l'application

``` bash
make docker-run
```

Cette commande : 
1. Télécharge l'image Docker depuis Docker Hub 
2. Lance le conteneur 
3. Injecte les variables d'environnement 
4. Expose le port 8000

Image utilisée :

    nzt48dev/oc-lettings:latest

Version spécifique :

``` bash
make docker-run TAG=<commit-sha>
```

------------------------------------------------------------------------

# 🔁 Intégration Continue (CI)

Sur **toutes les branches et Pull Requests** :

-   Installation de l'environnement
-   Linting (`pre-commit`)
-   Tests unitaires et d'intégration
-   Couverture minimale ≥ 80 %

------------------------------------------------------------------------

# 📦 Conteneurisation

Uniquement lors d'un **push sur la branche `master`** :

1.  Les tests doivent réussir
2.  L'image Docker est construite
3.  L'image est poussée sur Docker Hub avec :
    -   `latest`
    -   `<commit-sha>`

Aucune conteneurisation n'est effectuée sur les autres branches.

------------------------------------------------------------------------

# 🚀 Déploiement en Production (Render)

## 🔄 Fonctionnement global

Branches ≠ master : → Tests uniquement

Push sur master : → Tests\
→ Build & Push Docker\
→ Déploiement automatique via Render Deploy Hook

Chaque étape dépend strictement de la réussite de la précédente.

------------------------------------------------------------------------

## ⚙️ Configuration requise

### 1️⃣ Secrets GitHub Actions

Repository → Settings → Secrets and variables → Actions

-   DOCKERHUB_USERNAME
-   DOCKERHUB_TOKEN
-   RENDER_DEPLOY_HOOK_URL
-   SECRET_KEY

------------------------------------------------------------------------

### 2️⃣ Configuration Render

Créer un Web Service basé sur une image Docker existante.

Image :

    nzt48dev/oc-lettings:latest

Port :

    8000

### Variables d'environnement (production)

``` env
SECRET_KEY=<clé secrète de production>
DEBUG=False
ALLOWED_HOSTS=<service>.onrender.com
CSRF_TRUSTED_ORIGINS=https://<service>.onrender.com
SENTRY_DSN=<dsn-production>
SENTRY_ENVIRONMENT=production
ENABLE_DEMO_ROUTES=false
```

------------------------------------------------------------------------

## 🔁 Procédure complète de déploiement

1.  Créer une Pull Request
2.  Merger sur `master`
3.  Le pipeline exécute automatiquement :
    -   Tests
    -   Build & push Docker
    -   Déclenchement du Deploy Hook Render
4.  Vérifier :
    -   Page publique (CSS/images)
    -   Interface `/admin`
    -   Chargement correct des staticfiles
    -   Monitoring Sentry actif

------------------------------------------------------------------------

# 🎭 Routes de démonstration (Soutenance)

Certaines routes sont disponibles uniquement pour démonstration :

-   `/test-404`
-   `/test-500`
-   `/sentry-debug`

Ces routes : 
- Sont accessibles uniquement aux utilisateurs staff 
- Sont activables via la variable `ENABLE_DEMO_ROUTES=true` 
- Permettent de démontrer : 
    - Les pages personnalisées 404 / 500 
    - La remontée d'erreurs vers Sentry

En production normale, `ENABLE_DEMO_ROUTES` doit être `false`.

------------------------------------------------------------------------

# 🛡️ Logs & Monitoring

## Logging

-   Logs console colorés
-   Logs persistants dans `logs/`
-   Rotation automatique :
    -   django.log → 14 jours
    -   access.log → 14 jours
    -   errors.log → 30 jours

## Sentry

-   Capture automatique des exceptions non gérées
-   Association environnement + release
-   Monitoring actif en production

------------------------------------------------------------------------

# 🔐 Sécurité

-   Aucun secret versionné
-   `.env` non versionné
-   DEBUG=False en production
-   WhiteNoise pour servir les fichiers statiques
-   Déploiement basé uniquement sur image Docker validée par la CI
-   Routes de démonstration désactivables via variable d'environnement

------------------------------------------------------------------------

# 🧪 Outils

-   Django Admin : `/admin`
-   Tests : `pytest`
-   Couverture : `pytest-cov`
-   Linting : `black`, `isort`, `flake8`, `pre-commit`
