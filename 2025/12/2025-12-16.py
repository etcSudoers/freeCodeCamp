def has_consonant_count(text: str, target: int) -> bool:
    count = 0
    ignoreLetters = ("a", "e", "i", "o", "u")
    breakDown = list(text)
    for a in breakDown:
        if a.lower() not in ignoreLetters and a.isalpha():
            count = count + 1
    if count == target:
        return True
    else:
        return False

assert has_consonant_count("helloworld", 7)  == True
assert has_consonant_count("eieio", 5)  ==  False
assert has_consonant_count("freeCodeCamp Rocks!", 11)  ==  True
assert has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 24)  ==  False
assert has_consonant_count("Th3 Qu!ck Br0wn F0x Jump5 0ver Th3 L@zy D0g.", 23)  ==  True

