def card_deck_generator():
    suits = ("diamonds", "clubs", "hearts", "spades")  # Масті
    values = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']  # Значення карт
    
    for suit in suits:
        for value in values:
            yield f"{value} {suit}"

deck = card_deck_generator()

try:
    while True:
        print(next(deck))  
except StopIteration:
    print("The deck of cards is complete.")  