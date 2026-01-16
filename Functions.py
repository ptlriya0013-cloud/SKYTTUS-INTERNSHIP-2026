# check if number is prime 
def check_prime(n):
    if n <= 1:
        print("Number is not prime")
        return
    
    for i in range(2, n):
       if n % i == 0:
        print("Number is not prime")
        return
    print("Number is prime")
    
num = int(input("Enter a number: "))
check_prime(num)


#reverse a string
def rev_str(s):
   return s[::-1]

print(rev_str("python"))

   
# function to find factorial
def factorial(n):
    if n < 0:
        print("Factorial does not exist for negative numbers")
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        print("Factorial of", n, "is", fact)

n = int(input("Enter integer number: "))
factorial(n)


#calculate simple interest
def simple_interest(p, r, t):
   return(p * r * t) / 100
print(simple_interest(1000, 5, 2))


#check if a word is palindrome
def check_palindrome(s):
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

word = input("Enter a word: ")
check_palindrome(word)
   

#count vowel's in a string
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

print(count_vowels("Python"))


#merge two lists
def merge_lists(l1, l2):
    return l1 + l2

print(merge_lists([1, 2], [3, 4]))


#function to find GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(12, 18))


#function to find area of rectangle
def area_rectangle(length, breadth):
    return length * breadth

print(area_rectangle(5, 4))


#function to check armstrong number
def is_armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == n

print(is_armstrong(153))






   

