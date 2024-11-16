print("Welcome to task 1!")
# Введення даних
while True:
    name = input("Name (it must begin with an uppercase letter). Please enter your name here: ") 
    if name.isdigit() or not name[0].isupper():
        print("Name cannot contain digits and other symbols and must begin with uppercase letter only!")
    else:
     surname = input("Surname (it must begin with an uppercase letter). Please enter your surname here: ")
     if surname.isdigit() or not surname[0].isupper():
        print("Surname cannot contain digits and other symbols and must begin with uppercase letter only!")
     else:
      telephone = input("Telephone number (it must have 10 digits). Please enter your telephone number: ")
      if telephone.isalpha() or len(telephone) != 10: 
         print("Telephone number cannot contain letters and must have 10 digits!")
      else:
       street = input("Street (it must begin with an uppercase letter). Please enter your street name: ")
       if street.isdigit() or not street[0].isupper():
        print("Street name cannot contain digits and other symbols and must begin with uppercase letter only!")
       else:
        building = input("Building number (it must conain only digits). Please enter your buildning number: ")
        if building.isalpha():
         print("Building number cannot contain letters!")
        else:
         apps = input("Appartment number  (it must contain only digits). Please enter your appartment number: ")
         if apps.isalpha():
          print("Appartment number cannot contain letters!")
         else:
          city = input("City (it must begin with uppercase letter). Please enter your city: ")
          if city.isdigit() or not city[0].isupper():
           print("City name cannot contain digits and other symbols and must begin with uppercase letter only!")
          else:
           post_index = input("Post index (it must contain only digits). Please enter your post index: ")
           if post_index.isalpha():
            print("Post index cannot contain letters!")
           else:
            country = input("Country (it must begin with uppercase digits). Please enter your country: ")
            if country.isdigit() or not country[0].isupper():
             print("Country name cannot contain digits and must begin with uppecase letter only!")
            else:
             break 
print(name, surname) # Виведення даних
print(telephone)
print("Str." + (street) + (building) + ", ap." + (apps) + "," + (city))
print(post_index)
print(country)