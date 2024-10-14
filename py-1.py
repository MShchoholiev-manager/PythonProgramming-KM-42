print("Lab 6, task 1: Write two sentences to check if we can make the second sentence from the letters of the first sentence.")

while True:
    inp_sent1 = input("Write the first sentence (only letters): ").lower() #input sentences
    inp_sent2 = input("Write the second sentence (only letters): ").lower()

    sent1 = inp_sent1.replace(" ", "") #removing spaces
    sent2 = inp_sent2.replace(" ", "")

    if not sent1.isalpha() or not sent2.isalpha(): #checking if all the symbols are letters
        print("Sentences can't contain any numbers or symbols. Please try again.")
    else:
        break

letters1 = set(sent1) #making the set
letters2 = set(sent2)

if letters2 <= letters1: #checking if the second sentence is a subset of the first sentence.
    print(f"Letters of the first sentence: {letters1}. Letters of the second sentence: {letters2}. We can make the second sentence from the letters of the first sentence.")
else:
    print(f"Letters of the first sentence: {letters1}. Letters of the second sentence: {letters2}. We can't make the second sentence from the letters of the first sentence.")

print("Done")