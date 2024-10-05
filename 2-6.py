index = {
    "X":"Nunavut or Northwest Territories",
    "A":"Newfoundland",
    "B":"Nova Scotia",
    "C":"Prince Edward Island",
    "E":"New Brunswick",
    "G":"Quebec",
    "H":"Quebec",
    "J":"Quebec",
    "K":"Ontario",
    "L":"Ontario",
    "M":"Ontario",
    "N":"Ontario",
    "P":"Ontario",
    "R":"Manitoba",
    "S":"Saskatchewan",
    "T":"Alberta",
    "V":"British Columbia",
    "Y":"Yukon",
  }

while True:
    location = input("Input your location:")
    location = location.upper()
    address = tuple(location)
    if len(address) == 3:
        if address[0].isalpha() and address[1].isdigit() and address[2].isalpha():
            print(f"Locaion: {location}")
            try:
                value = address[0]
                print(f"You are in province: {index[value]}")
            except KeyError:
                print("Frong location!")
            number = address[1]
            if number == "0":
                print("In country")
                break
            if number == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9":
                print("In town")
            break
        else:
            print("Frong location!")
    else:
        print ("Frong location!")