def check_eligibility(athlete_weights, sled_weight):
    athletes = len(athlete_weights)
    athletesWeights = sum(athlete_weights)
    totalWeight = athletesWeights + sled_weight
    eligible = True

    # check min
    match athletes:
        case 1:
            if totalWeight - athletesWeights < 162:
                eligible = False
        case 2:
            if totalWeight - athletesWeights < 170:
                eligible = False
        case 4:
            if totalWeight  - athletesWeights < 210:
                eligible = False

    # check max
    match athletes:
        case 1:
            if totalWeight > 247:
                eligible = False
        case 2:
            if totalWeight > 390:
                eligible = False
        case 4:
            if totalWeight > 630:
                eligible = False

    if eligible:
        return "Eligible"
    else:
        return "Not Eligible"


assert check_eligibility([78], 165) == "Eligible"
assert check_eligibility([80], 160) == "Not Eligible"
assert check_eligibility([80], 170) == "Not Eligible"
assert check_eligibility([85, 90], 170) == "Eligible"
assert check_eligibility([85, 95], 168) == "Not Eligible"
assert check_eligibility([112, 97], 185) == "Not Eligible"
assert check_eligibility([110, 102, 90, 106], 222) == "Eligible"
assert check_eligibility([106, 99, 90, 88], 205) == "Not Eligible"
assert check_eligibility([106, 99, 103, 96], 227) == "Not Eligible"