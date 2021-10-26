# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/26/2021
# This is the 2D Average program
# The program asks the user how many rows and cloumns they want
# The program generates random numbers between 1-50 to fill the rows/columns
# The program then figures out and displays the average of all the numbers

import random


def sum_of_numbers(passed_in_2D_list):
    # this function adds up all the elements in a 2D array

    total = 0
    for row_value in passed_in_2D_list:
        for single_element in row_value:
            total += single_element

    return total


def main():
    # this function uses a 2D array

    a_2d_list = []

    # input
    rows = int(input("How many rows would you like: "))
    columns = int(input("How many columns would you like: "))
    print("")

    for loop_counter_rows in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 50)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_list.append(temp_column)
        print("")

    divide = rows * columns

    average = sum_of_numbers(a_2d_list) / divide

    print("\nThe average of all the numbers is: {0} ".format(average))

    print("\nDone")


if __name__ == "__main__":
    main()
