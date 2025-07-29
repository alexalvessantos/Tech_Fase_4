# 📊 Tech Challenge – Fase 4

Este projeto realiza previsão de preços de ações utilizando redes neurais LSTM (Long Short-Term Memory), expondo uma API via Flask para consumo do modelo treinado.

---

## ✅ Funcionalidades

- 📈 Coleta de dados históricos de ações (Yahoo via Stooq)
- 🧹 Pré-processamento com MinMaxScaler
- 🧠 Treinamento de modelo LSTM com Keras
- 🔮 Previsão do próximo valor com base em sequência de 60 dias
- 🌐 Exposição de API REST para consumo do modelo
- 🧪 Testes com Postman
- 🐳 Containerização com Docker

---

## 📁 Estrutura do Projeto

Tech_Fase_4/
│
├── api/ # API Flask para servir o modelo
│ └── main.py
│
├── data/ # Dados brutos (opcional, usado durante EDA)
│ └── dataset.csv
│
├── docker/ # Dockerfile e recursos para containerização
│ └── Dockerfile
│
├── model/ # Modelos salvos
│ ├── lstm_model.h5
│ └── lstm_model.keras
│
├── notebook/ # Notebook com EDA, modelagem e treinamento
│ └── eda_model_lstm.ipynb
│
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto

yaml
Copiar
Editar

---

## ⚙️ Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seuusuario/Tech_Fase_4.git
cd Tech_Fase_4
2. Crie um ambiente virtual
bash
Copiar
Editar
python -m venv .venv
source .venv/bin/activate       # Linux/macOS
.venv\Scripts\activate          # Windows
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Treinar o modelo (opcional)
Se quiser treinar o modelo novamente:

bash
Copiar
Editar
jupyter notebook notebook/eda_model_lstm.ipynb
Isso gerará um modelo salvo em model/lstm_model.keras.

🚀 Executar a API Flask
bash
Copiar
Editar
python api/main.py
Acesse em: http://127.0.0.1:5000/predict

🧪 Testar com Postman
Endpoint
http
Copiar
Editar
POST http://127.0.0.1:5000/predict
Headers
pgsql
Copiar
Editar
Content-Type: application/json
Body (JSON)
json
Copiar
Editar
{
  "sequence": [0.15, 0.17, 0.18, 0.21, 0.22, ..., 0.30]
}
Resposta
json
Copiar
Editar
{
  "prediction": 0.19852642714977264
}
🐳 Executar com Docker
1. Build da imagem
bash
Copiar
Editar
docker build -t tech_challenge_lstm -f docker/Dockerfile .
2. Rodar o container
bash
Copiar
Editar
docker run -p 5000:5000 tech_challenge_lstm
Acesse em: http://localhost:5000/predict

📦 Requisitos
nginx
Copiar
Editar
Flask
numpy
pandas
scikit-learn
tensorflow
pandas_datareader
Instalados automaticamente com:

bash
Copiar
Editar
pip install -r requirements.txt
🛠️ Tecnologias
Python 3.11+

TensorFlow / Keras

Flask

Pandas / NumPy

Scikit-learn

Jupyter Notebook

Docker

Postman

👨‍💻 Autor
Alex Santos
Desafio Técnico | Pós-Tech Avançado | FIAP

