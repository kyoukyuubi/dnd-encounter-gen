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