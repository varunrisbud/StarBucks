import logging

from flask import Flask, jsonify
from flask import request
from CustQueue import CustomerQueue


app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

q = CustomerQueue()


@app.route('/queue/cashierqueue', methods=['POST'])
def addCustomer():
    if request.method == 'POST':
        requestdatajson = request.get_json()
        custId = requestdatajson['custId']
        q.custQueue.put(custId)
        return jsonify({"status": "customer added successfully"}), 200


# @app.route('/addcustomer/<int:custId>', methods=['POST'])
# def addCustomer(custId):
# if request.method=='POST':
#         q.custQueue.put(custId)
#         # q.printQ()
#         return jsonify({"status": "customer added successfully"}), 200

@app.route('/queue/cashierqueue', methods=['DELETE'])
def reomveCustomer():
    if request.method == 'DELETE':
        if q.custQueue.empty():
            return jsonify({"status": "No Customer in queue"}), 204
        else:
            custId = q.custQueue.get(block=False)
            return jsonify({"status": "customer deleted successfully", "id": custId}), 200

# @app.route('/removecustomer', methods=['DELETE'])
# def reomveCustomer():
# if request.method=='DELETE':
#         if q.custQueue.empty():
#             return jsonify({"status": "No Customer Found"}), 204
#         else:
#             custId = q.custQueue.get(block=False)
#             return jsonify({"status": "customer deleted successfully", "id": custId}), 200

if __name__ == '__main__':
    app.run(debug=True)