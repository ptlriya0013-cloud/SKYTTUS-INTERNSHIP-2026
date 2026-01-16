#print numbers from 1 to 10
for i in range(1,11):
 print(i)


 #display multiplication table for a given number
 start = int(input("Enter start number: "))
 end = int(input("Enter end number: "))
 num = int(input("Enter number for a table: "))

 for n in range(start,end+1):
   print(f"{num} X {n} = {num * n}")


#find factorial of a number
n = int(input("Enter interger number: "))
fact = 1

if n >= 0:
  for i in range(1,n+1):
    fact = fact * i
    print("Factorial of", n, "is", fact)
else :
  print("Factorial does not exist for negative numbers")


#generate the first N fibonacci numbers
n = int(input("Enter integer number: "))
a = 0
b = 1

if n <= 0:
  print("Please enter a positive number")
elif n == 1:
  print(a)
else :
  print(a, b, end="")
  for i in range(2,n):
     c = a + b
     print(c,end="")
     a = b
     b = c


#check if a number is prime 
n = int(input("Enter integer number: "))

if n <= 1:
    print("It's not a prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print("It's not a prime number")
            break
    else:
        print("It's a prime number")

#reverse a number(e.g. 123 ---> 321)
n = int(input("Enter a number: "))
rev = 0
original = n

while n > 0:
   digit = n % 10 
   rev = rev * 10 + digit
   n = n // 10

print("Reverse of", original, "is", rev)


#count digits in a number
n = int(input("Enter a number: "))

if n <= 0:
   print("Please enter positive number")

else :
    count = 0
    temp = n  
    while temp > 0:
        temp = temp // 10  
        count += 1          
    print("Number of digits in", n, "is", count)


#find sum of even numbers between 1-100

sum_even = 0

for i in range(2,101):
   if i % 2 == 0:
      sum_even += i
      print("print("Sum of even numbers from 1 to 100 is:", sum_even)")


#print a pyramid pattern 
n = 5

for i in range(1, n + 1):
    print("*" * i)


#find all divisors of a number
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)


   
