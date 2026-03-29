# Esercizio 5

def rimuovi_duplicati(file):
    righe_uniche = [] #lista vuota in cui inserirò le righe uniche del file
    with open(file, 'r') as file_considerato: # apro il file in modalità lettura
        for riga in file_considerato:
            if riga not in righe_uniche:  # aggiunge la riga solo se non è già presente
                righe_uniche.append(riga)
    
    with open('unique.txt', 'w') as file_output: #apro file unique.txt in modalità scrittura
        for riga in righe_uniche:
            file_output.write(riga) 

nome_file = "prova.txt"
rimuovi_duplicati(nome_file)

