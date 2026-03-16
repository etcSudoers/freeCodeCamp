def get_captured_value(pieces):
    total = 0
    dict = {
        "P": {"quantity": 8, "value": 1},
        "R": {"quantity": 2, "value": 5},
        "N": {"quantity": 2, "value": 3},
        "B": {"quantity": 2, "value": 3},
        "Q": {"quantity": 1, "value": 9},
        "K": {"quantity": 1, "value": 0},
    }

    for i in pieces:
        dict[i]["quantity"] -= 1

    if dict["K"]["quantity"] == 1:
        return "Checkmate"

    for d in dict.values():
        total += d["quantity"] * d["value"]

    return total


assert (
    get_captured_value(["P", "P", "P", "P", "P", "P", "R", "R", "N", "B", "Q", "K"])
    == 8
)
assert get_captured_value(["P", "P", "P", "P", "P", "R", "B", "K"]) == 26
assert (
    get_captured_value(["K", "P", "P", "N", "P", "P", "R", "P", "B", "P", "N", "B"])
    == 16
)
assert (
    get_captured_value(
        ["P", "Q", "N", "P", "P", "B", "K", "P", "R", "R", "P", "P", "B", "P"]
    )
    == 4
)
assert get_captured_value(["P", "K"]) == 38
assert (
    get_captured_value(
        ["N", "P", "P", "B", "K", "P", "Q", "N", "P", "P", "R", "R", "P", "P", "P", "B"]
    )
    == 0
)
assert (
    get_captured_value(["N", "P", "P", "B", "P", "R", "Q", "P", "P", "P", "B"])
    == "Checkmate"
)
