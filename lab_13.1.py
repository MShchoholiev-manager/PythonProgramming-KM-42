print('Welcome to lab 11 task 1.')
print('Persentages of each letter in gadsby.txt(5 most common and 5 least common)')
let_count = 0
lst = []

with open('gadsby.txt', 'r') as file:
    for line in file:
        for letter in line:
            if letter.isalpha():
                letter = letter.lower()
                let_count += 1
                found = False
                for index, item in enumerate(lst):
                    if item[0] == letter:
                        lst[index] = (item[0], item[1] + 1)
                        found = True
                        break
                if not found:
                    lst.append((letter, 1))

lst_sorted = sorted(lst, key=lambda x: x[1], reverse=True)

result = [(letter, (count / let_count) * 100) for letter, count in lst_sorted[:5] + lst_sorted[-5:]]

for item in result:
    letter, percentage = item
    print(f'{letter}: {percentage:.3f}%')