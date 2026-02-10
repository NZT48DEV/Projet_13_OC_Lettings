# Orange County Lettings

Application web Django permettant de gérer des locations immobilières et des profils utilisateurs.

---

## ⚙️ Installation (développement local)

### Prérequis
- Python 3.10 ou supérieur
- Pipenv

### Mise en place

Cloner le dépôt puis installer les dépendances :

```bash
pipenv install
pipenv shell
```

---

## 🔐 Configuration des variables d’environnement

Avant de lancer l’application, certaines variables d’environnement doivent être définies.  
Elles sont regroupées dans un fichier `.env` à la racine du projet et **ne doivent jamais être versionnées**.

### Variables obligatoires

```env
DEBUG=False
SECRET_KEY=votre-cle-secrete-django
ALLOWED_HOSTS=localhost,127.0.0.1
LOG_LEVEL=INFO
EVENT_LEVEL=WARNING
```

#### Détail des variables

- **DEBUG**  
  Active ou désactive le mode debug de Django.  
  ⚠️ Doit impérativement être à `False` en production.

- **SECRET_KEY**  
  Clé secrète utilisée par Django pour la sécurité (sessions, tokens, hashage).  
  Elle doit rester strictement confidentielle.

- **ALLOWED_HOSTS**  
  Liste des hôtes autorisés à accéder à l’application, séparés par des virgules.

- **LOG_LEVEL**  
  Niveau minimum de logs affichés par l’application.

- **EVENT_LEVEL**  
  Niveau minimum des événements envoyés à Sentry.

---

### Génération de la clé secrète Django

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### Variables Sentry (optionnelles)

```env
SENTRY_DSN=your_sentry_dsn_here
SENTRY_ENVIRONMENT=development
SENTRY_RELEASE=oc-lettings-1.0.0
SENTRY_TRACES_SAMPLE_RATE=0.0
SENTRY_PROFILES_SAMPLE_RATE=0.0
SEND_DEFAULT_PII=false
```

---

## ▶️ Utilisation (développement)

```bash
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

Application accessible sur :

```
http://127.0.0.1:8000/
```

---

## 🐳 Exécution locale avec Docker (commande unique)

L’application peut être exécutée **uniquement avec Docker**, sans installer Python ou Pipenv localement.

### Prérequis
- Docker installé et fonctionnel
- Un fichier `.env` configuré à la racine du projet
- `make` disponible (Git Bash / WSL / Linux / macOS)

### Commande unique

```bash
make docker-run
```

Cette commande :
1. télécharge l’image depuis Docker Hub,
2. lance le conteneur,
3. injecte les variables d’environnement depuis `.env`,
4. expose l’application sur le port `8000`.

Par défaut, l’image utilisée est :

```
nzt48dev/oc-lettings:latest
```

### Lancer une version précise (tag commit)

```bash
make docker-run TAG=<commit-sha>
```

### Variante debug (sans `--rm`)

```bash
make docker-run-debug
```

---

## 🔁 Intégration Continue (CI)

Un pipeline CI/CD est mis en place via **GitHub Actions**.

### Étapes exécutées automatiquement

À chaque **push** ou **pull request** :
- installation de l’environnement via Pipenv,
- linting (`pre-commit`),
- exécution des tests unitaires et d’intégration,
- vérification d’une couverture de tests ≥ **80 %**.

Les secrets sensibles (`SECRET_KEY`, credentials Docker Hub) sont gérés via **GitHub Secrets**.

---

## 📦 Conteneurisation et publication Docker

Lorsqu’un commit est poussé sur la branche `master` :

1. les tests doivent réussir,
2. l’image Docker est construite,
3. l’image est poussée sur Docker Hub avec deux tags :
   - `latest`
   - le hash du commit Git.

Aucune conteneurisation ni publication n’est effectuée sur les autres branches.

---

## 🚀 Déploiement

### Fonctionnement (vue d’ensemble)

Le déploiement s’appuie sur :
- GitHub Actions pour l’automatisation,
- Docker pour la portabilité de l’application,
- Docker Hub comme registre d’images.

Le déploiement en production repose **strictement** sur l’image Docker validée par la CI.

---

### Configuration requise

Pour qu’un déploiement fonctionne correctement, il faut :
- une image Docker disponible sur Docker Hub,
- un fichier `.env` configuré avec les variables de production,
- un environnement capable d’exécuter Docker (Render, VM, cloud provider).

---

### Étapes de déploiement

1. Récupérer l’image Docker depuis le registre :
   ```bash
   docker pull nzt48dev/oc-lettings:latest
   ```

2. Lancer l’application :
   ```bash
   docker run -d      -p 8000:8000      --env-file .env      nzt48dev/oc-lettings:latest
   ```

3. Vérifier :
   - accès au site public,
   - chargement correct des fichiers statiques,
   - interface `/admin` fonctionnelle

---

## 🛡️ Surveillance des erreurs et journalisation

### Sentry
- capture automatique des exceptions non gérées,
- remontée des erreurs critiques,
- environnement et version associés aux événements.

### Logging
- logs colorés en console (si disponible),
- logs persistants dans `logs/`,
- rotation quotidienne automatique :
  - `django.log` : 14 jours
  - `access.log` : 14 jours
  - `errors.log` : 30 jours

---

## 🧪 Outils de développement

- Django Admin : `/admin`
- Tests : `pytest`
- Couverture : `pytest-cov`
- Linting : `black`, `isort`, `flake8`, `pre-commit`

---

## 🔐 Sécurité et bonnes pratiques

- aucune donnée sensible versionnée,
- secrets gérés via variables d’environnement,
- fichiers statiques servis via WhiteNoise,
- déploiement basé sur une image Docker validée par la CI.
