#python -m venv .venv
#venv\Scripts\activate
#pip install Flask flask-cors scikit-learn
from flask import Flask, request, render_template, jsonify
import pandas as pd

# Configuração da aplicação Flask
app = Flask(__name__)

@app.route("/previsao_chuva", methods=["POST"])
def previsao_chuva():
    # Captura os parâmetros enviados pelo formulário (método POST)
    print('Log: Recebendo variáveis do formulário POST')
    
    data = request.get_json()
    lat = data.get('latitude')
    lon = data.get('longitude')
    temp = data.get('temperature')
    hum = data.get('humidity')
    wind_speed = data.get('wind_speed')

    print('Log: Latitude = ', lat)
    print('Log: Longitude = ', lon)
    print('Log: Temperatura = ', temp)
    print('Log: Umidade = ', hum)
    print('Log: Velocidade do Vento = ', wind_speed)

    # Cria um DataFrame com as novas variáveis
    novo_dado = pd.DataFrame([[lat, lon, temp, hum, wind_speed]], 
                             columns=['latitude', 'longitude', 'temperature', 'humidity', 'wind_speed'])

    # Faz a previsão de chuva com o modelo KNN
    previsao = knn.predict(novo_dado)
    result = "Vai chover" if previsao[0] == 1 else "Não vai chover"

    # Retorna o resultado da previsão como JSON
    return jsonify({'message': f'Recebido {lat}, {lon}, {temp}, {hum}, {wind_speed}'}), 200


if __name__ == "__main__":
    app.run()
