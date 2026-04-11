# Esercizio 6

while True:
    x=input("Inserisci un numero intero: ")
    try:
        x=int(x) #provo a convertire in int ( input() restituisce stringa )
        quadrato = x**2
        print(f"Il quadrato è {x**2}")
        break
    except ValueError:
        print("Hai inserito un valore non valido!")