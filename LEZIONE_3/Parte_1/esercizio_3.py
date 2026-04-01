# Esercizio 3

def scambia_elementi(A, i, j):
    A[i], A[j] = A[j], A[i]  # scambio elemento i-esimo con elemento j-esimo e viceversa
    return A

lista = [1, 2, 3, 4]
print("Lista originale:", lista)
scambia_elementi(lista, 1, 3) #i=1, j=3 (scambierà 2 con 4)
print("Lista dopo lo scambio:", lista)
