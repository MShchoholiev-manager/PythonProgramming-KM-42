print("Welcome to task 1!")
import string
eng_letters = list(string.ascii_lowercase)
let_count = 0
list = []
with open ("gadsby.txt", "r") as file:
    for line in file:
        for letter in line:
            if letter.isalpha():
                let_count += 1

for eng_letter in eng_letters:
     x = 0
     with open ("gadsby.txt", "r") as file:
          for line in file:
               for letter in line:
                    if letter.isalpha():
                         letter = letter.lower()
                         if letter == eng_letter:
                              x += 1
     elem = [round((x*100)/let_count,3),eng_letter]
     list.append(elem)
     list = sorted(list, reverse=True)

top_list = list[:5]
lower_list = list[-5:]
print()
print("Top 5 most common letters")
for count, letter in top_list:
     print(f"{letter}= {count}%")
print()
print("Bottom 5 least common letters:")
for count, letter in lower_list:
     print(f"{letter}= {count}%")
