#------------------------------------------------------------------- #СПИСОК РОКІВ З 1900 ДО 2024 (МОЖНА ЗАМІНЯТИ)

import numpy as np

years = np.arange(1900, 2020+5, 1)

#------------------------------------------------------------------- #ФУНКЦІЯ, ЩО РОЗРАХОВУЄ ЧИ РІК ВИСОКОСНИЙ

def leap_years(list1, x):
    global l  # ЗМІНА l СТВОРЕНА ДЛЯ ТОГО ЩОБ ЗВ'ЯЗАТИ ФУНКЦІЮ "leap_years(list1, x)" ТА "month(y)"
    l = 2
    if x in range(1900, 2025):
        list1 = list(list1)
        y400 = list(filter(lambda i: (i / 400) == int(i / 400), list1))
        y100 = list(filter(lambda r: r % 100, list1))
        y4 = list(filter(lambda l: l / 4 == int(l / 4), y100))
        leap_years = (y4 + y400)
        if x in leap_years:
            type_year = print ("Високосний")
            l = 1
        else:
            type_year = print ("Не високосний")
            l = 0
    if l == 2:
        type_year = print("Обрано невірне значення року")
    return type_year

#-------------------------------------------------------------------  #ФУНКЦІЯ, ЩО РОЗРАХОВУЄ КІЛЬКІСТЬ ДНІВ У МІСЯЦІ

def month(y):
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    days_28or29 = [2]
    if l == 2:
        pr = print("Не вдалося визначити кількість днів")
        y = 0
    if y in range(1, 13):
        if y in days_31:
            pr = print("31 День")
        if y in days_30:
            pr = print("30 День")
        if y in days_28or29:
            if l == 1:
                pr = print("29 Днів")
            if l != 1:
                pr = print("28 Днів")
    return pr

#-------------------------------------------------------------------  #ФУНКЦІЯ ВИЩОГО ПОРЯДКУ

def apply(func_y, y, func_x, list1, x):
    print(f"Обраний рік ({x}):")
    func_x(list1, x)
    print(f"Кількість днів в обраному місяці ({y}):")
    func_y(y)

#-------------------------------------------------------------------  #ЗАПУСК ФУНКЦІЇ 

try:
    j = int(input("Оберіть рік за його номером (1900 - 2024):\n "))
    i = int(input("Оберіть місяць за його номером (1 - 12):\n "))

    apply(month, i, leap_years, years, j)

except:  #ПЕРЕВІРКА НА БУДЬ-ЯКІ ПОМИЛКИ
    pass 