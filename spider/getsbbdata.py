#### Imports ####
import requests
import pandas as pd
#### Imports ####

# Liste von Postleitzahlen in Kanton Zürich
listOfPLZ = [8001, 8002, 8003, 8004, 8005, 8006, 8008, 8032, 8037, 8038, 8041, 8044, 8045, 8046, 8047, 8048, 8049, 8050, 8051, 8052, 8053, 8055, 8057, 8064, 8102, 8103, 8104, 8105, 8106, 8107,
            8108, 8112, 8113, 8114, 8115, 8117, 8118, 8121, 8122, 8123, 8124, 8125, 8126, 8127, 8132, 8133, 8134, 8135, 8136, 8142, 8143, 8152, 8153, 8154, 8155, 8156, 8157, 8158, 8162, 8164,
            8165, 8166, 8172, 8173, 8174, 8175, 8180, 8181, 8182, 8184, 8185, 8187, 8192, 8193, 8194, 8195, 8196, 8197, 8245, 8246, 8247, 8248, 8302, 8303, 8304, 8305, 8306, 8307, 8308, 8309,
            8310, 8311, 8312, 8314, 8315, 8317, 8320, 8322, 8330, 8331, 8332, 8335, 8340, 8342, 8344, 8345, 8352, 8353, 8354, 8400, 8404, 8405, 8406, 8408, 8409, 8412, 8413, 8414, 8415, 8416,
            8418, 8421, 8422, 8424, 8425, 8426, 8427, 8428, 8442, 8444, 8447, 8450, 8451, 8452, 8453, 8457, 8458, 8459, 8460, 8461, 8462, 8463, 8464, 8465, 8466, 8467, 8468, 8471, 8472, 8474,
            8475, 8476, 8477, 8478, 8479, 8482, 8483, 8484, 8486, 8487, 8488, 8489, 8492, 8493, 8494, 8495, 8496, 8497, 8498, 8499, 8523, 8542, 8543, 8544, 8545, 8548, 8600, 8602, 8603, 8604,
            8605, 8606, 8607, 8608, 8610, 8614, 8615, 8616, 8617, 8618, 8620, 8623, 8624, 8625, 8626, 8627, 8630, 8632, 8633, 8634, 8635, 8636, 8637, 8700, 8702, 8703, 8704, 8706, 8707,
            8708, 8712, 8713, 8714, 8800, 8802, 8803, 8804, 8805, 8806, 8810, 8815, 8816, 8820, 8824, 8825, 8833, 8902, 8903, 8904, 8906, 8907, 8908, 8909, 8910, 8911, 8912, 8913, 8914,
            8915, 8925, 8926, 8932, 8933, 8934, 8942, 8951, 8952, 8953, 8954, 8955]

# Liste von Jahren für Analyse
ListOfYears = [2022, 2021, 2020, 2019]

def getSBBHalbtaxInfo():

    #api_url = "https://data.sbb.ch/api/explore/v2.1/catalog/datasets/generalabo-halbtax/records?where=plz_npa%3D1003%20and%20(jahr_an_anno%20%3D%20date'2022'%20OR%20jahr_an_anno%20%3D%20date'2021')&limit=20"
    resultset = []

    # Schleife durch jede Postleitzahl
    for plz in listOfPLZ:

        # API Zusammenbau       
        api_url = f"https://data.sbb.ch/api/explore/v2.1/catalog/datasets/generalabo-halbtax/records?where=plz_npa%3D{plz}%20and%20("
        for year in ListOfYears:
            textconcat = f"jahr_an_anno%20%3D%20date\'{year}\'%20OR%20"
            api_url = api_url + textconcat
        
        api_url = api_url[:-8]
        api_url = api_url + ")&limit=100"

        # API-Aufruf
        response = requests.get(api_url)
        data = response.json()

        # Ausgabe für den Fortschritt
        print('Retrieving PLZ: ', plz)

        # Extrahieren der relevanten Daten und Hinzufügen zur resultset 
        for result in data['results']:
            jahr = result['jahr_an_anno']
            plz = result['plz_npa']
            anz_GA = result['ga_ag']
            anz_Halbtax = result['hta_adt_meta_prezzo']

            resultset.append([jahr, plz, anz_GA, anz_Halbtax])

    # Erstellung DataFrame von resultset als Output
    df = pd.DataFrame(resultset, columns=['Jahr', 'PLZ', 'Anzahl_GA', 'Anzahl_Halbtax'])

    # Konvertiere die Spalten 'Jahr', 'PLZ', 'Anzahl_GA', 'Anzahl_Halbtax' in int (Ganzzahlen)
    df['Jahr'] = pd.to_numeric(df['Jahr'], downcast='integer')
    df['PLZ'] = pd.to_numeric(df['PLZ'], downcast='integer')
    df['Anzahl_GA'] = pd.to_numeric(df['Anzahl_GA'], downcast='integer')
    df['Anzahl_Halbtax'] = pd.to_numeric(df['Anzahl_Halbtax'], downcast='integer')

    return df
