def calculate_parking_fee(park_time, pickup_time):
    afterHours = 0

    diffHours = int(pickup_time.split(":")[0]) - int(park_time.split(":")[0])
    diffMin = int(pickup_time.split(":")[1]) - int(park_time.split(":")[1])
    if diffMin > 0:
        diffHours += 1

    if diffHours <= 0:
        diffHours = diffHours * -1
        diffHours = 24 - diffHours
        #    if diffHours <= 0:
        afterHours += 10

    cost = diffHours * 3
    if cost <= 5:
        return "$5"
    return f"${cost + afterHours}"


assert calculate_parking_fee("09:00", "11:00") == "$6"
assert calculate_parking_fee("10:00", "10:31") == "$5"
assert calculate_parking_fee("08:10", "10:45") == "$9"
assert calculate_parking_fee("14:40", "23:10") == "$27"
assert calculate_parking_fee("18:15", "01:30") == "$34"
assert calculate_parking_fee("11:11", "11:10") == "$82"
