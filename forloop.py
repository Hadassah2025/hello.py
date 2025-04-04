cart = [
    {"item": "Book", "Price": 200},
    {"item": "Pen", "Price": 100},
    {"item": "Bag", "Price": 350}
]

total = 0

for product in cart:
    total += product["Price"]

print(f"Total cost: {total:2f}")

votes = ["Yes", "No", "Yes", "Yes", "No", "Yes"]

yes_count = 0
no_count = 0

for vote in votes:
    if vote == "Yes":
        yes_count += 1
    elif vote == "No":
        no_count += 1

print(f"Yes votes: {yes_count}")
print(f"No votes: {no_count}")

students_score = { 
    "Alice": 89,
    "James": 75,
    "Bolaji": 59,
    "Dorcas": 90,
    "Bola": 65,
    "Kola": 70,
    "Kunle": 45,
    "Kelvin": 95,
    "Adeola": 89
}

for name, score in students_score.items():
    status = "Passed" if score >= 70 else "Failed"
    print(f"{name}: {score} - {status}")

    workers = ["Ade", "Tolu", "Thomas", "Kenny", "Precious"]

    for worker in workers:
        print(f"Good day {worker}, \nThis is to remind you of our meeting scheduled for 10am  tomorrow. \nThank You")


books_title =["a good day", "enemy within", "god's goodness", "mercy throne", "the new creation"]

for title in books_title:
    print(title.title())
