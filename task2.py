print('\nЗавдання 2:')

while True:
    try:
     rs = int(input('Enter your R score:'))
     if rs < 0:
      print('Enter non-negative integer number.')
    except ValueError:
     print('Enter integer number, not letter.')
    else:
      if rs >= 0 and rs <= 60:
       print(f'Your R score {rs} is: Unsatisfactory.')
       break
      if rs > 60 and rs <= 65:
        print(f'Your R score {rs} is: Marginal.')
        break
      if rs > 65 and rs <= 75:
        print(f'Your R score {rs} is: Satisfactory.')
        break
      if rs > 75 and rs <= 85:
        print(f'Your R score {rs} is: Good.')
        break
      if rs > 85 and rs <= 95:
        print(f'Your R score {rs} is: Very good.')
        break
      if rs > 95 and rs <= 100:
        print(f'Your R score {rs} is: Excellent.')
        break
      if rs > 100:
        print('Your R score can only be less than 100.')
        continue