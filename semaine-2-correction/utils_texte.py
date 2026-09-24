def nettoyer_nom(texte):
    return texte.strip().title()

def initiales(prenom, nom):
    return prenom.strip()[0].upper() + nom.strip()[0].upper()

def creer_identifiant(prenom, nom, annee):
    prenom = prenom.strip().lower()
    nom = nom.strip().lower()
    annee = annee.strip()
    return prenom[0] + nom + annee

def extraire_domaine(email):
    email = email.strip().lower()
    position = email.find("@")
    return email[position+1:]

def nettoyer_telephone(telephone):
    telephone = telephone.replace(" ", "")
    telephone = telephone.replace("-", "")
    telephone = telephone.replace("(", "")
    telephone = telephone.replace(")", "")
    return telephone
