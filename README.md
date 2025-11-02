# 🎨 Portfolio Django — Guide d’installation et d’exécution

Ce projet est un **portfolio minimal développé avec Django**.
Il comprend :

* 🧱 Un projet principal : `portfolio_project`
* 💼 Une application : `portfolio_app` (avec un modèle `Project`)
* 🖼️ Des templates HTML et des fichiers statiques prêts à être personnalisés

---

## ⚙️ Prérequis

Avant de commencer, assurez-vous d’avoir installé :

* **Python 3.8+**
* **virtualenv** *(optionnel mais recommandé)*
* **pip** (gestionnaire de paquets Python)

---

## 🚀 Installation et exécution (Windows PowerShell)

### 1️⃣ Créer et activer un environnement virtuel

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

---

### 2️⃣ Installer les dépendances

```powershell
pip install -r requirements.txt
```

---



### 4️⃣ Lancer le serveur de développement

```powershell
python manage.py runserver
```

🖥️ Ouvrez ensuite votre navigateur sur :

* Page d’accueil : [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧩 Notes et prochaines étapes


* 🖼️ **Médias :** ajoutez une gestion des fichiers médias (images, PDF, etc.)
  pour permettre l’upload d’images de projets.
* 🎨 **Personnalisation :** modifiez les templates (`templates/`) et le CSS (`static/`)
  pour adapter le design à votre style personnel.
* 🧠 **Optimisation :** pensez à configurer le déploiement (base de données, serveur, collectstatic, etc.) pour la production.

---

🧾 **Auteur :** *Kodjo Koua Andre j-w*
📅 **Dernière mise à jour :** Novembre 2025
💡 *“Un portfolio bien conçu est la meilleure vitrine d’un développeur.”*
