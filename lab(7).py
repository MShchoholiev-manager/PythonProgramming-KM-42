from datetime import datetime
print("Welcome!")
data = [
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, datetime(2010, 10, 10, 10)),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33)),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143)),
]

print(f"|{'Post code':^13}|{'Cost, thousands USD':^23}|{'Country':^13}|{'City':^15}|{'Street':^20}|{'Build.':^10}|{'App.':^10}|{'Date':^30}|")
print(f"|{'-' * 13}+{'-' * 23}+{'-' * 13}+{'-' * 15}+{'-' * 20}+{'-' * 10}+{'-' * 10}+{'-' * 30}|")


for line in data:
    (post_code, cost, country, city, street, build, app, date) = line 
    datetime_iso = date.isoformat(timespec="microseconds")
    print(f"|{post_code:>6}{" ":<7}|{round(cost/1000, 3):>22.3f}{" ":<1}|{" ":>1}{country:<12}|{" ":>1}{city:<14}|{" ":>1}{street:<19}|{build:>9}{" ":<1}|{app:>9}{" ":<1}|{" ":>1}{datetime_iso:<29}|")
