#### Imports ####
import pandas as pd
from old.training import modelGA, modelHA
#### Imports ####

def vorhersage(plz, bevoelkerungsgroesse):

    # Vorverarbeitung der Eingaben
    input_data = pd.DataFrame({'Total_Einwohner': [bevoelkerungsgroesse]})
    
    # Vorhersage mit den trainierten Modellen
    halbtax_vorhersage = modelHA.predict(input_data)[0]
    ga_vorhersage = modelGA.predict(input_data)[0]
    
    # print(f"Vorhersage für PLZ {plz}:")
    # print(f"Anzahl Halbtax-Abonnements: {halbtax_vorhersage}")
    # print(f"Anzahl GA-Abonnements: {ga_vorhersage}")

    return ga_vorhersage, halbtax_vorhersage


# Testaufruf der Funktion
# vorhersage(8004, 100000)