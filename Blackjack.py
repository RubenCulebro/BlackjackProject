import random
import db


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

    money = playerWallet()

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

    turn = "player"
    playerScore = choiceHitStand(deck, playerHand, turn, dealerScore, playerScore)

    turn = "dealer"
    dealerScore = choiceHitStand(deck, dealerHand, turn, dealerScore, playerScore)

    print()
    print(f"YOUR POINTS:     {playerScore}")
    print(f"DEALER'S POINTS: {dealerScore}")
    print()

    print(f"\nMoney: {money}")

def dealCard(deck, hand, score, turn):
    selectedCard = drawCard(deck)
    aceCard(selectedCard, score, turn)
    score += selectedCard[2]
    hand.append(selectedCard)
    return score


def aceCard(selectedCard,score, turn):
    if selectedCard[0] == "Ace" and (score < 11):
        if turn == "player":
            while True:
                try:
                    aceValue = int(input("\nAce value equals 1 or 11?:"))
                    if aceValue == 1:
                        selectedCard[2] = 1
                        break
                    elif aceValue == 11:
                        selectedCard[2] = 11
                        break
                    else:
                        print("Invalid number, please try again.")
                except ValueError:
                    print("Not a valid input. Try again!")
                    continue
        elif turn == "dealer":
            selectedCard[2] = 11 # If dealer's score is < 10 assign the value of 11
    elif selectedCard[0] == "Ace" and (score >= 11):
        selectedCard[2] = 1


def choiceHitStand(deck, hand, turn, dealerScore, playerScore):
    if turn == "player":
        displayCards(hand, turn)

        while True:
            if playerScore <= 21:
                command = input("\nHit or stand? (hit/stand): ")
                if (command.lower() != "hit") and (command.lower() != "stand"):
                    print("Not a valid command. Try again!")
                    continue
                else:
                    break
        while (command.lower() == "hit") and (playerScore <= 21):
            playerScore = dealCard(deck, hand, playerScore, turn)
            displayCards(hand, turn)
            if playerScore >= 21:
                return playerScore
            while True:
                command = input("\nHit or stand? (hit/stand): ")
                if (command.lower() != "hit") and (command.lower() != "stand"):
                    print("Not a valid command. Try again!")
                    continue
                else:
                    break
        return playerScore
    elif turn == "dealer":
        while (playerScore <= 21) and (dealerScore <= 17):
            dealerScore = dealCard(deck, hand, dealerScore, turn)
        displayCards(hand, turn)
        return dealerScore


def displayCards(hand, turn):
    if turn == "player":
        print()
        print("YOUR CARDS:")
    elif turn == "dealer":
        print()
        print("DEALER'S CARDS:")
    for card in hand:
        print(f"{card[0]} of {card[1]}")


def isWinner(playerScore, dealerScore):
    if playerScore <= 21:
        if (dealerScore > 21) or (dealerScore < playerScore):
            if playerScore == 21:
                print("Blackjack!\nCongratulations!")
            elif dealerScore > 21:
                print("Dealer busts. You win!\nCongratulations!")
            else:
                print("You win!\nCongratulations!")

        elif playerScore == dealerScore:
            if playerScore == 21:
                print("You both have Blackjack.\nYou push.")
            else:
                print("It's a tie.\nNo one wins")

        elif playerScore < dealerScore:
            if dealerScore == 21:
                print("Sorry, dealer has a Blackjack.\nYou lose.")
            else:
                print("Sorry.\nYou lose.")
    else:
        print("You busted and lost.\nSorry.")


def playerWallet():
    money = db.readFile()
    buyChips = 0
    if money < 5:
        print(f"\nYour money amount (${money}) dropped below the minimum bet ($5.0).")
        while buyChips < 5:
            try:
                buyChips = float(input("You must buy a minimum of 5 chips. Please enter number of chips: "))
            except ValueError:
                print("Invalid input, try again.")
                continue
            db.writeFile(buyChips)
            money = db.readFile()
        return money
    else:
        return money


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

