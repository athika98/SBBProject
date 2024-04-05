#### Imports ####
import matplotlib.pyplot as plt
from model import X_test, y_test, z_test, predictionsGA, predictionsHA
import os
#### Imports ####

# Pfad zum Verzeichnis, in dem das Bild gespeichert werden soll
dir_path = 'c:\\Users\\athik\\OneDrive\\Desktop\\MDM\\SBBProject-20240329\\frontend\\static'
image_path_HA = os.path.join(dir_path, 'halbtax_vorhersagen.png')
image_path_GA = os.path.join(dir_path, 'ga_vorhersagen.png')


# Plot für Halbtax-Vorhersagen
plt.scatter(X_test, y_test, color='black', label='Tatsächliche Halbtax')
plt.plot(X_test, predictionsHA, color='blue', linewidth=3, label='Vorhersagen Halbtax')
plt.xlabel('Total_Einwohner')
plt.ylabel('Anz_Halbtax')
plt.title('Tatsächliche Werte vs. Vorhersagen für Halbtax')
plt.legend()
# plt.show()
plt.savefig(image_path_HA)
plt.close()


# Plot für GA-Vorhersagen
plt.scatter(X_test, z_test, color='black', label='Tatsächliche GA')
plt.plot(X_test, predictionsGA, color='green', linewidth=3, label='Vorhersagen GA')
plt.xlabel('Total_Einwohner')
plt.ylabel('Anz_GA')
plt.title('Tatsächliche Werte vs. Vorhersagen für GA')
plt.legend()
# plt.show()
plt.savefig(image_path_GA)
plt.close()