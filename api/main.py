#from keras.models import load_model
from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
model = load_model('notebook/model/lstm_model.keras')

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    sequence = np.array(data['sequence']).reshape(1, -1, 1)
    prediction = model.predict(sequence)
    return jsonify({'prediction': float(prediction[0][0])})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

