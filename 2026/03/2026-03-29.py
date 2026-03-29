"""
ISBN-10 Validator

Given a string, determine if it's a valid ISBN-10

An ISBN-10 consists of hyphens ("-") and 10 other characters. After removing the hyphens ("-"):

    The first 9 characters must be digits, and
    The final character may be a digit or the letter "X", which represents the number 10

To validate it:

    Multiply each digit (or value) by its position (multiply the first digit by 1, the second by 2, and so on)
    Add all the results together
    If the total is divisible by 11, it's valid

"""


def is_valid_isbn10(s: str):
    # Remove hyphens
    s = s.replace("-", "")

    # Check if first 9 characters are digits
    if not s[:9].isdigit():
        return False

    # Check if final character is a digit or X
    if not s[-1].isdigit() and s[-1] != "X":
        return False

    # Calculate total
    total = 0
    for i, c in enumerate(s[:9]):
        total += int(c) * (10 - i)
    if s[-1] == "X":
        total += 10
    else:
        total += int(s[-1])

    # Check if total is divisible by 11
    if total % 11 == 0:
        return True
    else:
        return False


# Tests:

assert is_valid_isbn10("0-306-40615-2")
assert not is_valid_isbn10("0-306-40615-1")
assert is_valid_isbn10("0-8044-2957-X")
assert not is_valid_isbn10("X-306-40615-2")
assert is_valid_isbn10("0-6822-2589-4")
