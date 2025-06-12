import random
import sys
money = 5000
dealermoney = 10000
suites = ["Diamonds", "Spades", "Clubs", "Hearts"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
deck = [(card, suite) for suite in suites for card in cards]
random.shuffle(deck)
card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

print("Hello! Welcome to Blackjack!")
while True:
    ask1 = input("If you'd like to play, type play. To exit, type quit or exit: ").strip().lower()
    if ask1.lower() == "play":
        print("Great, lets get started!")
        break
    elif ask1.lower() in ["exit", "quit"]:
        print("Exiting...")
        sys.exit()
    else:
        print("That answer is not recognized! please try again!")    

def play_round(player_hand, money, initialbet, deck):
    while True:
        print("Now that the betting is complete, lets get started!")
        ask2 = input("What would you like to do? Hit, Stand, Double Down or Split?")
        if ask2.lower() == "hit":
            print("You have decided to hit! You will recieve one more additional card.")
            player_hand.append(deck.pop())
            print("Your hand is: ", player_hand)
        elif ask2.lower() == "stand":
            print("You have decided to stand! you will not select any more cards!")
        elif ask2.lower() == "double down":
            print("You have decided to double down! you will bet your initial bet and then recieve an additional card")
            initialbet *= 2
            money -= initialbet
            print("You have bet " + str(initialbet * 2) + " dollars now")
            player_hand.append(deck.pop())
        else:
            print("Thats not a valid option, please retry!")
    
def hand_value(player_hand, cards ):
    value = 0
    ace_counter = 0
            




while True:
    initialbet = input(f"Lets start by betting! How much would you like to bet? you have {money} dollars")
    if int(initialbet) <= money:
        print("Great! you have bet " + str(initialbet) + " dollars!")
        money -= int(initialbet)
        print(f"You now have {money} dollars")
        break
    elif int(initialbet) > money:
        print("Oof, unfortunately you don't have enough money to bet!")
    else:
        print("I don't recgonize this answer! please try again!")

while True:
    if dealermoney >= int(initialbet):
        print(f"The dealer has bet {initialbet} dollars")
        dealermoney -= int(initialbet)
        break
    elif dealermoney < int(initialbet):
        print(f"The dealer has gone all in! They have bet {dealermoney}")
        dealerbet = dealermoney
        dealermoney = 0
        break

print("Now that the betting has concluded lets begin by dealing the cards!")

player_hand = []
dealer_hand = []

def dealing(deck):#Beginning of the round with dealing.
    
    #System of betting in card games (left to right, alternating to increase randomness.)
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    return player_hand, dealer_hand



