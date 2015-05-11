__author__ = 'Sameer Ranade'
import requests
import json
import sys
import time
from random import randint

count = 1
order=[["Shaken Sweet Tea", "Coffee1"], ["Coffee2"], ["Coffee3","Coffee4","Coffee5"],["Coffee6"],["Coffee7","Coffee8"],["Coffee9"],["Coffee10","Coffee11"]]

def main_loop():
    while 1:
        # do your stuff...
        createCustomer = 'http://localhost:4000/customer'
        customername = "Customer %d" % count
        custheader = {'Content-Type': 'application/json'}
        addOrder = requests.post(createCustomer, data=json.dumps({"custId": count, "customerName": customername, "items": order[randint(0, 6)]}), headers=custheader)
        print('Create Customer')

        addcustomertoqueue = 'http://localhost:5000/addcustomer/%d' %count
        addcustomertoqueuerequest = requests.post(addcustomertoqueue)
        print('Added to queue')

        time.sleep(0.1)
        ++count

if __name__ == '__main__':
    try:
        main_loop()
    except KeyboardInterrupt:
        print >> sys.stderr, '\nExiting by user request.\n'
        sys.exit(0)