# Esercizio 2 (Modifica esercizio veicolo della lezione 4)

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


class Auto(Veicolo): #sottoclasse di Veicolo (aggiunge numero di porte)
    def __init__(self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte

    def __str__(self):
        return f"{self.marca} {self.modello} {self.anno} - {self.speed} km/h con {self.numero_porte} porte"


class Moto(Veicolo): #sottoclasse di Veicolo (aggiunge tipo di moto)
    def __init__(self, modello, marca, anno, tipo):
        super().__init__(modello, marca, anno)
        self.tipo = tipo

    def __str__(self):
        return f"{self.marca} {self.modello} {self.anno} - {self.speed} km/h di tipo {self.tipo}"


# creazione oggetti
auto = Auto("Giulia", "Alfa Romeo", 2020, 4)
moto = Moto("CBR600", "Honda", 2022, "sportiva")

print(auto)
print(moto)

#provo metodi
auto.accelerare()
auto.accelerare()
auto.frenare()
print(auto)


moto.frenare()
moto.accelerare()
print(moto)

