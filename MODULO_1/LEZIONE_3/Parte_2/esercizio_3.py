# Esercizio 3

def conta_parola(file, parola):
    conteggio = 0
    with open(file, 'r') as file_considerato:
        for riga in file_considerato:
            elementi = riga.split(",") 
            for elem in elementi:
                if elem.strip() == parola:
                    conteggio += 1
    return conteggio

nome_file = "shampoo_sales.csv"
parola_da_cercare = "Date"
occorrenze = conta_parola(nome_file, parola_da_cercare)
print(f"La parola '{parola_da_cercare}' appare {occorrenze} volte nel file.")