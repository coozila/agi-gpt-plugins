import json
import re

def extract_fibonacci_parameters_from_context_and_input(context, input_text):
    fibonacci_parameters = {}

    # Extract Fibonacci numbers from the context
    context_fibonacci_numbers = extract_fibonacci_numbers(context)

    # Extract Fibonacci numbers from the input
    input_fibonacci_numbers = extract_fibonacci_numbers(input_text)

    # Combine the Fibonacci numbers from both the context and input
    fibonacci_numbers = context_fibonacci_numbers + input_fibonacci_numbers

    # Add the Fibonacci numbers to the dictionary
    for number in fibonacci_numbers:
        if number not in fibonacci_parameters:
            fibonacci_parameters[number] = get_fibonacci_textual_representation(number)

    # Save the dictionary of Fibonacci parameters to the JSON file
    with open("fibonacci_quantitative_parameters.json", "w") as file:
        json.dump(fibonacci_parameters, file, indent=4)

def extract_fibonacci_numbers(text):
    # Extract Fibonacci numbers from the given text using regular expressions or any other method
    # Return a list of Fibonacci numbers

    # Example logic using regular expressions:
    fibonacci_numbers = []
    matches = re.findall(r'\b[0-9]+\b', text)
    for match in matches:
        number = int(match)
        if is_fibonacci(number):
            fibonacci_numbers.append(number)
    
    return fibonacci_numbers

def is_fibonacci(number):
    # Check if the given number is a Fibonacci number
    # Return True if it is, False otherwise

    # Example logic to check if a number is Fibonacci:
    sqrt5 = 5 ** 0.5
    phi = (1 + sqrt5) / 2
    n1 = number * number * 5
    if is_perfect_square(n1 + 4) or is_perfect_square(n1 - 4):
        return True
    return False

def is_perfect_square(number):
    # Check if the given number is a perfect square
    # Return True if it is, False otherwise

    # Example logic to check if a number is a perfect square:
    square_root = int(number ** 0.5)
    return square_root * square_root == number

def get_fibonacci_textual_representation(number):
    # Generate the textual representation for the Fibonacci number
    # Return a string representing the number

    # Example logic to generate textual representation for Fibonacci numbers:
    return str(number)

