# Esercizio 7

def leggi_due_numeri():
    while True:
        try:
            x = float(input("Primo numero: "))
            y = float(input("Secondo numero: "))
            return x, y
        except ValueError:
            print("Errore: devi inserire numeri validi.\n")

def somma():
    print("Hai scelto la somma!\n Inserisci 2 numeri da sommare!")
    x, y = leggi_due_numeri()
    return x+y

def differenza():
    print("Hai scelto la differenza!\n Inserisci 2 numeri da sottrarre!")
    x, y = leggi_due_numeri()
    return x-y

print("Il Menu è:\n" \
      "1: Calcola la somma tra due numeri\n" \
      "2: Calcola la differenza tra 2 numeri\n" \
      "3: Esci dal menu\n")


while True:
    print("Scegli un'opzione tra 1,2 o 3: \n")
    while True:
        n=input()
        try:
            n=int(n)
            break
        except ValueError:
            print("Hai inserito un valore non valido, prova a mettere un numero intero\n")
    if n not in (1,2,3):
        print("Hai inserito un valore non valido, riguarda il menu e scegli di nuovo!")
        continue # torno al menu
    if n==1:
        print(f"La somma tra i due numeri è: {somma()}\n")
    if n==2:
        print(f"La differenza tra i due numeri è: {differenza()}")
    if n==3:
        print("Sei uscito correttamente!\n")
        break





