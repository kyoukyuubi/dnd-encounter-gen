import argparse

def parse_arguments():
    # set the program name in argparse and tell it to keep \n for formatting
    parser = argparse.ArgumentParser(prog="D&D Encounter Generator", formatter_class=argparse.RawTextHelpFormatter)

    # set valid valid_environments and valid_planes for the help command
    valid_environments = [
        "Arctic", "Coastal", "Desert", "Forest", "Grassland", "Hill", 
        "Mountain", "Swamp", "Underdark", "Underwater", "Urban"
    ]
    valid_planes = [
        "Feywild", "Shadowfell", "Ethereal Plane", "Air", "Earth", "Fire", "Water", "Upper Planes", "Neutral Planes", "Lower Planes", "Astral Plane"
    ]

    # loops through the valid_environments and makes them each go on a new line and add a dot for a cleaner look
    # do the same thing for plane and difficulty
    env_options = "\n".join(f" • {env}" for env in valid_environments)
    plane_options = "\n".join(f" • {plane}" for plane in valid_planes)

    # the actual help text, with the env_options
    # do the same thing for planes
    env_help = (
        "Environment types (comma-separated).Leave empty for any\n"
        "Valid options:\n"
        f"{env_options}"
    )
    plane_help = (
        "Planes of existence (comma.separated). Leave empty for any\n"
        "Valid options:\n"
        f"{plane_options}"
    )

    # set the arguments, with the name which type and the help text
    # the lamba types allows for multiple arguments
    parser.add_argument('--environment', type=lambda s: s.split(','), help=env_help)
    parser.add_argument('--level', type=int, help='Which level your party is. Default is 1 and max is 20', default=1)
    parser.add_argument('--size', type=int, help="What size your party is, default is 4 and max is 6. Going by Xanathar's Guide to Everything", default=4)
    parser.add_argument('--plane', type=lambda s: s.split(','), help=plane_help)

    # return the args
    return parser.parse_args()