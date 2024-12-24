# Define the function to sum two numbers
def sum_two_numbers(a, b):
    return a + b

# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calculate the sum
result = sum_two_numbers(num1, num2)

# Print the result
print("The sum of {} and {} is: {}".format(num1, num2, result))
