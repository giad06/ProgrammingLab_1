# Esercizio 1

def conta_occorrenze(lista):
    """
    Restituisce un dizionario con il conteggio delle occorrenze
    di ogni elemento nella lista.
    """
    dizionario = {}
    for parola in lista:
        if parola in dizionario:
            dizionario[parola] += 1
        else:
            dizionario[parola] = 1
    return dizionario

lista_parole = ["verde", "verde", "blu", "rosso", "rosso", "rosso", "giallo"]
conteggio = conta_occorrenze(lista_parole)
print("Conteggio delle occorrenze:", conteggio) 