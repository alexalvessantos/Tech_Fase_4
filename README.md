Tech Challenge – Fase 4

Este projeto faz parte do desafio técnico da fase 4 do Pós-Tech da FIAP. O objetivo é prever o preço de ações usando redes neurais do tipo LSTM (Long Short-Term Memory). Para isso, foi criada uma API com Flask que permite consumir o modelo de forma simples e direta.

Funcionalidades
O projeto contempla todas as etapas essenciais de um pipeline preditivo:

Coleta de dados históricos de ações através do Yahoo (via Stooq)

Pré-processamento com normalização dos dados usando MinMaxScaler

Treinamento de uma rede neural LSTM com TensorFlow/Keras

Previsão do próximo valor com base em uma janela de 60 dias

Exposição de uma API REST que entrega o resultado da previsão

Testes de consumo com Postman

Containerização com Docker para facilitar a execução

Estrutura do Projeto

Tech_Fase_4/
 api/          # Código da API em Flask
    main.py
 data/         # Arquivo de dados brutos (opcional)
    dataset.csv
 docker/       # Dockerfile e arquivos de build
    Dockerfile
 model/        # Modelos treinados
    lstm_model.h5
    lstm_model.keras
 notebook/     # Notebook com EDA, modelagem e treino
    eda_model_lstm.ipynb
 requirements.txt
 README.md
Como Executar Localmente
1. Clonar o repositório

git clone https://github.com/seuusuario/Tech_Fase_4.git
cd Tech_Fase_4

2. Criar ambiente virtual

python -m venv .venv
Ative o ambiente:

Linux/macOS:
source .venv/bin/activate
Windows:
.venv\Scripts\activate

3. Instalar as dependências
pip install -r requirements.txt

4. Treinar o modelo (opcional)
Se quiser treinar novamente o modelo do zero, abra o notebook:
jupyter notebook notebook/eda_model_lstm.ipynb
Ao final, um novo modelo será salvo em model/lstm_model.keras.

Executar a API Flask

python api/main.py
A API estará disponível em:
http://127.0.0.1:5000/predict

Testar com Postman
Endpoint:
POST http://127.0.0.1:5000/predict

Headers:
Content-Type: application/json

Body (exemplo):

json
Copiar
Editar
{
  "sequence": [0.15, 0.17, 0.18, 0.21, 0.22, ..., 0.30]
}
Resposta esperada:

{
  "prediction": 0.1985
}
Executar com Docker
Criar a imagem:

docker build -t tech_challenge_lstm -f docker/Dockerfile .
Rodar o container:

docker run -p 5000:5000 tech_challenge_lstm
Acesse em: http://localhost:5000/predict

Requisitos
O projeto usa as seguintes bibliotecas (todas são instaladas automaticamente):
Flask
NumPy
Pandas
Scikit-learn
TensorFlow
Pandas DataReader
Tecnologias Utilizadas
Python 3.11+
TensorFlow / Keras
Flask
Pandas / NumPy
Scikit-learn
Jupyter Notebook
Docker
Postman

Autor
Alex Santos
Desafio Técnico – Pós-Tech Avançado – FIAP