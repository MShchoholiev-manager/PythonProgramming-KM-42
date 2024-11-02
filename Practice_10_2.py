import numpy as np

years = np.arange(1900, 2020+5, 1)

def jumpy(years):
    result = list(filter(lambda i: i % 4 == 0, (filter(lambda i: i % 400, years))))
    return result

def quentity(jumpy, month, year):

    months_days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }
    if month == 2:
        if year in jumpy:
            return months_days[month] + 1
        else:
            return months_days[month]
    else:
        return months_days[month]


while True:
    try:
        print("year -> (1900 <= year <= 2025)")
        year = int(input("year: "))
        if year >= 1900 and year <=  2025:
            break
        else:
            print("Write correct year")
    except ValueError:
        print("Input correct symvol")

while True:
    try:
        print("month -> (1 <= month <= 12)")
        month = int(input("month: "))
        if month >= 1 and month <= 12:
            break
        else:
            print("Write correct month")
    except ValueError:
        print("Input correct symvol")


print("jumpy years -> ", jumpy(years))
print("days -> ", quentity(jumpy(years), month, year))