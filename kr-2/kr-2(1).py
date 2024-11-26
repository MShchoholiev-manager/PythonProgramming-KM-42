def try_deconstraction(input_string, separator):
    if not isinstance(input_string, str) or not isinstance(separator, str):
        raise ValueError("The input parameter must be a string")
    
    if input_string == "":
        raise ValueError("The string cannot be empty")
    
    return input_string.split(separator)

input_string = input("Enter string: ")
separator = input("Enter separator: ")
print(try_deconstraction(input_string, separator))