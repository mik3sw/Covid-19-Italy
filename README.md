# Covid-19-Italy

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/a68996467f58458987d375750adf3ee0)](https://www.codacy.com/manual/mik3sw/Covid-19-Italy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mik3sw/Covid-19-Italy&amp;utm_campaign=Badge_Grade)

A python Class that provide you all the latest informations about COVID-19 from "protezione civile" (https://github.com/pcm-dpc/COVID-19)
## Install

```
pip install covid19it
```

## Dependencies

```
requests
```

## How to use 

### Import the Class:
```
from covid19it import covid19

c = covid19.Covid()
```
### Here the list of class arguments:
```
# Variazione rispetto al giorno precedente
c.nuovi_deceduti 
c.nuovi_guariti
c.nuovi_tamponi
c.nuovi_positivi

# Incremento percentuale
c.incremento_p_contagiati
c.incremento_p_deceduti
c.incremento_p_tamponi
c.incremento_p_guariti

# Rapporto tamponi-positivi
c.rapp_tamponi_positivi

# Others
c.stato
c.ricoverati_con_sintomi
c.terapia_intensiva
c.totale_ospedalizzati 
c.isolamento_domiciliare 
c.totale_positivi 
c.variazione_totale_positivi 
c.nuovi_positivi 
c.dimessi_guariti 
c.deceduti 
c.nuovi_deceduti
c.casi_da_sospetto_diagnostico 
c.casi_da_screening 
c.totale_casi
c.tamponi 
c.casi_testati 
c.note
```

### Here the list of class functions:
```
c.get_media_settimanale()
c.get_media_mensile()
c.getSmallReport()
c.getFullReport()
```
**getSmallReport()** will provide you some minimal but important information about latest Covid19 news (from Italy)

**getFullReport()** will provide you all the latest available information about Covid19 (from Italy)

**get_media_settimanale()** will provide you last 7 days numbers

**get_media_mensile()** will provide you last 30 days numbers

## Example code

**Source**
```
from covid19it import covid19
c = covid19.Covid()

print(c.getSmallReport())

```

**Output**

```
Totale positivi: 21932
Nuovi positivi: 1411
Guariti: 206554
Deceduti: 35463
Nuovi Deceduti: 5
Tamponi: 8313445
```

