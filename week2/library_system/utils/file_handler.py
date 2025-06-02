import json

def load_data(filepath):
    # Loads JSON data from a file.
    with open(filepath, 'r') as file:
        return json.load(file)

def save_data(filepath, data):
    # Saves data (list/dict) to a JSON file.
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)