import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4


def play_again():
    user_input = input("Do you want to play again? (Y/N): ").lower()
    if user_input == "y":
        dealer_hand = []
        player_hand = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
        game()
    elif user_input == "n":
        print("Goodbye!")
    else:
        print("Invalid option!")


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 14:
            card = "A"
        hand.append(card)
    return hand


def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >= 11:
                total += 1
            else:
                total += 11
        else:
            total += card
    return total


def hit(hand):
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"
    hand.append(card)
    return(hand)


def print_results(dealer_hand, player_hand):
    print("The dealer has a " + str(dealer_hand) +
          " for a total of " + str(total(dealer_hand)))
    print("You have a " + str(player_hand) +
          " for a total of " + str(total(player_hand)))


def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("You got a Blackjack! You win!")
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, the dealer got a Blackjack. You lose.")
        play_again()


def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("You got a Blackjack! You win!\n")
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, the dealer got a Blackjack. You lose.\n")
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Sorry, you busted. You lose.\n")
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)
        print("Dealer busted. You win!\n")
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Sorry, the dealer has a higher score. You lose.\n")
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)
        print("Your score is higher than the dealer! You win!\n")


def game():
    choice = 0
    print("Let's play Blackjack!\n")
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != "q":
        print("The dealer is showing a " + str(dealer_hand[0]))
        print("You have a " + str(player_hand) +
              " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        user_input = input(
            "Do you want to [H]it, [S]tand, or [Q]uit? ").lower()
        if user_input == "h":
            hit(player_hand)
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif user_input == "s":
            while total(dealer_hand) < 17:
                hit(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif user_input == "q":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


game()
