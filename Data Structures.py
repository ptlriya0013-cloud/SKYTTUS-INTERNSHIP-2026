#create a tupple with five numbers
t = (45,34,23,12,56)
print(t)

#access the third element of the tuple
print(t[2])

#unpack a tuple into seperate variables
a, b, c, d, e = t
print(a, b, c, d, e)

#create a set of 5 fruits
fruits = ["Mango","Apple","Banana","Guava","Graps"]
print(fruits)

#add a new fruit to the list
fruits.append("pineapple")
print(fruits)


#remove an element from a set 
fruits.remove("Banana")
print(fruits)

#find union of two swts
set1 = {1,2,3}
set2 = {4,5,6}
print(set1| set2)

#find intersection of two sets
set1 = {1,2,3,4}
list2 = {3,5}
print(set1 & set2)

#check if one set is subset of another
a = {1,2}
b = {1,2,4,8}
print(a.issubset(b))

#convert a list with duplicate values into a set to remove duplicates
list = [1,1,2,2,2,3,4,4,4,5,5]
unique_set = set(list)
print(unique_set)


#create a dictonary storing student name and marks
students = {"Srushti": 87, "Avani": 58, "Riddhi": 70}
print(students)

#add a new key-value pair to existing dictonary
students["Densi"] = 65
print(students)


#delete a key-value pair from a dictonary
del students["Avani"]
print(students)



#merge two dictonaries into one 
s1 = {"s": 87, "a": 58}
s2 = {"d": 65, "r": 70}
merged = s1 | s2
print(merged)

#check if a key exists in a dictonary
key = "Srushti"

if key in students:
    print("Key exists")
else:
    print("Key does not exist")


#count word frequency in a given string using dictonary
sentence = "python is easy and python is powerful"
words = sentence.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)


#find the key with the maximum value in a dictonary
marks = {"A": 70, "B": 85, "C": 90}
print(max(marks, key=marks.get))

#reverse keys and values in a dictonary
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)


#update the value for a specific value 
students["Riya"] = 95
print(students)


#convert a list of tuples into a dictonary
lst = [("a", 1), ("b", 2), ("c", 3)]
d = dict(lst)
print(d)

