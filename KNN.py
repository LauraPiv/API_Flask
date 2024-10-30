# Importando as bibliotecas necessárias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Carregar os dados do CSV
data = pd.read_csv('clima.csv')

# Separar as características (latitude, longitude, temperature, humidity, wind_speed) e o rótulo (chuva)
X = data[['latitude', 'longitude', 'temperature', 'humidity', 'wind_speed']]
y = data['chuva']

# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Criar o modelo KNN (com k=5)
knn = KNeighborsClassifier(n_neighbors=5)

# Treinar o modelo
knn.fit(X_train, y_train)

# Função para fazer a previsão com novos dados
def prever_chuva(lat, lon, temp, hum, wind_speed):
    # Cria um DataFrame com os novos dados e aplica a padronização
    novo_dado = pd.DataFrame([[lat, lon, temp, hum, wind_speed]], 
                             columns=['latitude', 'longitude', 'temperature', 'humidity', 'wind_speed'])
    novo_dado = scaler.transform(novo_dado)
    
    # Fazer a previsão
    previsao = knn.predict(novo_dado)
    
    # Exibir o resultado da previsão
    resultado = "Vai chover" if previsao[0] == 1 else "Não vai chover"
    print(resultado)
    return resultado

# Exemplo de uso da função com novas variáveis
prever_chuva(lat=-23.55, lon=-46.63, temp=85, hum=85, wind_speed=15)

# Avaliar o modelo com o conjunto de teste
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2f}")
print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred))
