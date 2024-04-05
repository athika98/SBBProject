#### Imports ####
from flask import Flask, request, jsonify
from flask_cors import CORS
from model import vorhersage
#### Imports ####

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Hello, this is the home page of the Flask backend.'

@app.route('/predict', methods=['POST'])
def predict():
    # Daten aus der Anfrage extrahieren
    data = request.json
    plz = data.get('plz')
    einwohnerzahl = data.get('einwohnerzahl')

    # Überprüfen, ob die notwendigen Daten vorhanden sind
    if plz and einwohnerzahl:
        try:
            # Vorhersage mit den trainierten Modellen
            ga_vorhersage, halbtax_vorhersage = vorhersage(plz, einwohnerzahl)
            
            # Antwort zurücksenden
            response = {
                'GA': ga_vorhersage,
                'Halbtax': halbtax_vorhersage
            }
            return jsonify(response), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Fehlende Daten: PLZ und Einwohnerzahl sind erforderlich.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
