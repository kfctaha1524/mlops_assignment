from flask import jsonify
from web3 import Web3
import requests

@app.route('/data')
def data():
    response = requests.get('https://api.blockcypher.com/v1/eth/main')
    data = []
    for block in response.json()['blocks']:
        number = block['height']
        gasPrice = Web3.fromWei(block['median_gas_price'], 'gwei')
        data.append({'number': number, 'gasPrice': gasPrice})
    return jsonify(data)
