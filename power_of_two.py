#!/usr/bin/env python3

# Made by Jaydin Madore
# Made on 2022-11-09
# This program tells the user the squared of the positive integer number they
# inputted and all the number the positive integer that come before it.


import math


def main():

    try:
        user_number = int(input("Enter a positive integer number:"))
        print()

    # Tells the user to restart if they did not enter a number
    except ValueError:
        print("You need to enter a positive integer.")
        main()
    if user_number < 0:
        print("You need to enter a positive integer.")
        main()
    # Loops through code until counter is equal to user_number
    for counter in range(1, user_number + 1, 1):
        print(f"Looped through {counter} times.")
        squared = math.pow(counter, 2)
        print(f"{counter}^2 = {squared}")


if __name__ == "__main__":
    main()
