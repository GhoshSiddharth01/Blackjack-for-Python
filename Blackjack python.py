# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Blackjack

import random
#Dealer cards
dealer_cards = []

#Player cards
player_cards = []

print()
print("Note: read only bottom line to know outcome of the game")
print()

#Deal the cards
while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1,11))
        if len(dealer_cards) ==2:
            print("Dealer has: X &", dealer_cards[1])


#Player Cards
while len(player_cards) != 2:
        player_cards.append(random.randint(1,11))
        if len(player_cards) ==2:
            print("Player 1 has: ", player_cards)
            
#Sum of Dealer Cards
if sum(dealer_cards) == 21:
    print("Dealer has 21, and wins the game!")
    
#Sum of player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit? "))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) + "from these cards ", player_cards)
    if action_taken == "stay":
        print("You have a total of " + str(sum(player_cards)) + " with ", player_cards)
        if 22 > sum(dealer_cards) > sum(player_cards):
            print("Dealer wins the game")
            break
        else:
            print("Player 1 wins!")
            break

#Dealer janky AI
if sum(dealer_cards) < 16 and action_taken == "stay":
    dealer_cards.append(random.randint(1, 11))
    
if sum(dealer_cards) > 16 and action_taken == "hit":
    print("The dealer has a total of " + str(sum(dealer_cards)) + "with", dealer_cards)

if sum(dealer_cards) > 21:
    print("Dealer busts, Player 1 wins the game!")

if sum(player_cards) > 21:
    print("Player 1 busts, Dealer wins")
elif sum(player_cards) == 21:
    print("Player 1 has blackjack!")
    print("Player 1 wins!")

if sum(player_cards) == sum(dealer_cards):
    print("It's a tie")

if sum(player_cards) > 21 and sum(dealer_cards) > 21:
    print("Both Dealer and Player 1 bust, it's a tie")