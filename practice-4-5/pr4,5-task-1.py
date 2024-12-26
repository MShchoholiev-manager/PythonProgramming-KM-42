while(True):
    print('--------------------------------------------------------------------------------\n'
          '|                      WELCOME TO THE UKRPOSHTA SITE!!                         |\n'
          '--------------------------------------------------------------------------------'
    )
    try:
        toggle = int(input("Enter '1' to  enter the recipient's details\n"
                           "Enter '0' to leave the site\n"
                           "Number "))
    except  ValueError:
        print("Oops..You've entered the wrong number!Try again.")
        continue
    match toggle:
        case 1:
            name = input("Enter the recipient's name: ")#data entry block
            surname = input("Enter the recipient's surname: ")
            phone_number = input("Enter the recipient's phone number: ")
            street = input('Enter the name of the street: ')
            house_number = input('Enter the house number: ')
            apartment_number = input('Enter the apartment number: ')
            city = input("Enter the city/village/: ")
            postcode = input("Enter the recipient's postal code: ")
            country = input('Enter the country: ')
            print("THE RECIPIENT'S DETAILS\n"#data output block
                  '--------------------------------------------------------------------------------\n',
                   name,"",surname,"\n",
                   phone_number,"\n",
                  "Str.",street,"",house_number,", ap.",apartment_number,"",city,"\n",
                   postcode,"\n",
                   country,"\n",
                  '--------------------------------------------------------------------------------'
            )
            while(True):
                try:
                    check = int(input("All details are right,aren't they?\n"#The user could have made a mistake
                                      "Enter '1' to send a parcel\n"
                                      "Enter '0' to change the recipient's details\n"
                                      "Number: "))
                except ValueError:
                    print("Oops..You've entered the wrong number!Try again.")
                    continue
                match check:
                    case 1:
                        print("The recipient's form has been filled in. The parcel will be sent in the soonest future.")
                        break
                    case 0:
                        print("The recipient's form has been deleted. Try again")
                        break
                    case _:
                        print("Oops..You've entered the wrong number!Try again.")
        case 0:
            print('Come back soon!')
            break
        case _:
            print("Oops..You've entered the wrong number!Try again.")