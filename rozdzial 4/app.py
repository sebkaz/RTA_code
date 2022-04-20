import numpy as np
from joblib import load
from flask import (
        Flask, 
        request, 
        jsonify
)
app = Flask(__name__)

@app.route('/api/predict', methods=['GET'])
def get_prediction():
    sepal_length = float(request.args.get('sl'))
    petal_length = float(request.args.get('pl'))
    
    features = [sepal_length, petal_length]
    model = load('model.joblib')
    predicted_class = int(model.predict(features))
    return jsonify(features=features,
    predicted_class=predicted_class)
if __name__ = '__main__':
    app.run(host='0.0.0.0')