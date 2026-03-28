# FCC instructions full of typos.   Hours of testing different code failed and failed.
# Got ChatGPT invovled and it could not even figure it out.
# https://github.com/freeCodeCamp/freeCodeCamp/issues/66646
# I dont even have my original code anymore (which i thought was pretty sweet.)
# The code below is chatgpt's final attempt before I seached if this was a bad FCC  problem.
#
# I GIVE UP AND GOING TO BED


"""
Truncate the Text 2

Given a string, return a new string that is truncated so that the total width of the characters does not exceed
50 units

Each character has a specific width:
Letters 	Width
"ilI" 	1
"fjrt" 	2
"abcdeghkmnopqrstuvwxyzJL" 	3
"ABCDEFGHKMNOPQRSTUVWXYZ" 	4

The table above includes all upper and lower case letters. Additionally:

    Spaces (" ") have a width of 2

    Periods (".") have a width of 1

    If the given string is 50 units or less, return the string as-is, otherwise

    Truncate the string and add three periods at the end ("...") so it's total width, including the three periods,
    is as close as possible to 60 units without going over
"""


def truncate_text(s: str):
    w = {}

    for c in "ilI":
        w[c] = 1
    for c in "fjrt":
        w[c] = 2
    for c in "abcdeghkmnopqrstuvwxyzJL":
        if c not in "ilIfjrt":
            w[c] = 3
    for c in "ABCDEFGHKMNOPQRSTUVWXYZ":
        w[c] = 4

    w[" "] = 2
    w["."] = 1

    total = sum(w[c] for c in s)

    # ✅ no truncation
    if total <= 50:
        return s

    # build up to 50
    res = ""
    width = 0

    for c in s:
        if width + w[c] > 50:
            break
        res += c
        width += w[c]

    # 🔥 key: REPLACE last 3 chars, not append
    return res[:-3] + "..."


print(truncate_text("The quick brown fox"))  # == "The quick brown f..."
print(truncate_text("THE LOUD BRIGHT BIRD"))
print(
    truncate_text("The silky smooth sloth")
)  # assert truncate_text("The quick brown fox") == "The quick brown f..."
# assert truncate_text("The silky smooth sloth") == truncate_text(
#    "The silky smooth sloth"
# )
# assert truncate_text("THE LOUD BRIGHT BIRD") == "THE LOUD BRIG..."
# assert truncate_text("The fast striped zebra") == "The fast striped z..."
# assert truncate_text("The big black bear") == "The big black bear"
