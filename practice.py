# keyword argument = an argument preceded by an identifier
#                    it helps with readability
#                    it order of argument doesn't matter
# basic style of argument 1. positional 2. default 3. keyword 4. arbitriary
# Keyword

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="Spongebob", first="Squarepants")

# generate a phone number
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=0, area=802, first=313, last=2854)

print(phone_num)

# Write a program to create a function that takes two arguments, name and age, and print their value.
def info(name, age):
    print(name, age)
info("Bola", 25)

# Find the largest item from a given list
x = [4, 6, 8, 24, 12, 2]

print(max(x))

# function that accepts two numbers as arguments and returns the sum
def numbers(x,y):
    sum = x+y
    return sum
output = numbers(54,14)
print(output)

# An argument is a value that is passed to a function when it is called. 
# It might be a variable, value or object passed to a function or method as input.

def sum(x, y):
    print(x+y)

sum(4, 8)
