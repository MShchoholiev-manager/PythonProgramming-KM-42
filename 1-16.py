from math import sqrt

#-----------------------------------------------------------------------------------------------------------------
#Перевірка значень

def check(a, b, c):
    try:
    
        if (a + b) > c and (a + c) > b and (b + c) > a:
            
            if a > 0 and b > 0 and c > 0:
                return True
            
        return False
    
    except ValueError:
        return False


#-----------------------------------------------------------------------------------------------------------------
#Декоратор

def triangle_ineq(func):
    def inner(a, b, c):
        
        a = float(a)
        b = float(b)
        c = float(c)
        
        if check(a, b, c) == True:
            return func(a, b, c)
        
        else: 
            return "Вказано неправильні значення!"
    
    return inner


#-----------------------------------------------------------------------------------------------------------------
#Розрахунок площі

@triangle_ineq
def area_calculation(a, b, c):
    p = (a + b + c) / 2

    s = p * (p - a) * (p - b) * (p - c)

    return f"S = {round(sqrt(s), 2)}"


#-----------------------------------------------------------------------------------------------------------------
#Інтерфейс користувача

while True:
    try: 
        choice = str(input("Хочете запустити розрахунок площі? (y/n): "))
        
        match choice:
            case "y":
                print("Введіть сторони A, B, C:")
               
                a = input("Сторона A = ")
                b = input("Сторона B = ")
                c = input("Сторона C = ")

                print(area_calculation(a, b, c))
        
            case "n":
                print("Вимикаю!")
                break

            case _:
                raise ValueError

    except:
        print("Щось не так, спробуйте ще раз!")