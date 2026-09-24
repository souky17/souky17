def nettoyer_nom(texte):
    return texte.strip().title()

def creer_identifiant(prenom, nom, annee):
    prenom = prenom.strip().lower()
    nom = nom.strip().lower()
    annee = annee.strip()
    return prenom[0] + nom + annee

def extraire_domaine(email):
    email = email.strip().lower()
    position = email.find("@")
    return email[position + 1:]

def nettoyer_telephone(tel):
    tel = tel.replace(" ", "")
    tel = tel.replace("-", "")
    tel = tel.replace("(", "")
    tel = tel.replace(")", "")
    return tel

def calculer_total(prix, quantite, taxe, rabais):
    sous_total = prix * quantite
    montant_taxe = sous_total * taxe
    return sous_total + montant_taxe - rabais

def convertir_secondes(total_secondes):
    heures = total_secondes // 3600
    reste = total_secondes % 3600
    minutes = reste // 60
    secondes = reste % 60
    return f"{heures} h {minutes} min {secondes} s"