# Esercizio 1

class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print('Ciao sono', self.ruolo + ",", self.nome, self.cognome)

class Studente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi = corsi #lista dei corsi che frequenta lo studente

    def saluta(self):
        Persona.saluta(self)
        print("> Frequento i seguenti corsi: ")
        for corso in self.corsi:     
            print("  - ", corso)

class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi #lista dei corsi che insegna il docente

    def saluta(self):
        Persona.saluta(self)
        print("> Insegno i seguenti corsi: ")
        for corso in self.corsi:     
            print("  - ", corso)


corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]
obj_Irene = Studente("Irene", "Rossi", corsi)
obj_Irene.saluta()
