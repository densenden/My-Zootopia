import json

animals_data = load_data('animals_data.json')

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name' from a JSON file.

    Args:
        animal_name (str): The name of the animal to fetch data for.

    Returns:
        list: A list of dictionaries containing animal data.
    """
    with open(animals_data, 'r') as file:
        data = json.load(file)
        return [animal for animal in data if animal_name.lower() in animal['name'].lower()]