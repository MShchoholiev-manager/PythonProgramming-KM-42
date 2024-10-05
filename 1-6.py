while True:
    first_word = input("Enter first phrase:")
    second_phrase = input("Enter second phrase:")
    check1 = set(first_word.lower())
    check2 = set(second_phrase.lower())
    set1 = set()
    set2 = set()
    print("Letters in 1st:")
    for letters1 in check1:
        if letters1.isalpha():
            print(letters1, end=", ")
            set1.add(letters1)
    print()
    print("Letters in 2nd:")
    for letters2 in check2:
        if letters2.isalpha():
            print (letters2, end=", ")
            set2.add(letters2)
    print()
    if set1 | set2 == set1:
        print("Yes, you can create second phrase using letters from first")
    else:
        print ("No, you can't create second phrase using letters from first")