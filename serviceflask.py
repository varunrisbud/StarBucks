from flask import Flask, jsonify
from flask import request
from customer import Customer
from utility import UtilityClass
import json
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

util=UtilityClass()

@app.route('/customer', methods=['POST'])
def create_customer():
    if request.method == 'POST':
        cust=Customer(request.json['customerName'], request.json['custId'], request.json['items'])
        util.addCustomer(cust)
        return jsonify({'status': 'customer successfully added'}), 200


@app.route('/customer/<int:custId>', methods=['GET'])
def get_customer(custId):
    if request.method == 'GET':
        cust=findCustomer(util.customers, custId)
        if cust is not None:
            return jsonify({'customerName': cust.name, 'custId': cust.id, 'items': cust.order}), 200
        else:
            return jsonify({"status": "customer not found"}), 200

@app.route('/customer/<int:custId>', methods=['DELETE'])
def delete_item(custId):
    if request.method == 'DELETE':
        cust=findCustomer(util.customers, custId)
        if cust is not None:
            cust.order.remove(request.json['itemName'])
            if len(cust.order) == 0:
                util.customers.remove(cust)
                return jsonify({"status": "Customer order completed"}), 200
            else:
                return jsonify({"status": "Item Served to Customer"}), 200
        else:
            return jsonify({"status": "customer not found"}), 200

def findCustomer(list, cid):
    for q in list:
        print(q)
        if q.id==cid:
            print(q.id)
            return q
    return None

if __name__ == '__main__':
    app.run(debug=True, port=4000)