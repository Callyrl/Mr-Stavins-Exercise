
import random
deck = []
def cards():
    value = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
    suites = ["Clubs", "Spades", "Diamonds", "Hearts"]


    for i in suites:
        for j in value:
            deck.append (i + " " + j)
def shuffle():
    cards()
    random.shuffle(deck)

for i in deck:
    print("You got:")
    print(deck)
