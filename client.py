import requests

url = "http://127.0.0.1:5000/previsao_chuva"

data = {
    'latitude': 23.55,
    'longitude': 46.63,
    'temperature': 30,
    'humidity': 85,
    'wind_speed': 15
}

response = requests.post(url, json=data)

print('Status Code:', response.status_code)
print('Response Json:', response.json())
