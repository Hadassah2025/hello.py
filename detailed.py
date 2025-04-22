first_name = "Bro" 
print(first_name)

first_name ="Bro"
print(f"Hello {first_name}")

first_name = "Bro"
food = "pizza"
print(f"Hello {first_name}")
print(f"You like {food}")

first_name = "Bro"
food = "pizza"
email = "ask4lari@yahoo.com"

print(f"Hello {first_name}")
print(f"You like {food}")
print(f"email is: {email}")

#Integers  is the whole number, including negative numbers but not fractions.
age = 25
quantity = 3
num_of_students = 30
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")

#float ) is a data type used to represent real numbers with a fractional compone
price =10.99
gpa = 3.2
distance = 5.5
print(f"The price is N{price}")
print(f"Your gpa is: {3.2}")
print(f"You ran {4.5}km")

#boolean (its either true or false)
is_student = False
print(f"Are you a student?: {is_student}")

if is_student:
    print("You are a student")
else:
    print("You are NOT a student")

is_student = False
for_sale = False

if for_sale:
    print("That item is for sale")
else:
    print("That item is NOT available")

is_online = False
if is_online:
    print("You are online")
else:
    print("You are offline")

# Typecasting = the process of converting a variable from one data type to another

name = "Hadassah"
age = 43
gpa = 4.5




age = float(age)
print(age)

age = str(age)
print(type(age))

name = bool(name)
print(name)

# input() = A function that prompts the user data
#           Returns the entered data as a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))

age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc
length = float(input("Enter the length: "))
width = float(input("Enter the length: "))
area = length * width

print(area)