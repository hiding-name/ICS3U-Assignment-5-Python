#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Nov 2019
# This is program randomly throws dice and says if it gets doubles

import random


def main():
    # This is randomly throws die until it gets doubles

    # repeater to know number of times it looped
    repeater = 0

    # Welcomes user
    print("Hi, this is DICE ROLLER.")
    input("Press Enter to continue.\n")

    # This will generate numbers until they are equal to each other
    while True:
        # This randomly generates two numbers from 1 to 6, a die
        die_0 = random.randint(1, 6)
        die_1 = random.randint(1, 6)

        # prints the two throws
        print("Roll " + str(repeater) + ": " + str(die_0) + ", " + str(die_1))
        repeater = repeater + 1

        # checks if numbers generated are equal to each other
        if die_0 == die_1:
            # output
            print("\nIt took " + str(repeater) + " roll(s) to get doubles.")
            break


if __name__ == "__main__":
    main()
