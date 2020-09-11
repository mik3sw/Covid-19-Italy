import requests

class Covid:
    def __init__(self):
        self.source_url='https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-andamento-nazionale.json' 
        y, length = self.get_covid()
        x = y[length]
        # Variazione rispetto al giorno precedente
        self.nuovi_deceduti = self.get_nuovi_deceduti(y, length)
        self.nuovi_guariti = self.get_nuovi_guariti(y, length)
        self.nuovi_tamponi = self.get_nuovi_tamponi(y, length)
        self.nuovi_positivi = x['nuovi_positivi']
        #self.nuovi_terapia_intensiva = self.get_nuovi_ti(y, length)

        # Incremento percentuale
        self.incremento_p_contagiati = round(((y[length]['nuovi_positivi'] - y[length-1]['nuovi_positivi'])*100)/y[length-1]['nuovi_positivi'] ,2)
        self.incremento_p_deceduti = self.get_incremento_p(y[length]['deceduti'], y[length-1]['deceduti'], y[length-2]['deceduti'])
        self.incremento_p_tamponi = self.get_incremento_p(y[length]['tamponi'], y[length-1]['tamponi'], y[length-2]['tamponi'])
        self.incremento_p_guariti = self.get_incremento_p(y[length]['dimessi_guariti'], y[length-1]['dimessi_guariti'], y[length-2]['dimessi_guariti'])
        #self.incremento_p_ti = self.get_incremento_p(y[length]['terapia_intensiva'], y[length-1]['terapia_intensiva'], y[length-2]['terapia_intensiva'])
        #rapporto tamponi-positivi
        self.rapp_tamponi_positivi = self.get_rapp_tamponi_positivi(self.nuovi_positivi, self.nuovi_tamponi)

        # Altri dati generali (giornalieri)
        self.stato = x['stato']
        self.ricoverati_con_sintomi = x['ricoverati_con_sintomi']
        self.terapia_intensiva = x['terapia_intensiva']
        self.totale_ospedalizzati = x['totale_ospedalizzati']
        self.isolamento_domiciliare = x['isolamento_domiciliare']
        self.totale_positivi = x['totale_positivi']
        self.variazione_totale_positivi = x['variazione_totale_positivi']
        self.dimessi_guariti = x['dimessi_guariti']
        self.deceduti = x['deceduti']
        self.casi_da_sospetto_diagnostico = x['casi_da_sospetto_diagnostico']
        self.casi_da_screening = x['casi_da_screening']
        self.totale_casi = x['totale_casi']
        self.tamponi = x['tamponi']
        self.casi_testati = x['casi_testati']
        self.note = x['note']   
    

    def get_covid(self):
        response = requests.get(self.source_url)
        x = response.json()
        length = -1
        for item in x:
            length = length+1
        return x, length

    def get_nuovi_deceduti(self, y, length):
        new = y[length]['deceduti'] - y[length-1]['deceduti']
        if new < 0:
            return 'ERROR'
        else:
            return new
    
    def get_nuovi_guariti(self, y, length):
        new = y[length]['dimessi_guariti'] - y[length-1]['dimessi_guariti']
        if new < 0:
            return 'ERROR'
        else:
            return new
    
    def get_nuovi_tamponi(self, y, length):
        new = y[length]['tamponi'] - y[length-1]['tamponi']
        if new < 0:
            return 'ERROR'
        else:
            return new
    
    def get_nuovi_ti(self, y, length):
        new = y[length]['terapia_intensiva'] - y[length-1]['terapia_intensiva']
        if new < 0:
            return 'ERROR'
        else:
            return new

    def getSmallReport(self):
        message = 'Totale positivi: {}\nNuovi positivi: {}\nGuariti: {}\nDeceduti: {}\nNuovi Deceduti: {}\nTamponi: {}'.format(self.totale_positivi, self.nuovi_positivi,self.dimessi_guariti,self.deceduti,self.nuovi_deceduti, self.tamponi)
        return message

    def getFullReport(self):
        message = '=======\nStato: {}\nRicoverati con sintomi: {}\nTerapia intensiva: {}\nTotale ospedalizzati: {}\nIsolamento domiciliare: {}\n\nTotale positivi: {}\nVariazione totale positivi: {}\n\nNuovi positivi: {}\nGuariti: {}\nDeceduti: {}\nNuovi Deceduti: {}\nCasi da sospetto diagnostico: {}\nCasi da screening: {}\nTotale casi: {}\nTamponi: {}\nCasi testati: {}\nNote {}\n======='.format(self.stato,self.ricoverati_con_sintomi,self.terapia_intensiva,self.totale_ospedalizzati ,self.isolamento_domiciliare ,self.totale_positivi ,self.variazione_totale_positivi ,self.nuovi_positivi ,self.dimessi_guariti ,self.deceduti ,self.nuovi_deceduti,self.casi_da_sospetto_diagnostico ,self.casi_da_screening ,self.totale_casi,self.tamponi ,self.casi_testati ,self.note)
        return message
    
    def get_covid_settimanale_list(self):
        response = requests.get(self.source_url)
        x = response.json()
        length = -1
        for item in x:
            length = length+1
        week = []
        i = 0
        while(i<8):
            week.append(x[length-i])
            i = i+1
        return week
    
    def get_covid_settimanale(self):
        week = self.get_covid_settimanale_list()
        somma_nuovi_contagiati = 0
        somma_nuovi_morti = 0
        somma_nuovi_guariti = 0
        somma_nuovi_tamponi = 0
        cont = 0
        while(cont<7):
            somma_nuovi_contagiati = somma_nuovi_contagiati + week[cont]['nuovi_positivi']
            somma_nuovi_morti = somma_nuovi_morti + (week[cont]['deceduti'] - week[cont+1]['deceduti'])
            somma_nuovi_guariti = somma_nuovi_guariti + (week[cont]['dimessi_guariti'] - week[cont+1]['dimessi_guariti'])
            somma_nuovi_tamponi = somma_nuovi_tamponi + (week[cont]['tamponi'] - week[cont+1]['tamponi'])
            cont = cont + 1
        
        return somma_nuovi_contagiati, somma_nuovi_morti, somma_nuovi_guariti, somma_nuovi_tamponi
    
    def get_media_settimanale(self):
        c1, c2, c3, c4 = self.get_covid_settimanale()
        media_contagiati = c1/7
        media_morti = c2/7
        media_guariti = c3/7
        media_tamponi = c4/7
        return round(media_contagiati,2), round(media_morti,2), round(media_guariti,2), round(media_tamponi,2)

    def get_covid_mensile_list(self):
        response = requests.get(self.source_url)
        x = response.json()
        length = -1
        for item in x:
            length = length+1
        week = []
        i = 0
        while(i<31):
            week.append(x[length-i])
            i = i+1
        return week
    
    def get_covid_mensile(self):
        week = self.get_covid_settimanale_list()
        somma_nuovi_contagiati = 0
        somma_nuovi_morti = 0
        somma_nuovi_guariti = 0
        somma_nuovi_tamponi = 0
        cont = 0
        while(cont<30):
            somma_nuovi_contagiati = somma_nuovi_contagiati + week[cont]['nuovi_positivi']
            somma_nuovi_morti = somma_nuovi_morti + (week[cont]['deceduti'] - week[cont+1]['deceduti'])
            somma_nuovi_guariti = somma_nuovi_guariti + (week[cont]['dimessi_guariti'] - week[cont+1]['dimessi_guariti'])
            somma_nuovi_tamponi = somma_nuovi_tamponi + (week[cont]['tamponi'] - week[cont+1]['tamponi'])
            cont = cont + 1
        
        return somma_nuovi_contagiati, somma_nuovi_morti, somma_nuovi_guariti, somma_nuovi_tamponi
    
    def get_media_mensile(self):
        c1, c2, c3, c4 = self.get_covid_settimanale()
        media_contagiati = c1/30
        media_morti = c2/30
        media_guariti = c3/30
        media_tamponi = c4/30
        return round(media_contagiati,2), round(media_morti,2), round(media_guariti,2), round(media_tamponi,2)

    def get_incremento_p(self, day_attuale, day_precedente, day_prima_ancora): 
        ieri = day_precedente - day_prima_ancora
        oggi = day_attuale-day_precedente
        perc = ((oggi-ieri)*100)/ieri
        return round(perc, 2)

    def get_rapp_tamponi_positivi(self, positivi, tamponi):
        ris = (positivi*100)/tamponi
        return round(ris, 2)
