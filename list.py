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