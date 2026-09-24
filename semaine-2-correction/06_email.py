email = input("Courriel : ").strip().lower()

position = email.find("@")
identifiant = email[:position]
domaine = email[position + 1:]

print("Identifiant :", identifiant)
print("Domaine :", domaine)