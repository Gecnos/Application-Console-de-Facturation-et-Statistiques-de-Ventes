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
    print("\n Liste des Produits disponibles")
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
    print("\n Liste des Clients disponibles")
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
    pdf.set_auto_page_break(auto=True, margin=15)

    # En-tête
    pdf.set_font("Arial", "B", 14)
    pdf.cell(100, 10, "Groupe numéro 8", ln=1)
    pdf.set_font("Arial", "", 10)
    pdf.cell(100, 6, "AWADJIHE Régina", ln=1)
    pdf.cell(100, 6, "AGBODO Fiacresse", ln=1)
    pdf.cell(100, 6, "DAYE KANLISOU Gildas", ln=1)
    pdf.cell(100, 6, "OLOULADE Ornelie", ln=1)
    pdf.cell(100, 6, "HOUEHO Vianney", ln=1)

    # Date à droite
    pdf.set_xy(130, 10)
    pdf.set_font("Arial", "", 10)
    pdf.cell(60, 6, f"Date d'émission : {datetime.now().strftime('%d/%m/%Y')}", ln=1)

    # Bloc destinataire
    pdf.set_xy(10, 50)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "Destinataire", ln=1)
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, "Entreprise", ln=1)
    pdf.cell(0, 6, f"{client['nom']}", ln=1)
    pdf.cell(0, 6, f"{client['contact']}", ln=1)
    pdf.cell(0, 6, f"IFU : {client['ifu']}", ln=1)
    pdf.cell(0, 6, "", ln=1)

    # Titre
    pdf.ln(5)
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, f"Facture Proforma n°{num_facture:06}", ln=1, align="C")

    # Tableau des produits
    pdf.set_font("Arial", "B", 10)
    headers = ["Désignation", "Quantité", "Unité", "Prix unitaire HT", "TVA", "TOTAL HT"]
    col_widths = [60, 25, 20, 35, 20, 30]

    for i, h in enumerate(headers):
        pdf.cell(col_widths[i], 8, h, 1, 0, 'C')
    pdf.ln()

    pdf.set_font("Arial", "", 10)
    for p in produits:
        pdf.cell(col_widths[0], 8, p['libelle'], 1)
        pdf.cell(col_widths[1], 8, str(p['quantite']), 1, 0, 'C')
        pdf.cell(col_widths[2], 8, "pce", 1, 0, 'C')
        pdf.cell(col_widths[3], 8, f"{p['prix_unitaire']:.0f} F", 1, 0, 'R')
        pdf.cell(col_widths[4], 8, "18%", 1, 0, 'C')
        pdf.cell(col_widths[5], 8, f"{p['total']:.0f} F", 1, 0, 'R')
        pdf.ln()

    # Résumé des totaux
    pdf.ln(5)
    resume_x = 135
    pdf.set_xy(resume_x, pdf.get_y())
    resume_data = [
        ("Total HT", totaux['total_ht']),
        ("Remise", totaux['reduction']),
        ("THT remise", totaux['total_ht_reduit']),
        ("TVA (18%)", totaux['tva']),
        ("Frais de port", 0),
        ("Total TTC", totaux['total_ttc'])
    ]

    pdf.set_font("Arial", "", 10)
    for label, value in resume_data:
        pdf.cell(40, 8, label, 0)
        pdf.cell(30, 8, f"{value:,.0f} F", 0, ln=1, align='R')
        pdf.set_x(resume_x)

    # Montant en lettres
    pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    ttc_lettres = num2words(int(totaux['total_ttc']), lang='fr').capitalize()
    pdf.multi_cell(0, 8, f"Arrêtée, la présente facture à la somme de : {ttc_lettres} francs CFA")

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

    nouvelle_ligne_df = pd.DataFrame([ligne])

    if os.path.exists(HISTORIQUE_FILE):
        try:
            ancien_df = pd.read_excel(HISTORIQUE_FILE)
            ancien_df = ancien_df[ancien_df.columns.intersection(nouvelle_ligne_df.columns)]
            historique_df = pd.concat([ancien_df, nouvelle_ligne_df], ignore_index=True)
            historique_df.dropna(how='all', inplace=True)
            historique_df.drop_duplicates(subset=['num_facture', 'code_client'], keep='last', inplace=True)
            if 'num_facture' in historique_df.columns:
                historique_df['num_facture'] = historique_df['num_facture'].astype(str)
                historique_df = historique_df.sort_values(by='num_facture')
        except Exception as e:
            print(f"Erreur lecture historique : {e}")
            historique_df = nouvelle_ligne_df
    else:
        historique_df = nouvelle_ligne_df

    for col in ['total_ht', 'reduction', 'total_ht_reduit', 'tva', 'total_ttc']:
        if col in historique_df.columns:
            historique_df[col] = pd.to_numeric(historique_df[col], errors='coerce')
            historique_df[col] = historique_df[col].apply(lambda x: f"{x:,.0f} F" if pd.notnull(x) else '')

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



