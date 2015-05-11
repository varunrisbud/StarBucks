from customer import Customer

class UtilityClass:
    customers = None

    def __init__(self):
        self.customers = []

    def addCustomer(self, customer):
        self.customers.append(customer)

    def displayCustomerList(self):
        print("Customer List: ", self.customers)