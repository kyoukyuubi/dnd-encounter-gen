import argparse

def parse_arguments():
    # set the program name in argparse and tell it to keep \n for formatting
    parser = argparse.ArgumentParser(prog="D&D Encounter Generator", formatter_class=argparse.RawTextHelpFormatter)

    # set valid options for the help menu to print.
    # For creature Environments/Habitats
    valid_environments = [
        "Arctic", "Coastal", "Desert", "Forest", "Grassland", "Hill", 
        "Mountain", "Swamp", "Underdark", "Underwater", "Urban"
    ]

    # For Planes of existence
    valid_planes = [
        "Feywild", "Shadowfell", "Ethereal Plane", "Air", "Earth", "Fire", "Water", "Upper Planes", "Neutral Planes", "Lower Planes", "Astral Plane"
    ]

    # For Creature Types
    valid_types = [
        "Aberration", "Beast", "Celestial", "Construct", "Dragon", "Elemental", "Fey", "Fiend", "Giant", "Humanoid", "Monstrosity", "Ooze", "Plant", "Undead"
    ]

    # For Difficulties
    valid_difficulties = [
        "Low", "Moderate", "High"
    ]

    # loops through the valid options and makes them each go on a new line and add a dot for a cleaner look
    env_options = "\n".join(f" • {env}" for env in valid_environments)
    plane_options = "\n".join(f" • {plane}" for plane in valid_planes)
    type_options = "\n".join(f" • {type}" for type in valid_types)
    difficulties_options = "\n".join(f" • {diffi}" for diffi in valid_difficulties)

    # Format how the help for Environments looks
    env_help = (
        "The Environment type(s) you wish to look for creatures in. (comma-separated). Leave empty for any\n"
        "Valid options:\n"
        f"{env_options}"
    )

    # Format how the help for Plane looks
    plane_help = (
        "The Planes of existence(s), you wish to look for creatures in. (comma.separated). Leave empty for any\n"
        "Valid options:\n"
        f"{plane_options}"
    )

    # Format how the help for Type looks
    type_help = (
        "Which type(s) of creature you are looking for. (comma.separated) Leave empty for any\n"
        "Valid options:\n"
        f"{type_options}"
    )

    # Format how the help for difficulty looks
    difficulty_help = (
        "The difficulty you want to be the encounter in. Default is Moderate\n"
        "Valid options:\n"
        f"{difficulties_options}"
    )

    # checks for negative numbers, which is not allowed
    def non_negative_int(value):
        ivalue = int(value)
        if ivalue < 0:
            raise argparse.ArgumentTypeError("Value cannot be negative")
        return ivalue

    # checks if the value is between 1 and 20
    def level_range(value):
        ivalue = int(value)
        if ivalue < 1 or ivalue > 20:
           raise argparse.ArgumentTypeError("Level must be between 1 and 20")
        return ivalue

    # set the arguments, with the name which type and the help text
    # the lamba types allows for multiple arguments
    parser.add_argument('--environment', type=lambda s: s.split(','), help=env_help)
    parser.add_argument('--level', type=level_range, help='The level of your party. Default is 1 and max is 20', default=1)
    parser.add_argument('--size', type=non_negative_int, help="The size of the party to wish to generate an encounter for. Default is 4", default=4)
    parser.add_argument('--plane', type=lambda s: s.split(','), help=plane_help)
    parser.add_argument('--type', type=lambda s: s.split(','), help=type_help)
    parser.add_argument('--difficulty', type=str, help=difficulty_help, default="Moderate")
    parser.add_argument('--min_exp', type=non_negative_int, help="The minimun exp to look for when generating the list of creatures. Leave blank for no limit",)
    parser.add_argument('--max_creatures', type=non_negative_int, help='Max amount of creatures in encounter. Leave blank for not limit')

    # return the args
    return parser.parse_args()