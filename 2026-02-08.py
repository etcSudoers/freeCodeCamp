def calculate_penalty_distance(rounds):
    total = 0
    for i in rounds:
        roundDist = (5 - i) * 150
        total = total + roundDist

    return total

assert calculate_penalty_distance([4, 4]) == 300
assert calculate_penalty_distance([5, 5]) == 0
assert calculate_penalty_distance([4, 5, 3, 5]) == 450
assert calculate_penalty_distance([5, 4, 5, 5]) == 150
assert calculate_penalty_distance([4, 3, 0, 3]) == 1500