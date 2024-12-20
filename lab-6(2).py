print('\nКурс "Програмування на мові Python"(\n')
print('Практичне зайняття №6\n\nТема: "Робота з кортежами, множинами та словниками"\n')
print("Завдання №2")
province_codes = {
    'A': 'Newfoundland',
    'B': 'Nova Scotia',
    'C': 'Prince Edward Island',
    'E': 'New Brunswick',
    'G': 'Quebec',
    'H': 'Quebec',
    'J': 'Quebec',
    'K': 'Ontario',
    'L': 'Ontario',
    'M': 'Ontario',
    'N': 'Ontario',
    'P': 'Ontario',
    'R': 'Manitoba',
    'S': 'Saskatchewan',
    'T': 'Alberta',
    'V': 'British Columbia',
    'X': 'Nanavut or Northern Territories',
    'Y': 'Yukon'
}


postal_code = input("\nEnter zip code (3 characters): ")


if len(postal_code) != 3 or not postal_code[0].isalpha() or not postal_code[1].isdigit() or not postal_code[2].isalpha():
    print("\nError: Postcode must be in the format 'A0A', where A is a letter and 0 is a number.")
else:
    
    first_char = postal_code[0].upper()
    second_char = postal_code[1]
    
    
    if first_char in province_codes:
        province = province_codes[first_char]
        if second_char == '0':
            area_type = 'rural areas'
        else:
            area_type = 'urban area'
        
        print(f"\nThe addressee is located in {area_type} of the province of {province}.\n")
    else:
        print("\nError: The code you entered does not match any Canadian province.\n")

