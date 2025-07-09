


# 🧾 Application Console de Facturation – Projet Python

## 🎯 Objectif pédagogique

Ce projet vise à vous initier à :
- La manipulation de fichiers **Excel** avec `pandas`, `openpyxl` ou `xlsxwriter`
- La conception d'une application **en mode console uniquement**
- La génération de factures **en PDF**
- La gestion de clients, produits, réductions, et calculs de totaux

---

## 📦 Fonctionnalités principales

- 🔍 Consulter les fichiers de données (clients, produits, réductions)
- 🧾 Générer une facture au format **PDF** avec réduction éventuelle
- 👤 Ajouter un nouveau client
- 📦 Ajouter un nouveau produit
- 💾 Persistance via fichiers Excel

---

## 🗂️ Structure du projet

```

facturation\_console/
│
├── main.py                    # Menu principal (Dev 2)
├── data\_manager.py           # Gestion des fichiers Excel (Dev 1)
├── client\_manager.py         # Ajout & validation client (Dev 3)
├── facture\_manager.py        # Génération facture PDF + cartes (Dev 4)
├── produit\_manager.py        # Ajout de produit (Dev 5)
│
├── fichiers/
│   ├── Clients.xlsx
│   ├── Produits.xlsx
│   └── CartesReduction.xlsx
│
├── factures/                 # Dossier de sortie des factures PDF
└── README.md

````

---

## 👥 Répartition des tâches par développeur

| Dév | Fichier(s) | Rôle / Description |
|-----|------------|--------------------|
| 🟦 **Dev 1** | `data_manager.py` | 📁 **Gestion des fichiers Excel** <br>• Lecture/écriture de `Clients.xlsx`, `Produits.xlsx`, `CartesReduction.xlsx`<br>• Validation des codes (code_client, code_produit)<br>• Utilise `pandas` + `openpyxl` |
| 🟩 **Dev 2** | `main.py` | 💻 **Interface console + menu principal** <br>• Affichage du menu principal (1 à 4)<br>• Navigation dans les sous-menus<br>• Appel aux fonctions des autres développeurs |
| 🟨 **Ornélie** | `client_manager.py` | 👤 **Gestion des clients** <br>• Saisie/validation d’un nouveau client (nom, contact, IFU 13 chiffres)<br>• Recherche client existant<br>• Interface entre console et `data_manager` |
| 🟥 **Dev 4** | `facture_manager.py` | 🧾 **Génération des factures PDF + cartes de réduction** <br>• Sélection produits à facturer<br>• Calcul total HT, TTC<br>• Génération d’une **facture en PDF**<br>• Création **automatique** d'une carte de réduction selon le montant<br>• Utilise `fpdf` ou `reportlab` + `num2words` |
| 🟪 **Dev 5** | `produit_manager.py` | 📦 **Ajout de produit** <br>• Saisie d’un nouveau produit (libellé, prix, code produit)<br>• Validation (code = 6 caractères, prix > 0)<br>• Ajout via `data_manager` |

---

## 🧾 Détails du contenu de la facture PDF

- **En-tête** :
  - En haut à gauche : nom du **groupe d'étudiants**
  - En haut à droite : **date d’émission**
  - En dessous : **informations du client** (nom, contact, IFU)

- **Titre centré** :
  ```text
  FACTURE n° XXXXXX


* **Tableau des produits facturés** :

  | Code | Libellé | Quantité | Prix Unitaire | Total Ligne |
  | ---- | ------- | -------- | ------------- | ----------- |

* **Bas de page** :

  ```text
  Arrêtée, la présente facture à la somme de : [Total TTC en lettres]
  ```

* **Format** : PDF avec `fpdf2`, `reportlab` ou `pdfkit`

---

## 🎁 Cartes de réduction (automatiques)

* Les **cartes de réduction** sont générées **uniquement à partir de la 2ème facture** du client.
* Plages à définir (exemple) :

  * ≥ 100 000 F → réduction de 5%
  * ≥ 200 000 F → réduction de 10%
  * ≥ 300 000 F → réduction de 15%
* Un client **ne peut avoir qu’une seule carte**.
* Les cartes sont ajoutées dans `CartesReduction.xlsx`.

---

## ▶️ Lancer l'application

### ✅ Prérequis

* Python 3.8 ou plus
* Modules nécessaires :

  ```bash
  pip install pandas openpyxl fpdf2 num2words
  ```

### ▶️ Exécution

```bash
python main.py
```

---

## 📄 Données initiales

| Fichier                | Contenu        |
| ---------------------- | -------------- |
| `Clients.xlsx`         | 2 clients      |
| `Produits.xlsx`        | 10 produits    |
| `CartesReduction.xlsx` | vide au départ |

---

## ✅ Menu principal

```text
1. Consulter un fichier
   └─ a. Afficher les clients
   └─ b. Afficher les produits
   └─ c. Afficher les cartes de réduction
2. Générer une facture
3. Ajouter un produit
4. Quitter l'application
```

---

## 📚 Modules utilisés

* `pandas`, `openpyxl` – manipulation des fichiers Excel
* `fpdf2`, `reportlab`, ou `pdfkit` – génération PDF
* `num2words` – conversion de chiffres en lettres (pour total en bas de facture)
