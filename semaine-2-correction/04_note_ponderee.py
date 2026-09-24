quiz = float(input("Quiz : "))
tp = float(input("TP : "))
devoir = float(input("Devoir : "))

note_finale = quiz * 0.20 + tp * 0.35 + devoir * 0.45
reussite = note_finale >= 60

print(f"Note finale : {note_finale:.2f}")
print("Réussite :", reussite)