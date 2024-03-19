import random
playerin = True
dealerin = True
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
playercards = []
dealercards = []
#adding cards value up
def value(turn):
    value = 0
    special = ["J", "Q", "K"]
    ace = ["A"]
    for card in turn:
        if card in range(1, 11):
            value += card
        elif card in special:
            value += 10
        elif card in ace:
            if value > 11:
                value += 1
            else:
                value += 11
    return value
#dealing out the deck
def deal(turn):
    card = random.choice(cards)
    turn.append(card)
    cards.remove(card)
for every in range(2):
    deal(dealercards)
    deal(playercards)
#showing cards of the dealer
def showdealercards():
    if len(dealercards) == 2:
        return dealercards[0]
    elif len(dealercards) > 2:
 
         return dealercards[0], dealercards[1]
#stand or hit for the player
while playerin or dealerin:
    print(f"The dealer has {value(dealercards)} from {showdealercards()} and ?")
    print(f"You have {value(playercards)} from {playercards}")
    if playerin:
        standorhit = input("Do you want to stand or hit?\n")
    if value(dealercards) > 16:
        dealerin = False
    else:
        deal(dealercards)
    if standorhit == 'stand':
        playerin = False
        deal(dealercards)
    else:
        deal(playercards)
    if value(playercards) >= 21:
        break
    elif value(dealercards) >= 21:
        break
#how to know if the dealer or player has won
if value(playercards) == 21:
    print(f"You have {playercards} for {value(playercards)} and the dealer has {dealercards} for {value(dealercards)}")
    print("YOU WIN!")
elif value(dealercards) == 21:
    print(f"You have {playercards} for {value(playercards)} and the dealer has {dealercards} for {value(dealercards)}")
    print("THE DEALER WINS!")
elif value(playercards) > 21:
    print(f"You have {playercards} for {value(playercards)} and the dealer has {dealercards} for {value(dealercards)}")
    print("THE DEALER WINS, YOU HAVE BUST!")
elif value(dealercards) > 21:
    print(f"You have {playercards} for {value(playercards)} and the dealer has {dealercards} for {value(dealercards)}")
    print("YOU WIN, THE DEALER HAS BUST!")
elif 21 - value(dealercards) < 21 - value(playercards):
    print(f"You have {playercards} for {value(playercards)} and the dealer has {dealercards} for {value(dealercards)}")
    print("YOU WIN!")
elif 21 - value(dealercards) > 21 - value(playercards):
    print(f"You have {playercards} for {value(playercards)} and the dealer has {dealercards} for {value(dealercards)}")
    print("THE DEALER WINS!")
elif 21 - value(dealercards) == 21 - value(playercards):
    print(f"You have {playercards} for {value(playercards)} and the dealer has {dealercards} for {value(dealercards)}")
    print("YOU ARE TIED WITH THE DEALER!")
 
