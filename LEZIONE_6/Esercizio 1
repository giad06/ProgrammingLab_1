# Esercizio 1

class CSVFile:
    def __init__(self, filename):
        self.name = filename

    def get_data(self):
        dati = []
        try:
            with open(self.name, 'r') as file:
                for riga in file:
                    elementi = riga.strip().split(',')
                    dati.append(elementi)
        except FileNotFoundError:
            print(f"Errore: il file '{self.name}' non esiste.")
            return []
        return dati
    