# Previsão de Chuva com API Flask e Algoritmo KNN

## Sumário
- [1. Descrição](Description)
- [2. Versão](Version)
- [3. Materiais](materials)
- [4. Estrutura do Projeto](Structure)
- [5. Como Usar](how-to-use)
- [6. Copyright](copyright)

## 1. Descrição
Este projeto utiliza uma API Flask para prever se vai chover com base em variáveis meteorológicas (latitude, longitude, temperatura, umidade e velocidade do vento). O modelo de previsão é um K-Nearest Neighbors (KNN) treinado com dados climáticos.

## 2. Versão
**py.3.13.0**

## 3. Materiais
Para executar este projeto, você precisa ter as seguintes ferramentas e bibliotecas instaladas:
- **Python 3.13.0**
- **VScode
- Código para Windows
- **Bibliotecas:**:
  - `pip install Flask flask-cors scikit-learn requests`

## 4. Estrutura do Projeto
- app.py: Arquivo principal da aplicação Flask que configura o servidor e a rota /previsao_chuva para receber dados e retornar a previsão.
- client.py: Cliente que envia dados para a API para obter a previsão de chuva.
- clima.csv: Arquivo CSV com dados históricos de clima para treinar o modelo.
- KNN.py: Arquivo que treina o modelo KNN com os dados do CSV e o disponibiliza para uso no app.py.

## 5. How to use/Como Usar
  1. Clonar o Repositório:
git clone https://github.com/seuusuario/previsao_chuva_api.git
cd previsao_chuva_api

  3. Criar e Ativar o Ambiente Virtual:
No diretório do projeto, crie um ambiente virtual:
`
python -m venv .venv
`

  4. Ative o ambiente virtual:
Windows:
`
.venv\Scripts\activate
`
Mac/Linux:
`
source .venv/bin/activate
`
  5. Instalar as Dependências
Com o ambiente virtual ativo, instale as bibliotecas necessárias

  6. Primeiro execute a KNN
`
python KNN.py
`

  7. Em seguida o app
`
python app.py
`

  8. Em outra janela de terminal (com o ambiente virtual ativado), execute o cliente:
`
python client.py
`

- Resultado Esperado
A saída do cliente exibirá o código de status da solicitação e a resposta JSON com a previsão de chuva.

- Exemplo:
`
Status Code: 200
Response Json: {'message': 'Vai chover'}
`

## 6. Copyright and Acknowledgements
- Direitos Autorais

Este projeto e seu código são [@LauraPiv], [2024]. Todos os direitos reservados.
