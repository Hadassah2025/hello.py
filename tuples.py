# Python Tuples
# Separated by commas
# Use round brackets ()
t = (10, 20, 30) 
print(t)
print(type(t))

# create tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples allow duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# Tuple Length
# To determine how many items a tuple has, use the len() function
# Print the number of items in the tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# To create a tuple with only one item, you have to add a comma after the item
# One item tuple, remember the comma
thistuple = ("apple",)
print(type(thistuple))

# data type of a tuple
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# Tuple() Constructor
# Use the tuple() constructor to make a tuple.
# Using the tuple() method to make a tuple
thistuple = tuple(("apple", "banana", "cherry")) 
# note the double round-brackets
print(thistuple)

# Access Tuple Items
# Python Access Tuple using a Positive Index
# Tuple items by referring to the index number, inside square brackets
# Print the second item in the tuple
# Using square brackets we can get the values from tuples in Python.
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Range of Indexes
# Specify a range of indexes by specifying where to start and where to end the range.
# Specifying a range, the return value will be a new tuple with the specified items.
# Return the third, fourth, and fifth item
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# By leaving out the start value, the range will start at the first item
# This example returns the items from the beginning to, but NOT included, "kiwi"
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword
# Check if "apple" is present in the tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Traversing Items of Python Tuples
# Like List Traversal, we can traverse through a tuple using for loop.
# Define a tuple
t = (1, 2, 3, 4, 5)
# Traverse through each item in the tuple
for x in t:
    print(x, end=" ")

# Concatenation of Python Tuples
# To Concatenation of Python Tuples, we will use plus operators(+).
# Code for concatenating 2 tuples
t1 = (0, 1, 2, 3)
t2 = ('python', 'geek')
# Concatenating above two
print(t1 + t2)

# Nesting of Python Tuples
# A nested tuple in Python means a tuple inside another tuple.
(0, 1, 2, 3, 'python', 'geek')

# Repetition Python Tuples
# Create a tuple of multiple same elements from a single element in that tuple.
# Code to create a tuple with repetition
t = ('python',)*3
print(t)

# Slicing Tuples in Python
# code to test slicing
t = (0 ,1, 2, 3)
print(t[1:])
print(t[::-1])
print(t[2:4])


# Multiple Data Types With Tuple
# Tuples in Python are heterogeneous in nature. This means tuples support elements with multiple datatypes.
# tuple with different datatypes
t = ("immutable", True, 23)
print(t)

# Converting a List to a Tuple
# Convert a list in Python to a tuple by using the tuple() constructor and passing the list as its parameters.
# Code for converting a list and a string into a tuple
a = [0, 1, 2]
t = tuple(a)
print(t)

# Change Tuple Values
# Convert the tuple into a list to be able to change it
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items
# Convert it into a list, add your item(s), and convert it back into a tuple
# Convert the tuple into a list, add "orange", and convert it back into a tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# Conditions and if statement in python
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or Equals to: a <= b
# Greater than: a > b
# Greater than or Equals to: a >= b
# An "IF STATEMENT" is written by using the "if" keyword

a = 100
b = 350

if a == b:
   print("a is equals to b") # Indentation

# Not Equals: a != b
if a != b:
   print("a is not equals to b")

# Less than: a < b
if a < b:
   print("a is less than b") 

# Less than or Equals to: a <= b
if a <= b:
   print("a is greater than or equals to b")


# Greater than: a > b
if a > b:
   print("a is greater than b")

# Greater than or Equals to: a >= b
if a>= b:
   print("a is greater than or equals to b")

# An "IF STATEMENT" is written by using the "if" keyword
if a == b:
   print("a is equals to b")
# ELIF STATEMENT
elif a < b: # elif ks short for else if
   print("a is less than b")
elif a <= b:
   print("a is less than or equals b")

if a == b:
    print("a is equals to b")  
# ELSE STATEMENT
else:
    print("a is not equals to b")

if a == b:
   print("a is equals to b")

elif a < b:
   print("a is less than b")

elif a <= b:
   print("a is less than or equals to b")

elif a >= b:
   print ("a is greater than or equals to b")

else:
   print("a is not equals to b")

# You can have as many ELIF statement as you want, If and ELSE statement.
# ELSE statement must always comes last in the condition and it is executed only if all other conditions are FALSE

# A python programme that builds a simple apllication that is only for men above 18 years.
# User input in python
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
print(num1 + num2)

# A python programme that builds a simple apllication that is only for men above 18 years.
name = input("Enter your fullname: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

if age >= 18 and gender =="Male":
   print(f"Hi {name}, welcome to my platform")
else: 
   print(f"Sorry {name}, you are not allowed to access this platform")

# Or operator in python 
#If one of the conditions is true then all conditions are true
# AND operator in python
# If one of the condition is false them all conditions are false and the operator is true
# All the conditions must be true