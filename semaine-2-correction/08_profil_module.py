import utils_tp

prenom = input("Prénom : ")
nom = input("Nom : ")
annee = input("Année : ")
email = input("Courriel : ")
telephone = input("Téléphone : ")
prix = float(input("Prix : "))
quantite = int(input("Quantité : "))

prenom_propre = utils_tp.nettoyer_nom(prenom)
nom_propre = utils_tp.nettoyer_nom(nom)
identifiant = utils_tp.creer_identifiant(prenom, nom, annee)
domaine = utils_tp.extraire_domaine(email)
telephone_nettoye = utils_tp.nettoyer_telephone(telephone)
total = utils_tp.calculer_total(prix, quantite, 0.13, 0)

print("--- Profil ---")
print(f"Nom : {prenom_propre} {nom_propre}")
print(f"Identifiant : {identifiant}")
print(f"Domaine : {domaine}")
print(f"Téléphone : {telephone_nettoye}")
print(f"Total exemple : {total:.2f}")