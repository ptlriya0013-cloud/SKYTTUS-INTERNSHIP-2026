# Create a CAR class with like Brand, Model, and Speed, and Methods to accelerate/brake
class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self, value):
        self.speed += value
        print("Speed after accelerating:", self.speed)

    def brake(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
        print("Speed after braking:", self.speed)

c = Car("Honda", "City")
c.accelerate(30)
c.brake(10)



#Bankaccount class with deposit and withdraw methods
class Bankaccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit", self.balance)
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance after withdrawal", self.balance)
        else:
            print("Insufficient Balance", self.balance)

acc = Bankaccount(1000)
acc.deposit(1000)
acc.withdraw(500)



#Student class with method to calculate average amrks
class Student:

    def __init__(self,marks):
        self.marks = marks
    
    def average(self):
        avg = sum(self.marks) / len(self.marks)
        print("Average marks of student", avg)

s1 = Student([45, 67, 70, 88, 79])
s1.average()


#Rectangle class with method to find area and perimeter
class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        ar = self.length * self.breadth 
        print("Area of Rectangle: ", ar)
        
    def perimeter(self):
        peri = 2 * (self.length + self.breadth)
        print("Perimeter of Rectangle: ", peri)

rect = Rectangle(13,12)
rect.area()
rect.perimeter()


#Employee class that display their salary details
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def employee(self): # instead of employee you can use display 
        print("Name:", self.name)
        print("Salary:", self.salary)

emp = Employee("Riya", 5000)
emp.employee()


#Book class to store title, author, and price and display details
class Book:

    def __init__(self,title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Price: ", self.price) 

b1 = Book("Saraswatichandra", "Pannalal Patel", 500) 
b1.display()      


#Circle class to find area and circumference
class Circle:

    def __init__(self, radius):
        self.radius = radius
        
    
    def area(self):
        ar = 3.14 * self.radius * self.radius
        print("Area of Circle: ", ar)
        
    def circumference(self):
        cf = 2 * 3.14 * self.radius
       
        print("Circumference of Circle: ", cf)

C1 = Circle(30)
C1.area()
C1.circumference()



#Laptop class with a method to apply discounts on price
class Laptop:

    def  __init__(self, brand, price):
        self.brand = brand
        self.price = price
    
    def apply_discounts(self, percents):
        dis = self.price * percents / 100 
        self.price -= dis
        print("Brand: ",self.brand)
        print("price of laptops after applying discounts: ", self.price)

l1 = Laptop("Dell",53000)
l1.apply_discounts(20)



#Flight class with seat booking functionality
class Flight:

    def __init__(self, seats):
        self.seats = seats

    def seat_booking(self, booking):
        
        if booking <= self.seats:
            self.seats -= booking 
            print("Booking Successful")
            print("Remaining Seats: ",self.seats)
        else:
            print("Booking failed! Not enough seats.")
            print("Available Seats: ",self.seats)
        
fly = Flight(50)
fly.seat_booking(40)
        


#Shop class with a method to add and list products
class Shop:

    def __init__(self):
        self.products = []
       

    def add_product(self, product):
        self.products.append(product)
        
    def list_products(self):
        print("Products in shop: ")
        for p in self.products:
            print(p)

sh = Shop()
sh.add_product("Laptop")
sh.add_product("Mobile")
sh.add_product("Charger")
sh.add_product("Power Bank")
sh.list_products()