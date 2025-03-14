from encounter_builder import generate_encounter, display_encounter
from input_handling import parse_arguments

def main():
    args = parse_arguments()
    encounter = generate_encounter(args, seed=45)
    print(encounter)
    # display_encounter(encounter)

if __name__ == "__main__":
    main()