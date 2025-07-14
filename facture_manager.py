import pandas as pd
from fpdf import FPDF
from num2words import num2words
from datetime import datetime
import os

PRODUITS_FILE = 'fichiers/Produits.xlsx'
CLIENTS_FILE = 'fichiers/Clients.xlsx'
HISTORIQUE_FILE = 'fichiers/HistoriqueFactures.xlsx'
CARTES_FILE = 'fichiers/CartesReduction.xlsx'
FACTURE_DIR = "factures/"
os.makedirs(FACTURE_DIR, exist_ok=True)


def selectionner_produits():
    produits_df = pd.read_excel(PRODUITS_FILE)
    print("\n--- Liste des Produits disponibles ---")
    print(produits_df[['code_produit', 'libelle', 'prix_unitaire']])
    produits_selectionnes = []

    while True:
        code = input("\nEntrez le code du produit à ajouter (ou 'fin' pour terminer) : ").strip()
        if code.lower() == 'fin':
            break
        if code not in produits_df['code_produit'].values:
            print(" Code produit introuvable.")
            continue
        try:
            quantite = int(input("Quantité : "))
            if quantite <= 0:
                print(" Quantité invalide.")
                continue
        except ValueError:
            print(" Veuillez entrer un nombre entier.")
            continue

        produit = produits_df[produits_df['code_produit'] == code].iloc[0]
        ligne_total = quantite * produit['prix_unitaire']

        produits_selectionnes.append({
            'code_produit': code,
            'libelle': produit['libelle'],
            'quantite': quantite,
            'prix_unitaire': produit['prix_unitaire'],
            'total': ligne_total
        })

        print(f" Produit {produit['libelle']} ajouté ({quantite} × {produit['prix_unitaire']} = {ligne_total} F)")
    return produits_selectionnes


def calculer_totaux(produits_selectionnes, taux_reduction=0, taux_tva=18):
    total_ht = sum(p['total'] for p in produits_selectionnes)
    montant_reduction = (total_ht * taux_reduction) / 100
    total_ht_reduit = total_ht - montant_reduction
    tva = (total_ht_reduit * taux_tva) / 100
    total_ttc = total_ht_reduit + tva

    return {
        'total_ht': total_ht,
        'reduction': montant_reduction,
        'total_ht_reduit': total_ht_reduit,
        'tva': tva,
        'total_ttc': total_ttc
    }


def choisir_client():
    clients_df = pd.read_excel(CLIENTS_FILE)
    print("\n--- Liste des Clients disponibles ---")
    print(clients_df[['code_client', 'nom', 'contact', 'IFU']])
    code = input("Entrez le code du client : ").strip()
    client = clients_df[clients_df['code_client'] == code].iloc[0]

    return {
        'code': client['code_client'],
        'nom': client['nom'],
        'contact': client['contact'],
        'ifu': client['IFU']
    }


def generer_facture_pdf(client, produits, totaux, num_facture):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    pdf.cell(100, 10, "Groupe Python Génial", ln=0)
    pdf.cell(0, 10, f"Date : {datetime.now().strftime('%d/%m/%Y')}", ln=1, align='R')

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Informations client :", ln=1)

    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Nom : {client['nom']}", ln=1)
    pdf.cell(0, 8, f"Contact : {client['contact']}", ln=1)
    pdf.cell(0, 8, f"IFU : {client['ifu']}", ln=1)

    pdf.ln(8)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, f"FACTURE n° {num_facture:06}", ln=1, align="C")

    pdf.ln(5)
    pdf.set_font("Arial", "B", 11)
    headers = ["N°", "Code Produit", "Libellé", "P.U", "Qté", "Total HT"]
    col_widths = [10, 35, 50, 25, 15, 30]

    for i, h in enumerate(headers):
        pdf.cell(col_widths[i], 8, h, 1, 0, "C")
    pdf.ln()

    pdf.set_font("Arial", "", 10)
    for idx, p in enumerate(produits, start=1):
        pdf.cell(col_widths[0], 8, str(idx), 1)
        pdf.cell(col_widths[1], 8, p['code_produit'], 1)
        pdf.cell(col_widths[2], 8, p['libelle'], 1)
        pdf.cell(col_widths[3], 8, f"{p['prix_unitaire']}", 1)
        pdf.cell(col_widths[4], 8, str(p['quantite']), 1)
        pdf.cell(col_widths[5], 8, f"{p['total']}", 1)
        pdf.ln()

    pdf.ln(5)
    resume_x = 120
    pdf.set_xy(resume_x, pdf.get_y())
    resume_data = [
        ("Total HT", totaux['total_ht']),
        ("Remise", totaux['reduction']),
        ("THT remise", totaux['total_ht_reduit']),
        ("TVA (18%)", totaux['tva']),
        ("Total TTC", totaux['total_ttc'])
    ]

    for label, value in resume_data:
        pdf.cell(40, 8, label, 1)
        pdf.cell(30, 8, f"{value:,.0f} F", 1, ln=1)

    pdf.ln(10)
    ttc_lettres = num2words(int(totaux['total_ttc']), lang='fr').capitalize()
    pdf.set_font("Arial", "I", 11)
    pdf.multi_cell(0, 10, f"Arrêtée, la présente facture à la somme de : {ttc_lettres} francs CFA")

    filename = os.path.join(FACTURE_DIR, f"facture_{num_facture:06}.pdf")
    pdf.output(filename)
    print(f"\n Facture générée : {filename}")


