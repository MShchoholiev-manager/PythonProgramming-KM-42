print("\nLab 6, task2: Post index.\n")


province_dictionary = { #creating a dictionary that contains provinces and their index
    "A": "Newfoundland",
    "B": "Nova Scotia",
    "C": "Prince Edward Island",
    "E": "New Brunswick",
    "G": "Quebec",
    "K": "Ontario",
    "R": "Manitoba",
    "S": "Saskatchewan",
    "T": "Alberta",
    "V": "British Columbia",
    "X": "Nunavut/Northwest Territories",
    "Y": "Yukon"}



while True:
    post_index = input("Enter the post index (3-character string: first and third must be a letter, second must be a number): ").upper()

    if len(post_index) == 3 and post_index[0].isalpha() and post_index[1].isdigit() and post_index[2].isalpha(): #checking if the index has 3 characters
        let1 = post_index[0]

        if let1 in province_dictionary: #checking if first letter is the letter from the dictionary
            if post_index[1] == '0': #if second character is 0 it's a countryside
                location = "Countryside"
            else: #if second character is any other number it's a city
                location = "City"

            province = province_dictionary[let1]
            break
        else:
            print("First letter is incorrect")
    else:
        print("Try again")
        
print(f"You entered: {post_index}") #value entered by the user
print(f"Location type: {location}") #second character value
print(f"Province: {province}") #first character value
print("\nDone\n")