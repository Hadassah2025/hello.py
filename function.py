def hello_world():
    print("Hello World")

hello_world()

def multiplier(num1, num2):
    result = num1 * num2
    return result

res = multiplier(8, 19)
print(res)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = multiplier(num1, num2)
print(result)

def guess_game():
    secret = 8
    guess = int(input("Guess the number: "))
    while guess != secret:
        print("Wrong! Try again.")
        guess = int(input("Guess the number: "))
    else:
        return "You guessed right"
print(guess_game())

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    print(result)
    