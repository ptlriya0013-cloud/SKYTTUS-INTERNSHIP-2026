#read a file and display its contents
try:
    with open("file.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found")


#count the number of lines in a file
try:
    with open("file.txt", "r") as f:
        lines = f.readlines()
        print("Number of lines:", len(lines))
except FileNotFoundError:
    print("File not found")


#count how many times each word appears in a file 
try:
    with open("file.txt", "r") as f:
        text = f.read().lower().split()
        word_count = {}
        for word in text:
            word_count[word] = word_count.get(word, 0) + 1
        print(word_count)
except FileNotFoundError:
    print("File not found")


#write 5 user-entered sentences in file
with open("file.txt", "w") as f:
    for i in range(5):
        sentence = input(f"Enter sentence {i+1}: ")
        f.write(sentence + "\n")


#Append a list of strings to an existing file
lines = ["Python", "is", "easy", "to", "learn"]

with open("file.txt", "a") as f:
    for line in lines:
        f.write(line + "\n")


#Read a file and print only lines containing a specific word
word = input("Enter the word to search: ")

try:
    with open("file.txt", "r") as f:
        for line in f:
            if word in line:
                print(line, end="")
except FileNotFoundError:
    print("File not found")


#Replace a specific word in a file and save changes
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

try:
    with open("file.txt", "r") as f:
        content = f.read()
    content = content.replace(old_word, new_word)
    with open("file.txt", "w") as f:
        f.write(content)
    print("Word replaced successfully")
except FileNotFoundError:
    print("File not found")


#Merge the contents of two text files into a third file
try:
    with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as f3:
        f3.write(f1.read() + "\n" + f2.read())
    print("Files merged successfully")
except FileNotFoundError:
    print("One of the files not found")


#Read a CSV file and display its content in a formatted way
import csv

try:
    with open("data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("\t".join(row))
except FileNotFoundError:
    print("CSV file not found")



#. Back up a file
import shutil

try:
    shutil.copy("file.txt", "file_backup.txt")
    print("Backup created successfully")
except FileNotFoundError:
    print("File not found")
