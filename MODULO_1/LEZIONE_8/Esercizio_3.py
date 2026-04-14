# Esercizio 3

def crea_lista():
    lista=[]
    print("Inserisci una lista di numeri, 0 per finire")

    while True:
        x = int(input())
        if x == 0:
            break
        lista.append(x)
    return lista

def prodotto_liste(lista_1, lista_2):
    prodotto = [x*y for x in lista_1 for y in lista_2 if x*y>10]
    if  not prodotto:
        print("Nessun prodotto era maggiore di 10!")
        return None
    return prodotto

print("Crea la prima lista")
lista_1 = crea_lista()

print("Crea la seconda lista")
lista_2 = crea_lista()

prod= prodotto_liste(lista_1, lista_2)
if prod is not None:
    print(f"La lista contenente il prodotto tra gli elementi delle liste è: {prod} ")

