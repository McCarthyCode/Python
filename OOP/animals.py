class Animal(object):
    def __init__(self):
        self.name = ""
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "Health:", self.health
        return self

a = Animal()
a.walk().walk().walk().run().run().display_health()

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        self.health = 150

    def pet(self):
        self.health -= 5
        return self

dog = Dog()
dog.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):
    def __init__(self):
        super(Dragon, self).__init__()
        self.health = 170
    
    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        print "I am a Dragon"
        super(Dragon, self).display_health()
        return self

dragon = Dragon()
dragon.walk().walk().walk().run().run().fly().display_health()
