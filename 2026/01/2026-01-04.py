'''
Leap Year Calculator

Given an integer year, determine whether it is a leap year.

A year is a leap year if it satisfies the following rules:

    The year is evenly divisible by 4, and
    The year is not evenly divisible by 100, unless
    The year is evenly divisible by 400.

'''
def is_leap_year(year:int):
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True

    return False

            


assert is_leap_year(2024) == True
assert is_leap_year(2023) == False
assert is_leap_year(2100) == False
assert is_leap_year(2000) == True
assert is_leap_year(1999) == False
assert is_leap_year(2040) == True
assert is_leap_year(2026) == False