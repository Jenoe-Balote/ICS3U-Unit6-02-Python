#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on: June 2021
# This program determines the largets of 10 numbers

import random


def determine_largest(numbers):
    # This function determines the largest number
    for counter in range(len(numbers)):
        if counter == 0:
            largest = numbers[counter]
        else:
            if numbers[counter] > largest:
                largest = numbers[counter]

    return largest


def main():
    # This function generates the random numbers

    numbers = []

    # Process
    print("Generating numbers...")
    print("")
    for loop_counter in range(1, 10):
        generated_number = random.randint(1, 100)
        print("Random number {0} is: {1}".format(loop_counter,
                                                 generated_number))
        numbers.append(generated_number)

    # Call functions
    number = determine_largest(numbers)

    # Output
    print("\nThe largest number is: {}".format(number))
    print("\nDone.")


if __name__ == "__main__":
    main()