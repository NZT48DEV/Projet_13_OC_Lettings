# Guide d'utilisation (cas d'usage)

## Cas d'usage : consulter des locations

1.  Ouvrir la page d'accueil `/`
2.  Aller sur **Lettings**
3.  Consulter le détail d'une location

------------------------------------------------------------------------

## Cas d'usage : consulter des profils

1.  Aller sur `/profiles/`
2.  Ouvrir le profil d'un utilisateur

------------------------------------------------------------------------

## Cas d'usage : administration

1.  Ouvrir `/admin/`
2.  Se connecter avec un compte **staff/superuser**

### Compte administrateur de démonstration

Le projet inclut une base de données SQLite fournie dans l'énoncé
contenant un compte administrateur destiné aux tests et à la
démonstration.

Identifiants :

-   **Username** : `admin`
-   **Password** : `Abc1234!`

3.  Créer / modifier des `Address`, `Letting` et `Profile`

> ⚠️ Ce compte est fourni uniquement à des fins pédagogiques.

------------------------------------------------------------------------

## Cas d'usage : démonstration (soutenance)

-   Vérifier la page 404 personnalisée via `/test-404/`
-   Vérifier la page 500 personnalisée via `/test-500/`
-   Vérifier l'intégration Sentry via `/sentry-debug/`
