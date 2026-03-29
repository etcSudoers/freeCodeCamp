"""Profile

    Daily Coding Challenge
    March 28, 2026

Pascal's Triangle Row

Given an integer n, return the nth row of Pascal's triangle as an array

In Pascal's Triangle, each row begins and ends with 1, and each interior value is the sum of the two values directly above it

Here's the first 5 rows of the triangle:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""


def pascal_row(n: int):
    for i in range(n):
        if i == 0:
            n = [1]
        else:
            n = [1] + [n[i] + n[i + 1] for i in range(len(n) - 1)] + [1]

    return n


# Tests:

assert pascal_row(5) == [1, 4, 6, 4, 1]
assert pascal_row(3) == [1, 2, 1]
assert pascal_row(1) == [1]
assert pascal_row(10) == [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
assert pascal_row(15) == [
    1,
    14,
    91,
    364,
    1001,
    2002,
    3003,
    3432,
    3003,
    2002,
    1001,
    364,
    91,
    14,
    1,
]
