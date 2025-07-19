import pandas as pd
import os

def ajouter_produit():
    
    dossier = "fichiers"
    fichier = "Produits.xlsx"
    chemin = os.path.join(dossier, fichier)
    
    df = pd.read_excel(chemin, index_col='code_produit')
    dernier_code = df.index[-1] 

    num = int(dernier_code[1:])  
    nouveau_code = f"P{num + 1:03d}"

    print("\nVous avez choisi d'enregistrer un nouveau produit")
    print("\nCelui-ci sera ajouté à la suite des produits existants")

    libelle = input("\nEntrez le nom du produit : ").strip()
    while True:
        try:
            prix_unitaire = float(input("Entrez le prix unitaire : "))
            if prix_unitaire <= 0:
                raise ValueError("Le prix doit être positif")
            break
        except ValueError as e:
            print(f"{str(e)}")

    print("\nVoici les informations du produit que vous voulez ajouter :")
    print(f"\nCode: {nouveau_code}")
    print(f"\nNom: {libelle}")
    print(f"\nPrix unitaire: {prix_unitaire}")

    while True:
        choix = input("\n Voulez vous confirmez l'ajout ? (y/n) ").lower()
        if choix == 'y':
            df.loc[nouveau_code] = [libelle, prix_unitaire]
            df.to_excel(chemin)
            print("\n Votre produit a été ajouté avec succès !")
            break
        elif choix == 'n':
            print("\nL'enregistrement du produit a été annulé")
            break
        else:
            print("\nRéponse invalide. Veuillez répondre par 'y' ou 'n'.")
# ajouter_produit()
