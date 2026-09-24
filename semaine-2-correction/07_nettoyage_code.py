telephone = input("Téléphone : ")
telephone = telephone.replace(" ", "")
telephone = telephone.replace("-", "")
telephone = telephone.replace("(", "")
telephone = telephone.replace(")", "")

code = input("Code cours : ").strip()
p1 = code.find("-")
p2 = code.find("-", p1 + 1)

numero = code[:p1]
programme = code[p1 + 1:p2]
groupe = code[p2 + 1:]

print("Téléphone :", telephone)
print("Numéro :", numero)
print("Programme :", programme)
print("Groupe :", groupe)