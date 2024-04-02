import pandas as pd
from training import modelGA, modelHA

def vorhersage(plz, bevoelkerungsgroesse):
    # Vorverarbeitung der Eingaben
    input_data = pd.DataFrame({'Total_Einwohner': [bevoelkerungsgroesse]})
    
    # Vorhersage mit den trainierten Modellen
    halbtax_vorhersage = modelHA.predict(input_data)[0]
    ga_vorhersage = modelGA.predict(input_data)[0]
    
    print(f"Vorhersage für PLZ {plz}:")
    print(f"Anzahl Halbtax-Abonnements: {halbtax_vorhersage}")
    print(f"Anzahl GA-Abonnements: {ga_vorhersage}")

# Beispielaufruf der Funktion
# vorhersage(8004, 100000)

# In model.py
def vorhersage(plz, bevoelkerungsgroesse):
    # Vorverarbeitung der Eingaben
    input_data = pd.DataFrame({'Total_Einwohner': [bevoelkerungsgroesse]})
    
    # Vorhersage mit den trainierten Modellen
    halbtax_vorhersage = modelHA.predict(input_data)[0]
    ga_vorhersage = modelGA.predict(input_data)[0]
    
    # Rückgabe der Vorhersagen
    return ga_vorhersage, halbtax_vorhersage

