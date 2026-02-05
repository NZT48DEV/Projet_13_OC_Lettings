# Orange County Lettings

Application web Django permettant de gérer des locations immobilières et des profils utilisateurs.

---

## ⚙️ Installation

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
```

La clé secrète Django peut être générée avec la commande suivante :

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Variables Sentry (optionnelles mais recommandées)

```env
SENTRY_DSN=your_sentry_dsn_here
SENTRY_ENVIRONMENT=development
SENTRY_RELEASE=oc-lettings-1.0.0
EVENT_LEVEL=ERROR
SEND_DEFAULT_PII=false
SENTRY_TRACES_SAMPLE_RATE=0.0
SENTRY_PROFILES_SAMPLE_RATE=0.0
```

- `SENTRY_DSN` : identifiant du projet Sentry.
- `EVENT_LEVEL` : niveau minimum des logs envoyés à Sentry (`ERROR` recommandé).
- Les autres variables permettent d’affiner le comportement de Sentry (environnement, performances, respect des données personnelles).

---

## ▶️ Utilisation

Appliquer les migrations de la base de données :

```bash
python manage.py migrate
```

Collecter les fichiers statiques :

```bash
python manage.py collectstatic
```

Lancer le serveur de développement :

```bash
python manage.py runserver
```

L’application sera accessible à l’adresse :

```
http://127.0.0.1:8000/
```

---

## 🛡️ Surveillance des erreurs et journalisation

### Surveillance des erreurs avec Sentry

L’application intègre **Sentry** afin d’assurer la surveillance des erreurs et événements applicatifs.

Fonctionnalités principales :
- capture automatique des exceptions non gérées (erreurs 500),
- centralisation des erreurs dans l’interface Sentry,
- enrichissement des événements avec des données contextuelles.

Les exceptions non gérées sont automatiquement envoyées à Sentry.
Les logs de niveau **ERROR** et **CRITICAL** sont également remontés via l’intégration avec le module `logging`.

---

### Journalisation (Logging)

Un système de journalisation est mis en place à l’aide du module standard `logging`.

Caractéristiques :
- un logger par module (`logging.getLogger(__name__)`),
- logs horodatés et colorés en console selon le niveau :
  - INFO : vert
  - WARNING : jaune
  - ERROR / CRITICAL : rouge
- filtrage des logs Django trop verbeux (404, sessions).

Les logs sont principalement placés dans :
- les vues (accès, paramètres, décisions métier),
- les blocs de gestion d’erreurs (`Http404`),
- les points critiques de l’application.

---

## 🧪 Outils de développement

- Interface d’administration Django : `/admin`
- Linting : `flake8`
- Tests unitaires et d’intégration : `pytest`
- Couverture de tests : `pytest-cov`
- Hooks de pré-commit pour garantir la qualité du code :
  - `isort` : tri automatique des imports
  - `black` : formatage automatique du code
  - `flake8` : analyse statique et respect des conventions PEP8

Les hooks de pré-commit sont exécutés automatiquement avant chaque commit afin d’assurer un code propre, cohérent et conforme aux standards du projet.

---

## 🔐 Sécurité et bonnes pratiques

- Aucune donnée sensible n’est stockée dans le dépôt Git.
- Les variables d’environnement sont gérées via `.env`.
- Les fichiers statiques sont servis avec WhiteNoise.
- Le dossier `staticfiles/` est généré automatiquement et ne doit pas être versionné.
- L’accès au projet Sentry est restreint aux utilisateurs autorisés via l’interface Sentry.

---
