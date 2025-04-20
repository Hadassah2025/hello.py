# Filter out even numbers from a list of number
def filter_even_numbers(numbers):
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
    return even

def find_prime_numbers(limit):
    primes = []
    for number in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
            if is_prime:
                primes.append(number)
    return primes

print(find_prime_numbers(20))


def count_vowels(string):
    vowels = "aeiou"
    count = 0
    for text in string.lower():
        if text in vowels:
            count += 1
    return count
    
print(count_vowels("Hadassah"))

def shopping_summary(prices: list):
    total_price = sum(prices)
    number_of_items = len(prices)

    return {"Total price": total_price, "Number of items": number_of_items}

print(shopping_summary([200, 53, 1000, 700, 980]))