import random
from data_handling import prepare_creatures


# Generate the encounter, only taking in the args and having seed as optional
# I am avoiding inputting the creatures to have encapsulation, to make the use of this function easier
def generate_encounter(args, seed=None):

    # sets the seed for the random gen if it is not None.
    # it is used for debugging purposes
    if seed is not None:
        random.seed(seed)

    # Base experience point budgets by encounter difficulty and character level
    # These values come from the D&D 2024 encounter building rules. From the Dungeons Masters Guide 2024
    # The final budget is calculated by multiplying the base value by the number of players
    base_exp = {
        "Low": {
            1: 50,
            2: 100,
            3: 150,
            4: 250,
            5: 500,
            6: 600,
            7: 750,
            8: 1000,
            9: 1300,
            10: 1600,
            11: 1900,
            12: 2200,
            13: 2600,
            14: 2900,
            15: 3300,
            16: 3800,
            17: 4500,
            18: 5000,
            19: 5500,
            20: 6400
        },
        "Moderate": {
            1: 75,
            2: 150,
            3: 225,
            4: 375,
            5: 750,
            6: 1000,
            7: 1300,
            8: 1700,
            9: 2000,
            10: 2300,
            11: 2900,
            12: 3700,
            13: 4200,
            14: 4900,
            15: 5400,
            16: 6100,
            17: 7200,
            18: 8700,
            19: 10700,
            20: 13200
        },
        "High": {
            1: 100,
            2: 200,
            3: 400,
            4: 500,
            5: 1100,
            6: 1400,
            7: 1700,
            8: 2100,
            9: 2600,
            10: 3100,
            11: 4100,
            12: 4700,
            13: 5400,
            14: 6200,
            15: 7800,
            16: 9800,
            17: 11700,
            18: 14200,
            19: 17200,
            20: 22000
        }
    }

    # Calculate the exp budget depending the the player level, party size and difficulty
    budget = base_exp[args.difficulty.capitalize()][args.level] * args.size

    # copy the budget data into remaing_budget to avoid mutating
    remaining_budget = budget

    # Get the list of creatures using the selected args
    # If an error happens while loading the creatures, return an empty list for future error handling
    try:
        creatures = prepare_creatures(args)
    except Exception as e:
        print(e)
        return {}

    # make an empty dictionary where the encouter will be stored
    encounter = {}

    # Keep adding creatures until we can't afford more
    while True:
        # Find creatures we can still afford
        affordable_creatures = [c for c in creatures if c['Exp'] <= remaining_budget]

        # Stop if we can't afford any more creatures
        if not affordable_creatures:
            break

        # Calculate total creatures in the encounter so far
        total_creatures = sum(details["Amount"] for details in encounter.values())
    
        # Stop if we've reached the maximum creatures allowed
        if args.max_creatures is not None and total_creatures >= args.max_creatures:
            break

        # Get a random creature from the affordable ones
        random_creature = random.choice(affordable_creatures)

        # subtract from the budget
        remaining_budget -= random_creature['Exp']

        # check if the dictionary is empty and add the creature if it is
        if not encounter or random_creature['Name'] not in encounter:

            # adds all we need from the json file and add the amount field to keep track of how many is added
            encounter[random_creature["Name"]] = {
                "Type": random_creature["Type"],
                "ChallengeRating": random_creature["ChallengeRating"],
                "Environment": random_creature["Environment"],
                "Plane": random_creature["Plane"],
                "Book": random_creature["Book"],
                "Page": random_creature["Page"],
                "Amount": 1
            }
        else:
            encounter[random_creature["Name"]]["Amount"] += 1

        # Stop if remaining budget is too small to be useful
        if remaining_budget < min(c['Exp'] for c in creatures):
            # Can't afford any more creatures
            break
    
    return encounter

# display the encounter data that has been made using the generate_encounter
# also handles things like en empty list
def display_encounter(encounter):
    # if encounter is empty, tell the user that an error has happened, and what might be the cause and return from the function
    if not encounter:
        print("No encounter was generated. Likely because no creatures where found")
        print("Please ensure spelling and correct inputs. You can use --h or --help to see a list of inputs allowed")
        print("note that for environment, plane, type and difficulty, capitalization doesn't matter")
        return
    
    
    print("Encounter Generated!")
    print("------------------------------")

    # print the encounter with the desired formatting and information
    for key in encounter.keys():
        print(f"Name: {key}")
        print(f"Amount: {encounter[key]['Amount']}")
        print(f"Challenge Rating: {encounter[key]['ChallengeRating']}")
        if encounter[key]['Environment'] != []:
            print(f"Environment: {', '.join(encounter[key]['Environment'])}")
        if encounter[key]['Plane'] != []:
            print(f"Plane: {', '.join(encounter[key]['Plane'])}")
        print(" ")
        print(f"The creature can be found in: {encounter[key]['Book']} on page: {encounter[key]['Page']}")
        print("------------------------------")

    # return from the function
    return