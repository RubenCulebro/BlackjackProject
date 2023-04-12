import sys

WALLET_FILE = "money.txt"


def exitBlackjackGame():
    print("Terminating game.\nBye!")
    sys.exit()


def readFile():
    try:
        with open(WALLET_FILE) as file:
            money = file.readline()
        return float(money)
    except FileNotFoundError:
        print(f"Could not find file: {WALLET_FILE}")
        exitBlackjackGame()
    except Exception as e:
        print("Unexpected error.")
        print(type(e), e)
        exitBlackjackGame()


def writeFile(money):
    try:
        with open(WALLET_FILE, "w", newline="") as file:
            file.write(str(money))
    except FileNotFoundError:
        print("File not found.")
        exitBlackjackGame()
    except Exception as e:
        print("Unexpected error.")
        print(type(e), e)
        exitBlackjackGame()
