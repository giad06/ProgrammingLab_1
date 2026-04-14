# Esercizio 2

def somma(file):
    totale = 0.0
    with open(file, 'r') as file_considerato:
        next(file_considerato)  # salto la riga di intestazione "Date,Sales"
        for riga in file_considerato:
            elementi = riga.split(",")    # divido la riga in [data, valore]
            valore = float(elementi[1].strip()) # prendo il secondo elemento (Sales) e lo converto in numero
            totale += valore
    return totale

nome_file = "shampoo_sales.csv"
risultato = somma(nome_file)
print(f"La somma totale delle vendite è: {risultato: .2f}")