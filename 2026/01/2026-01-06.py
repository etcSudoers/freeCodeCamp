"""
vOwElcAsE

Given a string, return a new string where all vowels are converted to uppercase and all other
alphabetical characters are converted to lowercase.

    Vowels are "a", "e", "i", "o", and "u" in any case.
    Non-alphabetical characters should remain unchanged.

"""


def vowel_case(s: str) -> str:
    s = s.lower()
    formatedS = (
        s.replace("a", "A")
        .replace("e", "E")
        .replace("i", "I")
        .replace("o", "O")
        .replace("u", "U")
    )
    return formatedS


assert vowel_case("vowelcase") == "vOwElcAsE"
assert vowel_case("coding is fun") == "cOdIng Is fUn"
assert vowel_case("HELLO, world!") == "hEllO, wOrld!"
assert vowel_case("git cherry-pick") == "gIt chErry-pIck"
assert vowel_case("HEAD~1") == "hEAd~1"
