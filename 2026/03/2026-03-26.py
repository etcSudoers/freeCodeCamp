"""
Movie Night

Given a string for the day of the week, another string for a showtime,
and an integer number of tickets, return the total cost of the movie tickets
for that showing

The given day will be one of:

    "Monday"
    "Tuesday"
    "Wednesday"
    "Thursday"
    "Friday"
    "Saturday"
    "Sunday"

The showtime will be given in the format "H:MMam" or "H:MMpm".
For example "10:00am" or "10:00pm"

Return the total cost in the format "$D.CC" using these rules:

    Weekend (Friday - Sunday): $12.00 per ticket
    Weekday (Monday - Thursday): $10.00 per ticket
    Matinee (before 5:00pm): subtract $2.00 per ticket (except on Tuesdays)
    Tuesdays: all tickets are $5.00 each
"""


def get_movie_night_cost(day: str, showtime: str, number_of_tickets: int):
    total = 0
    hour = showtime.split(":")[0]
    minute = showtime.split(":")[1][:2]
    afternoon = True if showtime[-2:] == "pm" else False

    if day == "Tuesday":
        total += 5 * number_of_tickets
    elif day == "Friday" or day == "Sunday" or day == "Saturday":
        total += 12 * number_of_tickets
    elif day == "Monday" or day == "Wednesday" or day == "Thursday":
        total += 10 * number_of_tickets

    if day != "Tuesday":
        if (
            (afternoon and int(hour) < 5)
            or (int(hour) == 5 and minute == "00")
            or (not afternoon)
        ):
            total -= 2 * number_of_tickets

    return f"${total:.2f}"


# Tests:

assert get_movie_night_cost("Saturday", "10:00pm", 1) == "$12.00"
assert get_movie_night_cost("Sunday", "10:00am", 1) == "$10.00"
assert get_movie_night_cost("Tuesday", "7:20pm", 2) == "$10.00"
assert get_movie_night_cost("Wednesday", "5:40pm", 3) == "$30.00"
assert get_movie_night_cost("Monday", "11:50am", 4) == "$32.00"
assert get_movie_night_cost("Friday", "4:30pm", 5) == "$50.00"
assert get_movie_night_cost("Tuesday", "11:30am", 1) == "$5.00"
