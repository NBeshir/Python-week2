import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:

    card_choice = input(

        "Press enter to pick a card, or Q then enter enter to quit")

    if card_choice == "Q":
        break

    else:
        card = random.choice(diamonds)

        index_of_card = diamonds.index(card)

        hand.append(card)
        diamonds.pop(index_of_card)
        print("Your hand:", hand)
        print("remaining cards: ", diamonds)
if len(diamonds) == 0:
    print("There are no more cards to pick.")
