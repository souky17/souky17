x1 = float(input("x1 : "))
x2 = float(input("x2 : "))
x3 = float(input("x3 : "))

somme = x1 + x2 + x3
moyenne = somme / 3
minimum = min(x1, x2, x3)
maximum = max(x1, x2, x3)
mediane = somme - minimum - maximum
variance = ((x1 - moyenne)**2 + (x2 - moyenne)**2 + (x3 - moyenne)**2) / 3

print(f"Moyenne : {moyenne:.2f}")
print(f"Médiane : {mediane:.2f}")
print(f"Variance population : {variance:.2f}")