"""
Daily Coding Challenge
March 7, 2026

Element Size

Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels

    The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example

    "vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window

    "vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window
"""


def get_element_size(window_size: str, element_v: str, element_vh: str):
    windowWidth, windowHeight = map(int, window_size.split(" x "))
    elementWidth = int(element_v[:-2])
    elementHeight = int(element_vh[:-2])

    return f"{(windowWidth * elementWidth) / 100:g} x {(windowHeight * elementHeight) / 100:g}"


# Tests:
assert get_element_size("1200 x 800", "50vw", "50vh") == "600 x 400"
assert get_element_size("320 x 480", "25vw", "50vh") == "80 x 240"
assert get_element_size("1000 x 500", "7vw", "3vh") == "70 x 15"
assert get_element_size("1920 x 1080", "95vw", "100vh") == "1824 x 1080"
assert get_element_size("1200 x 800", "0vw", "0vh") == "0 x 0"
assert get_element_size("1440 x 900", "100vw", "114vh") == "1440 x 1026"
