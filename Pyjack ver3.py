import random

def blackjack():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4  # Four decks for better realism
    random.shuffle(deck)

    def deal_card(hand):
        card = deck.pop()  # Deal a card and remove it from the deck
        hand.append(card)
        return card

    def calculate_score(hand):
        score = sum(hand)
        num_aces = hand.count(11)
        while score > 21 and num_aces:
            score -= 10
            num_aces -= 1
        return score

    player_hand = []
    dealer_hand = []
    
    for _ in range(2):
        deal_card(player_hand)
        deal_card(dealer_hand)

    print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
    print(f"Dealer's first card: {dealer_hand[0]}")

    while True:
        player_choice = input("Type 'hit' to get another card, type 'stand' to pass: ").lower()
        if player_choice == 'hit':
            deal_card(player_hand)
            print(f"Your cards: {player_hand}, current score: {calculate_score(player_hand)}")
            if calculate_score(player_hand) > 21:
                print("You bust! Dealer wins.")
                return
        elif player_choice == 'stand':
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

    while calculate_score(dealer_hand) < 17:
        deal_card(dealer_hand)
        print(f"Dealer's cards: {dealer_hand}, current score: {calculate_score(dealer_hand)}")

    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)

    if dealer_score > 21:
        print("Dealer busts! You win.")
    elif player_score > dealer_score:
        print("You win!")
    elif dealer_score > player_score:
        print("Dealer wins.")
    else:
        print("It's a tie!")
blackjack()
