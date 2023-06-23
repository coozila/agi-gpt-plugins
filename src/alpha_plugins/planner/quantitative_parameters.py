import json
import re

def extract_parameters_from_context_and_input(context, input_text):
    quantitative_parameters = {}

    # Extract natural numbers from the context
    context_numbers = re.findall(r'\b\d+\b', context)

    # Extract natural numbers from the input
    input_numbers = re.findall(r'\b\d+\b', input_text)

    # Combine the numbers from both the context and input
    numbers = context_numbers + input_numbers

    # Add your logic here to extract relevant quantitative numbers from the context and input

    for number in numbers:
        if number not in quantitative_parameters:
            quantitative_parameters[number] = get_number_textual_representations(int(number))

    # Save the dictionary of quantitative parameters to the JSON file
    with open("quantitative_parameters.json", "w") as file:
        json.dump(quantitative_parameters, file, indent=4)

def get_number_textual_representations(number):
    # Add your logic here to generate the textual representations for a given number
    # Return a list of textual representations for the number

    # Example logic:
    if number == 1:
        return ["unu", "una", "doar unul"]
    elif number == 2:
        return ["doi", "două"]
    elif number == 3:
        return ["trei"]
    else:
        return [str(number)]
