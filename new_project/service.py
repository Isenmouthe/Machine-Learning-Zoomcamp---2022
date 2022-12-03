import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load("rain")

def predict(customer, dv, model):
    X = dv.transform([rain])

from flask import Flask, request, jsonify

app = Flask('rain')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    prediction = predict(data, dv, model)
    rain = prediction >= 0.5

    result = {
        'Rain Probability': float(prediction),
        'rain': bool(rain)
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)