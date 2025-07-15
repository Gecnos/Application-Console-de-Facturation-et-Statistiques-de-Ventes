import pandas as pd
from os.path import exists
from data_manager import (ecrire_clients, ecrire_produits, generer_code_client, generer_code_produit)

# Chargement des fichiers Excel
clients = pd.read_excel("./fichiers/Clients.xlsx", engine="openpyxl") if exists("./fichiers/Clients.xlsx") else pd.DataFrame(columns=["nom", "contact", "code_client", "IFU"])
produits = pd.read_excel("./fichiers/Produits.xlsx", engine="openpyxl") if exists("./fichiers/Produits.xlsx") else pd.DataFrame(columns=["code_produit", "libelle", "prix_unitaire"])

# 🔤 Saisie des infos client
nom = input("Nom du client : ")
contact = input("Contact du client : ")
IFU = input("IFU du client : ")
code_client = generer_code_client(nom, contact, IFU)
nouveau_client = ecrire_clients(nom, contact, code_client, IFU)
clients = pd.concat([clients, nouveau_client], ignore_index=True)
clients.to_excel("./fichiers/Clients.xlsx", index=False, engine="openpyxl")
print(f"✅ Client '{nom}' enregistré avec le code : {code_client}")

# 📦 Saisie des infos produit
libelle = input("Nom du produit : ")
prix = float(input("Prix unitaire : "))
code_produit = generer_code_produit(libelle)
nouveau_produit = ecrire_produits(code_produit, libelle, prix)
produits = pd.concat([produits, nouveau_produit], ignore_index=True)
produits.to_excel("./fichiers/Produits.xlsx", index=False, engine="openpyxl")
print(f"✅ Produit '{libelle}' enregistré avec le code : {code_produit}")
