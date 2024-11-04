import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Carregar os dados do CSV
data = pd.read_csv('clima.csv')

# Verificar as colunas
print("Nomes das colunas:", data.columns.tolist())

# Separar as características e o rótulo
X = data[['latitude', 'longitude', 'temperature', 'humidity', 'wind_speed']]
y = data['chuva']

# Dividir os dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Criar e treinar o modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Realizar previsões com o conjunto de teste
y_pred = knn.predict(X_test)

# Avaliar o modelo com o conjunto de teste
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia: {accuracy:.2f}")

# Exibir o relatório de classificação com zero_division=1 para evitar erros em métricas indefinidas
print("\nRelatório de Classificação:\n", classification_report(y_test, y_pred, zero_division=1))

# Guardar o modelo e o scaler para uso posterior
knn = knn
scaler = scaler