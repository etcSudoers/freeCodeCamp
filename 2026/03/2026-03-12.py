def is_valid_domino_chain(dominoes):
    previous = dominoes[0]
    for i in dominoes[1:]:
        if previous[1] != i[0]:
            return False
        previous = i
    return True


assert is_valid_domino_chain([[1, 3], [3, 6], [6, 5]])
assert not is_valid_domino_chain([[6, 2], [3, 4], [4, 1]])
assert not is_valid_domino_chain([[2, 5], [5, 6], [5, 1]])
assert is_valid_domino_chain(
    [[4, 3], [3, 1], [1, 6], [6, 6], [6, 5], [5, 1], [1, 1], [1, 4], [4, 4], [4, 2]]
)
assert not is_valid_domino_chain(
    [[2, 3], [3, 3], [3, 6], [6, 1], [1, 4], [3, 5], [5, 5], [5, 4], [4, 2], [2, 2]]
)
