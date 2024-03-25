# Lesson 1

# Lists and Tuples

# Lists Elements
numbers = [1, 2, 3]
print(numbers)
#  empty list
my_list = []
# list with mixed data types
my_list = [1, "Hello", 3.4]

# Access Python List Elements
languages = ["Python", "Swift", "C++"]
print(languages[0])
print(languages[2])

# Slicing of a List
languages = ["Python", "Swift", "C++"]
print(languages[-1])
my_list = ['p', 'r', 'e', 'o', 'r', 'm', 'i']
# items from 2 index to index 4
print(languages[2:5])
# items from 5 index to end
print(languages[5:])
# items beginning to end
print(languages[:])
# access item at index 2
print(languages[-3])

# Add Elemnets to a Python List
# 1. Using append()

numbers = [21, 24, 34, 54, 12]
print("Before Append:", numbers)
# using append method
numbers.append(32)
print("After Append:", numbers)

# 2. Using extend()

prime_numbers = [2, 3, 5]
print("List:", prime_numbers)
even_numbers = [4, 6, 8]
# join two lists togther
prime_numbers.extend(even_numbers)
print("List after append:", prime_numbers)

# Change List Items
languages = ['Python', 'Swift', 'C++']
# changing the third item to C
languages[2] = 'C'
print(languages)

# Remove an item from a List
# 1. Using del()

languages = ['Python', 'Swift', 'C++', 'C', 'Java', 'Rust', 'R']
# deleting thw second item
del languages[1]
print(languages)
# deleting the last item
del languages[-1]
print(languages)
# delete first two items 
del languages[0:2]
print(languages)

# 2. Using remove
languages = ['Python', 'Swift', 'C++']
languages.remove('Python')
print(languages)

# Iterating through a List
languages = ['Python', 'Swift', 'C++']
for language in languages:
    print(language)

# List Comprehension
numbers = [number*number for number in range(1, 6)]
print(numbers)

# Tuples

var1 =("Hello")
print(var1)

# Access Python Tuple Elements
# 1. Indexing

letters = ("p", "r", "g", "r", "a")
print(letters[0])
print(letters[4])

# 2. Negative Indexing
letters = ("p", "r", "g", "r", "a")
print(letters[-3])
print(letters[-1])

# Python Tuple Method
my_tuple = ('a','p','l','e')
print(my_tuple.count('p'))
print(my_tuple.index('l'))

# ----------------------------------------------------------------

# Lesson 2

# Dictionaries
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "Engaland": "London"}
print(capital_city)
numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)

# Add Elments to Dictionary
capital_city = {"Nepal": "Kathmandu", "Italy": "Rome", "Engaland": "London"}
print("Initail Dictionary: ",capital_city)
capital_city["Japan"] = "Tokyo"
print("Updated Dictionary: ",capital_city)

# Change Value of Dictionary
student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
del student_id[111]
print("Updated Dictionary ", student_id)

# -----------------------------------------------------------

# Lesson 3

# Dictionary Membership Test
# Testing Keys
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(1 in squares)
print(2 not in squares)
print(49 in squares)

# # Iterating Through a Dictionary
# squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# for 25 in squares:
# print(squares[9])

# -------------------------------------------------------------------

# Lesson 4

# Sets

# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)
# create a set of string type
vowel_letters = {'a', 'e', 'l', 'o', 'u'}
print('Vowel Letters:', vowel_letters)
# create a set of mixed data types
mixed_set = {'Hello', 101, -2, 'Bye'}
print('Set of mixed data types:', mixed_set)
# create an empty set
empty_set = set()
# create an empty dictionary
empty_dictionary = {}
# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))
# check data type of empty_ser
print('Data type of empty_set:', type(empty_set))

# Duplicate Items in a set
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)

# Add and Update Set Items in Python

# Add Items to a Set in Python
numbers = {21, 34, 54, 12}
print('Initial Set:',numbers)
numbers.add(32)
print('Update Set:',numbers)

# Update Python Set
companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
companies.update(tech_companies)
print(companies)

# Remove an Element from a Set
languages = {'Swift', 'Java', 'Python'}
print('Initial Set:', languages)
removeValue = languages.discard('Java')
print('Set after removal():', languages)

