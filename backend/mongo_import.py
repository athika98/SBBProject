#### Imports ####
import pandas as pd
from pymongo import MongoClient
import getsbbdata as apiConnector
import os
#### Imports ####

# Zugriff auf die Umgebungsvariablen
MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME')

# MongoDB-Client initialisieren und Datenverbindung herstellen
client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]

# Funktion zum Einfügen von SBB-Daten in MongoDB
def insertSbbDataIntoMongo():

    # Datenbank und Sammlung definieren
    db = client[MONGODB_DB_NAME]
    collection = db['sbbdaten']

    # Datenframe von der API abrufen
    df = apiConnector.getSBBHalbtaxInfo()
    print(df)

    # DataFrame in das Dictionary-Format 'records' konvertieren
    data_dict = df.to_dict("records")

    # In MongoDB einfügen
    collection.insert_many(data_dict)

    print('Insertion Completed')

# Funktion zum Abrufen von SBB-BFS-Join-Daten
def retrieveSbbBfsJoinData():

    # collection definieren
    collection = db['sbbdaten']

    # Aggregationspipeline definieren
    pipeline = [
    {
        '$lookup': {
            'from': 'bfsdaten', 
            'localField': 'PLZ', 
            'foreignField': 'Postleitzahl', 
            'as': 'verknuepfte_daten'
        }
    }, {
        '$unwind': {
            'path': '$verknuepfte_daten'
        }
    }, {
        '$match': {
            '$expr': {
                '$eq': [
                    '$Jahr', '$verknuepfte_daten.Jahr'
                ]
            }
        }
    }, {
        '$project': {
            'Jahr': '$Jahr', 
            'PLZ': '$PLZ', 
            'Total_Einwohner': '$verknuepfte_daten.Total', 
            'Anz_Schweizer': '$verknuepfte_daten.Schweiz', 
            'Anz_Auslaender': '$verknuepfte_daten.Ausland', 
            'Anz_Maenner': '$verknuepfte_daten.Mann', 
            'Anz_Frauen': '$verknuepfte_daten.Frau', 
            'Anz_0bis4': '$verknuepfte_daten.0-4', 
            'Anz_5bis9': '$verknuepfte_daten.5-9', 
            'Anz_10bis14': '$verknuepfte_daten.10-14', 
            'Anz_15bis19': '$verknuepfte_daten.15-19', 
            'Anz_20bis24': '$verknuepfte_daten.20-24', 
            'Anz_25bis29': '$verknuepfte_daten.25-29', 
            'Anz_30bis34': '$verknuepfte_daten.30-34', 
            'Anz_35bis39': '$verknuepfte_daten.35-39', 
            'Anz_40bis44': '$verknuepfte_daten.40-44', 
            'Anz_45bis49': '$verknuepfte_daten.45-49', 
            'Anz_50bis54': '$verknuepfte_daten.50-54', 
            'Anz_55bis59': '$verknuepfte_daten.55-59', 
            'Anz_60bis64': '$verknuepfte_daten.60-64', 
            'Anz_65bis69': '$verknuepfte_daten.65-69', 
            'Anz_70bis74': '$verknuepfte_daten.70-74', 
            'Anz_75bis79': '$verknuepfte_daten.75-79', 
            'Anz_80bis84': '$verknuepfte_daten.80-84', 
            'Anz_85bis89': '$verknuepfte_daten.85-90', 
            'Anz_90undmehr': '$verknuepfte_daten.90 und mehr', 
            'Anz_ledig': '$verknuepfte_daten.Ledig', 
            'Anz_verheiratet': '$verknuepfte_daten.Verheiratet', 
            'Anz_verwitwet': '$verknuepfte_daten.Verwitwet', 
            'Anz_geschieden': '$verknuepfte_daten.Geschieden', 
            'Anz_unverheiratet': '$verknuepfte_daten.Unverheiratet', 
            'Anz_eing_partnerschaft': '$verknuepfte_daten.In eingetrage-ner Partner-schaft', 
            'Anz_aufg_partnerschaft': '$verknuepfte_daten.Aufgelöste Partnerschaft', 
            'Anz_GA': '$Anzahl_GA', 
            'Anz_Halbtax': '$Anzahl_Halbtax'
        }
    }
    ]

    # Pipeline auf die erste Kollektion anwenden
    ergebnis = collection.aggregate(pipeline)

    # Ergebnis in DataFrame umwandeln
    df = pd.DataFrame(list(ergebnis))

    return df

# Funktion zum Abrufen von BFS-Daten
def retrieveBfsData():

    # collection für bfs-admin-daten definieren
    collection = db['bfsdaten']

    # Aggregationspipeline definieren
    pipeline = [
        {
            '$project': {
                'Jahr': '$Jahr', 
                'PLZ': '$Postleitzahl', 
                'Total_Einwohner': '$Total', 
                'Anz_Schweizer': '$Schweiz', 
                'Anz_Auslaender': '$Ausland', 
                'Anz_Maenner': '$Mann', 
                'Anz_Frauen': '$Frau', 
                'Anz_0bis4': '$0-4', 
                'Anz_5bis9': '$5-9', 
                'Anz_10bis14': '$10-14', 
                'Anz_15bis19': '$15-19', 
                'Anz_20bis24': '$20-24', 
                'Anz_25bis29': '$25-29', 
                'Anz_30bis34': '$30-34', 
                'Anz_35bis39': '$35-39', 
                'Anz_40bis44': '$40-44', 
                'Anz_45bis49': '$45-49', 
                'Anz_50bis54': '$50-54', 
                'Anz_55bis59': '$55-59', 
                'Anz_60bis64': '$60-64', 
                'Anz_65bis69': '$65-69', 
                'Anz_70bis74': '$70-74', 
                'Anz_75bis79': '$75-79', 
                'Anz_80bis84': '$80-84', 
                'Anz_85bis89': '$85-90', 
                'Anz_90undmehr': '$90 und mehr'
            }
        }
    ]

    # Pipeline auf die bfs-admin-daten Kollektion anwenden
    ergebnis = collection.aggregate(pipeline)

    # Ergebnis in DataFrame umwandeln
    df = pd.DataFrame(list(ergebnis))

    return df

# Funktion zum Abrufen von SBB-Daten
def retrieveSbbData():

    # collection definieren
    collection = db['sbbdaten']

    # Aggregationspipeline definieren
    pipeline = [
        {
            '$project': {
                'Jahr': '$Jahr', 
                'PLZ': '$PLZ',  
                'Anz_GA': '$Anzahl_GA', 
                'Anz_Halbtax': '$Anzahl_Halbtax'
            }
        }
    ]

    # Pipeline auf die Kollektion anwenden
    ergebnis = collection.aggregate(pipeline)

    # Ergebnis in DataFrame umwandeln
    df = pd.DataFrame(list(ergebnis))

    return df