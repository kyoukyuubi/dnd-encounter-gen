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

        # If all checks passed, add to filtered list
        if matches:
            filtered_creatures.append(creature)

    # Return the list
    return filtered_creatures

def calc_creatures(creatures, args):
    # set the dict that stores the challenge rating for set level and party size
    solo_creature = {
        4: {
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 7,
            6: 8,
            7: 9,
            8: 10,
            9: 11,
            10: 12,
            11: 13,
            12: 15,
            13: 16,
            14: 17,
            15: 18,
            16: 19,
            17: 20,
            18: 20,
            19: 21,
            20: 23,
        },
        5: {
            1: 2,
            2: 3,
            3: 4,
            4: 5,
            5: 8,
            6: 9,
            7: 10,
            8: 11,
            9: 12,
            10: 13,
            11: 14,
            12: 16,
            13: 17,
            14: 18,
            15: 19,
            16: 20,
            17: 21,
            18: 21,
            19: 22,
            20: 23,
        },
        6:{
            1: 2,
            2: 4,
            3: 5,
            4: 6,
            5: 9,
            6: 10,
            7: 11,
            8: 12,
            9: 13,
            10: 14,
            11: 15,
            12: 17,
            13: 18,
            14: 19,
            15: 20,
            16: 21,
            17: 22,
            18: 22,
            19: 23,
            20: 24,
        },
    }

    # prepare the result list
    result_creatures = []

    # set the arg values for level and size
    level = args.level
    size = args.size

    # check if level is within the allowed range of 1-20
    if level < 1 or level > 20:
        raise Exception(f"The allowed level is between 1 and 20. A level of {level} is not allowed")
    
    # check if the group size is between the allowed range on 4-6
    if size < 4 or size > 6:
        raise Exception(f"The allowed size is between 4 and 6. A size of {size} is not allowed")
    
    # get the correct challenge level
    challenge_rating = str(solo_creature[size][level])
    
    # loop through the creatures list and append the ones with a matching challenge rating to result_creatures
    for creature in creatures:
        if creature["ChallengeRating"] == challenge_rating:
            result_creatures.append(creature)

    # return the list
    return result_creatures