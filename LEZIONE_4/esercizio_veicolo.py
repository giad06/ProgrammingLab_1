# Esercizio 1

class Veicolo:

    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0

    def __str__(self):
        return f"{self.marca} {self.modello} {self.anno} - {self.speed} km/h"
    
    def accelerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed
    
def vai(auto): #funzione prova per far accelerare 5 voltw e frenare una 
    for i in range(5):
        auto.accelerare()
    auto.frenare()
    print("Velocità corrente:", auto.get_speed(), "km/h")

macchina = Veicolo('Panda', 'Fiat', 2020)
vai(macchina)
print(macchina) #Stampo dati macchina
