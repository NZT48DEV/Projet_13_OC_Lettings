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
  Exemple :
  ```
  localhost,127.0.0.1,mon-domaine.fr
  ```
  En production, ce champ doit contenir le nom de domaine public du site.

- **LOG_LEVEL**  
  Niveau minimum de logs affichés par l’application.  
  Valeurs possibles :
  - `DEBUG`
  - `INFO`
  - `WARNING`
  - `ERROR`
  - `CRITICAL`  

  👉 `INFO` est un bon compromis entre visibilité et bruit.

- **EVENT_LEVEL**  
  Niveau minimum des événements envoyés à Sentry.  
  Valeurs possibles :
  - `WARNING`
  - `ERROR`
  - `CRITICAL`  

  👉 Recommandé : `WARNING` ou `ERROR` afin d’éviter un volume excessif d’événements.

---

### Génération de la clé secrète Django

La clé secrète peut être générée avec la commande suivante :

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

---

### Variables Sentry (optionnelles mais recommandées)

```env
SENTRY_DSN=your_sentry_dsn_here
SENTRY_ENVIRONMENT=development
SENTRY_RELEASE=oc-lettings-1.0.0
SENTRY_TRACES_SAMPLE_RATE=0.0
SENTRY_PROFILES_SAMPLE_RATE=0.0
SEND_DEFAULT_PII=false
```

- **SENTRY_DSN** : identifiant du projet Sentry.
- **SENTRY_ENVIRONMENT** : environnement d’exécution (`development`, `staging`, `production`).
- **SENTRY_RELEASE** : version applicative associée aux événements.
- **SENTRY_TRACES_SAMPLE_RATE** : taux d’échantillonnage des performances (0.0 = désactivé).
- **SENTRY_PROFILES_SAMPLE_RATE** : taux d’échantillonnage du profiling.
- **SEND_DEFAULT_PII** : envoi ou non de données personnelles (recommandé : `false`).

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

---

## 🧪 Outils de développement

- Interface d’administration Django : `/admin`
- Linting : `flake8`
- Tests unitaires et d’intégration : `pytest`
- Couverture de tests : `pytest-cov`
- Hooks de pré-commit :
  - `isort`
  - `black`
  - `flake8`

---

## 🔐 Sécurité et bonnes pratiques

- Aucune donnée sensible n’est stockée dans le dépôt Git.
- Les variables d’environnement sont gérées via `.env`.
- Les fichiers statiques sont servis avec WhiteNoise.
- Le dossier `staticfiles/` est généré automatiquement et ne doit pas être versionné.
- L’accès au projet Sentry est restreint aux utilisateurs autorisés.

---
