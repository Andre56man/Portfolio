# Portfolio Django — Instructions

Ceci est un scaffold minimal d'un portfolio en Django. Il inclut :

- un projet `portfolio_project`
- une app `portfolio_app` avec un modèle `Project`
- templates et fichiers statiques

Prérequis
- Python 3.8+ installé
- virtualenv (optionnel mais recommandé)

Installation et exécution (Windows PowerShell)

1. Créer et activer un environnement virtuel :

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Installer les dépendances :

```powershell
pip install -r requirements.txt
```

3. Appliquer les migrations et créer un superuser :

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Lancer le serveur de développement :

```powershell
python manage.py runserver
```

5. Ouvrir http://127.0.0.1:8000/ pour voir la page d'accueil et http://127.0.0.1:8000/admin/ pour ajouter des projets.

Notes et prochaines étapes
- Remplacer `SECRET_KEY` dans `portfolio_project/settings.py` par une valeur sûre pour la production.
- Ajouter gestion des médias (images) si vous voulez uploader des images de projets.
- Personnaliser templates et styles.
