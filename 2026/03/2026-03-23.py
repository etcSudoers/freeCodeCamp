"""
    No Consecutive Repeats

Given a string, determine if it has no repeating characters.

    A string has no repeats if it does not have the same character two or more times in a row.

"""


def has_no_repeats(s: str):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


# Tests:

assert has_no_repeats("hi world") is True
assert has_no_repeats("hello world") is False
assert has_no_repeats("abcdefghijklmnopqrstuvwxyz") is True
assert has_no_repeats("freeCodeCamp") is False
assert has_no_repeats("The quick brown fox jumped over the lazy dog.") is True
assert has_no_repeats("Mississippi") is False
