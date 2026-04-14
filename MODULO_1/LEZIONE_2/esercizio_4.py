# Esercizio 4

def ripetizioni_lettera(parola, lettera):
    count = 0
    for i in parola:
        if i == lettera:
            count += 1
    return count

parola = input("Inserisci una parola: ")
lettera = input("Inserisci una lettera: ")

print("La lettera inserita si ripete",ripetizioni_lettera(parola, lettera), "volte nella parola") 