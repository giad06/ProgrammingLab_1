# Esercizio 5

from datetime import datetime, timedelta

mesi = {
    'gennaio': 1, 'febbraio': 2, 'marzo': 3, 'aprile': 4,
    'maggio': 5, 'giugno': 6, 'luglio': 7, 'agosto': 8,
    'settembre': 9, 'ottobre': 10, 'novembre': 11, 'dicembre': 12
}

#INPUT DATA DI NASCITA
print("Giorno:")
giorno = int(input()) #input() restituisce una stringa, quindi cast in intero con int()
print("Mese (in lettere, es. Marzo):")
mese = mesi[input().lower()] 
print("Anno:")
anno = int(input())

data_nascita = datetime(anno, mese, giorno) #datetime è una classe che rappresenta una data e un'ora, in questo caso usiamo solo la data
print(f"\nLa data di nascita è: {giorno}/{mese}/{anno}\n")

#DATA ATTUALE
oggi = datetime.now() #datetime.now() restituisce la data e l'ora attuali del sistema, in questo caso usiamo solo la data
print(f"Oggi è il: {oggi.day}/{oggi.month}/{oggi.year}\n") #day, month e year sono attributi della classe datetime 


def calcola_eta(data_nascita, oggi):
    eta = oggi.year - data_nascita.year
    if (oggi.month, oggi.day) < (data_nascita.month, data_nascita.day): 
        eta -= 1
    return eta

eta = calcola_eta(data_nascita, oggi)
print(f"Hai {eta} anni.\n")

# TEMPO AL PROSSIMO COMPLEANNO
def tempo_al_prossimo_compleanno(data_nascita, oggi):
    prossimo = datetime(oggi.year, data_nascita.month, data_nascita.day) #

    # se il compleanno di quest’anno è già passato, il prossimo compleanno sarà l’anno prossimo
    if prossimo < oggi: 
        prossimo = datetime(oggi.year + 1, data_nascita.month, data_nascita.day)

    delta = prossimo - oggi #se è gia passato, calcolo la differenza tra il prossimo compleanno (l’anno prossimo) e oggi, altrimenti calcolo la differenza tra il compleanno di quest’anno e oggi
    giorni = delta.days #giorni interi dalla differenza
    ore = delta.seconds // 3600 #un'ora ha 3600 secondi, quindi divido i secondi rimanenti per 3600 per ottenere le ore intere
    minuti = (delta.seconds % 3600) // 60 #prendo i secondi rimanenti dopo aver calcolato le ore (delta.seconds % 3600) e li divido per 60 per ottenere i minuti interi
    secondi = delta.seconds % 60 #prendo i secondi rimanenti dopo aver calcolato le ore e i minuti (delta.seconds % 60) per ottenere i secondi rimanenti

    return giorni, ore, minuti, secondi 

giorni, ore, minuti, secondi = tempo_al_prossimo_compleanno(data_nascita, oggi) #la funzione ritorna 4 valori, quindi li assegno a 4 variabili

print(f"Mancano al tuo prossimo compleanno:")
print(f"{giorni} giorni, {ore} ore, {minuti} minuti e {secondi} secondi.")