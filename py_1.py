print("Завдання 1: Enter information about yourself:)\n")

while True:
    name = input("Enter your Name: ") #введення даних
    if not name.isalpha() or not name.istitle():
        print("Please enter your name correctly (start with a capital letter)!")
        continue
    last_name = input("Enter your Last name: ") #введення даних
    if not last_name.isalpha() or not last_name.istitle():
        print("Please enter your last name correctly (start with a capital letter)!")
        continue
    phone_number = input("Enter your phone number: ") #введення даних
    if not phone_number.isdigit():
        print("Please enter your phone number correctly!")
        continue
    street = input("Enter your Street name: ") #введення даних
    if not street.isalpha() or not street.istitle():
        print("Please enter your street name correctly (start with a capital letter)!")
        continue
    house_number = input("Enter your house number: ") #введення даних
    if not house_number.isdigit():
        print("Please enter your house number correctly!")
        continue
    ap_number = input("Enter your apartment number: ") #введення даних
    if not ap_number.isdigit():
        print("Please enter your apartment number correctly!")
        continue
    city = input("Enter the City name: ") #введення даних
    if not city.isalpha() or not city.istitle():
        print("Please enter the city name correctly (start with a capital letter)!")
        continue
    index = input("Enter your post index: ") #введення даних
    if not index.isdigit():
        print("Please enter your post index correctly!")
        continue
    country = input("Enter the name of the Country: ") #введення даних
    if not country.isalpha() or not country.istitle():
        print("Please enter the name of the country correctly (start with a capital letter)!")
        continue
    break
print(name, last_name + "\n" + phone_number + "\n" + "Str." + street, house_number + ",", "ap." + ap_number + ',', city + "\n" + index + "\n" + country) #виведення даних
print("\nDone")


