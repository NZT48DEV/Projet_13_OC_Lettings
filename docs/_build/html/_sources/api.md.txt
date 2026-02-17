# Interfaces de programmation

L’application expose des **interfaces web (HTML)** via les routes Django, ainsi que l’interface **Django Admin**.

## Routes principales

### Application (`oc_lettings_site/urls.py`)

- `/` → page d’accueil
- `/lettings/` → routes de l’app *lettings*
- `/profiles/` → routes de l’app *profiles*
- `/admin/` → interface d’administration

### Routes de test / démonstration

- `/test-404/` → déclenche une 404 contrôlée
- `/test-500/` → déclenche une erreur serveur (500)
- `/sentry-debug/` → route de test Sentry

## App `lettings`

- `/lettings/` → liste des locations
- `/lettings/<letting_id>/` → détail d’une location

## App `profiles`

- `/profiles/` → liste des profils
- `/profiles/<username>/` → détail d’un profil (par username)
