#Esercizio 9

def conta_vocali(testo):
    vocali = ["a", "e", "i", "o", "u"]
    totale = 0

    for carattere in testo:
        if carattere in vocali:
            totale = totale + 1

    return totale

parola = input("Inserisci una parola: ")
print(conta_vocali(parola))
