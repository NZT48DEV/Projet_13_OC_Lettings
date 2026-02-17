# ⚙️ Installation & Configuration

Cette section décrit l'installation complète du projet **OC Lettings**
en environnement de développement local, ainsi que l'exécution via
Docker.

------------------------------------------------------------------------

# 1️⃣ Prérequis

## Environnement recommandé

-   **Python 3.13** (version utilisée en CI)
-   **Pipenv**
-   Git
-   (Optionnel) Docker
-   (Optionnel) GNU Make (pour exécuter les commandes Docker via
    Makefile)

Vérification rapide :

``` bash
python --version
pipenv --version
```

------------------------------------------------------------------------

# 2️⃣ Installation en local (Pipenv)

## Cloner le projet

``` bash
git clone https://github.com/NZT48DEV/Projet_13_OC_Lettings
cd "13 Projet - OC Lettings"
```

## Installer les dépendances

``` bash
pipenv install --dev
pipenv shell
```

Cela installe : 
- Les dépendances applicatives 
- Les dépendances de développement (lint, tests, couverture)

------------------------------------------------------------------------

# 3️⃣ Configuration des variables d'environnement

Le projet fournit un fichier `.env.example` à copier en `.env`.

``` bash
cp .env.example .env
```

## Variables obligatoires (développement)

``` bash
DEBUG=True
SECRET_KEY=votre-cle-secrete-django
ALLOWED_HOSTS=localhost,127.0.0.1
LOG_LEVEL=INFO
EVENT_LEVEL=WARNING
ENABLE_DEMO_ROUTES=true
```

### 🔐 Génération d'une SECRET_KEY sécurisée

``` bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

------------------------------------------------------------------------

## Variables Sentry (optionnelles en développement)

``` bash
SENTRY_DSN=your_sentry_dsn_here
SENTRY_ENVIRONMENT=development
SENTRY_RELEASE=oc-lettings-dev
ATTACH_STACKTRACE=true
SENTRY_TRACES_SAMPLE_RATE=0.0
SENTRY_PROFILES_SAMPLE_RATE=0.0
SEND_DEFAULT_PII=false
```

------------------------------------------------------------------------

# 4️⃣ Lancement en développement

``` bash
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

Application accessible à l'adresse :

http://127.0.0.1:8000/

------------------------------------------------------------------------

# 5️⃣ Exécution locale avec Docker (commande unique)

Le projet fournit un **Makefile** permettant d'exécuter l'application
via Docker en une seule commande.

## Prérequis

-   Docker installé et démarré
-   Fichier `.env` configuré
-   GNU Make

## Lancer l'application

``` bash
make docker-run
```

------------------------------------------------------------------------

## ⚠️ Utilisateurs Windows

La commande `make` n'est pas installée par défaut.

### Méthode 1 --- Via Chocolatey

``` bash
choco install make
```

Redémarrer ensuite le terminal puis vérifier :

``` bash
make --version
```

### Méthode 2 --- Via WSL (recommandé)

Installer WSL puis :

``` bash
sudo apt install make
```

------------------------------------------------------------------------

# Résumé des modes d'exécution

| Mode | Commande | Usage |
|------|----------|-------|
| Développement classique | `pipenv shell` + `python manage.py runserver` | Debug & développement |
| Docker local | `make docker-run` | Test environnement conteneurisé |


------------------------------------------------------------------------

# Dépannage rapide

-   Vérifier que `.env` est présent
-   Vérifier la version Python (3.13 recommandée)
-   Supprimer l'environnement Pipenv si nécessaire :

``` bash
pipenv --rm
pipenv install --dev
```

------------------------------------------------------------------------

Cette procédure garantit un environnement de développement reproductible
et cohérent avec la configuration CI/CD du projet.
