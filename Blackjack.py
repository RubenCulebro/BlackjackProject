def cardDeck():
    deck = []
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for suit in range(len(suits)):
        for rank in range(len(ranks)):
            card = [ranks[rank], suits[suit], points[rank]]  # reference: suits [0] #ranks[1]
            deck.append(card)
    return deck


def main():
    print("Blackjack Project\n")
    deck = cardDeck()
    print(deck)


if __name__ == '__main__':
    main()

