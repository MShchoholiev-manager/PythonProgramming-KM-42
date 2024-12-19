print("Welcome to task 2!")

suits = ("diamonds", "clubs", "hearts", "spades")
cards = ("A",) + tuple(str(i) for i in range(2,11)) + ("J", "Q", "K")

def cards_gen(suits, cards):
    for suit in suits:
        for card in cards:
            yield(f"{card} {suit}")

gen = cards_gen(suits, cards)
try:
    while True:
        print(next(gen))
except StopIteration:
    print("StopIteration! All cards have been passed!")