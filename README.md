
# 🧾 Application Console de Facturation – Projet Python

## 🎯 Objectif pédagogique
Développer une application en mode console permettant :
- La gestion de fichiers clients, produits, cartes de réduction
- La création de factures avec réduction automatique
- L’interaction utilisateur via menus en console
- L’utilisation de **Pandas** pour manipuler des fichiers **Excel (.xlsx)**

---

## 📦 Fonctionnalités principales
- 🔍 Consulter les fichiers (clients, produits, réductions)
- 🧾 Générer une facture (client existant ou nouveau)
- 👤 Ajouter un client
- 📦 Ajouter un produit
- 💾 Persistance automatique des données dans les fichiers Excel

---

## 🗂️ Structure du projet

```

facturation\_console/
│
├── main.py                        # Menu principal (Dev 2)
├── data\_manager.py               # Accès fichiers Excel (Dev 1)
├── client\_manager.py             # Gestion clients (Dev 3)
├── facture\_manager.py            # Génération factures (Dev 4)
├── produit\_manager.py            # Ajout produits (Dev 5)
│
├── fichiers/
│   ├── Clients.xlsx
│   ├── Produits.xlsx
│   └── CartesReduction.xlsx
│
├── factures/                     # Factures générées
└── README.md

````

---

## 👥 Répartition des tâches par développeur

| Dév | Fichier(s) | Rôle / Description |
|-----|------------|--------------------|
| 🟦 **Dev 1** | `data_manager.py` | 📁 **Manipulation des fichiers Excel** (Pandas) <br>• Charger les données (`get_clients()`, `get_produits()`, etc.)<br>• Ajouter un client ou un produit aux fichiers<br>• Vérification de l’unicité des codes et format IFU |
| 🟩 **Dev 2** | `main.py` | 💻 **Interface console + Menu principal** <br>• Affichage des options 1, 2, 3, 4<br>• Appel des modules des autres développeurs<br>• Navigation entre les sous-menus |
| 🟨 **Dev 3** | `client_manager.py` | 👤 **Gestion des clients** <br>• Saisie d’un nouveau client (nom, contact, IFU)<br>• Validation de l’IFU (13 chiffres)<br>• Ajout du client via `data_manager`<br>• Recherche client existant |
| 🟥 **Dev 4** | `facture_manager.py` | 🧾 **Génération de factures** <br>• Sélection des produits (code + quantité)<br>• Calcul total + application de réduction<br>• Génération d’un fichier facture (Excel)<br>• Liaison avec clients et produits |
| 🟪 **Dev 5** | `produit_manager.py` | 📦 **Ajout de produits** <br>• Saisie du libellé, prix, code produit<br>• Validation (code = 6 caractères, prix > 0)<br>• Enregistrement via `data_manager`<br>• Retour console en cas d’erreur |

---

## ▶️ Lancer l'application

### Prérequis
- Python 3.8 ou plus
- Bibliothèques : `pandas`, `openpyxl`

### Installation des dépendances
```bash
pip install pandas openpyxl
````

### Exécution

```bash
python main.py
```

---

## ✅ Données initiales

| Fichier                | Contenu initial              |
| ---------------------- | ---------------------------- |
| `Clients.xlsx`         | 2 clients                    |
| `Produits.xlsx`        | 10 produits                  |
| `CartesReduction.xlsx` | Réductions liées aux clients |



