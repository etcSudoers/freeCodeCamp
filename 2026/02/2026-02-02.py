"""

main.py Editor
JavaScript
Python
Console
Hide the previewTerminal
Move the preview to a new window and focus it
Groundhog Day
Today is Groundhog Day, in which a groundhog predicts the weather based on whether or not it sees its shadow.

Given a value representing the groundhog's appearance, return the correct prediction:

If the given value is the boolean true (the groundhog saw its shadow), return "Looks like we'll have six more weeks of winter.".
If the value is the boolean false (the groundhog did not see its shadow), return "It's going to be an early spring.".
If the value is anything else (the groundhog did not show up), return "No prediction this year.".
"""


def groundhog_day_prediction(appearance):
    if appearance is True:
        return "Looks like we'll have six more weeks of winter."
    if appearance is False:
        return "It's going to be an early spring."
    return "No prediction this year."


assert (
    groundhog_day_prediction(True) == "Looks like we'll have six more weeks of winter."
)
assert groundhog_day_prediction(False) == "It's going to be an early spring."
assert groundhog_day_prediction(None) == "No prediction this year."
assert groundhog_day_prediction(" ") == "No prediction this year."
assert groundhog_day_prediction("True") == "No prediction this year."
