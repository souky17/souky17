# ============================================================
# 030464 - Correction professeur
# Analyse de trois temps de réponse
# Notions utilisées : variables, str, float, opérateurs,
# comparaisons, fonctions simples. Pas de if, pas de boucle.
# ============================================================

# Partie ENTREES
# input() lit toujours une chaîne de caractères str.
nom1 = input("Nom du serveur 1 : ")
nom2 = input("Nom du serveur 2 : ")
nom3 = input("Nom du serveur 3 : ")

# float() convertit la saisie en nombre décimal.
x1 = float(input("Temps du serveur 1 en ms : "))
x2 = float(input("Temps du serveur 2 en ms : "))
x3 = float(input("Temps du serveur 3 en ms : "))

# Partie TRAITEMENT

# Afficher les observations.
print(nom1, ":", x1, "ms")
print(nom2, ":", x2, "ms")
print(nom3, ":", x3, "ms")

# Vérifier les types.
print("Type de nom1 :", type(nom1))   # str
print("Type de x1 :", type(x1))       # float

# Comparaisons relationnelles.
# == produit True si les deux valeurs sont égales, False sinon.
print("x1 == x2 :", x1 == x2)
print("x1 == x3 :", x1 == x3)
print("x2 == x3 :", x2 == x3)

print("x1 < x2 :", x1 < x2)
print("x1 > x2 :", x1 > x2)

# Somme et moyenne.
somme = x1 + x2 + x3
moyenne = somme / 3

# Minimum et maximum.
minimum = min(x1, x2, x3)
maximum = max(x1, x2, x3)

# Médiane de trois valeurs.
# Pour trois valeurs : médiane = somme - minimum - maximum.
mediane = somme - minimum - maximum

# Mode.
# Hypothèse de l’exercice : exactement deux valeurs sont identiques.
# Dans ce cas précis, avec trois valeurs, le mode est aussi la médiane.
mode = mediane

# Écarts absolus à la moyenne.
ecart1 = abs(x1 - moyenne)
ecart2 = abs(x2 - moyenne)
ecart3 = abs(x3 - moyenne)

# Écart moyen absolu.
ecart_moyen = (ecart1 + ecart2 + ecart3) / 3

# Variance de population.
# ** 2 signifie « au carré ».
variance = ((x1 - moyenne) ** 2 + (x2 - moyenne) ** 2 + (x3 - moyenne) ** 2) / 3

# Partie SORTIES
print()
print("--- Résumé statistique ---")
print("Minimum :", minimum)
print("Maximum :", maximum)
print("Moyenne :", round(moyenne, 2))
print("Médiane :", round(mediane, 2))
print("Mode :", round(mode, 2))
print("Écart moyen :", round(ecart_moyen, 2))
print("Variance :", round(variance, 2))
