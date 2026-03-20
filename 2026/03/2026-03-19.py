"""
Inverted Matrix

Given a matrix (an array of arrays) filled with two distinct values, return a new matrix where all occurrences of one value are swapped with the other.

For example, given:

[
  ["a", "b"],
  ["a", "a"]
]

Return:

[
  ["b", "a"],
  ["b", "b"]
]

"""


def invert_matrix(matrix: list):
    unique = list(set(matrix[0]))
    newList = []
    for i in matrix:
        i = list(map(lambda x: unique[1] if x == unique[0] else unique[0], i))
        newList.append(i)

    return newList


assert invert_matrix([["a", "b"], ["a", "a"]]) == [["b", "a"], ["b", "b"]]
assert invert_matrix([[1, 0, 1], [1, 1, 1], [0, 1, 0]]) == [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 1],
]
assert invert_matrix(
    [
        ["apple", "banana", "banana", "apple"],
        ["banana", "apple", "apple", "banana"],
        ["banana", "banana", "banana", "apple"],
    ]
) == [
    ["banana", "apple", "apple", "banana"],
    ["apple", "banana", "banana", "apple"],
    ["apple", "apple", "apple", "banana"],
]
assert invert_matrix(
    [
        [6, 7, 7, 7, 6],
        [7, 6, 7, 6, 7],
        [7, 7, 6, 7, 7],
        [7, 6, 7, 6, 7],
        [6, 7, 7, 7, 6],
    ]
) == [
    [7, 6, 6, 6, 7],
    [6, 7, 6, 7, 6],
    [6, 6, 7, 6, 6],
    [6, 7, 6, 7, 6],
    [7, 6, 6, 6, 7],
]
assert invert_matrix(
    [[1.2, 2.1, 2.1, 2.1], [2.1, 1.2, 2.1, 1.2], [1.2, 1.2, 2.1, 2.1]]
) == [[2.1, 1.2, 1.2, 1.2], [1.2, 2.1, 1.2, 2.1], [2.1, 2.1, 1.2, 1.2]]
