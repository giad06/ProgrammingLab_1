# Esercizio 1

def lista_dispari(lista):
    lista_disp= [n for n in lista if n%2!=0]
    return lista_disp

lista=[]
print("Inserisci una lista di numeri, 0 per finire\n")

while True:
    x = int(input())
    if x==0:
        break
    else:
        lista.append(x)
print(f"La lista dei numeri dispari è: {lista_dispari(lista)}")
    