# Iterate Over a Set in Python
fruits = {"Apple", "Peach", "Mango"}
#  for loop to acces each fruits
for fruit in fruits:
    print(fruit)

# Find Number of Set Elements
even_numbers = {2,4,6,8}
print('Set:',even_numbers)
# find number of elements
print('Total Elements:', len(even_numbers))

# Python Set Operations

# Union of Twon Sets
A = {1,3,5}
B = {0,2,4}
# perform union operation using |
print('Union using |:', A | B)
# perform union operation using union()
print('Union using union():', A.union(B))

# Set Intersection
A = {1,3,5}
B = {1,2,3}
# perform intersection operation using &
print('Intersection using &:', A & B)
# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))

# Difference between Two Sets
A = {2,3,5}
B = {1,2,6}
# perform difference operation using &
print('Difference using &:', A - B)
# perform difference operation using difference()
print('Difference using difference():', A.difference(B))

# Set Symmetric Difference
A = {2,3,5}
B = {1,2,5}
# perform difference operation using &
print('using ^:', A ^ B)
# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))

# Check if two sets are equal
A = {1,3,5}
B = {3,5,1}
# perfom difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal') 

# --------------------------------------------------------------------

# Lesson 5

# Python String and String Methods

# Python String
name = "Python"
print(name)
message = "I love Python."
print(message)

greet = 'hello'
print(greet[1])
print(greet[-4])
print(greet[1:4])

# message = 'Hola Amigos'
# message[0] = 'H'
# print(message)

message = 'Hola Amigos'
message = 'Hello Friends'
print(message)

# multiline string
message = """
Never gonna give you up
Never gonna let you down"""
print(message)

# Python String Operations
# 1. Compare Two Strings

str1 = "Hello, world!"
str2 = "I Love Python."
str3 = "Hello, world!"
# compare str1 and str2
print(str1 == str2)
# compare str1 and str3
print(str1 == str3)

# 2. Join Twon or More Strings
greet = "Hello, "
name = "Jack"
# using + operator
result = greet + name
print(result)

# Iterate Through a Python String
greet = 'Hello'
for letter in greet:
    print(letter)
# count length of greet string
print(len(greet))

# escape double quotes
example = "He said, \"What's there?\""
# escape single quotes
example = 'He said, "What\'s there?"'
print(example)

# Python String Formatting (f-Strings)
name = 'Cathy'
country = 'UK'
print(f'{name} is from {country}')

# -----------------------------------------------------------

# Weekly Challenge

# Accepting user input to create a list of integers
numbers = input("Enter a list of integers separated by spaces: ").split()

# Converting input strings to integers
numbers = [int(num) for num in numbers]

# Computing the sum of all integers in the list
sum_of_numbers = sum(numbers)

print("Sum of the integers:", sum_of_numbers)

# Creating a tuple containing the names of favorite books
favorite_books = ("Getting Things Done", "The Black Dawn", "B.L.F", "Long Walk To Freedom", "Bible")

# Printing each book name on a separate line using a for loop
for book in favorite_books:
    print(book)

# Using a dictionary to store information about a person
person = {}

# Asking user for input
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")

# Printing the dictionary
print(person)

# Accepting user input to create two sets of integers
set1 = set(map(int, input("Enter elements of set 1 separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of set 2 separated by spaces: ").split()))

# Finding the intersection of the two sets
intersection_set = set1.intersection(set2)

print("Common elements:", intersection_set)

# Storing a list of words
words = ["apple", "banana", "orange", "grape", "pineapple", "kiwi"]

# Creating a new list using list comprehension with words having odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

print("Words with odd number of characters:", odd_length_words)

# ------------------------------------------------------------------------------

# Week two : Assignment

# 1. Create an empty list called my_list.
my_list = []

# 2. Append the following elements to my_list: 10, 20, 30, 40.
my_list.extend([10, 20, 30, 40])

# 3. Insert the value 15 at the second position in the list.
my_list.insert(1, 15)

# 4. Extend my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

# 5. Remove the last element from my_list.
my_list.pop()

# 6. Sort my_list in ascending order.
my_list.sort()
