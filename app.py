#python -m venv .venv
#venv\Scripts\activate
#pip install Flask flask-cors scikit-learn

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# Configuração da API
app = Flask(__name__)
CORS(app)  # Habilita CORS

# Carregando o conjunto de dados
data = pd.read_csv('compras.csv')

# Separando características e rótulos
X = data[['user_id', 'valor_compra']].values
y = data['produto_categoria'].values

# Dividindo os dados
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Função para mapear categorias para nomes
def map_category(prediction):
    categories = {
        0: "Higiene",
        1: "Maquiagem",
        2: "Skincare",
        3: "Perfume",
        4: "Cabelo"
    }
    return categories.get(prediction, "Categoria Desconhecida")

# Rota para página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para previsão
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    user_id = data.get('user_id')
    valor_compra = data.get('valor_compra')

    # Constrói o vetor de entrada para a previsão
    input_data = np.array([[user_id, valor_compra]])
    
    # Previsão
    prediction = knn.predict(input_data)[0]
    
    # Converte o número da categoria para o nome da categoria
    category_name = map_category(prediction)
    
    # Retorna a previsão em JSON
    return jsonify({'categoria_recomendada': category_name})

if __name__ == '__main__':
    print("Iniciando o servidor Flask...")
    app.run(debug=True)
