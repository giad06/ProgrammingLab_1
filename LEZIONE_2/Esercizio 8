#Esercizio 8

# verifica se i lati possono formare un triangolo
def triangolo(l1, l2, l3):
    # controllo se è un triangolo
    if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
        # è un triangolo, ora classificazione
        if l1 == l2 == l3:
            print("È un triangolo equilatero")
        elif l1 == l2 or l1 == l3 or l2 == l3:
            print("È un triangolo isoscele")
        elif l1**2 + l2**2 == l3**2 or l1**2 + l3**2 == l2**2 or l2**2 + l3**2 == l1**2:
            print("È un triangolo rettangolo")
        else:
            print("È un triangolo scaleno")
    else:
        print("Non è un triangolo")



a = int(input("Primo lato: "))
b = int(input("Secondo lato: "))
c = int(input("Terzo lato: "))

triangolo(a, b, c)