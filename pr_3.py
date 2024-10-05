xv = int(input("How many minutes do you have: "))
money_spend = 0
if xv < 0:
    print("Incorrect information")
elif xv == 0:
    print(money_spend)
else: 
    money_spend += 100
    xv = xv - 50
    if xv > 0:
        money_spend += 50
        xv = xv - 50
        if xv > 0:
            money_spend += xv * 2
    print(money_spend)