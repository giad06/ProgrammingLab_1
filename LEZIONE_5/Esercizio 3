# Esercizio 3 (modifica Esercizio 1 della Lezione 5)

class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("Ciao sono", self.ruolo + ",", self.nome, self.cognome)


class Studente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.corsi = corsi

    def saluta(self):
        Persona.saluta(self)
        print("> Frequento i seguenti corsi:")
        for corso in self.corsi:
            print(" -", corso)


class Docente(Persona):
    def __init__(self, nome, cognome, corsi):
        super().__init__("Docente UNITS", nome, cognome)
        self.corsi = corsi

    def saluta(self):
        Persona.saluta(self)
        print("> Insegno i seguenti corsi:")
        for corso in self.corsi:
            print(" -", corso)


# verifica se un docente insegna tutti i corsi di uno studente
def insegna_corsi_studente(docente, studente):
    for corso in studente.corsi:
        if corso not in docente.corsi:
            return False
    return True

#Verifica che i corsi di uno studente siano tutti insegnati da almeno un docente (usando funzione precedente  )
def corsi_coperti_da_docenti(studente, docenti):
    for corso in studente.corsi:
        corso_coperto = False
         # creo uno studente “temporaneo” con un solo corso
        studente_temp = Studente(studente.nome, studente.cognome, [corso])
        for docente in docenti:
            if insegna_corsi_studente(docente, studente_temp):
                corso_coperto = True
                break
        if not corso_coperto:
            return False
    return True


corsi_studente = ["Programmazione", "Analisi", "Laboratorio"]
corsi_docente1 = ["Programmazione", "Laboratorio", "Analisi"]
corsi_docente2 = ["Analisi"]

studente = Studente("Irene", "Rossi", corsi_studente)
docente1 = Docente("Mario", "Grandi", corsi_docente1)
docente2 = Docente("Luigi", "Viola", corsi_docente2)

docenti = [docente1, docente2]

#Verifica algoritmo 1
print("\nVerifica se " + docente1.nome + " " + docente1.cognome + " insegna tutti i corsi dello studente:", 
      insegna_corsi_studente(docente1, studente))
print("Verifica se " + docente2.nome + " " + docente2.cognome + " insegna tutti i corsi dello studente:", 
      insegna_corsi_studente(docente2, studente))

#Verifica algoritmo 2
if corsi_coperti_da_docenti(studente, docenti):
    print("\nTutti i corsi dello studente sono insegnati da almeno un docente")
else:
    print("\nAlcuni corsi dello studente non sono insegnati da nessun docente")