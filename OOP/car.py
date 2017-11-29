class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.15 if price > 10000 else 0.12

    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax
        return self

cars = [
    Car(2000, "35mph", "Full", "15mpg"),
    Car(2000, "5mph", "Not Full", "105mpg"),
    Car(2000, "15mph", "Kind of Full", "95mpg"),
    Car(2000, "25mph", "Full", "25mpg"),
    Car(2000, "45mph", "Empty", "25mpg"),
    Car(20000000, "35mph", "Empty", "15mpg"),
]

for i in cars:
    i.display_all()
