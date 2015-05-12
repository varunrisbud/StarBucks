__author__ = 'Akshay_Jarandikar'

from random import randint
import logging
import json
import time

import requests


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def get_time():
    wallClockURL = 'http://localhost:10001/wallclock'
    queueResponse = requests.get(wallClockURL).json()
    # print("Printing time %s" %queueResponse['time'])
    return queueResponse['time']


while(True):
    custQueueUrl = "http://localhost:3000/queue/orderqueue"
    response = requests.delete(custQueueUrl)
    if response.status_code == 200:
        r = response.json()
        customerId = r['custId']
        customerName = r['customerName']
        itemName = r['itemName']

        time.sleep(randint(4, 10))
        print("{} Barista: Hey {}, your {} is ready..".format(get_time(), customerName, itemName))
        # print("Barista: Thank you..")
        QueueUrl = "http://localhost:4000/customer/" + str(customerId)
        custheader = {'Content-Type': 'application/json'}
        requests.delete(QueueUrl, data=json.dumps({"itemName": itemName}), headers=custheader)
    elif response.status_code == 204:
        # print("Waiting for next order..")
        time.sleep(randint(3, 6))