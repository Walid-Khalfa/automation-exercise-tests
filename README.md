# 🧪 Projet d’automatisation de tests – Automation Exercise

**Auteur : Walid Khalfa**  
**GitHub : [Walid-Khalfa/automation-exercise-tests](https://github.com/Walid-Khalfa/automation-exercise-tests)**

Ce projet contient une suite de **tests automatisés** pour le site de démonstration [Automation Exercise](http://automationexercise.com).  
Il est conçu avec les **bonnes pratiques** du test logiciel :

- **Page Object Model (POM)** : chaque page web est une classe dédiée.
- **Data‑driven testing** : les données de test sont externalisées (JSON, Faker).
- **Intégration continue** : GitHub Actions exécute les tests à chaque push.
- **Framework** : Playwright + pytest (Python).

L’objectif est de couvrir **26 cas de test** (inscription, connexion, panier, commande, etc.) et d’obtenir une suite fiable et maintenable.

---

## 📋 Table des matières

1. [Prérequis](#prérequis)
2. [Installation](#installation)
3. [Structure du projet](#structure-du-projet)
4. [Exécution des tests](#exécution-des-tests)
5. [Résultats actuels](#résultats-actuels)
6. [CI/CD avec GitHub Actions](#cicd-avec-github-actions)
7. [Technologies utilisées](#technologies-utilisées)
8. [Améliorations possibles](#améliorations-possibles)
9. [Contact](#contact)

---

## 🔧 Prérequis

- **Python 3.11 ou supérieur**  
- **pip** (gestionnaire de paquets Python)  
- **Git** (optionnel, pour cloner le dépôt)  
- Un navigateur Chromium (installé automatiquement par Playwright)

---

## ⚙️ Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Walid-Khalfa/automation-exercise-tests.git
   cd automation-exercise-tests
   Créer un environnement virtuel :

bash
python -m venv venv
source venv/bin/activate    # Sur Linux/macOS
# ou `venv\Scripts\activate` sur Windows
Installer les dépendances :

bash
pip install -r requirements.txt
Installer les navigateurs Playwright :

bash
playwright install chromium
📁 Structure du projet
text
automation-exercise-tests/
├── .github/workflows/        # CI/CD : GitHub Actions
│   └── test.yml
├── config/                   # Paramètres (URL, timeout...)
│   └── settings.py
├── data/                     # Données de test (JSON)
│   ├── users.json
│   └── payment_data.json
├── pages/                    # Page Object Model
│   ├── base_page.py
│   ├── home_page.py
│   ├── signup_login_page.py
│   ├── account_creation_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── contact_us_page.py
│   ├── test_cases_page.py
│   ├── category_page.py
│   └── brand_page.py
├── tests/                    # Tous les cas de test (26)
│   ├── conftest.py
│   ├── test_register_login.py
│   ├── test_products_cart.py
│   ├── test_order_checkout.py
│   ├── test_contact_subscription.py
│   └── test_scrolling_categories_brands.py
├── utils/                    # Helpers
│   ├── data_loader.py
│   └── helpers.py
├── requirements.txt          # Dépendances Python
├── pytest.ini                # Configuration pytest
└── README.md
🚀 Exécution des tests
Lancer tous les tests en mode headless (sans interface graphique) :

bash
pytest -v
Lancer un groupe spécifique (par exemple les tests de panier) :

bash
pytest tests/test_products_cart.py -v
Lancer un test unique (par exemple TC1) :

bash
pytest tests/test_register_login.py::test_tc1_register_user -v
Afficher le navigateur (mode headed) pour observer :

bash
pytest --headed -v
Générer un rapport HTML :

bash
pytest --html=report.html --self-contained-html
📊 Résultats actuels
22 tests passent sur 26 (84 % de succès).
Les 4 échecs restants sont mineurs et liés à :

L’affichage des messages d’erreur (login incorrect, email existant) – légères variations du site.

Un timeout occasionnel sur le bouton de paiement (lenteur réseau).

L’ajout aux articles recommandés (nécessite un survol supplémentaire).

Des correctifs sont disponibles dans la branche fix/remaining-fails (à venir).

🔁 CI/CD avec GitHub Actions
Le fichier .github/workflows/test.yml exécute automatiquement la suite de tests à chaque push ou pull request sur la branche main.

Que fait la pipeline ?

Vérification du code.

Installation de Python et des dépendances.

Installation du navigateur Chromium.

Exécution de pytest (mode headless).

Upload du rapport HTML en tant qu’artefact (téléchargeable depuis GitHub).

Pour voir les résultats, rends-toi dans l’onglet Actions de ton dépôt GitHub.

🛠️ Technologies utilisées
Technologie	Rôle
Python 3.12	Langage principal
Playwright	Pilotage du navigateur (automatisation)
pytest	Framework de test
pytest-playwright	Intégration Playwright avec pytest
Faker	Génération de données aléatoires (emails, noms…)
GitHub Actions	Intégration continue

📫 Contact
Walid Khalfa
GitHub : Walid-Khalfa
Projet : automation-exercise-tests

N’hésitez pas à ouvrir une issue ou une pull request pour toute suggestion ou amélioration.

🎉 Bon test !

