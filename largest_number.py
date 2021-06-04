#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on June 2021
# This program finds the largest of 10 random numbers

import random


def main():
    # this function determines the largest number

    numbers = []

    # process and output
    print("Generating numbers...")
    print("")
    for loop_counter in range(0, 10):
        number_created = random.randint(1, 100)
        numbers.append(number_created)
    largest = 0
    for loop_counter in range(len(numbers)):
        print("Number {0} is {1}.".format(
            loop_counter + 1, numbers[loop_counter]))
        if loop_counter == 0:
            largest = numbers[loop_counter]
        else:
            if numbers[loop_counter] > largest:
                largest = numbers[loop_counter]
    print("\nThe largest number is: {}.".format(largest))
    print("\nDone.")


if __name__ == "__main__":
    main()
