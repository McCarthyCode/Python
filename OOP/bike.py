class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self

    def displayInfo(self):
        print "    price:", self.price
        print "max_speed:", self.max_speed
        print "    miles:", self.miles
        return self

bike_one = Bike(200, "25mph")
bike_two = Bike(300, "30mph")
bike_three = Bike(250, "20mph")

bike_one.ride().ride().ride().reverse().displayInfo()
bike_two.ride().ride().reverse().reverse().displayInfo()
bike_three.reverse().reverse().reverse().displayInfo()
