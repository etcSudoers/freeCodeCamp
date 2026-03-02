def is_flat(arr):
    for i in arr:
        if isinstance(i,list):
            return False
    return True

assert is_flat([1, 2, 3, 4]) == True
assert is_flat([1, [2, 3], 4]) == False
assert is_flat([1, 0, False, True, "a", "b"]) == True
assert is_flat(["a", [0], "b", True]) == False
assert is_flat([1, [2, [3, [4, [5]]]], 6]) == False