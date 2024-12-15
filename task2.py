suits = ('diamonds', 'hearts', 'clubs', 'spades')
values = ('A', *range(2, 11), 'J', 'Q', 'K')

def card_generator(values, suits):
    for suit in suits:
        for value in values:
            yield f'{value} {suit}'

cards = card_generator(values, suits)

try:
    while True:
        print(next(cards))
except StopIteration:
    print('Iteration stopped')