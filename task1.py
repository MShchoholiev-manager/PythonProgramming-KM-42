
phrase1 = input("Enter first phrase: ")
phrase2 = input("Enter second phrase: ") #Введення користувачем фраз

def can_form_phrase(phrase1, phrase2): 

    phrase1_cleaned = set(lett.lower() for lett in phrase1 if lett.isalpha()) # Створення множин з літер фраз
    phrase2_cleaned = set(lett.lower() for lett in phrase2 if lett.isalpha())


    print(f"Set of unique letters of first phrase: {phrase1_cleaned}") # Виведення множин унікальних літер з кожної фрази
    print(f"Set of unique letters of second phrase: {phrase2_cleaned}")


    if phrase2_cleaned.issubset(phrase1_cleaned):
        print("It is possible to make the second phrase from the letters of the first.")
    else:
        print("It is not possible to make the second phrase from the letters of the first.") # Виведення результату: чи можна утворити другу фразу з літер першої


can_form_phrase(phrase1, phrase2)