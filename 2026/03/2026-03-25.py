"""Cooldown Time

Given two timestamps, the first representing when a user finished an exam,
and the second representing the current time, determine whether the user can take an exam again

    Both timestamps will be given the format: "YYYY-MM-DDTHH:MM:SS", for example "2026-03-25T14:00:00"
    Note that the time is 24-hour clock
    A user must wait at least 48 hours before retaking an exam
"""


def can_retake(finish_time: str, current_time: str):
    # since these are all the same month and year I will focus on day and timestamps
    dayFinished = finish_time.split("-")[2].split("T")[0]
    timeFinished = finish_time.split("-")[2].split("T")[1].split(":")
    print(dayFinished)
    print(timeFinished)

    currentDay = current_time.split("-")[2].split("T")[0]
    currentTime = current_time.split("-")[2].split("T")[1].split(":")
    print(currentDay)
    print(currentTime)

    # maths
    diffHours = 0

    # days
    diffHours += (int(currentDay) - int(dayFinished)) * 24
    # previous day hours to midnight plus curtrent day hours
    diffHours += int(24 - int(timeFinished[0])) + int(currentTime[0])

    if diffHours >= 48:
        return True
    else:
        return False


# Tests:

assert can_retake("2026-03-23T08:00:00", "2026-03-25T14:00:00") is True
assert can_retake("2026-03-24T14:00:00", "2026-03-25T10:00:00") is False
assert can_retake("2026-03-23T09:25:00", "2026-03-25T09:25:00") is True
assert can_retake("2026-03-25T11:50:00", "2026-03-23T11:49:59") is False
