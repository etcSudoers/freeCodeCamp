

def tire_status(pressures_psi, range_bar):
    tireLevel = []
    lowPSI = range_bar[0] * 14.5038
    highPSI = range_bar[1] * 14.5028
    for i in pressures_psi:
        if i >= lowPSI and i <= highPSI:
            tireLevel.append("Good")
        if i > highPSI:
            tireLevel.append("High")
        if i < lowPSI:
            tireLevel.append("Low")
    return tireLevel


'''
Tire Pressure

Given an array with four numbers representing the tire pressures in psi of the four tires in your vehicle, 
and another array of two numbers representing the minimum and maximum pressure for your tires in bar, 
return an array of four strings describing each tire's status.

    1 bar equal 14.5038 psi.

Return an array with the following values for each tire:

    "Low" if the tire pressure is below the minimum allowed.
    "Good" if it's between the minimum and maximum allowed.
    "High" if it's above the maximum allowed.


'''

assert tire_status([32, 28, 35, 29], [2, 3]) ==["Good", "Low", "Good", "Low"]
assert tire_status([32, 28, 35, 30], [2, 2.3]) ==["Good", "Low", "High", "Good"]
assert tire_status([29, 26, 31, 28], [2.1, 2.5]) ==["Low", "Low", "Good", "Low"]
assert tire_status([31, 31, 30, 29], [1.5, 2]) ==["High", "High", "High", "Good"]
assert tire_status([30, 28, 30, 29], [1.9, 2.1]) ==["Good", "Good", "Good", "Good"]