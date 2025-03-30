# LIsts in Python
fruits = ["Mango", "Banana", "Pineapple", "Orange", "Apple"]
print(fruits)

# LIsts in Python
another = ["Blackberry", "Coconut"]

# List methods
# Adding item to list
# 1. Adding item to the end of the list
fruits.append("Strawberry")

# 2. Adding item to a specific position (index)
fruits.insert(2, "Kiwi")
print(fruits)

# 3. Adding multiple items to the end of a list
fruits.extend(another)
print(fruits)

# List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7,9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)

# Different Data Type
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# Data type of a list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# List() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Access items
# print second item on the list
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
# Negative indexing means start from the end
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#Range of indexes
# Return the third, fourth, and fifth item
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Range of Negative Indexes
# Negative indexing means starting from the end of the list.
# Return the item from "orange" (-4) to, but NOT including "mango" (-1)
# Remember that the last items has index -1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if Item Exists
# Check if "apple" ispresent in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

  # Change item value of a specific item
  # Change second item
  thislist = ["apple", "banana", "cherry"]
  thislist[1] = "blackcurrant"
  print(thislist)

 # Change a Range of Item Values
 # Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Remove Specified Item
# The remove() method removes the specified item.
# Remove "banana"
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the first occurrence of "banana"
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
# Remove the second item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# If you do not specify the index, the pop() method removes the last item.
# Remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index
# Remove the first item
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
# Delete the entire list
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
# Clear the list content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Loop through a list
# Print all items in the list, one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  # Loop through the index numbers
  # Loop through the list items by referring to their number
  # Use the range() and lens()functions to create a suitable iterable
  # Print all items by referring to their index number
  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

  # Using a while loop 
  # Use the len()function to determine the length of the list
  # Increase index by 1 after each iteration.
  thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  # Looping using list comprehension
  # List Comprehension offers the shortest syntax for looping through lists:
  # A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# Tuples in python
mytuple = ("Apple", "Banana", "Orange")
mylist =list(mytuple)
mylist.append("Mango")
mytuple = tuple(mylist)
print(mytuple)

myset = {"Apple", "Banana", "Orange", "Mango", "Orange"}
print(myset)

myset = {"Apple", "Banana", "Orange", "Banana", "Mango", "Orange"}
print(myset)

myset = {"Banana", "Apple", "Orange", "Banana", "Mango"}
print(myset)
# Adding items to a set
myset.add("Pineapple")
print(myset)
another_set = {"Grape", "Guava", "Kiwi"}
myset.update(another_set)
print(myset)
myset.update(["pomegranate", "Papaya"])
print(myset)
# Removing items from a set
myset.remove("Guava")
print(myset)
myset.discard("Pineapple")
print(myset)
myset.pop()
print(myset)

#Dictionaries in python
person = {
  "name": "Adeola James",
  "age": 36,
  "gender": "Male",
  "fav_colours": ["Red", "Blue", "White"]
  }
print(person)
print(person["age"])

#dict() constructor in python
another_person = dict(
  name="Adeola James",
  age=36,
  gender="Male",
  fav_colours=["Red", "Blue", "White"]
          )

print(person)

#Accessing items in a dictionary
print(person["name"])
name = person.get("name")
print(name)
keys = person.keys()
print(keys)
values =person.values()
print(values)
items = person.items()
print(items)


# Changing items in dictionary
person["age"] = 45
print(person)

person["age"] = 45

person.update({"gender": "Female"})
print(person)

# Removing items in dictionary
person.pop("fav_colours")
print(person)
person.popitem()
print(person)

# Sort List Alphanumerically
# List objects that have a sort() method that will sort the list alphanumerically, ascending, by default
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort Descending
# To sort descending, use the keyword argument reverse = True
# Sort the list descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Sort the list descending
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Customize Sort Function
# Customize your own function by using the keyword argument key = function
# The function will return a number that will be used to sort the list (the lowest number first)
# Sort the list based on how close the number is to 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
# Case sensitive sorting can give an unexpected result
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# For a case-insensitive sort function, use str.lower as a key function
# Perform a case-insensitive sort of the list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
# Reverse the order of the list items
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Copy a List
# Use the copy() method
# You can use the built-in List method copy() to copy a list.
# Make a copy of a list with the copy() method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Use the list() method
# Another way to make a copy is to use the built-in method list().
# Make a copy of a list with the list() method.
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.
# Make a copy of a list with the : operator
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# Join Two Lists
# Ways to join, or concatenate, two or more lists in Python.
# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Another way to join two lists is by appending all the items from list2 into list1, one by one
# Append list2 into list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Or you can use the extend() method, where the purpose is to add elements from one list to another list
# Use the extend() method to add list2 at the end of list1
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)