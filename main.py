<<<<<<< HEAD

=======
import pandas as pd
from os.path import exists
from data_manager import (
    creer_fichier_cartes_reduction,
    ecrire_clients,generer_code_client
)
from produit_manager import(ajouter_produit)
#creation du fichier cartes_reduction si nécessaire
creer_fichier_cartes_reduction()
cartes = pd.read_excel("./fichiers/cartes_reduction.xlsx", engine="openpyxl")

#  Chargement des fichiers Excel
clients = pd.read_excel("./fichiers/Clients.xlsx", engine="openpyxl") \
    if exists("./fichiers/Clients.xlsx") else pd.DataFrame(columns=["nom", "contact", "code_client", "IFU"])

produits = pd.read_excel("./fichiers/Produits.xlsx", engine="openpyxl") \
    if exists("./fichiers/Produits.xlsx") else pd.DataFrame(columns=["code_produit", "libelle", "prix_unitaire"])

cartes = pd.read_excel("./fichiers/cartes_reduction.xlsx", engine="openpyxl")

# Saisie des infos client
nom = input("Nom du client : ")
contact = input("Contact du client : ")
IFU = input("IFU du client : ")
code_client = generer_code_client(nom, contact, IFU)
nouveau_client = ecrire_clients(nom, contact, code_client, IFU)
clients = pd.concat([clients, nouveau_client], ignore_index=True)
clients.to_excel("./fichiers/Clients.xlsx", index=False, engine="openpyxl")
print(f"Client '{nom}' enregistré avec le code : {code_client}")

ajouter_produit()
>>>>>>> b7116766681e9dc6e16e36814a265ceb83e2f9af
