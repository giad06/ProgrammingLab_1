# Esercizio 2

class CSVFile:
    def __init__(self, filename):
        self.name = filename  # attributo con il nome del file

    def get_data(self):
        dati = []
        with open(self.name, 'r') as file:
            for riga in file:
                elementi = riga.strip().split(',')  # rimuovo spazi  e divido la riga in elementi
                dati.append(elementi)
        return dati # restituisce una lista di liste, dove ogni sotto-lista rappresenta una riga del file CSV
    
file_csv = CSVFile('shampoo_sales.csv')
contenuto = file_csv.get_data()
print("Dati CSV:")
for riga in contenuto:
    print(riga)
#ogni elemento della lista sarà una riga del file, e ogni riga sarà a sua volta una lista di elementi (data, sales)