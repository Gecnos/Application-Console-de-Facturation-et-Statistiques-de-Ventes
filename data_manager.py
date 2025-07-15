import pandas as pd 
#lecture du fichier clients et produit 
clients = pd.read_excel("./fichiers/Clients.xlsx",engine="openpyxl")
produits = pd.read_excel("./fichiers/Produits.xlsx", engine="openpyxl")
cartes = pd.read_excel("./fichiers/cartes_reduction.xlsx", engine="openpyxl")

#function qui permet d'ecrire les clients dans le fichier clients.xlsx
def ecrire_clients(nom, contact, code_client, IFU):
    nouveau_client = pd.DataFrame({
        "nom": [nom],
        "contact": [contact],
        "code_client": [code_client],
        "IFU": [IFU],
    })
    #function qui permet d'ecrire les produits dans le fichier produits.xlsx
def ecrire_produits(code_produit, libelle, prix_unitaire):
    nouveau_produit = pd.DataFrame({
        "code_produit": [code_produit],
        "libelle": [libelle],
        "prix_unitaire": [prix_unitaire]
    })
     
    
    #ajout du nouveau client au dataframe existant
    global clients
    clients = pd.concat([clients, ecrire_clients], ignore_index=True)
    #ecriture dans le fichier excel
    clients.to_excel("./fichiers/Clients.xlsx", index=False, engine="openpyxl")
    #ajout du nouveau produit au dataframe existant
    global produits 
    produits = pd.concat([produits,ecrire_produits], ignore_index=True)
    #ecriture dans le fichier excel
    produits.to_excel("./fichiers/Produits.xlsx", index=False, engine="openpyxl")   
   
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
    