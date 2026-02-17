# Exploitation & gestion de l’application

## Logs

- Les logs applicatifs sont persistés dans le dossier `logs/`.
- La rotation / niveau de log dépend de la configuration (variables d’environnement).

## Monitoring (Sentry)

- Sentry capture les exceptions côté serveur.
- La route `/sentry-debug/` permet de valider l’intégration.

## Mises à jour de dépendances (Dependabot)

- Dependabot ouvre automatiquement des PR de mise à jour (Python / Actions / Docker).
- Les PR doivent passer le check **CI / test** avant merge (branche protégée).
- Les correctifs de sécurité sont proposés dès détection de vulnérabilité.
