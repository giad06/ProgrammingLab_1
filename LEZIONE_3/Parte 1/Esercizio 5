# Esercizio 5

def numeri_in_parole(lista):
    """
    Trasforma una lista di numeri interi da 0 a 9
    in una lista dei loro nomi in italiano
    """
    dizionario_nomi = {
        0: "Zero", 1: "Uno", 2: "Due", 3: "Tre", 4: "Quattro",
        5: "Cinque", 6: "Sei", 7: "Sette", 8: "Otto", 9: "Nove"
    }

    parole = [] #lista vuota in cui inserirò nomi dei numeri
    for numero in lista:
        parole.append(dizionario_nomi[numero]) #finchè c'è un numero, trasformo in parols e lo aggiungo alla nuova lista    
    
    return parole

lista_numeri = [1, 0, 7, 9, 8]
conversione = numeri_in_parole(lista_numeri)
print("Numeri convertiti in parole:", conversione)