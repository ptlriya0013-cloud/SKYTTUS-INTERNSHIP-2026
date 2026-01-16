# take string input and print its length
s = input("Enter a string: ")
print("Length =", len(s))


#convert a sentence into lowercase 
sentence = input("Enter a sentence: ")
print(sentence.lower())


#replace spaces with underscores in a string
s = input("Enter a string: ")
print(s.replace(" ","_"))

#extract the first and last characters of string 
s = input("Enter a string:")
print("First Character:", s[0])
print("Last Character:", s[-1])

#reverse a string using slicing 
s = input("Enter a string:")
print("Revrsed string:", s[::-1])

#count how many times a letter appears in a string
s = input("Enter a string:")
ch = input("Enter a character:")
print("Count =", s.count(ch))

#check if word is a present in a sentence
sentence = input("Enter a sentence:")
word = input("Enter a word:")

if word in sentence: 
    print ("word found")
else:
    print ("word not found")


#Take name & age and print using f-string formatting
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and I am {age} years old")


#Remove extra spaces from start and end of a string
s = input("Enter a string: ")
print(s.strip())


#Join a list of words into a single string
words = ["Python", "is", "easy"]
sentence = " ".join(words)
print(sentence)



#CREATE A LIST OF 5 FAVOURITE MOVIES
movies = ["Chhichhore","Shrikanth","Dangal","3 Idiots","Ramsetu"]
print(movies)

#add a new movie to the list
movies.append("RRR")
print(movies)

#remove the first movie from the list
movies.pop(0)
print(movies)


#sort a list of numbers in ascending order
nums = [5, 2, 9, 1, 3]
nums.sort()
print(nums)


#reverse a list
nums.reverse()
print(nums)


#find the largest number in a list
nums = [10, 25, 8, 40, 15]
print("Largest number:", max(nums))


#merge two lists into one
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print(merged_list)


#access the last element of a list without using index number
my_list = [10, 20, 30, 40]
print(my_list[-1])


#create a nested list and access a specific inner element
nested = [[1, 2, 3], [4, 5, 6]]
print(nested[1][2])   # Access 6


#count how many times an element appears in a list
nums = [1, 2, 3, 2, 4, 2, 5]
print(nums.count(2))
