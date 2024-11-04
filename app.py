#python -m venv .venv
#.venv\Scripts\activate
#pip install Flask flask-cors scikit-learn
from flask import Flask, request, jsonify
import pandas as pd
from KNN import knn, scaler

# Configuração da aplicação Flask
app = Flask(__name__)

@app.route("/previsao_chuva", methods=["POST"])
def previsao_chuva():
    # Captura os parâmetros enviados pelo formulário (método POST)
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    temp = data.get('temperature')
    hum = data.get('humidity')
    wind_speed = data.get('wind_speed')

    # Cria um DataFrame com as novas variáveis
    novo_dado = pd.DataFrame([[lat, lon, temp, hum, wind_speed]], 
                             columns=['latitude', 'longitude', 'temperature', 'humidity', 'wind_speed'])
    novo_dado = scaler.transform(novo_dado)  # Padroniza os dados

    # Faz a previsão de chuva com o modelo KNN
    previsao = knn.predict(novo_dado)
    result = "Vai chover" if previsao[0] == 1 else "Não vai chover"

    # Retorna o resultado da previsão como JSON
    return jsonify({'message': result}), 200

if __name__ == "__main__":
    app.run(debug=True)
