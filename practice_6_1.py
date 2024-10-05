
def d_lish(args):
    args = set(args)
    args_new = ""
    for i in args:
        if i.isalpha():
            args_new += i
        else:
            None
    return args_new

first_phrase = input("First_phrase =>").lower()
second_phrase = input("Second phrase 2=>").lower()
result = True
first_phrase, second_phrase = d_lish(first_phrase), d_lish(second_phrase)
if first_phrase.isalpha() and second_phrase.isalpha():
    for i in set(second_phrase):
        if i in set(first_phrase):
            None
        else:
            result = False
    if result == True:
        print(set(first_phrase), "\n", "You can create new phrase\n", set(second_phrase))

    if result == False:
        print(set(first_phrase), "\n", "You can not create new phrase\n", set(second_phrase))
else:
    print("Please input correct information")
