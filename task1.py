print('\nЗавдання 1:')

while True: 

 name = input('Write here recipient\'s name:')
 if not name.isalpha() or not name.istitle():
       print('Invalid input/Write recipient\'s name with capital letter at the beginning just after <:>.')
       continue

 
 surname = input('Write here recipient\'s surname:')
 if not surname.isalpha or not surname.istitle():
      print('Invalid input/Write recipient\'s surname with capital letter at the beginning just after <:>.')
      continue


 phone_number = input('Write here recipient\'s phone number:')
 if not phone_number.isdigit():
     print('Write here only integer numbers')
     continue
  
 street = input('Write here recipient\'s street:')
 if not street.isalpha() or not street.istitle():
     print('You need to write here only letters and begin with capital letter.')
     continue
 street_number = input('Write here recipient\'s street number')
 if street_number.isalpha():
     print('Write here only integer numbers.')
     continue
 
 apartment_number = input('Write here recipient\'s apartment number:')
 if not apartment_number.isdigit():
     print('Write here only integer numbers.')
     continue
 
 city = input('Write here recipient\'s city:')
 if not city.isalpha() or not city.istitle():
     print('You need write here only letters, begin with capital letter')
     continue
 
 postcode = input('Write here recipient\'s postcode:')
 if not postcode.isdigit():
     print('You need to write here only integer numbers. Try again.')
     continue
 
 country = input('Write here recipient\'s country:')
 if not country.isalpha or not country.istitle():
     print('You need write here only letters, begin with capital letter')
     continue
 
 print('\n')
 print(name, surname, '\n')
 print(phone_number,'\n')
 print( 'Str.',street, street_number, apartment_number, city, '\n' )
 print(postcode,'\n' )
 print(country)
 break