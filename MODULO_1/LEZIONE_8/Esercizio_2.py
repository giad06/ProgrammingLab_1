#Esercizio 2

def compatta_lista(lista_principale):
    lista_compatta= [x for lista in lista_principale for x in lista]
    return lista_compatta


n=int(input("Quante liste vuoi che contenga la lista?"))
lista= []
for i in range(n):
    print(f"Inserisci la lista {i+1}")
    print("Inserisci gli elementi, 0 per terminare\n")
    lista_interna = []
    while True:
        x=int(input())
        if x == 0:
            break
        lista_interna.append(x)
    lista.append(lista_interna)

print(f"La lista non compatta è: {lista}")
print(f"La lista compatta è: {compatta_lista(lista)}")
