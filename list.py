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