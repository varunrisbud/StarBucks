__author__ = 'Sameer Ranade'
import requests
import json
import sys
import time
from random import randint


order=[["Shaken Sweet Tea","Caffe Latte"],["Fresh Brewed Coffee"],["Caffe Latte","Caffe Mocha","Iced Coffee"],["Iced Coffee"],["Espresso","Iced Coffee"],["Espresso"],["Espresso","Iced Coffee"]]

def main_loop():
    count = 1
    while 1:
        # do your stuff...
        createCustomer = 'http://localhost:4000/customer'
        customername = "Customer %d" % count
        custheader = {'Content-Type': 'application/json'}
        addOrder = requests.post(createCustomer, data=json.dumps({"custId": count, "customerName": customername, "items": order[randint(0, 6)]}), headers=custheader)

        addcustomertoqueue = 'http://localhost:5000/addcustomer/%d' %count
        addcustomertoqueuerequest = requests.post(addcustomertoqueue)
        count += 1
        time.sleep(0.1)


if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)