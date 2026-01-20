# Base class Animal with their subclasses Dog and Cat
class Animal:
    def speak(self):
        print("Animal maks a sounds")

class dog:
    def speak(self):
        print("Dog Barks")

class cat:
    def speak(self):
        print("Cat Meow")

d = dog()
c = cat()
d.speak()
c.speak()


#A class hieararchy for vehicle ---> Car ---> Electric car
class Vehicle:
    def fuel(self):
        print("Vehicle use fuel.")

class Car:
    def fuel(self):
        print("Car used petrol/diesel.")

class ElectricCar:
    def fuel(self):
        print("Electric Car used Electricity.")


C1 = Car()
E1 = ElectricCar()
C1.fuel()
E1.fuel()



#Implement method overriding in a base and derived class.
class Fruit:
    def color(self):
        print("Some Fruit comes red in color.")

class Strawberry(Fruit):
    def color(self):
        print("Strawberry comes red in color.")

class Cherry(Fruit):
    def color(self):
        print("Cherry comes red in color.")

class Apple(Fruit):
    def color(self):
       print("Apple comes red in color.")

F = Fruit()
S = Strawberry()
C = Cherry()
A = Apple()

F.color()
S.color()
C.color()
A.color()



#Demonstrate multiple inheritance with two parent class.
class Flower:
    def color(self):
        print("Flower comes in different colors")

class Lotus:
    def pink(self):
        print("Lotus comes in pink color")

class WhiteLotus(Flower,Lotus):
    def white(self):
        print("White Lotus comes in white color")

L = Lotus()
W = WhiteLotus()

W.color()
W.pink()
W.white()



#Polymorphic function that works with different shapes.
class Shapes:
    def area(self):
        print("Area of different shapes")

class Rectangle(Shapes):
    def area(self):
        print("Area of rectangle")

class Circle(Shapes):
    def area(self):
        print("Area of Circle")

shapes_list = [Rectangle(), Circle()]

for s in shapes_list:
    s.area()



#Create a BankSystem with CurrentAccount and SavingAccount 
class BankSystem:
    def  account_type(self):
        print("General Account")
        
class SavingAccount(BankSystem):
    def account_type(self):
        print("Saving Account")

class CurrentAccount(BankSystem):
    def account_type(self):
        print("Current Account")
      
s1 = SavingAccount()
a1 = CurrentAccount()
s1.account_type()
a1.account_type()


#A class with private attributes and getter/setter methods        
class Person:
    def __init__(self):
        self.__age = 0   

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

p = Person()
p.set_age(20)
print("Age:", p.get_age())


#A Teacher and Student Class to show inheritance
class Teacher:
    def teach(self):
        print("Teaching students")

class Student(Teacher):
    def study(self):
        print("Student is studying")

s = Student()
s.teach()
s.study()


#A Musicplayer class and subclass Spotify to override play method
class Musicplayer:
    def play(self):
        print("Playing Music")

class Spotify(Musicplayer):
    def play(self):
        print("Playing music on Spotify")

sf = Spotify()
sf.play()



#Demonstrate the use of super() in inheritance
class Base:
    def __init__(self):
        print("Base class constructor")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Derived class constructor")

d = Derived()

