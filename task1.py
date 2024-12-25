from collections import Counter
import string

with open("gadsby.txt", "r", encoding="utf-8") as file:
    text = file.read()

letters = ''.join(filter(lambda char: char in string.ascii_letters, text)).lower()

letter_counts = Counter(letters)
total_letters = sum(letter_counts.values())


letter_percent = {letter: (count / total_letters) * 100 for letter, count in letter_counts.items()}

sorted_letters = sorted(
    letter_percent.items(),
    key=lambda x: (-x[1], x[0] if x[0] != 'e' else '')
)

sorted_letters = {letter: round(percent, 3) for letter, percent in sorted_letters}

for letter, percent in sorted_letters.items():
    print(f"{letter}: {percent}%")