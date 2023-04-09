import random
def cardDeck():
    deck = []
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    points = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    for suit in range(len(suits)):
        for rank in range(len(ranks)):
            card = [ranks[rank], suits[suit], points[rank]]
            deck.append(card)
    return deck

def drawCard(deck):
    selectCard = random.choice(deck)
    deck.remove(selectCard)

    return selectCard

def main():
    print("Blackjack Project\n")
    deck = cardDeck()
    print(deck)


if __name__ == '__main__':
    main()

