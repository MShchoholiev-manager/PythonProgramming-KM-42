while(True):
    postal_code = list(str(input("Greetings from Canada Post!\n"
                                 "Please enter the recipient's postal code: ")).upper())
    if len(postal_code) != 3:#verification of the entered data
        print('You entered an invalid postal code!')
        continue
    elif postal_code[0].isalpha() != True:
        print('You entered an invalid postal code!')
        continue
    elif postal_code[1].isdigit() != True:
        print('You entered an invalid postal code!')
        continue
    elif postal_code[2].isalpha() != True:
        print('You entered an invalid postal code!')
        continue
    else:
        exception = ['D','F','I','O','Q','U','W','Z']
        if postal_code[0] in exception:
            print('There are no provinces with this index!You entered an invalid postal code!')
            continue
        else:
            province = {"A":"Newfoundland",
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
                        "X":"Nunavut",
                        "Y":"Yukon"}
            province_addition = {"X":"Northwest Territories"}
            if (postal_code[0] in province) and (postal_code[0] in province_addition):#terrain definition
                if postal_code[1] == '0':
                    print("The parcel will be sent to rural areas of the province ", province[postal_code[0]],' or ',province_addition[postal_code[0]])
                else:
                    print("The parcel will be sent to an urban area of the province ",province[postal_code[0]],' or ',province_addition[postal_code[0]])
            elif postal_code[0] in province:
                if postal_code[1] == '0':
                    print("The parcel will be sent to rural areas of the province ", province[postal_code[0]])
                else:
                    print("The parcel will be sent to an urban area of the province ", province[postal_code[0]])
            break
                    