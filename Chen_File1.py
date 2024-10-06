# блоки введення
name = input("Please enter the recipent's first name: ")
surname = input("Please enter the recipent's surname: ")
num_tele = input("Please enter the recipent's phone number: ")
street = input("Please enter the name of street: ")
build_num = input("Please enter the number of building: ")
room_num = input('Please enter the number of the apartment: ')
city = input("Please enter city: ")
index_num = input("Please enter the number of index: ")
country = input("Please enter the country: ")

# блоки виведення
print("\nRecipient's mailing information:")
print(f"Name: {name} {surname}")
print(f"Phone Number: {num_tele}")
print(f"Adress: str.{street} {build_num} ap.{room_num} {city}")
print(f"Index: {index_num}")
print(f"Country: {country}")
