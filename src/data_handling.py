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
    for b in array_b:
        b = b.capitalize()
        if b in array_a:
            return True
    return False

def prepare_creatures(args):
    # prepare the creatures and the return list
    creatures = []
    creatures_sorted = []

    # set the arg values
    environment = args.environment
    plane = args.plane

    # try to load all the creatures, print the error and return if it fails
    try:
        creatures = load_all_creatures()
    except Exception as e:
        print(e)
        return
    
    # loop through the loaded creatures
    for creature in creatures:
        # check the creatures if environment has an element that matches and add the creature to the list
        if environment is not None and plane is None:
            if does_element_match(creature["Environment"], environment):
                creatures_sorted.append(creature)
        # check the creatures if plane has an element that matches and add the creature to the list
        elif plane is not None and environment is None:
            if does_element_match(creature["Plane"], plane):
                creatures_sorted.append(creature)
        # check the creatures if environment and plane has an element that matches and add the creature to the list
        else:
            if does_element_match(creature["Environment"], environment) and does_element_match(creature["Plane"], plane):
                creatures_sorted.append(creature)

    # return the list
    return creatures_sorted