#### Imports ####
import pandas as pd
from pymongo import MongoClient
import os
#### Imports ####

# Zugriff auf die Umgebungsvariablen
MONGODB_URI = os.getenv('MONGODB_URI')
MONGODB_DB_NAME = os.getenv('MONGODB_DB_NAME')

# DB Verbindungsdaten
MONGODB_COLLECTION_NAME = 'bfsdaten'

# CSV-Dateipfad
csv_file_path = 'getbfsdata/BFS_Stats_bereinigt.csv'

# Verbindung zu Cosmos DB herstellen
client = MongoClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]
collection = db[MONGODB_COLLECTION_NAME]

# CSV-Datei lesen
data = pd.read_csv(csv_file_path, delimiter=';')

# Daten in Cosmos DB einfügen
collection.insert_many(data.to_dict('records'))

print("Daten erfolgreich hochgeladen.")

# Ausführen auf Terminal mit: python uploadbfsdata.py
