# Esercizio 4

def conteggio(file):
    dizionario = {}
    with open(file, 'r') as file_considerato:
        for riga in file_considerato:
            elementi = riga.split(",") # divido la riga in elementi separati da virgola
            for elem in elementi:
                elem_pulito = elem.strip() # rimuovo spazi extra rispetto all'elemento
                if elem_pulito in dizionario: 
                    dizionario[elem_pulito] += 1
                else:
                    dizionario[elem_pulito] = 1 
                # se l'elemento è già presente nel dizionario, incremento il suo conteggio
                # altrimenti, lo aggiungo al dizionario e lo conto come primo
    return dizionario

nome_file = "shampoo_sales.csv"
risultato = conteggio(nome_file)
for parola, occorrenze in risultato.items():
    print(f"'{parola}' appare {occorrenze} volta/e nel file.")