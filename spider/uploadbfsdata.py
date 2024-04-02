#### Imports ####
import pandas as pd
from pymongo import MongoClient
from mongo_user import cosmos_url, cosmos_db_name
#### Imports ####

# Cosmos DB Verbindungsdaten
cosmos_collection_name = 'bfsdaten'

# CSV-Dateipfad
csv_file_path = 'getbfsdata/BFS_Stats_bereinigt.csv'

# Verbindung zu Cosmos DB herstellen
client = MongoClient(cosmos_url)
db = client[cosmos_db_name]
collection = db[cosmos_collection_name]

# CSV-Datei lesen
data = pd.read_csv(csv_file_path, delimiter=';')

# Daten in Cosmos DB einfügen
collection.insert_many(data.to_dict('records'))

print("Daten erfolgreich hochgeladen.")

# Ausführen auf Terminal mit: python uploadbfsdata.py