# Esercizio 4

# Classe base Poligono
class Poligono:
    def __init__(self, num_lati):
        self.num_lati = num_lati

    def descrizione(self):
        return f"Sono un poligono con {self.num_lati} lati"

# Sottoclasse Quadrilatero
class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)  # un quadrilatero ha sempre 4 lati

    def descrizione(self):
        return "Sono un quadrilatero"
    
# Sottoclasse Rettangolo di Quadrilatero
class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza

    def descrizione(self):
        return f"Sono un rettangolo con base {self.base} e altezza {self.altezza}"

    def perimetro(self):
        return 2 * (self.base + self.altezza)

    def area(self):
        return self.base * self.altezza
    
# Classe Triangolo
class Triangolo(Poligono):
    def __init__(self, lato1, lato2, lato3):
        super().__init__(3)
        self.lati = [lato1, lato2, lato3]

    def descrizione(self):
        return f"Sono un triangolo con lati {self.lati[0]}, {self.lati[1]}, {self.lati[2]}"

    def perimetro(self):
        return sum(self.lati)

    def is_equilatero(self):
        return self.lati[0] == self.lati[1] == self.lati[2]
    

print(Poligono(6).descrizione())
print(Quadrilatero().descrizione())

rett = Rettangolo(5, 3)
print(rett.descrizione(), "Perimetro:", rett.perimetro(), "Area:", rett.area())

triang = Triangolo(4, 4, 4)
print(triang.descrizione(), "Perimetro:", triang.perimetro(), "Equilatero?", "Si" if triang.is_equilatero() else "No")