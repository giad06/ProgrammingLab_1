# Esercitazione 1

class ExamException(Exception):
    pass

def crea_lista():
    lista=[]
    print("Inserisci una lista di numeri, 0 per finire")

    while True:
        x = int(input())
        if x == 0:
            break
        lista.append(x)
    return lista

class MovingAverage:

    def __init__(self, window_length):
        # Controllo tipo
        if not isinstance(window_length, int):
            raise ExamException("La lunghezza della finestra deve essere un intero!")

        # Controllo valore
        if window_length <= 0:
            raise ExamException("La lunghezza della finestra deve essere positiva!")
        
        self.window_length = window_length


    def compute(self, serie):

         # Controllo che sia una lista
        if not isinstance(serie, list):
            raise ExamException("Il dato in input non è una lista!")

        # Controllo che gli elementi siano numeri
        for x in serie:
            if not isinstance(x, (int, float)):
                raise ExamException("La lista contiene elementi non numerici!")

        # Controllo lunghezza minima
        if len(serie) < self.window_length:
            raise ExamException("La lista è troppo corta!")
        
        lista_medie = []
        for i in range(len(serie) - self.window_length + 1):
            finestra = serie[i : i + self.window_length]
            media = sum(finestra) / self.window_length
            lista_medie.append(round(media, 1))
            
        return lista_medie
    
lista = crea_lista()
print(f"La lista è: {lista}")
media_mobile = MovingAverage(int(input("Inserisci dimensione finestra: ")))
print(f"La media mobile della lista è : {media_mobile.compute(lista)}")

        

        