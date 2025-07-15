import pandas as pd 
import os 

#  Création du fichier cartes_reduction si nécessaire
def creer_fichier_cartes_reduction():
    dossier = "./fichiers"
    fichier_path = f"{dossier}/cartes_reduction.xlsx"

    # Crée le dossier s'il n'existe pas
    if not os.path.exists(dossier):
        os.makedirs(dossier)

    # Crée le fichier Excel s'il n'existe pas
    if not os.path.exists(fichier_path):
        donnees = {
            "code_reduction": [],
            "pourcentage_reduction": [],
            "valide_jusquau": []
        }
        dataframe = pd.DataFrame(donnees)
        dataframe.to_excel(fichier_path, index=False, engine="openpyxl")
        print(" Fichier 'cartes_reduction.xlsx' créé avec succès.")
    else:
        print(" Le fichier 'cartes_reduction.xlsx' existe déjà.")


#lecture du fichier clients et produit 
clients = pd.read_excel("./fichiers/Clients.xlsx",engine="openpyxl")
produits = pd.read_excel("./fichiers/Produits.xlsx", engine="openpyxl")

#function qui permet d'ecrire les clients dans le fichier clients.xlsx
def ecrire_clients(nom, contact, code_client, IFU):
    nouveau_client = pd.DataFrame({
        "nom": [nom],
        "contact": [contact],
        "code_client": [code_client],
        "IFU": [IFU],
    })
    return nouveau_client
    #function qui permet d'ecrire les produits dans le fichier produits.xlsx
def ecrire_produits(code_produit, libelle, prix_unitaire):
    nouveau_produit = pd.DataFrame({
        "code_produit": [code_produit],
        "libelle": [libelle],
        "prix_unitaire": [prix_unitaire]
    })
    return nouveau_produit
     
   
#function qui permet de generer un code client 
def generer_code_client(nom, contact,IFU):
    code = nom[:3].lower() + contact[:3].upper() + IFU[-3:]
    return code

#function qui permet de generer un code produit
def generer_code_produit(libelle):
    code = libelle[:3].lower() + str(len(libelle))
    return code


#function qui permet de creer le fichier de la carte de reduction 

def creer_fichier_cartes_reduction():
    donnees={
        "code_reduction":[],
        "pourcenntage_reduction":[],
        "valide_jusquau":[]
    }
    #creation du dataframe vide 
    dataframe = pd.DataFrame(donnees)
    dataframe.to_excel("./fichiers/cartes_reduction.xlsx", index=False, engine="openpyxl")
    

#function de verification de l'existance des codes 

def valider_code(code_client,code_produit):
    client_existe = code_client in clients['code_client'].values
    produit_existe = code_produit in produits['code_produit'].values
    return client_existe and produit_existe
    