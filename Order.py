__author__ = 'Monil'


class Order:
    """Base class for order object"""
    def __init__(self, customerid, customername, itemname):
        self.customerid = customerid
        self.customername = customername
        self.itemname = itemname

    def displayOrder(self):
        print("Order => {}...{}...{}".format(self.customerid, self.customername, self.itemname))