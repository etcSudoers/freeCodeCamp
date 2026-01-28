"""
FizzBuzz Mini

Given an integer, return a string based on the following rules:

    If the number is divisible by 3, return "Fizz".
    If the number is divisible by 5, return "Buzz".
    If the number is divisible by both 3 and 5, return "FizzBuzz".
    Otherwise, return the given number as a string.

"""


def fizz_buzz_mini(n: int):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)


assert fizz_buzz_mini(3) == "Fizz"
assert fizz_buzz_mini(4) == "4"
assert fizz_buzz_mini(35) == "Buzz"
assert fizz_buzz_mini(75) == "FizzBuzz"
assert fizz_buzz_mini(98) == "98"
