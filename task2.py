
province_dict = {
    'Newfoundland': 'A',
    'Nova Scotia': 'B',
    'Prince Edward Island': 'C',
    'New Brunswick': 'E',
    'Quebec': ('G', 'H', 'J'),
    'Ontario': ('K', 'L', 'M', 'N', 'P'),
    'Manitoba': 'R',
    'Saskatchewan': 'S',
    'Alberta': 'T',
    'British Columbia': 'V',
    'Nunavut': 'X',
    'Northwest Territories': 'X',
    'Yukon': 'Y'
 }          # Словник, що заданий умовою

while True:   # Початок циклу
    postcode = input('Enter postcode: ').upper()  # Введення поштового індексу користувачем, та переведення його одразу у верхній регістр

    if len(postcode) != 3 or not postcode[0].isalpha() or not postcode[1].isdigit() or not postcode[2].isalpha(): # Перевірка різних умов
        print('Uncorrect postcode. Postcode must have 3 symbols: first - letter, second - number, third - letter.')
        continue

    province = None
    for key, values in province_dict.items():    # Створення ключа
        if (isinstance(values, tuple) and postcode[0] in values) or (postcode[0] == values):
            province = key
            break

    if province is None:
        print('Uncorrect. Try again.')
        continue

    if postcode[1] == '0':
        print(f'Recipient lives in the countryside of {province}.')
    else:
        print(f'Recipient lives in a city in {province}.')
    
    break # Кінець циклу