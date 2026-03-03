def fuel_to_add(current_gallons:int , required_liters: int):
    addGals = 0
    while True:
        current_liters = current_gallons * 3.78541
        #print(f"Current liters: {current_liters}, Required liters:  {required_liters}")
        if current_liters >= required_liters: break
        addGals += 1
        current_gallons += 1
    
    return addGals



assert fuel_to_add(0, 1) == 1
assert fuel_to_add(5, 40) == 6
assert fuel_to_add(10, 30) == 0
assert fuel_to_add(896, 20500) == 4520
assert fuel_to_add(1000, 50000) == 12209

"""
Given the numbers of gallons of fuel currently in your airplane, 
and the required number of liters of fuel to reach your destination, 
determine how many additional gallons of fuel you should add.
    1 gallon equals 3.78541 liters.
    If the airplane already has enough fuel, return 0.
    You can only add whole gallons.
    Do not include decimals in the return number.
"""

'''
assert fuel_to_add(0, 1) == 1
assert fuel_to_add(5, 40) == 6
assert fuel_to_add(10, 30) == 0
assert fuel_to_add(896, 20500) == 4520
assert fuel_to_add(1000, 50000) == 12209
'''