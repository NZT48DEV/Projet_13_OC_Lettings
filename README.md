# 🏡 Orange County Lettings

[![CI](https://github.com/NZT48DEV/Projet_13_OC_Lettings/actions/workflows/ci.yml/badge.svg)](https://github.com/NZT48DEV/Projet_13_OC_Lettings/actions/workflows/ci.yml)
[![Couverture](https://img.shields.io/badge/couverture-≥80%25-brightgreen)](#)
[![Documentation](https://readthedocs.org/projects/projet-13-oc-lettings-nzt48dev/badge/?version=latest)](https://projet-13-oc-lettings-nzt48dev.readthedocs.io/fr/latest/)
[![Docker Image](https://img.shields.io/docker/v/nzt48dev/oc-lettings?sort=semver)](https://hub.docker.com/r/nzt48dev/oc-lettings)
[![Docker Pulls](https://img.shields.io/docker/pulls/nzt48dev/oc-lettings)](https://hub.docker.com/r/nzt48dev/oc-lettings)

------------------------------------------------------------------------

## 📌 Présentation

Application web Django démontrant une architecture prête pour la
production avec :

-   Architecture modulaire Django
-   CI/CD automatisé (GitHub Actions)
-   Gestion automatisée des dépendances
-   Conteneurisation Docker
-   Déploiement automatique (Render)
-   Monitoring via Sentry
-   Documentation technique versionnée (Sphinx + Read the Docs)

------------------------------------------------------------------------

## 🌍 Application en production

L'application est déployée et accessible en ligne :

👉 https://oc-lettings-p2wk.onrender.com/


------------------------------------------------------------------------

## 📚 Documentation complète

La documentation détaillée (installation, architecture, déploiement,
logging, monitoring, CI/CD) est disponible sur Read the Docs :

👉 https://projet-13-oc-lettings-nzt48dev.readthedocs.io/fr/latest/


------------------------------------------------------------------------

## 🚀 Lancement rapide (développement)

``` bash
git clone https://github.com/NZT48DEV/Projet_13_OC_Lettings
cd Projet_13_OC_Lettings
pipenv install --dev
pipenv shell
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

Application accessible sur :\
http://127.0.0.1:8000/

------------------------------------------------------------------------

## 🐳 Exécution via Docker

``` bash
make docker-run
```

Image utilisée :

    nzt48dev/oc-lettings:latest

------------------------------------------------------------------------

## 🔐 Administration (démo pédagogique)

Accès : `/admin/`

Identifiants fournis avec la base de démonstration :

-   **Username** : `admin`
-   **Password** : `Abc1234!`

⚠️ Compte fourni uniquement à des fins pédagogiques.

------------------------------------------------------------------------

## 📄 Licence

Projet réalisé dans le cadre du parcours OpenClassrooms.