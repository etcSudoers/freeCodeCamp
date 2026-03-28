def get_shadow(time: str):
    hour, min = map(int, time.split(":", 1))
    if hour * 60 + min < 360 or hour * 60 + min >= 1080 or hour * 60 + min == 720:
        return "No shadow"

    # shadow length
    length = ((720 - ((hour * 60) + min)) / 60) ** 3
    print(f"{length:g}")
    if length < 0:
        return f"{length * -1:g}ft east"
    if length > 0:
        return f"{length:g}ft west"
    return time


assert get_shadow("10:00") == "8ft west"
assert get_shadow("15:00") == "27ft east"
assert get_shadow("12:00") == "No shadow"
assert get_shadow("17:30") == "166.375ft east"
assert get_shadow("05:00") == "No shadow"
assert get_shadow("06:00") == "216ft west"
assert get_shadow("18:00") == "No shadow"
assert get_shadow("07:30") == "91.125ft west"
assert get_shadow("00:00") == "No shadow"
