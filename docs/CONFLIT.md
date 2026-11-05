# Conflit de fusion : feature/login -> main

## Contexte
- Branche `feature/login` : la ligne 3 de `afficher_menu()` devient
  `print("1. Se connecter")`.
- Branche `main` : la même ligne devient `print("1. Commencer")`.

## Cause
Les deux branches ont modifié la même ligne du même fichier à partir du
même ancêtre commun. Git ne peut pas choisir automatiquement.

## Résolution
Édition manuelle de `main.py` : suppression des marqueurs
`<<<<<<<`, `=======`, `>>>>>>>` et fusion des deux idées dans
`print("1. Commencer / Se connecter")`. Puis `git add main.py` et
`git commit`.
