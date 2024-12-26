with open('gadsby.txt') as f:
    
    string = f.read().upper()
    dicti = dict()
    
    for i in range(ord('A'), ord('Z') + 1):
        countl = string.count(f'{chr(i)}')
        dicti[f'{chr(i)}'] = countl
        
    amount = sum(dicti.values())
    dict_sorted = sorted(dicti.items(), key=lambda i: i[1], reverse=True)
   
    for i in range(len(dict_sorted)):
        if (i <= 4) or (i >= len(dict_sorted) - 5):
            print(f'|{dict_sorted[i][0]:^3}|{round((dict_sorted[i][1] * 100) / amount , 3):<6}|')