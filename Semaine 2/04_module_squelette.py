# 04_module_squelette.py
# Renommer utils_texte_squelette.py en utils_texte.py avant d'exécuter.

import utils_texte

nom = utils_texte.nettoyer_nom("  sara qarboua  ")
identifiant = utils_texte.creer_identifiant("Sara", "Qarboua", "1986")
domaine = utils_texte.extraire_domaine("sara@lacite.ca")

print(nom)
print(identifiant)
print(domaine)
