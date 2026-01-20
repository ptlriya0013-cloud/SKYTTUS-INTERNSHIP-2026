#math module 
import mymath

print(mymath.add(10,5))
print(mymath.subtract(10,5))
print(mymath.multiply(10,5))
print(mymath.division(10,5))



#string module 
import string_op

print(string_op.to_upper("python"))
print(string_op.reverse("python"))
print(string_op.length("python"))



#Use a random module to generate 5 random integers
import random

for i in range(5):
    print(random.randint(1, 100))



#Use datetime module to display current date and time
import datetime

now = datetime.datetime.now()
print("Current Date & Time:", now)



#use math module to find factorial of a number
import math

n = int(input("Enter number: "))
print("Factorial:", math.factorial(n))



#package shapes
from shapes import circle, rectangle

print("Circle Area:", circle.area(7))
print("Circle Circumference:", circle.circumference(7))

print("Rectangle Area:", rectangle.area(10, 5))
print("Rectangle Perimeter:", rectangle.perimeter(10, 5))



#import multiple functions from one module
from calc import add, mul, sub, div, mod

print(add(3, 4))
print(mul(3, 4))
print(sub(3, 4))
print(div(3, 4))
print(mod(30, 4))



#Shuffle a list using random module
import random

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print("Shuffled list:", numbers)



#calculate the difference between two dates
from datetime import date

d1 = date(2024, 1, 5)
d2 = date(2024, 11, 19)

diff = d2 - d1
print("Difference in days:", diff.days)



#Use OS Module to list files in a directory
import os

path = "."   # current directory
files = os.listdir(path)

for file in files:
    print(file)

