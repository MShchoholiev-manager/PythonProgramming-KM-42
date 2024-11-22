print("Введіть свій бал:")
mark = int(input())

if 0<=mark<=60:
    print("Unsatisfactory")

if 60<mark<=65:
    print("Marginal")

if 65<mark<=75:
    print("Satisfactory")

if 75<mark<=85:
    print("Good")

if 85<mark<=95:
    print("Very good")

if 95<mark<=100:
    print("Excellent!")

if mark>100:
    print("Lier!")
    
if mark<0:
    print("HOW")
