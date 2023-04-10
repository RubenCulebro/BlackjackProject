import random


def showHeader():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")


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


def startBlackjackGame(deck):
    dealerScore = 0
    dealerHand = []
    playerScore = 0
    playerHand = []

    for i in range(1, 5):
        if i % 2 != 0:
            turn = "player"
            playerScore = dealCard(deck, playerHand, playerScore, turn)
        else:
            turn = "dealer"
            dealerScore = dealCard(deck, dealerHand, dealerScore, turn)
            if i == 2:
                print()
                print("DEALER'S SHOW CARD")
                print(f"{dealerHand[0][0]} of {dealerHand[0][1]}")


def dealCard(deck, hand, score, turn):
    selectedCard = drawCard(deck)
    aceCard(selectedCard, score, turn)
    score += selectedCard[2]
    hand.append(selectedCard)
    return score


def aceCard(selectedCard,score, turn):
    if selectedCard[0] == "Ace" and (score < 11):
        if turn == "player":
            aceValue = int(input("\nAce value equals 1 or 11?:"))
            if aceValue == 1:
                selectedCard[2] = 1
            elif aceValue == 11:
                selectedCard[2] = 11
        elif turn == "dealer":
            selectedCard[2] = 11 # If dealer's score is < 10 assign the value of 11
    elif selectedCard[0] == "Ace" and (score >= 11):
        selectedCard[2] = 1


def drawCard(deck):
    selectCard = random.choice(deck)
    deck.remove(selectCard)
    return selectCard


def main():
    deck = cardDeck()
    showHeader()
    startBlackjackGame(deck)


if __name__ == '__main__':
    main()

