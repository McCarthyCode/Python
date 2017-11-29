class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    
    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        return self.price * (1 + tax)

    def return_item(self, state):
        if(state == "defective"):
            self.status = "defective"
            self.price = 0
        elif(state == "in box"):
            self.status = "for sale"
        elif(state == "opened"):
            self.status = "used"
            self.price *= 0.80
        else:
            print "Return reason unknown."
        return self

    def display_info(self):
        print "Price: ", self.price
        print "Name:  ", self.name
        print "Weight:", self.weight
        print "Brand: ", self.brand
        print "Status:", self.status
        return self

item = Product(299.99, "Switch", 10, "Nintendo")

item.display_info()
print "Price with Chicago tax (10.25%):", item.add_tax(.1025)
item.sell().display_info()
item.return_item("in box").display_info()
item.sell().return_item("opened").display_info()
