
# Assignment 2: Polymorphism Chall

# I decided to use cars for this part.
# Each car will have a move() method,
# but each type of car will move in its own way.

class Car:
    def move(self):
        return "The car is moving..."


class SportsCar(Car):
    def move(self):
        return "The sports car is racing fast! 🏎️"


class ElectricCar(Car):
    def move(self):
        return "The electric car is driving silently. ⚡🚗"


class Truck(Car):
    def move(self):
        return "The truck is transporting goods on the road. 🚚"


# Making objects
car1 = SportsCar()
car2 = ElectricCar()
car3 = Truck()

# Putting them in a list so I can loop through them
cars = [car1, car2, car3]

for c in cars:
    print(c.move())
