from data_handling import prepare_creatures
from input_handling import parse_arguments

def main():
    args = parse_arguments()

    creatues = prepare_creatures(args)
    for create in creatues:
        print(create['Name'])

if __name__ == "__main__":
    main()