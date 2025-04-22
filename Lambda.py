# Lambda functions in python
var = "Random" 
another = lambda first_name, last_name: f"{first_name.upper()} {last_name.upper()}"

print(another("andrew", "johnson"))

# Check if a number is Positive, Negative or Zero using Lambda function
number = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(number(10))
print(number(0))
print(number(-10))
