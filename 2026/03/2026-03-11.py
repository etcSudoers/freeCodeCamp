"""
Word Length Converter

Given a string of words, return a new string where each word is replaced by its length.

    Words in the given string will be separated by a single space
    Keep the spaces in the returned string.

For example, given "hello world", return "5 5".

"""


def convert_words(s):
    newStr = ""
    splitWords = s.split(" ")
    for i in splitWords:
        newStr += f"{len(i)} "

    return newStr[:-1]


assert convert_words("hello world") == "5 5"
assert convert_words("Thanks and happy coding") == "6 3 5 6"
assert convert_words("The quick brown fox jumps over the lazy dog") == "3 5 5 3 5 4 3 4 3"
assert convert_words("Lorem ipsum dolor sit amet consectetur adipiscing elit donec ut ligula vehicula iaculis orci vel semper nisl") == "5 5 5 3 4 11 10 4 5 2 6 8 7 4 3 6 4"
