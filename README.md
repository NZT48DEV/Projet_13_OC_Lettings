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

Créer un fichier `.env` à la racine du projet :

```env
DEBUG=False
SECRET_KEY=votre-cle-secrete
```

Générer une clé secrète Django :

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

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

## 🧪 Outils de développement

- Interface d’administration Django : `/admin`
- Linting : `flake8`
- Tests : `pytest`

---

## 📄 Notes

- Les variables d’environnement sont gérées via un fichier `.env`
- Les fichiers statiques sont servis avec WhiteNoise
- Le dossier `staticfiles/` est généré automatiquement et ne doit pas être versionné
