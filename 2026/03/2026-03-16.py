def is_evenly_divisible(a, b):
    if a % b == 0:
        return True

    return False


assert is_evenly_divisible(4, 2)
assert not is_evenly_divisible(7, 3)
assert not is_evenly_divisible(5, 10)
assert is_evenly_divisible(48, 6)
assert is_evenly_divisible(3186, 9)
assert not is_evenly_divisible(4192, 11)
