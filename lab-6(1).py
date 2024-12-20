print('\nКурс "Програмування на мові Python"\n')
print('Практичне зайняття №6\n\nТема: "Робота з кортежами, множинами та словниками"\n')
print("Завдання №1")

phrase1 = input("\nEnter first phrase: ")
phrase2 = input("\nEnter second phrase: ")
letters1 = {char.lower() for char in phrase1 if char.isalpha()}
letters2 = {char.lower() for char in phrase2 if char.isalpha()}
can_form = letters2.issubset(letters1)
print("\nThe first phrase contains", len(letters1), f"unique letters: {letters1}")
print("\nThe second phrase contains", len(letters2), f"unique letters: {letters2}")
if can_form:
    print("\nThe letters of the first phrase can be used to form the second phrase.\n")
else:
    print("\nThe letters of the first phrase cannot form the second phrase.\n")