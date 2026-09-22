# 03_calcul_surface.py
# Objectif : lire deux valeurs et calculer une surface

longueur = float(input("Longueur : "))
largeur = float(input("Largeur : "))

surface = longueur * largeur
perimetre = 2 * (longueur + largeur)

print("Surface :", surface)
print("Périmètre :", perimetre)
