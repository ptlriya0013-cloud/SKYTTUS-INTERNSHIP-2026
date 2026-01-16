#print your name, age, city in one line 
name, age, city = "Riya ", 21, "Chikhli" 
print(name, age, city)


#take user input for two numbers and print their sum 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


#convert temperature from celcius to fahrenhit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print("Temperature in Fahrenheit:", f)


#store your name in a variable and print it in uppecase
name = "Riya Patel"
print(name.upper())


#ask the user for their birth year and calculate current age 
birth_year = int(input("Enter your birth year: "))
current_year = 2026
print("Your age is:", current_year - birth_year)


#swap the values of two varivables 
a = int(input("Enter a: "))
b = int(input("Enter b: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)


#calculate the area of a rectangle 
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
print("Area of rectangle:", area)



#check is the number is posituve or negative 
num = int(input("Enter a number: "))

if num >= 0:
    print("Positive number")
else:
    print("Negative number")


#ask for two numbers and print their average 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
avg = (a + b) / 2
print("Average =", avg)

