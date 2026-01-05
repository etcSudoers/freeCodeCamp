def find_left_handed_seats(table):
    availableSpots = 0
    leftSide = table[0]
    rightSide = table[1]

    toLeft = ""
    for l in leftSide:
        #print(l)
        if l == "U":
            if toLeft != "R": 
                #print("added left")
                availableSpots += 1
                toLeft = "L"
                continue
        toLeft = l

    toLeft = ""    
    for r in rightSide:
        #print(r)
        if r == "U":
            if toLeft != "R": 
                #print("added right")
                availableSpots += 1
                toLeft = "L"
                continue
        toLeft = r

    return availableSpots

assert find_left_handed_seats([["U", "R", "U", "L"], ["U", "R", "R", "R"]]) == 2
assert find_left_handed_seats([["U", "U", "U", "U"], ["U", "U", "U", "U"]]) == 8
assert find_left_handed_seats([["U", "R", "U", "R"], ["L", "R", "R", "U"]]) == 0
assert find_left_handed_seats([["L", "U", "R", "R"], ["L", "U", "R", "R"]]) == 1
assert find_left_handed_seats([["U", "R", "U", "U"], ["U", "U", "L", "U"]]) == 5

"""
Left-Handed Seat at the Table

Given a 4x2 matrix (array of arrays) representing the seating arrangement for a meal, determine how many seats a left-handed person can sit at.

    A left-handed person cannot sit where a right-handed person would be in the seat to the immediate left of them.

In the given matrix:

    An "R" is a seat occupied by a right-handed person.
    An "L" is a seat occupied by a left-handed person.
    An "U" is an unoccupied seat.
    Only unoccupied seats are available to sit at.
    The seats in the top row are facing "down", and the seats in the bottom row are facing "up" (like a table), so left and right are relative to the seat's orientation.
    Corner seats only have one seat next to them.

For example, in the given matrix:
"""

