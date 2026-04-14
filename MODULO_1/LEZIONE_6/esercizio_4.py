# Esercizio 4

class CSVFile:
    def __init__(self, filename):
        if type(filename) != str:
            raise TypeError("Il nome del file deve essere una stringa.")
        self.name = filename

    def get_data(self, start = None, end = None):
        dati = []

    #Apro il file
        with open(self.name, "r") as file:
            for riga in file:
                elementi = riga.strip().split(',') # rimuovo newline finale e divido riga
                dati.append(elementi)

        total_len = len(dati)

    #Sanitizzo input
        if start == None:
            start = 1

        if end == None:
            end = total_len

    # Controlli di tipo
        if type(start) != int or type(end) != int:
            raise TypeError("I valori di start e end devono essere interi.")

    # Sanitizzazione dei limiti
        if start < 1:
            print("Start troppo piccolo, imposto start = 1")
            start = 1

        if end > total_len:
            print("End troppo grande, imposto end =", total_len)
            end = total_len

        if start > end:
            raise ValueError("Start non può essere maggiore di end.")
        
        return dati[start-1:end]

#NumericalCSVFile eredita da CSVFile (estensione piu robusta)

class NumericalCSVFile(CSVFile):
    def get_data(self, *args, **kwargs): #Per poter ereditare qualsiasi combinazione di parametri        lista = super().get_data(*args, **kwargs) 
        lista = super().get_data(*args,**kwargs)
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