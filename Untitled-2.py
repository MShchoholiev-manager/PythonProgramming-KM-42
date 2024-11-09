print("\nWelcome to lab 10 task 2!")

import numpy as np

years = np.arange(1900, 2020+5, 1) 
months = np.arange(1, 13, 1) 

while True:
    try:
        year = int(input("Enter the year you want to check (1900-2024): "))
        if year not in years:
            raise ValueError("Enter the correct value!")
        month = int(input("Enter the month (as a number 1-12): "))
        if month not in months:
            raise ValueError("Enter the correct value!")
    except ValueError as e:
        print(e)
        continue 
    break  

def leap_year(y):
    global leap
    leap = 0
    if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
        print(f"{y} is a leap year")
        leap = 1
    else:
        print(f"{y} is not a leap year")
        leap = 2

def days_count(m):
    days28_29 = [2]
    days30 = [4, 6, 9, 11]
    days31 = [1, 3, 5, 7, 8, 10, 12]
    if m in days28_29:
        if leap == 1:
            print("There are 29 days in this month.")
        else:
            print("There are 28 days in this month.")
    elif m in days30:
        print("There are 30 days in this month.")
    elif m in days31:
        print("There are 31 days in this month.")
    else:
        print("Oops")


def apply(fun1, arg1, fun2, arg2):
    fun1(arg1)
    fun2(arg2)


apply(leap_year, year, days_count, month)
print("\nDone!")