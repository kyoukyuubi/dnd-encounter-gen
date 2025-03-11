import os
import json
import sys

def load_all_creatures(data_dir="data"):
    all_creatures = []
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
            all_creatures.extend(data["Creatures"])
    return all_creatures

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = ""
    creatures = load_all_creatures()
    for creature in creatures:
        if creature["Name"] == name:
            print("Creature found!")
            print("------------------------")
            print(f'Name: {creature["Name"]}')
            print(f'Type: {creature["Type"]}')
            print(f'CR: {creature["ChallengeRating"]}')
            print(f'From the book: {creature["Book"]}')
            print(f'on page: {creature["Page"]}')
            print("------------------------")
            return
    print("No creature found!")
    return

main()