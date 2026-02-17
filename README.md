# 🏡 Orange County Lettings

[![CI](https://github.com/NZT48DEV/Projet_13_OC_Lettings/actions/workflows/ci.yml/badge.svg)](https://github.com/NZT48DEV/Projet_13_OC_Lettings/actions/workflows/ci.yml)
[![Couverture](https://img.shields.io/badge/couverture-≥80%25-brightgreen)](#)
[![Documentation](https://readthedocs.org/projects/projet-13-oc-lettings-nzt48dev/badge/?version=latest)](https://projet-13-oc-lettings-nzt48dev.readthedocs.io/en/latest/)
[![Docker Image](https://img.shields.io/docker/v/nzt48dev/oc-lettings?sort=semver)](https://hub.docker.com/r/nzt48dev/oc-lettings)
[![Docker Pulls](https://img.shields.io/docker/pulls/nzt48dev/oc-lettings)](https://hub.docker.com/r/nzt48dev/oc-lettings)

---

## 📌 Présentation

Application web Django démontrant une architecture prête pour la production, incluant :

- Architecture modulaire Django
- Intégration Continue / Déploiement Continu (CI/CD)
- Conteneurisation Docker
- Déploiement automatisé
- Gestion automatisée des dépendances
- Journalisation avancée
- Supervision via Sentry
- Documentation technique versionnée (Sphinx + Read the Docs)

Ce projet illustre un workflow d’ingénierie moderne orienté qualité, sécurité et maintenabilité.

---

## 🏗️ Architecture & Stack Technique

- **Langage** : Python 3.13
- **Framework** : Django
- **Base de données (dev)** : SQLite
- **Serveur WSGI** : Gunicorn
- **Fichiers statiques** : WhiteNoise
- **Conteneurisation** : Docker
- **CI/CD** : GitHub Actions
- **Registry** : Docker Hub
- **Déploiement** : Render
- **Monitoring** : Sentry
- **Documentation** : Sphinx + Read the Docs

---

## ⚙️ Installation (Développement local)

### Prérequis

- Python 3.13
- Pipenv
- Git

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/NZT48DEV/Projet_13_OC_Lettings
cd Projet_13_OC_Lettings
```

### 2️⃣ Installer les dépendances

```bash
pipenv install --dev
pipenv shell
```

### 3️⃣ Configurer les variables d’environnement

```bash
cp .env.example .env
```

Modifier ensuite le fichier `.env`.

Exemple minimal :

```bash
DEBUG=True
SECRET_KEY=votre_cle_secrete
ALLOWED_HOSTS=localhost,127.0.0.1
LOG_LEVEL=INFO
EVENT_LEVEL=WARNING
ENABLE_DEMO_ROUTES=true
```

### 4️⃣ Lancer l’application

```bash
python manage.py migrate
python manage.py runserver
```

Application accessible sur :

http://127.0.0.1:8000/

---

## 🔐 Panel d’administration (Accès examinateur)

Accéder à :

http://localhost:8000/admin

Identifiants :

- **Utilisateur** : `admin`
- **Mot de passe** : `Abc1234!`

---

## 🐳 Exécution via Docker

### Prérequis

- Docker
- Make
- Fichier `.env` configuré

### Lancer l’application

```bash
make docker-run
```

Cette commande :

1. Télécharge l’image Docker depuis Docker Hub
2. Lance le conteneur
3. Injecte les variables d’environnement
4. Expose le port 8000

Image utilisée :

```
nzt48dev/oc-lettings:latest
```

---

## 🔄 CI/CD & Automatisation

Le pipeline GitHub Actions exécute automatiquement :

- Linting (`pre-commit`)
- Tests unitaires et d’intégration
- Couverture minimale ≥ 80 %
- Auto-merge Dependabot (si tests OK)
- Build et push Docker sur `master`
- Déclenchement du déploiement Render

La branche `master` est protégée : aucun merge sans validation du CI.

---

## 📦 Gestion des dépendances

- Pipenv pour la gestion des dépendances
- Dependabot pour les mises à jour automatiques
- Pull Requests automatiques pour correctifs de sécurité

---

## 🛡️ Journalisation & Monitoring

### Logging

- Logs console colorés
- Fichiers persistants :
  - `django.log` (14 jours)
  - `access.log` (14 jours)
  - `errors.log` (30 jours)
- Rotation automatique quotidienne

### Sentry

- Capture des exceptions non gérées
- Environnements différenciés (dev / production)
- Paramétrage via variables d’environnement

---

## 🚀 Déploiement en production

Déclenché automatiquement lors d’un push sur `master` :

1. Validation des tests
2. Construction et push de l’image Docker
3. Appel du Deploy Hook Render
4. Mise à jour du service en production

---

## 📚 Documentation technique

Documentation complète disponible en ligne :

👉 https://projet-13-oc-lettings-nzt48dev.readthedocs.io/

Elle inclut :

- Guide d’installation
- Architecture détaillée
- Description des modèles de données
- Interfaces applicatives
- Procédures de déploiement
- Guide d’exploitation

---

## 🧪 Outils de développement

- Tests : `pytest`
- Couverture : `pytest-cov`
- Linting : `black`, `isort`, `flake8`
- Hooks Git : `pre-commit`

---

## 📄 Licence

Projet réalisé dans le cadre d’un parcours OpenClassrooms.
