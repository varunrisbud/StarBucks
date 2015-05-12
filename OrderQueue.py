import queue
import logging

from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from flask import Response
from Order import Order


app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

orderQueue = queue.Queue()

@app.route('/')
def hello_world():
    return 'Welcome to Flask Rest service!'


@app.route('/queue/orderqueue', methods=['POST'])
def queue_order():
    if request.headers['Content-Type'] == 'application/json':

        requestdatajson = request.get_json()

        custid = requestdatajson['custId']
        custname = requestdatajson['customerName']
        itemname = requestdatajson['itemName']

        neworder = Order(customerid=custid, customername=custname, itemname=itemname)

        # neworder.displayOrder()

        orderQueue.put(neworder)

        responsedata = {
            'status': 'Order Queued'
        }

        # resp = jsonify(responsedata)
        responsedata = json.dumps(responsedata)

        resp = Response(responsedata, status=201, mimetype='application/json')

        return resp
    else:
        responsedata = {
            'status': '415 - Unsupported media type!!! '
        }

        resp = jsonify(responsedata)
        resp.status_code = 415
        return resp


@app.route('/queue/orderqueue', methods=['DELETE'])
def deque_order():
    if orderQueue.empty():
        # print("No order in queue")
        responsedata = {
            'status': 'No order'
        }

        jsondata = jsonify(responsedata)
        jsondata.status_code = 204

    else:
        order = orderQueue.get(block=False)
        # order.displayOrder()

        responsedata = {
            'custId': order.customerid,
            'customerName': order.customername,
            'itemName': order.itemname
        }

        jsondata = jsonify(responsedata)
        jsondata.status_code = 200

    return jsondata


if __name__ == '__main__':
    app.run(port=3000)
