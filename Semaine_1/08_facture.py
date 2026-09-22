# 08_facture.py
# Objectif : programme intégrateur avec variables, types, opérateurs et arrondi

prix = float(input("Prix d’un article : "))
quantite = int(input("Quantité : "))
taux_taxe = 0.13

sous_total = prix * quantite
montant_taxe = sous_total * taux_taxe
total = sous_total + montant_taxe
total = round(total, 2)

print("Sous-total :", sous_total)
print("Taxe :", montant_taxe)
print("Total :", total)
