import os
import json

# load all the json files inside the data folder.
def load_all_creatures(data_dir="data"):
    all_creatures = []
    for filename in os.listdir(data_dir):
        # take the folder and combine it with the file name
        filepath = os.path.join(data_dir, filename)
        # use the combined name and open the file
        with open(filepath, 'r') as file:
            # store the file contents in data and extend it to all_creatures
            data = json.load(file)
            all_creatures.extend(data["Creatures"])
    if len(all_creatures) <= 0:
        raise Exception("No file found!")
    return all_creatures

def does_element_match(array_a, array_b):
    # Capitilize the input to make it match with the json data correctly
    array_b = [b.capitalize() for b in array_b]

    # Return True if b is found in array_a
    return any(b in array_a for b in array_b)

def prepare_creatures(args):
    # Try to load all the creatures, print the error and return if it fails
    try:
        creatures = load_all_creatures()
    except Exception as e:
        print(e)
        return[]
    
    # If no filters provided, return all creatures
    if all(getattr(args, attr) is None for attr in ['environment', 'plane', 'type']):
        return creatures

    # Filter creatures based on provided criteria
    filtered_creatures = []

    for creature in creatures:
        # Start with the assumption that this creature matches
        matches = True

        # Check environment if specified
        if args.environment is not None:
            if not does_element_match(creature["Environment"], args.environment):
                matches = False
                continue # Skip to next creature

        # Check plane if specified
        if args.plane is not None:
            if not does_element_match(creature["Plane"], args.plane):
                matches = False
                continue # Skip to next creature

        # Check type if specified
        if args.type is not None:
             if creature["Type"] != args.type.capitalize():
                matches = False
                continue # Skip to the next creature
             
        # Check if the exp is specified
        if args.min_exp is not None:
            if not creature['Exp'] >= args.min_exp:
                matches = False
                continue # Skip to the next creature

        # If all checks passed, add to filtered list
        if matches:
            filtered_creatures.append(creature)

    # Return the list
    return filtered_creatures

def calc_creatures(creatures, args):
    # set the dictionary that stores the difficulty and the base exp based on character level.
    pass