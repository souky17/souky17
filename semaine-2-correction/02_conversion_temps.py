total_secondes = int(input("Durée en secondes : "))

heures = total_secondes // 3600
reste = total_secondes % 3600
minutes = reste // 60
secondes = reste % 60

print(f"{heures} h {minutes} min {secondes} s")