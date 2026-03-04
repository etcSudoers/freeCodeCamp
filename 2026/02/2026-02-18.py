def calculate_start_delays(jump_scores):
    bestScore = max(jump_scores)
    delays = []
    for i in jump_scores:
        delays.append(round(((bestScore - i)*1.5)+.4))
        

    return delays


assert calculate_start_delays([120, 110, 125])  == [8, 23, 0]
assert calculate_start_delays([118, 125, 122, 120])  == [11, 0, 5, 8]
assert calculate_start_delays([100, 105, 95, 110, 120, 115, 108])  == [30, 23, 38, 15, 0, 8, 18]
assert calculate_start_delays([130, 125, 128, 120, 118, 122, 127, 115, 132, 124])  == [3, 11, 6, 18, 21, 15, 8, 26, 0, 12]