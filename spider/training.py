#### Imports ####
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd
from pymongo import MongoClient
from mongo_import import retrieveSbbBfsJoinData
#### Imports ####

# Daten abrufen
df = retrieveSbbBfsJoinData()

# 'Total_Einwohner' ist das Feature und 'Anz_Halbtax' und 'Anz_GA' sind die Zielvariablen
X = df[['Total_Einwohner']]  # Feature
y = df['Anz_Halbtax']  # Ziel HA
z = df['Anz_GA'] # Ziel GA

# Train-Test-Split für HA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train-Test-Split für GA
X_train, X_test, z_train, z_test = train_test_split(X, z, test_size=0.2, random_state=42)

# Modell initialisieren und trainieren HA
modelHA = LinearRegression()
modelHA.fit(X_train, y_train)

# Modell initialisieren und trainieren GA
modelGA = LinearRegression()
modelGA.fit(X_train, z_train)

# Modellbewertung HA
score = modelHA.score(X_test, y_test)
print(f"Modellgenauigkeit (Halbtax): {score}")

# Modellbewertung GA
score = modelGA.score(X_test, z_test)
print(f"Modellgenauigkeit (GA): {score}")

# Vorhersage mit dem Modell HA
predictionsHA = modelHA.predict(X_test)

# Vorhersage mit dem Modell HA
predictionsGA = modelGA.predict(X_test)

