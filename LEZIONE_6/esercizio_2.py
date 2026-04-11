# Esercizio 2
#Modifico oggetto CSVFile in NumericalCSVFile

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
        lista = super().get_data()
        lista_float = []

        for riga in lista:
            try: 
                valori = [riga[0]] + [float(x) for x in riga[1:]]
                lista_float.append(valori)
            except ValueError:
                print("Questa riga contiene dati non numerici. La riga {} verrà ignorata.".format(riga))

        return lista_float
    
file = NumericalCSVFile("shampoo_sales.csv")
dati = file.get_data()

for r in dati:
    print(r)

