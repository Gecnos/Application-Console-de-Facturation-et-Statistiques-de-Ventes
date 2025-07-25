import pandas as pd 
import os 
from os.path import exists
# #  Création du fichier cartes_reduction si nécessaire
# def creer_fichier_cartes_reduction():
#     dossier = "./fichiers"
#     fichier_path = f"{dossier}/cartes_reduction.xlsx"

#     # Crée le dossier s'il n'existe pas
#     if not os.path.exists(dossier):
#         os.makedirs(dossier)

#     # Crée le fichier Excel s'il n'existe pas
#     if not os.path.exists(fichier_path):
#         donnees = {
#             "code_reduction": [],
#             "pourcentage_reduction": [],
#             "valide_jusquau": []
#         }
#         dataframe = pd.DataFrame(donnees)
#         dataframe.to_excel(fichier_path, index=False, engine="openpyxl")
#         print(" Fichier 'cartes_reduction.xlsx' créé avec succès.")
#     else:
#         print(" Le fichier 'cartes_reduction.xlsx' existe déjà.")


#lecture du fichier clients et produit 
def lire_clients():
    try:
        df = pd.read_excel("./fichiers/Clients.xlsx", engine="openpyxl")
        print("\nLISTE DES CLIENTS")
        print(df.to_string(index=False))
        print("\n")
        return df
    except Exception as e:
        print(f"\nErreur lors de la lecture des clients : {e}")
        return pd.DataFrame()

def lire_produits():
    try:
        df = pd.read_excel("./fichiers/Produits.xlsx", engine="openpyxl")
        print("\nLISTE DES PRODUITS")
        print(df.to_string(index=False))
        print("\n")
        return df
    except Exception as e:
        print(f"\nErreur lors de la lecture des produits : {e}")
        return pd.DataFrame()

def lire_cartes_reduction():
    try:
        df = pd.read_excel("./fichiers/CartesReduction.xlsx", engine="openpyxl")
        print("\nLISTE DES CARTES DE RÉDUCTION")
        print(df.to_string(index=False))
        print("\n")
        return df
    except Exception as e:
        print(f"\nErreur lors de la lecture des cartes : {e}")
        return pd.DataFrame()

def lire_factures():
    try:
        df = pd.read_excel("./fichiers/HistoriqueFactures.xlsx", engine="openpyxl")
        print("\nHISTORIQUE DES FACTURES")
        print(df.to_string(index=False))
        print("\n")
        return df
    except Exception as e:
        print(f"\nErreur lors de la lecture des factures : {e}")
        return pd.DataFrame()

#     #function qui permet d'ecrire les produits dans le fichier produits.xlsx
# def ecrire_produits(code_produit, libelle, prix_unitaire):
#     nouveau_produit = pd.DataFrame({
#         "code_produit": [code_produit],
#         "libelle": [libelle],
#         "prix_unitaire": [prix_unitaire]
#     })
#     return nouveau_produit
     

# #function qui permet de generer un code produit
# def generer_code_produit(libelle):
#     code = libelle[:3].lower() + str(len(libelle))
#     return code


# #function qui permet de creer le fichier de la carte de reduction 

# # def creer_fichier_cartes_reduction():
# #     donnees={
# #         "code_reduction":[],
# #         "pourcenntage_reduction":[],
# #         "valide_jusquau":[]
# #     }
# #     #creation du dataframe vide 
# #     dataframe = pd.DataFrame(donnees)
# #     dataframe.to_excel("./fichiers/cartes_reduction.xlsx", index=False, engine="openpyxl")
    

# #function de verification de l'existance des codes 

# # def valider_code(code_client,code_produit):
# #     client_existe = code_client in clients['code_client'].values
# #     produit_existe = code_produit in produits['code_produit'].values
# #     return client_existe and produit_existe
# #     #creation du fichier cartes_reduction si nécessaire
    
# # creer_fichier_cartes_reduction()
# # cartes = pd.read_excel("./fichiers/cartes_reduction.xlsx", engine="openpyxl")

# #function qui permet de generer un code client 
# def generer_code_client(nom, contact,IFU):
#     code = nom[:3].lower() + contact[:3].upper() + IFU[-3:]
#     return code

# #function qui permet d'ecrire les clients dans le fichier clients.xlsx
# def ecrire_clients(nom, contact, code_client, IFU):
#     nouveau_client = pd.DataFrame({
#         "nom": [nom],
#         "contact": [contact],
#         "code_client": [code_client],
#         "IFU": [IFU],
#     })
#     return nouveau_client
    
# def ajouter_client(nom,contact,IFU,code_client,clients,produits,cartes):

#     # Chargement des fichiers
#     clients = pd.read_excel("./fichiers/Clients.xlsx", engine="openpyxl") \
#         if exists("./fichiers/Clients.xlsx") else pd.DataFrame(columns=["nom", "contact", "code_client", "IFU"])

#     produits = pd.read_excel("./fichiers/Produits.xlsx", engine="openpyxl") \
#         if exists("./fichiers/Produits.xlsx") else pd.DataFrame(columns=["code_produit", "libelle", "prix_unitaire"])

#     # cartes = pd.read_excel("./fichiers/cartes_reduction.xlsx", engine="openpyxl")

    
#  # Saisie des infos client
#     nom = input("Nom du client : ")
#     contact = input("Contact du client : ")
#     IFU = input("IFU du client : ")

#     # Traitement
#     code_client = generer_code_client(nom, contact, IFU)
#     nouveau_client = ecrire_clients(nom, contact, code_client, IFU)

#     # Ajout et sauvegarde
#     clients = pd.concat([clients, nouveau_client], ignore_index=True)
#     clients.to_excel("./fichiers/Clients.xlsx", index=False, engine="openpyxl")

#     # Confirmation
#     print(f"Client '{nom}' enregistré avec le code : {code_client}")

# # lire_factures()
# # lire_cartes_reduction()
# # lire_clients()
# # lire_produits()
    