import requests
from flask import Flask, render_template, jsonify
from datetime import datetime
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction')
def prediction():
    # Send a GET request to the Coinbase API to retrieve the current Ethereum price
    response = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/spot')
    if response.status_code != 200:
        return jsonify({'error': 'Unable to retrieve Ethereum price'}), 500

    # Extract the price value from the response JSON object
    data = response.json()
    price = float(data['data']['amount'])
    print(price)

    # Build a JSON object containing the current Ethereum price and timestamp
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    prediction = {'price': price, 'timestamp': timestamp}

    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
