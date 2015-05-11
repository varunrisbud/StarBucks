class Customer:

    def __init__(self, name, id, order):
        self.name = name
        self.id = id
        self.order = order

    def displayName(self):
        print("Customer Name ", self.name)

    def displayCustId(self):
        print("Customer ID %d" % self.id)

    def displayOrder(self):
        print("Customer Order ", self.order)