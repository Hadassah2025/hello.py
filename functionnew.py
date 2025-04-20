def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Denominator cannot be 0"
        return num1 / num2
    else:
        return "Invalid operation!"    

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the secon number: "))
operation = input("Enter the operation: ")

print(calculator(num1, num2, operation))

def max_of_two(x,y):
    if x > y:
        return x
    return y

def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))

max_of_three(2,5,1)
