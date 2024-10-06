base_count = 100
addition1 = 50
extra_fee = 2

while True:
    minutes = float(input("Будь ласка, введіть тривалість розмов (у хвилинах) з користувачами інших мобільних операторів: "))
    ex_time = minutes - 100
    ex_total = base_count + addition1 + extra_fee * ex_time
    if 0 <= minutes <= 50 :
        print(f"Загальна сума до сплати за місяць становить: {base_count}")
        break
    elif 50 < minutes <= 100 :
        print(f"Загальна сума до сплати за місяць становить: {base_count + addition1}")
        break
    elif minutes > 100 :
        print(f"Загальна сума до сплати за місяць становить: {ex_total}")
        break
    else: 
        print("Помилка, введіть додатне число!")
        
    