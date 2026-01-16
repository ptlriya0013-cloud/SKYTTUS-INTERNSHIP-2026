#handle division by zero error
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denomirator: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


#handle invalid integer input
try:
    num = int(input("Enter a number: "))
    print("You Entered", num)
except ValueError:
    print("Error: Invalid integer input")


#open a file and handle "file not found error"
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Error: File not found")


#demonstrate multiple error blocks
try:
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    print(a / b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

except  ValueError:
    print("Error: Invalid integer input")


#use finally for resource cleanup
try:
    file = open("test.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File not found")
finally:
    print("Program execution completed")


#create a custom exception for invalid age (<18)
class InvalidAgeError(Exception):
    pass
try:
    age = int(input("Enter age: "))
    if age <18:
        raise InvalidAgeError
    print("Person is eligible for vote")

except InvalidAgeError:
    print("Person not eligible for vote")


#handle IndexError when accessing a list
try:
    a = [1, 2, 3, 4, 5]
    print(a[5])
except IndexError:
    print("Enter correct index")


#takes two numbers and handle all possible errors
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a/b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")
except ValueError:
    print("Error: Invalid Integer")
except Exception as e:
    print("Error", e)


#log error to a file instead of printing them 
class LogError(Exception):
    pass
try:
    file = open("data.txt", "r")
    print(file.read())
    file.close()
except Exception as e: 
    with open("error.log", "a") as log:
        log.write{f"Logged Error: {e}\n"}
        raise LogError
    


#validate an email format
email = input("Enter email: ")

try:
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")
    print("Valid email")
except ValueError as e:
    print(e)
