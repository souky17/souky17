import utils_texte

nom_complet = input("Nom complet Prénom Nom : ").strip()
courriel = input("Courriel : ").strip()
telephone = input("Téléphone : ").strip()
code_cours = input("Code de cours : ").strip()
annee = input("Année de naissance : ").strip()

prenom, nom = nom_complet.split(" ")

prenom_normalise = utils_texte.nettoyer_nom(prenom)
nom_normalise = utils_texte.nettoyer_nom(nom)

ini = utils_texte.initiales(prenom, nom) if hasattr(utils_texte, "initiales") else prenom[0].upper() + nom[0].upper()
identifiant = utils_texte.creer_identifiant(prenom, nom, annee)
domaine = utils_texte.extraire_domaine(courriel)
telephone_nettoye = utils_texte.nettoyer_telephone(telephone)
dossier = nom.strip().lower() + "_" + prenom.strip().lower() + "_" + code_cours.strip().lower()

print("--- Fiche profil étudiant ---")
print(f"Nom : {prenom_normalise} {nom_normalise}")
print(f"Initiales : {ini}")
print(f"Identifiant : {identifiant}")
print(f"Domaine courriel : {domaine}")
print(f"Téléphone : {telephone_nettoye}")
print(f"Dossier dépôt : {dossier}")
