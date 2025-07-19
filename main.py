import pandas as pd
from os.path import exists
from data_manager import (lire_clients, lire_produits, lire_cartes_reduction, lire_factures)
from produit_manager import(ajouter_produit)
from facture_manager import (creer_facture)

def afficher_menu():
    print("Bienvenue sur notre application de gestion de factures")
    while True:
        print("\nMenu principal:")
        choix = input("1. Consulter un fichier\n"
                     "2. Générer une facture\n"
                     "3. Ajouter un produit\n"
                     "4. Voir l'historique des factures\n"
                     "5. Quitter l'application\n"
                     "Entrez votre choix : ")
        
        if choix == '1':
            while True:
                sub_choice = input("\na. Afficher les clients\n"
                                 "b. Afficher les produits\n"
                                 "c. Afficher les cartes de réduction\n"
                                 "d. Retour au menu principal\n"
                                 "Entrez votre choix : ")
                
                if sub_choice == 'a':
                    lire_clients()  # Affiche les clients
                    input("\nAppuyez sur Entrée pour continuer...")  # Attend avant de revenir au menu
                    # break  # Retourne au menu principal après affichage
                
                elif sub_choice == 'b':
                    lire_produits()
                    input("\nAppuyez sur Entrée pour continuer...")
                    # break
                
                elif sub_choice == 'c':
                    lire_cartes_reduction()
                    input("\nAppuyez sur Entrée pour continuer...")
                    # break
                
                elif sub_choice == 'd':
                    break  # Retour au menu principal
                
                else:
                    print("Choix invalide, veuillez réessayer.")
                    
        elif choix == '2':
            creer_facture()
        elif choix == '3':
            ajouter_produit()
        elif choix == '4':
            lire_factures()
        elif choix == '5':
            print("\nMerci d'avoir utilisé notre application. Au revoir !")
            break
        else:
            print("\nChoix invalide, veuillez réessayer.")

afficher_menu()