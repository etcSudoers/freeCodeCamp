"""
    Array Insertion

Given an array, a value to insert into the array, and an index to insert the value at,
return a new array with the value inserted at the specified index
"""


def insert_into_array(arr: list, value, index: int):
    arr.insert(index, value)

    return arr


# Tests:

assert insert_into_array([2, 4, 8, 10], 6, 2) == [2, 4, 6, 8, 10]
assert insert_into_array(["the", "quick", "fox"], "brown", 2) == [
    "the",
    "quick",
    "brown",
    "fox",
]
assert insert_into_array([], 0, 0) == [0]
assert insert_into_array([0, 1, 1, 2, 3, 8, 13], 5, 5) == [0, 1, 1, 2, 3, 5, 8, 13]
