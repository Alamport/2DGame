'''
Will simulate a game of blackjack where the user can be interactive
'''
# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import random

def dealer():
    hand = []
    while sum(hand) < 15:
        hand = draw(hand)

    if (is_legal(hand)):
        return hand
    else:
        return "Bust"

    print(hand)

def draw(hand):
    # Random card from 1 - 13 (Jack = 11, Queen = 12, King = 13)
    card = random.randint(1,14)
    hand.append(card)
    return hand

# Checks if the sum of cards in a hand is too large
def is_legal(hand):
    if sum(hand) > 21:
        return False
    else:
        return True

def main():
    print(dealer())

main()