
import pandas as pd
from os.path import exists
from data_manager import (ajouter_client)
from produit_manager import(ajouter_produit)
from client_manager import(recherche_client)
from facture_manager import (verifier_et_ajouter_carte, choisir_client, selectionner_produits, calculer_totaux)

def afficher_menu():
    print("\n=== Menu Principal ===")
    print("1. Consulter un fichier")
    print("   a. Afficher les clients")
    print("   b. Afficher les produits")
    print("   c. Afficher les cartes de réduction")
    print("2. Générer une facture")
    print("3. Ajouter un produit")
    print("4. Quitter l'application")

def main():
    while True:
        afficher_menu()
        choix = input("\n Entrez votre choix (1/a/b/c/2/3/4) : ").strip().lower()

        if choix == "1" or choix == "a":
            ajouter_client('nom','contact','IFU','code_client','clients','produits','cartes',)
        elif choix == "b":
            recherche_client()
        elif choix == "c":
             recherche_client()
        elif choix == "2":
             recherche_client()
        elif choix == "3":
            ajouter_produit()
        elif choix == "4":
            print(" Au revoir, et a la prochaine!")
            break
        else:
            print("Choix invalide, essaie encore.")
