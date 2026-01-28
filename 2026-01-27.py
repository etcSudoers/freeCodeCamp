"""
Odd or Even Day

Given a timestamp (number of milliseconds since the Unix epoch), return:

    "odd" if the day of the month for that timestamp is odd.
    "even" if the day of the month for that timestamp is even.

For example, given 1769472000000, a timestamp for January 27th, 2026, return "odd" because the day number (27) is an odd number.

"""

from datetime import datetime


def odd_or_even_day(timestamp: int):
    seconds = timestamp / 1000
    formatedDate = int(datetime.utcfromtimestamp(seconds).strftime("%d"))
    if formatedDate % 2 == 0:
        return "even"
    else:
        return "odd"


assert odd_or_even_day(1769472000000) == "odd"
assert odd_or_even_day(1769444440000) == "even"
assert odd_or_even_day(6739456780000) == "odd"
assert odd_or_even_day(1) == "odd"
assert odd_or_even_day(86400000) == "even"
