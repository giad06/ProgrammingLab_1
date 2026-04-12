# Esercitazione 2

class ExamException(Exception):
    pass


class CSVTimeSeriesFile:

    def __init__(self,name):
        try:
            with open(name, "r") as file:
                next(file) #Salto l'intestazione
                self.name = name
        except ExamException:
            print("Errore nell'apertura file!") #Verifica apertura file, altrimenti eccezione


    def get_data(self):

        with open(self.name, "r") as file:
            next(file) 
            lista_tot = []
            date_controllate = set() #Creo set vuoto per tenere conto delle date già viste (serve per non creare duplicati)

            for riga in file:
                riga=riga.strip() 
                elementi = riga.split(",") #Divido riga in una lista (Date e Passengers)
                if len(elementi) < 2:
                    continue  #controlla che ci siano almeno 2 elementi nella lista, altrimenti salta la riga e va avanti con il ciclo (se sono piu elementi considera comunque)
                
                data = elementi[0]
                passeggeri = elementi [1] # cosi anche se ho piu elementi, trascuro

                #Controllo validità data
                try:
                    anno, mese = data.split("-") #Divido data in lista di 2 elementi e assegno alle variabili anno e mese
                    anno = int(anno)
                    mese = int(mese)
                    if mese < 1 or mese > 12:
                        continue
                except ExamException:
                    continue #ignoro la riga se non valida
                
                # Controllo che il campo passeggeri non sia vuoto
                if passeggeri == "":
                    continue

                #Controllo validità valore di passengers
                try:
                    passeggeri = int(passeggeri)
                except ExamException:
                    print("Valore di passeggeri non valido, questa riga verrà ignorata!")
                    continue #se passeggeri ha un valore non valido, ignoro
                
                #Controllo che le date non abbiano duplicati
                if data in date_controllate:
                    raise ExamException("C'è una data duplicata!")
                else:
                    date_controllate.add(data)
                    
                lista_tot.append([data, passeggeri])

            #Ordinamento crescente
            if len(lista_tot) > 1:
                for i in range(1, len(lista_tot)):
                    if lista_tot[i][0] <= lista_tot[i-1][0]:
                        raise ExamException("Le date non sono ordinate in maniera crescente!")  
                          
        return lista_tot
    
def compute_variations(time_series, first_year, last_year):

    try:
        first_year = int(first_year)
        last_year = int(last_year)
    except:
        raise ExamException("I valori di first_year e second_year devono essere interi")

    if(first_year>last_year):
        raise ExamException("L'intervallo inserito non è valido")

    lista_intervallo = [] #Otterrò una lista di liste, che contengono ciascuna i seguenti valori interi: [anno,mese,valore] considerandole sull'intervallo scelto

    #CREO LISTA SU CUI DEVO LAVORARE (RISPETTA INTERVALLO ANNI)

    for elemento in time_series: #elemento è una lista ["Anno-Mese", Valore]
        data_str = elemento[0]     # data_str = "Anno-Mese" (str)
        valore = elemento[1]      # int

        anno, mese = data_str.split("-") #è una stringa, separo e metto rispettivamente in anno e mese
        anno = int(anno) 
        mese = int(mese)

        # filtro gli anni
        if first_year <= anno <= last_year: # Man mano prenderà gli anni, rispettando l'intervallo da considerare
            lista_intervallo.append([anno, mese, valore]) #se rispetta aggiunge alla lista di liste (I VALORI SONO INT)
        else:
            continue #altrimenti scorre la time_series

    #RAGGRUPPO I PASSEGGERI IN BASE AGLI ANNI

    #Creo un dizionario per riordinare in base agli anni
    anni = dict() #le chiavi saranno gli anni, i valori per ogni chiave una lista massima di 12 elementi

    for anno,mese,valore in lista_intervallo: #ogni elemento è una lista [anno,mese,valore]
        
        if anno not in anni:
            anni[anno] = [None]*12 #se non ho ancora registrato l'anno nel dizionario, lo aggiungo inserendo 12 valori None

        anni[anno][mese-1] = valore  #in base all'anno, metto in posizione mese-1 della lista il rispettivo valore per ogni mese

    #CALCOLO MEDIA PASSEGGERI PER OGNI ANNO

    #creo dizionario per inserire media per ogni anno
    medie = dict() 

    for anno,valori in anni.items():
        somma = 0
        count = 0

        for valore in valori:
            if valore is not None:
                somma += valore
                count +=1
        if count == 0:
            medie[anno] = None
        else:
            medie[anno] = round(float(somma / count), 1)

    #DIFFERENZA MEDIE OGNI DUE ANNI (per capire incremento rispetto anno precedente)
    incremento = dict()

    anni_ordinati = list(sorted(medie.keys())) #tramite il metodo keays mi costruisco una lista con ogni anno

    for i in range(len(anni_ordinati)-1): # scorro lista degli anni dal primo all'ultimo
        anno_corr = anni_ordinati[i] #anno corrente
        anno_succ = anni_ordinati[i+1] #anno successivo

        media_corr = medie[anno_corr] # media per l'anno corrente
        media_succ = medie[anno_succ] # media per l'anno successivo

        if media_corr is None or media_succ is None:
            incremento[f"{anno_corr}-{anno_succ}"] = None
        else:
            incremento[f"{anno_corr}-{anno_succ}"] =  round(float(media_succ-media_corr), 1)

    return incremento


time_series_file = CSVTimeSeriesFile(name = "data.csv")
time_series = time_series_file.get_data()
incrementi = compute_variations(time_series, 1949, 1951)
print(incrementi)
                