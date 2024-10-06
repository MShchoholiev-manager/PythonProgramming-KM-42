def order_list(items):
    if len(items) > 1:
        return ', '.join(items[:-1]) + ' and ' + items[-1]
    return items[0]

items = input("Будь ласка, введіть список елементів, розділених комами(a, b): ").split(', ')
order_output = order_list(items)

print(f"{order_output}")