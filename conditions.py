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