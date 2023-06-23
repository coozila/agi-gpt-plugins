import json
import re

def extract_object_parameters(text):
    object_parameters = {}

    # Extract object parameters from the given text
    # Add the extracted object parameters to the object_parameters dictionary

    # Example logic using regular expressions:
    matches = re.findall(r'\b[a-zA-Z]+\b', text)
    for match in matches:
        if match not in object_parameters:
            object_parameters[match] = {"object": True, "definitions": [match]}
        else:
            if match not in object_parameters[match]["definitions"]:
                object_parameters[match]["definitions"].append(match)

    return object_parameters

def save_object_parameters(object_params):
    with open("object_parameters.json", "w") as file:
        json.dump(object_params, file, indent=4)

# Example usage
project_description = "This project involves building a house and installing a new computer. The house will have multiple rooms and a garden. The building will also include a factory."
parameters = extract_object_parameters(project_description)
save_object_parameters(parameters)
