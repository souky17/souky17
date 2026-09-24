prenom = input("Prénom : ").strip().lower()
nom = input("Nom : ").strip().lower()
annee = input("Année : ").strip()

identifiant = prenom[0] + nom + annee
print("Identifiant :", identifiant)
print("Longueur :", len(identifiant))