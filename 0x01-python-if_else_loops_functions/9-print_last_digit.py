#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(number):
    """Print the last digit of a number and return it."""
    if number >= 0:
        last_digit = number % 10
    else:
        last_digit = number % -10
        last_digit *= -1

    print("{:d}".format(last_digit), end='')
    return (last_digit)
