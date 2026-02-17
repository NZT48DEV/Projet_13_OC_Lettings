# Démarrage rapide

## Exécution en local (dev)

```bash
pipenv shell
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

Accès :
- Application : `http://127.0.0.1:8000/`
- Admin : `http://127.0.0.1:8000/admin/`

## Exécution via Docker (commande unique)

Prérequis :
- Docker installé
- `.env` configuré

Commande (via le Makefile) :

```bash
make docker-run
```
