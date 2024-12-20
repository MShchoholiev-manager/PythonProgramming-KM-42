print('\nКурс "Програмування на мові Python" \n')
print("Практичні зайняття №4-5 \n")
print('Тема: "Перші програми на Python. Введення та виведення даних. Інструкція if. Цикли. Робота зі списками" \n')
print("Завдання №4")

def format_list(items):
    if not items: 
        return ""
    elif len(items) == 1: 
        return items[0]
    elif len(items) == 2:  
        return f"{items[0]} and {items[1]}"
    else: 
        return ", ".join(items[:-1]) + " and " + items[-1]
input_string = input("\nEnter items separated by commas: ")
items = [item.strip() for item in input_string.split(",")]
formatted_string = format_list(items)
print("\n", formatted_string, "\n")


