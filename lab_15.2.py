print('Welcome to lab 15 task 2!')

card_suits = ['heart', 'diamond', 'club', 'spade']
values = ['A'] + [str(i) for i in range(2, 11)] + ['J', 'Q', 'K']

def card_gen(card_suits, values):
    for suit in card_suits:
        for value in values:
            yield f'{value} {suit}'

gen = card_gen(card_suits, values)
try:
    while True:
        print(next(gen))
except StopIteration:
    print('Playing cards are over.')
    pass