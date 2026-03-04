def card_values(cards):
    numberedCards = []
    for i in cards:
        currentCard = i[:-1]
        match currentCard:
            case "A":
                numberedCards.append(1)
            case "J" | "Q" | "K":
                numberedCards.append(10)
            case _:
                numberedCards.append(int(currentCard))


    return numberedCards

assert card_values(["3H", "4D", "5S"]) == [3, 4, 5]
assert card_values(["AS", "10S", "10H", "6D", "7D"]) == [1, 10, 10, 6, 7]
assert card_values(["8D", "QS", "2H", "JC", "9C"]) == [8, 10, 2, 10, 9]
assert card_values(["AS", "KS"]) == [1, 10]
assert card_values(["10H", "JH", "QH", "KH", "AH"]) == [10, 10, 10, 10, 1]