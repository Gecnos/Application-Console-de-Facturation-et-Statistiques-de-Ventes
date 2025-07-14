import pandas as pd
from fpdf import FPDF
from num2words import num2words
from datetime import datetime
import os

PRODUITS_FILE = 'fichiers/Produits.xlsx'
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

def generer_facture_pdf(client, produits, totaux, num_facture):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    # En-tête
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

    # Tableau des produits
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

    # Résumé total
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

    # Ligne modifiée pour éviter OverflowError
    pdf.ln(10)
    ttc_lettres = num2words(int(totaux['total_ttc']), lang='fr').capitalize()
    pdf.set_font("Arial", "I", 11)
    pdf.multi_cell(0, 10, f"Arrêtée, la présente facture à la somme de : {ttc_lettres} francs CFA")

    filename = os.path.join(FACTURE_DIR, f"facture_{num_facture:06}.pdf")
    pdf.output(filename)
    print(f"\n Facture générée : {filename}")

# Test manuel
if __name__ == "__main__":
    produits = selectionner_produits()
    totaux = calculer_totaux(produits, taux_reduction=5)

    print("\n--- Totaux Calculés ---")
    print(f"Total HT : {totaux['total_ht']} F")
    print(f"Réduction : {totaux['reduction']} F")
    print(f"TVA : {totaux['tva']} F")
    print(f"Total TTC : {totaux['total_ttc']} F")

    client_exemple = {
        'nom': "Dupont SA",
        'contact': "97 00 00 00",
        'ifu': "1234567890123"
    }

    generer_facture_pdf(client_exemple, produits, totaux, num_facture=1)
