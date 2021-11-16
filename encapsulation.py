class computer:
    def __init__(self):
        self.price=1000
    def sell(self):
        print("selling price {}".format(self.price))
    def set(self,p):
        self.price=p
c=computer()
c.sell()
c.price=1100
c.sell()
c.set(1200)
c.sell()
