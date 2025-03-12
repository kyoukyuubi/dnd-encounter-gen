import sys

from data_handling import load_all_creatures
from input_handling import parse_arguments

def main():
    args = parse_arguments()

    environment = args.environment
    level = args.level 

    print(f"Generating encounter for a level {level} party in a {environment} environment")

if __name__ == "__main__":
    main()