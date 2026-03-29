# Esercizio esempio

#Lancia una moneta e stampa se è uscita testa o croce
import random

class Coin:
    def __init__(self, faccia):
        self.faccia = faccia

    def lanciare(self):
        if random.randint(0,1) == 0:
            self.faccia = 'testa'
        else:
            self.faccia = 'croce'

    def che_faccia(self):
        return self.faccia

moneta = Coin('testa')
moneta.lanciare()
print(moneta.che_faccia())