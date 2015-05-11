__author__ = 'Varun'
from flask import Flask, jsonify
import requests, json, time, random
import logging

app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def add_orders_for_Barista(custID, custName, custOrder):
    baristaQueueURL = 'http://localhost:3000/queue/orderqueue'
    # payload = {"customerId": custID, "customerName": custName, "itemName": custOrder}
    # print(payload)
    # jsonPayload = jsonify({"customerId": custID, "customerName": custName, "itemName": custOrder})
    custheader = {'Content-Type': 'application/json'}
    addOrder = requests.post(baristaQueueURL, data=json.dumps({"customerId": custID, "customerName": custName, "itemName": custOrder}), headers=custheader)


def get_customer_order(custID):
    quickOrders = ['Fresh Brewed Coffee', 'Caffe Latte', 'Caffe Mocha', 'Iced Coffee', 'Espresso']
    provideCoffee = []
    addOrderToQueue = []
    custQrderURL = "http://localhost:4000/customer/" + str(custID)
    # payload = {'custId': custID}
    custDetails = requests.get(custQrderURL).json()
    customerID = custDetails['custId']
    customerName = custDetails['customerName']
    customerOrder = custDetails['items']
    print("Hi, what can I get for you today!")
    print("Hello, I would like to have ")
    for i, order in enumerate(customerOrder):
        print(order)
        if(order not in quickOrders):
            addOrderToQueue.append(order)
        else:
            provideCoffee.append(order)
    time.sleep(random.randrange(2, 6))
    if len(provideCoffee) > 0:
        print("Hi %s, here is your " % customerName)
        for i, v in enumerate(provideCoffee):
            print(v)
            QueueUrl = "http://localhost:4000/customer/" + str(customerID)
            custheader = {'Content-Type': 'application/json'}
            requests.delete(QueueUrl, data=json.dumps({"itemName": v}), headers=custheader)
    if len(addOrderToQueue) > 0:
        print("{} {} will be provided in a while ".format(customerName, addOrderToQueue))
        for i, v in enumerate(addOrderToQueue):
            add_orders_for_Barista(customerID, customerName, v)
    else:
        print("Have a good day! Bye")

def get_customer_in_queue():
    custQueueURL = 'http://localhost:5000/removecustomer'
    queueResponse = requests.delete(custQueueURL)
    if(queueResponse.status_code == requests.codes.ok):
        custQueueResponse = queueResponse.json()
        custID = custQueueResponse['id']
        # print(custID)
        waitTime = random.randrange(2, 6)
        time.sleep(waitTime)
        get_customer_order(custID)
    elif queueResponse.status_code == 204:
        print("Awaiting customers!!")
        time.sleep(random.randrange(2, 6))
    else:
        print("Server Error!!")
        time.sleep(random.randrange(2, 6))


def get_time():
    wallClockURL = 'http://localhost:10001/wallclock'
    queueResponse = requests.get(wallClockURL).json()
    print("Printing time %s" %queueResponse['time'])


print("Cashier Started")
while(True):
    get_customer_in_queue()
    get_time()
# get_customer_order(2)