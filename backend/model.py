#### Imports ####
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from pymongo import MongoClient
from mongo_import import retrieveSbbBfsJoinData
import pickle

#### Datenabruf ####
df = retrieveSbbBfsJoinData()

#### Daten vorbereiten ####
X = df[['Total_Einwohner']]  # Feature
y = df['Anz_Halbtax']  # Zielvariablen Halbtax
z = df['Anz_GA']  # Zielvariablen GA

#### Train-Test-Split ####
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, z_train, z_test = train_test_split(X, z, test_size=0.2, random_state=42)

#### Modelle trainieren ####
modelHA = LinearRegression()
modelHA.fit(X_train, y_train)

modelGA = LinearRegression()
modelGA.fit(X_train, z_train)

#### Modellbewertung ####
print(f"Modellgenauigkeit (Halbtax): {modelHA.score(X_test, y_test)}")
print(f"Modellgenauigkeit (GA): {modelGA.score(X_test, z_test)}")

#### Vorhersagen ####
predictionsHA = modelHA.predict(X_test)
predictionsGA = modelGA.predict(X_test)

#### Modellspeicherung ####
model_ha_path = 'modelHA.pkl'
model_ga_path = 'modelGA.pkl'

with open(model_ha_path, 'wb') as file:
    pickle.dump(modelHA, file)
    
with open(model_ga_path, 'wb') as file:
    pickle.dump(modelGA, file)

print("Modelle wurden erfolgreich gespeichert.")

#### Modellladen für Vorhersagefunktion (optional) ####
with open('modelHA.pkl', 'rb') as file:
    modelHA_loaded = pickle.load(file)
    
with open('modelGA.pkl', 'rb') as file:
    modelGA_loaded = pickle.load(file)

print("Modelle wurden erfolgreich geladen.")

#### Vorhersagefunktion ####
def vorhersage(plz, bevoelkerungsgroesse):
    input_data = pd.DataFrame({'Total_Einwohner': [bevoelkerungsgroesse]})
    halbtax_vorhersage = modelHA_loaded.predict(input_data)[0]
    ga_vorhersage = modelGA_loaded.predict(input_data)[0]
    return ga_vorhersage, halbtax_vorhersage

# Beispielaufruf der Vorhersagefunktion
# print(vorhersage(8004, 100000))
