# Esercizio 3

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
    
if __name__ == '__main__':
    file = CSVFile("shampoo_sales.csv")
    dati = file.get_data(start=3, end=6)
    print(dati)
