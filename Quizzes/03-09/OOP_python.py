#Polymorphism in Python
#Python allows polymorphism in the form of the same function names being used for different types of objects.
#This can be exemplified with:
# - Built-in methods like len()

items = [1,2,3,4,5,6,"String"]
sentence = "This is a sentence"

print("Length of the items list : {}".format(len(items)))
print("Length of the sentence string : {}".format(len(sentence)))

# - With class methods
# As a dynamic typed language, we need to assume methods to be called exists in each class. 

class Cat:
    def eat(self):
        print("The cat eats fish.")
    def sound(self):
        print("The cat says 'Meow'")
    def move(self):
        print("The cat jumps.")

class Dog:
    def eat(self):
        print("The dog eats meat.")
    def sound(self):
        print("The dog says 'Woof'")
    def move(self):
        print("The dog runs.")

class Bird:
    def eat(self):
        print("The bird eats worms.")
    def sound(self):
        print("The bird says 'Chirp'")
    def move(self):
        print("The bird flies.")

objList = [Dog(),Cat(),Bird(),Cat(),Bird(),Dog()]

#Type of variable is determined only during run time.
#However, due to polymorphism we can do the following:
for obj in objList:
    print(type(obj))
    obj.move()
    obj.eat()
    obj.sound()

# - With functions that take any object, again we need to assume objects passed have the methods specified. 
def actions(obj):
    print("Actions function!")
    print(type(obj))
    obj.move()
    obj.eat()
    obj.sound()

actions(Dog())
actions(Cat())
    
# Inheritance in Python
# Inheritance allows us to re use code by defining a class that will inherit the properties and methods of a base class,
# extending its functionality and enabling re usability.
# -Polymorphism can also be achieved by defining methods in a derived class that have the same
# name as methods in the base class. This method is inherited, but we can modifiy it using the same name. (Method Overriding)

#The __init__ method is a reserved method, meant to be the constructor function.
class Vehicle():
    def __init__(self,speed):
        self.speed = speed

    def maxSpeed(self):
        print("A vehicle is used for transport, this means it has a max speed")

# A derived class can override the __init__ method of the base class, extending its functionality.
# The super() function will make the derived class inherit all the methods and properties from its base class.

class Car(Vehicle):
    def __init__(self,speed):
        super().__init__(speed)
        #Added additional variables to the car class,but keeping speed from its base class. 
        self.numberOfDoors = 4

    def maxSpeed(self):
        print("A car can achieve a max speed of {} km/h".format(self.speed))

class MotorBike(Vehicle):
    def __init__(self,speed):
        super().__init__(speed)
        #Added additional variables to the motorbike class,but keeping speed from its base class. 
        self.numberOfSeats = 1

    def maxSpeed(self):
        print("A motorbike can achieve a max speed of {} km/h".format(self.speed))

class AirPlane(Vehicle):
    def  __init__(self,speed):
        super().__init__(speed)

    def maxSpeed(self):
        print("A plane can achieve a max speed of {} km/h".format(self.speed))

vehicles = [Vehicle(0),Car(250),MotorBike(300),AirPlane(1500)]

#Again we need to assume all objects in list has maxSpeed() method
for v in vehicles:
    v.maxSpeed()

print("A car has {} doors".format(vehicles[1].numberOfDoors))

print("A bike has {} seats".format(vehicles[2].numberOfSeats))
