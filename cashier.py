__author__ = 'Varun'
import json
import time
import random
import logging

from flask import Flask
import requests


app = Flask(__name__)

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def add_orders_for_Barista(custID, custName, custOrder):
    baristaQueueURL = 'http://localhost:3000/queue/orderqueue'
    custheader = {'Content-Type': 'application/json'}
    addOrder = requests.post(baristaQueueURL,
                             data=json.dumps({"custId": custID, "customerName": custName, "itemName": custOrder}),
                             headers=custheader)


def get_customer_order(custID):
    quickOrders = ['Fresh Brewed Coffee', 'Caffe Latte', 'Caffe Mocha', 'Iced Coffee', 'Espresso']
    provideCoffee = []
    addOrderToQueue = []
    custQrderURL = "http://localhost:4000/customer/" + str(custID)
    custDetails = requests.get(custQrderURL).json()
    customerID = custDetails['custId']
    customerName = custDetails['customerName']
    customerOrder = custDetails['items']

    for i, order in enumerate(customerOrder):
        # print(order)
        if(order not in quickOrders):
            addOrderToQueue.append(order)
        else:
            provideCoffee.append(order)
    time.sleep(random.randrange(2, 6))
    if len(provideCoffee) > 0:
        print("{} Cashiser: Hi {}, here is your {}".format(get_time(), customerName, provideCoffee))
        for i, v in enumerate(provideCoffee):
            QueueUrl = "http://localhost:4000/customer/" + str(customerID)
            custheader = {'Content-Type': 'application/json'}
            requests.delete(QueueUrl, data=json.dumps({"itemName": v}), headers=custheader)
    if len(addOrderToQueue) > 0:
        print("{} Cashier: {} {} will be provided in a while ".format(get_time(), customerName, addOrderToQueue))
        for i, v in enumerate(addOrderToQueue):
            add_orders_for_Barista(customerID, customerName, v)
    else:
        print("{} Cashier: Have a good day! Bye".format(get_time()))

def get_customer_in_queue():
    custQueueURL = 'http://localhost:5000/removecustomer'
    queueResponse = requests.delete(custQueueURL)
    if(queueResponse.status_code == requests.codes.ok):
        custQueueResponse = queueResponse.json()
        custID = custQueueResponse['id']
        waitTime = random.randrange(2, 6)
        time.sleep(waitTime)
        print("{} Cashier: Hi, what can I get for you today!".format(get_time()))
        get_customer_order(custID)
    elif queueResponse.status_code == 204:
        time.sleep(random.randrange(2, 6))


def get_time():
    wallClockURL = 'http://localhost:10001/wallclock'
    queueResponse = requests.get(wallClockURL).json()
    return queueResponse['time']


print("Cashier Started")
while(True):
    get_customer_in_queue()
    get_time()