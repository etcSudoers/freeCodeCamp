def count_letters_and_numbers(s:str):
    letters = 0
    numbers = 0
    for i in list(s):
        if i.isnumeric():
            numbers += 1
        if i.isalpha():
            letters += 1
    
    # Determine the correct singular or plural forms
    letter_word = "letter" if letters == 1 else "letters"
    number_word = "number" if numbers == 1 else "numbers"
    
    return f"The string has {letters} {letter_word} and {numbers} {number_word}."


assert count_letters_and_numbers("helloworld123") == "The string has 10 letters and 3 numbers."
assert count_letters_and_numbers("Catch 22") == "The string has 5 letters and 2 numbers."
assert count_letters_and_numbers("A1!") == "The string has 1 letter and 1 number."
assert count_letters_and_numbers("12345") == "The string has 0 letters and 5 numbers."
assert count_letters_and_numbers("password") == "The string has 8 letters and 0 numbers."