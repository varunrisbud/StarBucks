__author__ = 'Akshay_Jarandikar'

from random import randint
import logging
import requests, json, time

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

while(True):
    custQueueUrl = "http://localhost:3000/queue/orderqueue"
    response = requests.delete(custQueueUrl)
    if response.status_code == 200:
        r = response.json()
        customerId = r['customerId']
        customerName = r['customerName']
        itemName = r['itemName']

        time.sleep(randint(3, 6))
        print("Hey {}, your {} is ready..".format(customerName, itemName))
        print("Thank you..")
        QueueUrl = "http://localhost:4000/customer/" + str(customerId)
        custheader = {'Content-Type': 'application/json'}
        requests.delete(QueueUrl, data=json.dumps({"itemName": itemName}), headers=custheader)
    elif response.status_code == 204:
        print("Waiting for next order..")
        time.sleep(randint(3, 6))
    else:
        print("Server Error!!")