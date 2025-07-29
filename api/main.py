# from keras.models import load_model
from prometheus_flask_exporter import PrometheusMetrics
from flask import Flask, request, jsonify, g
from tensorflow.keras.models import load_model
import numpy as np
import time
import logging

# Inicializa a aplicação Flask
app = Flask(__name__)

metrics = PrometheusMetrics(app)

# Configura o logging
logging.basicConfig(level=logging.INFO)

# Middleware para medir o tempo de resposta
@app.before_request
def start_timer():
    g.start = time.time()

@app.after_request
def log_request(response):
    if request.path == '/health':
        return response
    duration = time.time() - g.start
    log_params = {
        'method': request.method,
        'path': request.path,
        'status': response.status_code,
        'duration': round(duration * 1000),  # em ms
        'remote_addr': request.remote_addr,
    }
    app.logger.info(f"{log_params}")
    return response

# Carrega o modelo LSTM treinado
model = load_model('model/lstm_model.keras')

# Endpoint de verificação de saúde
@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

# Endpoint para fazer previsão
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    sequence = np.array(data['sequence']).reshape(1, -1, 1)
    prediction = model.predict(sequence)
    return jsonify({'prediction': float(prediction[0][0])})

# Inicializa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
