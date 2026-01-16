#calculate the remainders of two numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Remainder =", a % b)


#check if number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#compare two numbers and print the larger one 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Larger number:", a)
else:
    print("Larger number:", b)


#calculate the square and a cube of a number
n = int(input("Enter a number: "))
print("Square =", n ** 2)
print("Cube =", n ** 3)


#check if two entered numbers are equal 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Both numbers are equal")
else:
    print("Numbers are not equal")


#print true if both numbers are positive else false
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a > 0 and b > 0)


#convert float into integer 
num = float(input("Enter a float number: "))
print("Integer value:", int(num))


#take a number as string , convert into int , multiply by 10 
num = input("Enter a number: ")
num = int(num)
print(num * 10)


#use AND and OR operators to check multiple conditions
a = int(input("Enter a number: "))

print(a > 0 and a < 100)   # AND condition
print(a < 0 or a > 100)   # OR condition


#divide two numbers and print the quotient 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient =", a / b)
