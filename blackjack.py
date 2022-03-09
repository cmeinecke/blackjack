import random
# import itertools

# vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
# suits = ['spades', 'clubs', 'hearts', 'diamonds']

# deck = list(itertools.product(vals, suits))

dealer_cards = []

player_cards = []

# Deal the cards


while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1, 11))
    if len(dealer_cards) == 2:
        print("Dealer has ? &", dealer_cards[1])

while len(player_cards) != 2:
    player_cards.append(random.randint(1, 11))
    if len(player_cards) == 2:
        print("Player has", player_cards)

# Sum of the cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

while sum(player_cards) < 21:
    action_taken = str(input("Stay or hit? "))
    if action_taken == "hit":
        player_cards.append(random.randint(1, 11))
        print("You now have a total of " + str(sum(player_cards)) +
              " from these cards ", player_cards)
    else:
        print("The dealer has a total of " +
              str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " +
              str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins!")
        else:
            print("You win!")
            break

if sum(player_cards) > 21:
    print("You busted! Dealer wins")
elif sum(player_cards) == 21:
    print("You have Blackjack! You win!")
