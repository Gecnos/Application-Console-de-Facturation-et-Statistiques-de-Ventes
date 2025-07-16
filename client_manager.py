
# client_manager.py
import pandas as pd
import os


def ajouter_client():
    dossier = "fichiers"
    fichiers = "Clients.xlsx"
    chemin = os.path.join(dossier, fichiers)

   
    df = pd.read_excel(chemin, index_col='code_client')
    code= df.index[-1]
    nbr = int(code[1:])
    code_new = f"C{nbr + 1:03d}"
    

    print("\nVoulez-vous enregistrer un nouveau client ?")
    print(f"\n le client {code_new} sera ajouté à la suite des clients existants")

    nom = input("\nEntrez le nom du client : ").strip()
    while True:
        contact = input("Entrez le contact du client : ").strip()
        if contact.isdigit():
            break
        print("Le contact doit contenir uniquement des chiffres.")
        

    while True:
        ifu = input("Entrez l'IFU du client : ").strip()

        if len(ifu) == 13 and ifu.isdigit():
            break
        print("L'IFU doit contenir 13 chiffres.")

    if not os.path.exists(chemin):
        df = pd.DataFrame(columns=['nom', 'contact', 'ifu'])
    else:
        df = pd.read_excel(chemin, index_col='code_client')
   
    if nom == "" or contact == "" or ifu == "":
        print("\nTous les champs doivent être remplis. Veuillez réessayer.")
        return  
    print("\nVoici les informations du nouveau client :")
    print(f"\nCode: {code_new}")
    print(f"\nNom: {nom}")
    print(f"\nContact: {contact}")
    print(f"\nIFU: {ifu}")
    while True:
        choix = input("\nVoulez-vous confirmer l'ajout ? (y/n) ").lower()
        if choix == 'y':
          df.loc[code_new] = [nom, contact, ifu]
          df.to_excel(chemin, index=True)
          print("\nLes informations du client ont été enregistrées avec succès.")
          break
            
        elif choix == 'n':
            print("\nL'enregistrement du client a été annulé.")
            break
        else:
            print("\nRéponse invalide. Veuillez répondre par 'y' ou 'n'.")
ajouter_client()
def recherche_client():
    dossier = "fichiers"
    fichiers = "Clients.xlsx"
    chemin = os.path.join(dossier, fichiers)
    df = pd.read_excel(chemin, index_col='code_client')
    #recherche d'un client
    while True: 
        code_client = input("\nEntrez le code du client à rechercher (ou 'q' pour quitter) : ").strip()
        if code_client.lower() == 'q':  
            print("Recherche annulée.")
            return

        if code_client in df.index:
            print("\nVoici les informations du client :")
            print(f"\nCode: {code_client}")
            print(f"\nNom: {df.loc[code_client, 'nom']}")
            print(f"\nContact: {df.loc[code_client, 'contact']}")
            print(f"\nIFU: {df.loc[code_client, 'ifu']}")
        else:
            print("Client non trouvé. Veuillez réessayer.")
            break
recherche_client()