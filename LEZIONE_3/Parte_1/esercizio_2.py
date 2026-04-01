# Esercizio 2

def is_palindromo(testo):
      testo_invertito = testo[::-1]
      return testo == testo_invertito #TRUE se palindromo, FALSE altrimenti

parola = input("Inserisci una parola o frase: ")
if is_palindromo(parola):
    print("È un palindromo")
else:
    print("Non è un palindromo")