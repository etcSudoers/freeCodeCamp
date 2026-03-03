from re import split


def sum_letters(s: str):
    letterVal = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    }
    total = 0
    for i in split("", s):
        if i.isalpha():
            total = total + letterVal.get(i.lower())
    return total


assert sum_letters("Hello") == 52
assert sum_letters("freeCodeCamp") == 94
assert sum_letters("The quick brown fox jumps over the lazy dog.") == 473
assert (
    sum_letters(
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ex nisl, pretium eu varius blandit, facilisis quis eros. Vestibulum ante ipsum primis in faucibus orci."
    )
    == 1681
)
assert sum_letters("</404>") == 0
