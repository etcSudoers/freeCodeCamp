def sum_array(numbers):

    return sum(numbers)

assert sum_array([1, 2, 3, 4, 5])  == 15
assert sum_array([42])  == 42
assert sum_array([5, -2, 7, -3])  == 7
assert sum_array([203, 145, -129, 6293, 523, -919, 845, 2434])  == 9395
assert sum_array([0, 0])  == 0