def enregistrer_historique(client, produits, totaux, num_facture):
    ligne = {
        'num_facture': f"{num_facture:06}",
        'date': datetime.now().strftime('%d/%m/%Y'),
        'code_client': client['code'],
        'nom': client['nom'],
        'total_ht': totaux['total_ht'],
        'reduction': totaux['reduction'],
        'total_ht_reduit': totaux['total_ht_reduit'],
        'tva': totaux['tva'],
        'total_ttc': totaux['total_ttc']
    }

    historique_df = pd.DataFrame([ligne])
    if os.path.exists(HISTORIQUE_FILE):
        ancien = pd.read_excel(HISTORIQUE_FILE)
        historique_df = pd.concat([ancien, historique_df], ignore_index=True)

    historique_df.to_excel(HISTORIQUE_FILE, index=False)
    print("Facture enregistrée dans l’historique.")


def verifier_et_ajouter_carte(client, total_ttc):
    if os.path.exists(CARTES_FILE):
        cartes_df = pd.read_excel(CARTES_FILE)
    else:
        cartes_df = pd.DataFrame(columns=['code_client', 'nom', 'contact', 'reduction'])

    if client['code'] in cartes_df['code_client'].values:
        print(f" Carte déjà existante pour {client['nom']}")
        return

    if not os.path.exists(HISTORIQUE_FILE):
        return

    historique_df = pd.read_excel(HISTORIQUE_FILE)
    nb_factures = historique_df[historique_df['code_client'] == client['code']].shape[0]

    if nb_factures < 2:
        print(f" Moins de 2 factures pour {client['nom']}, pas de carte générée.")
        return

    reduction = 0
    if total_ttc >= 300_000:
        reduction = 15
    elif total_ttc >= 200_000:
        reduction = 10
    elif total_ttc >= 100_000:
        reduction = 5

    if reduction == 0:
        print(f" Montant insuffisant pour carte ({total_ttc} F)")
        return

    nouvelle_carte = {
        'code_client': client['code'],
        'nom': client['nom'],
        'contact': client['contact'],
        'reduction': reduction
    }
    cartes_df = pd.concat([cartes_df, pd.DataFrame([nouvelle_carte])], ignore_index=True)
    cartes_df.to_excel(CARTES_FILE, index=False)
    print(f"Carte {reduction}% ajoutée pour {client['nom']}")


if __name__ == "__main__":
    client = choisir_client()
    produits = selectionner_produits()
    totaux = calculer_totaux(produits, taux_reduction=5)

    print("\n--- Totaux Calculés ---")
    print(f"Total HT : {totaux['total_ht']} F")
    print(f"Réduction : {totaux['reduction']} F")
    print(f"TVA : {totaux['tva']} F")
    print(f"Total TTC : {totaux['total_ttc']} F")

    num_facture = 1
    if os.path.exists(HISTORIQUE_FILE):
        historique_df = pd.read_excel(HISTORIQUE_FILE)
        if not historique_df.empty:
            dernier_num = historique_df['num_facture'].iloc[-1]
            try:
                num_facture = int(dernier_num) + 1
            except:
                num_facture = 1

    generer_facture_pdf(client, produits, totaux, num_facture)
    enregistrer_historique(client, produits, totaux, num_facture)
    verifier_et_ajouter_carte(client, totaux['total_ttc'])
