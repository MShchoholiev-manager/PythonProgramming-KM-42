
import math
while True:
    try:
        a, b, c = [float(i) for i in input("numbers a, b, c: ").split()]
        1 / a
        D = b**2 - 4 * a * c
        try:
            sq = math.sqrt(D)
            if sq > 0:
                print(f"Корень перший {round(((-b + sq) / (a * 2)), 2)}")
                print(f"Корень Другий {round(((-b - sq) / (a * 2)), 2)}")
                break
            if sq == 0:
                print(f"Один корень {round((-b / (a * 2)), 2)}")
                break
        except ValueError:
            print("Дискримінант менше 0")
            break
    except ValueError as ve:
        print(ve)
        print("Ви водите букви замість числа, або в вашій строці менше або більш як 3 числа")
    except EOFError:
        print("Ви намагаєтесь завершити програму комбінацією ctrl Z, не робіть так")
    except ZeroDivisionError:
        print("В знаменнику число буде дорівнювати 0")
    except Exception:
        print("Сталася невідома помилка, спробуйте ще")
    except KeyboardInterrupt:
        print("Комбінація ctrl C не спрацює")
