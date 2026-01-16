#check if a person is eligible for vote 
age = int(input("Enter a number: "))

if age < 18 :
    print("Person is not eligible for vote")
else :
    print("Person is eligible for vote")

#grade calculator based on marks.90+ = A, 80+ = B, else C
marks = int(input("Enter marks: "))

if marks >= 90:
    print("You got A+")
elif marks >= 80:
    print("You got B+")
else :
    print("You got C")


#simulate a traffic light. Red = Stop, Yellow = Wait, Green = Go
light = ("Enter a color of light: ")

if light == Red:
    print("You have to stop")
elif light == Yellow:
    print("You have to wait")
elif light == Green:
    print("You have to go")
else :
    print("Invalid Color")


#ATM widthdrawal check : sufficient balance or not
balance = float(input("Enter balance: "))
widthdraw = float(input("Enter widthdrawal amount: "))

if widthdraw <= balance:
    print("Withdrawal successful")
    balance -= widthdraw
else:
    print("Insufficient balance")

print("Remaining balance:", balance)


#check if a number is positive, negative or zero
num = float(input("Enter a number: "))

if num < 0:
    print("Number is negative")
elif num == 0:
    print("Number is zero")
else :
    print("Number is positive")


#check if a number lies within given range
num = int(input("Enter a number: "))
low = int(input("Enter a lower limit: "))
high = int(input("Enter a upper limit: "))

if low <= num >= high:
    print("Number lies within range")
else :
    print("Number does not lies within range")


#username and password varification 
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and  password == "1234":
    print("Login Successful")
else :
    print("Login Failed")


#electricity bill calculated based on unit consumed
units = int(input("Enter consumed units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100*5 + (units-100)*8
else:
    bill = 100*5 + 100*8 + (units-200)*10

print("Electricity bill:", bill)


#simple calculator (add, subtract, multiply, divide)
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operation")


#check type of triangle  (equilateral, isosceles, scalene).	
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
