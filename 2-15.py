suits = ("diamonds", "clubs", "hearts", "spades")
cards = ("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")

def cards_gen(suits, cards):
    for suit in suits:

        for card in cards:
            yield (card, suit)

gen = cards_gen(suits, cards)

while True:
    try: 
        print(next(gen))

    except StopIteration:
        print("All cards have been written!")
        
        break

        