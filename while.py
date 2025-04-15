initial_value = 1
while initial_value <= 10:
    print(f"Initial value: {initial_value}")
    initial_value += 1

piggy_bank_balance = 100
while piggy_bank_balance > 0:
    piggy_bank_balance -= 10
    print(f"Remaining Balance: {piggy_bank_balance}")
print("You have spent all your saved money")

secret = 9
guess = int(input("Guess the secret number: "))
while guess != secret:
    print("Wrong!, Try again.")
    guess = int(input("Guess the secret number: "))    
else:   
    print("You guessed right")


correct_password = "Python123"
user_input = ""

while user_input != correct_password:
    user_input = input("Enter Password: ")
    if user_input != correct_password:
        print("Incorrect password! Try again.")
else:
    print("Password accepted")