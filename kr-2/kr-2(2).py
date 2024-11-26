def counter(lst, element):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += counter(item, element)
        elif item == element:
            count += 1
    return count

lst = input("Enter list: ")
element = input("Enter the element to be found: ")
print(counter(lst, element))
