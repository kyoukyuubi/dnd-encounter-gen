import random
from data_handling import prepare_creatures, calc_creatures
from input_handling import parse_arguments

def main():
    args = parse_arguments()

    creatures = prepare_creatures(args)
    creatures_sorted = calc_creatures(creatures, args)
    random_creature = random.choice(creatures_sorted)
    print("Creature Found!")
    print("----------------------------------------------")
    print(f"Name: {random_creature['Name']}")
    print(f"Type: {random_creature['Type']}")
    print(f"Challenge Rating: {random_creature['ChallengeRating']}")
    print(f"Environment: {random_creature['Environment']}")
    # check if plane is not empty, if it isn't print what plane the creature is on
    if random_creature["Plane"] is not None:
        print(f"Plane: {random_creature["Plane"]}")
    # a space for formatting
    print(" ")
    print(f"The creature can be found in: {random_creature["Book"]} on page: {random_creature["Page"]}")
    print("----------------------------------------------")

if __name__ == "__main__":
    main()