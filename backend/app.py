from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'modelo_pinguins.joblib')

final_model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return "API de predição dos pinguins está online!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = final_model.predict(input_data)
    return jsonify({'predicao': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)