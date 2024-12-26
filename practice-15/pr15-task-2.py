suits = ['diamonds', 'clubs', 'hearts', 'spades']
values = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']

def card_deck_gen(list1, list2):
    for suit in list1:
        for value in list2:
            yield f'{value} {suit}'

card_desk = card_deck_gen(suits, values)
while(True):
    print(next(card_desk))