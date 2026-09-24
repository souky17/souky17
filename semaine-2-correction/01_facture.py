prix_unitaire = float(input("Prix unitaire : "))
quantite = int(input("Quantité : "))
taux_taxe = float(input("Taux de taxe : "))
rabais = float(input("Rabais : "))

sous_total = prix_unitaire * quantite
taxe = sous_total * taux_taxe
total_avant_rabais = sous_total + taxe
total_final = total_avant_rabais - rabais

print(f"Sous-total : {sous_total:.2f}")
print(f"Taxe : {taxe:.2f}")
print(f"Total final : {total_final:.2f}")
print("Total >= 100 :", total_final >= 100)