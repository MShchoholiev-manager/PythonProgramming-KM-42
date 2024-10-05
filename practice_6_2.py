
index = input("Input your index: ")
province = {
    'A': 'Newfoundland',
    'B': 'Nova Scotia',
    'C': 'Prince Edward Island',
    'E': 'New Brunswick',
    'G': 'Quebec',
    'H': 'Quebec',
    'J': 'Quebec',
    'K': 'Ontario',
    'L': 'Ontario',
    'M': 'Ontario',
    'N': 'Ontario',
    'P': 'Ontario',
    'R': 'Manitoba',
    'S': 'Saskatchewan',
    'T': 'Alberta',
    'V': 'British Columbia',
    'X': ['Northwest Territories', 'Nunavut'], 
    'Y': 'Yukon'
}

if len(index) == 3 and index[0::2].isalpha() and index[1].isdigit():
    if index[0] not in province:
        print("Таких символів немає")

    else:
        if index[1] == "0":
            if index[0].upper() == "X":
                print(f"Сільська місцевість {province[index[0]][0]} або {province[index[0]][1]}")
            else:
                print(f"Сільська місцевість {province[index[0]]}")

        if index[1] != "0":
            if index[0].upper() == "X":
                print(f"Міська місцевість {province[index[0]][0]} або {province[index[0]][1]}")
            else:
                print(f"Міська місцевість {province[index[0]]}")

else:
    print("Please, input correct informaion")
