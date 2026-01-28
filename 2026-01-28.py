"""
Flatten the Array

Given an array that contains nested arrays, return a new array with all values flattened into a single,
one-dimensional array. Retain the original order of the items in the arrays.

"""

flattened = []


def flatten(arr):
    for i in arr:
        if type(i) is not list:
            flattened.append(i)
        if type(i) is list:
            flatten(i)

    return flattened


# assert flatten([1, [2, 3], 4]) == [1, 2, 3, 4]
# assert flatten([5, [4, [3, 2]], 1]) == [5, 4, 3, 2, 1]
# assert flatten(["A", [[[["B"]]]], "C"]) == ["A", "B", "C"]
# assert flatten([["L", "M", "N"], ["O", ["P", "Q", ["R", ["S", ["T", "U"]]]]], "V", ["W", ["X", ["Y", ["Z"]]]]]) == ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
assert flatten(
    [
        ["red", ["blue", ["green", ["yellow", ["purple"]]]]],
        "orange",
        ["pink", ["brown"]],
    ]
) == ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown"]
