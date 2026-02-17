# Déploiement

## CI (GitHub Actions)

Le workflow `CI` exécute :

- Installation des dépendances (Pipenv)
- Lint via `pre-commit`
- Tests via `pytest` + couverture minimale **≥ 80%**

## Docker

Un job Docker est exécuté **uniquement** sur :
- event : `push`
- branche : `master`
- condition : succès du job `test`

Il :
- construit l’image
- push sur Docker Hub avec les tags :
  - `latest`
  - `<git sha>`

## Render

Déploiement via Render (hook/auto-deploy).  
Le principe recommandé :
- la CI valide le code
- l’image Docker est poussée
- Render déploie la nouvelle version
