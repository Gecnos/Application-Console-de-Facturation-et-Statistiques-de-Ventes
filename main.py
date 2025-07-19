
import pandas as pd
from os.path import exists
from data_manager import (lire_clients, lire_produits, lire_cartes_reduction)
from produit_manager import(ajouter_produit)
from client_manager import(recherche_client)
from facture_manager import (creer_facture)

def afficher_menu():
    print ("Bienvenue sur notre application de gestion de factures")
    while True:
        print ("Menu principal:")
        choix = input("1.Consulter un fichier \n 2.Générer une facture \n 3. Ajouter un produit \n 4.Quitter l'application.\n Entrez votre choix :") 
        if choix == '1':
            sub_choice = input("a.Afficher les clients \n b. Afficher les produits \n c. Afficher les cartes de réduction \n Entrez votre choix :") 
            if sub_choice == 'a':
                lire_clients()
            elif sub_choice == 'b':
                lire_produits()
            elif sub_choice == 'c':
                lire_cartes_reduction()
        elif choix == '2':
            creer_facture()
        elif choix == '3':
            ajouter_produit()
        elif choix == '4':
            print("Merci d'avoir utilisé notre application . Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
                        

        