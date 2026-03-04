def largest_difference(skater1:list, skater2:list):
    compareLaps = []
    for i in range(0,len(skater1)):
        compareLaps.append(skater1[i] + skater2[i])

    greatestLap = compareLaps.index(max(compareLaps)) + 1

    print(greatestLap)

    return greatestLap

assert largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30]) == 3
assert largest_difference([27.04, 25.94, 26.22, 26.07, 26.18], [25.59, 25.80, 26.11, 26.01, 26.23]) == 1
assert largest_difference([25.82, 25.90, 26.05, 26.00, 26.48], [25.85, 25.92, 26.07, 25.98, 25.95]) == 5
assert largest_difference([25.88, 26.10, 25.95, 26.05, 26.00], [25.90, 26.55, 25.92, 26.03, 26.01]) == 2
assert largest_difference([25.92, 26.01, 26.05, 25.88, 26.12], [25.95, 26.00, 26.03, 26.45, 26.10]) == 4