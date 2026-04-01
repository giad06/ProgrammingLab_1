# Esercizio 2
#Modifico oggetto CSVFile in NumericalCSVFile

#Esercizio 1
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

#NumericalCSVFile eredita da CSVFile

class NumericalCSVFile(CSVFile):
    def get_data(self):
        dati_originari= super().get_data()
        dati_numerici = []

        for riga in dati_originari:
            try:
                nuova_riga = [riga[0]]  # la data resta stringa

                for valore in riga[1:]:
                    nuova_riga.append(float(valore))

                dati_numerici.append(nuova_riga)

            except ValueError:
                print(f"Errore di conversione nella riga: {riga} -> valore non numerico")
                continue

        return dati_numerici

file = NumericalCSVFile("shampoo_sales.csv")
dati = file.get_data()

for r in dati:
    print(r)

