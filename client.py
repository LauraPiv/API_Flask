import requests
import json

url = 'http://127.0.0.1:5000/previsao_chuva'

data = {
    "latitude": 40.7128,
    "longitude": -74.0060,
    "temperature": 85,
    "humidity": 70,
    "wind_speed": 10
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Lança um erro para códigos de status HTTP 4xx/5xx

    print('Status Code: ', response.status_code)
    print('Response: ', response.json())
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Mostra o erro HTTP
except Exception as err:
    print(f'Other error occurred: {err}')  # Mostra qualquer outro erro
