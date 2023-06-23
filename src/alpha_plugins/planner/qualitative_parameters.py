import json

def extract_parameters_from_context(context, user_input):
    qualitative_adjectives = ["qualitative adj1", "qualitative adj2", "qualitative adj3"]
    qualitative_parameters = []

    # Add your logic here to extract relevant qualitative adjectives from the context or user input

    # Extract qualitative adjectives from context
    # ...

    # Extract qualitative adjectives from user input
    # ...

    for adj in qualitative_adjectives:
        parameter = {
            "adjective": adj,
            "calitative": adj
        }
        qualitative_parameters.append(parameter)

    # Check for duplicates
    unique_qualitative_parameters = []
    for parameter in qualitative_parameters:
        if parameter not in unique_qualitative_parameters:
            unique_qualitative_parameters.append(parameter)

    # Save the list of unique qualitative parameters to the JSON file
    with open("qualitative_parameters.json", "w") as file:
        json.dump(unique_qualitative_parameters, file, indent=4)
