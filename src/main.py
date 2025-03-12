import random
from data_handling import prepare_creatures, calc_creatures
from input_handling import parse_arguments

def main():
    # get the args from argsparse
    args = parse_arguments()

    # run prepare_creatures to sort the loaded list by env, plane and type if set
    creatures = prepare_creatures(args)

    # calculate which creature using challenge rating, size and level
    creatures_sorted = calc_creatures(creatures, args)

    # try to get a random creature, if it fails print the error and return to stop the code from running.
    try:
        random_creature = random.choice(creatures_sorted)
    except IndexError as i:
        print(i)
        return
    except Exception as e:
        print(e)
        return
    
    # print the information about the random creauture that was found
    print("Creature Found!")
    print("----------------------------------------------")
    print(f"Name: {random_creature['Name']}")
    print(f"Type: {random_creature['Type']}")
    print(f"Challenge Rating: {random_creature['ChallengeRating']}")
    print(f"Environment: {random_creature['Environment']}")
    # check if plane is not empty, if it isn't print what plane the creature is on
    if random_creature["Plane"] != []:
        print(f"Plane: {random_creature["Plane"]}")
    # a space for formatting
    print(" ")
    print(f"The creature can be found in: {random_creature["Book"]} on page: {random_creature["Page"]}")
    print("----------------------------------------------")

if __name__ == "__main__":
    main()