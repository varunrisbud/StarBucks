import queue

class CustomerQueue:

    custQueue = None

    def __init__(self):
        self.custQueue = queue.Queue()

    def printQ(self):
        print(self.custQueue)