print("\n\tWelcome to the lab 7.\n")

from datetime import datetime
data = [
    ("Post code", "Cost, thousands USD", "Country", "City", "Street", "Build.", "App.", "Date"),
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, datetime(2010, 10, 10, 10)),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33)),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143)),
]



data1 = data[0]

data2 = data[1]
isof1 = data2[7].isoformat(timespec="microseconds")

data3 = data[2]
isof2 = data3[7].isoformat(timespec="microseconds")

data4 = data[3]
isof3 = data4[7].isoformat(timespec="microseconds")

data5 = data[4]
isof4 = data5[7].isoformat(timespec="microseconds")

data6 = data[5]
isof5 = data6[7].isoformat(timespec="microseconds")

symbol = '-'

print(f"""|{data1[0]:^16}|{data1[1]:^22}|{data1[2]:^16}|{data1[3]:^16}|{data1[4]:^21}|{data1[5]:^13}|{data1[6]:^10}|{data1[7]:^29}|
|{symbol * 16}+{symbol * 22}+{symbol * 16}+{symbol * 16}+{symbol * 21}+{symbol * 13}+{symbol * 10}+{symbol * 29}|
| {data2[0]:<15}|{round(data2[1]/1000, 3):>21} | {data2[2]:<15}| {data2[3]:<15}| {data2[4]:<20}|{data2[5]:>12} |{data2[6]:>9} |{isof1:^29}|
| {data3[0]:<15}|{round(data3[1]/1000, 3):>21} | {data3[2]:<15}| {data3[3]:<15}| {data3[4]:<20}|{data3[5]:>12} |{data3[6]:>9} |{isof2:^29}|
| {data4[0]:<15}|{round(data4[1]/1000, 3):>21} | {data4[2]:<15}| {data4[3]:<15}| {data4[4]:<20}|{data4[5]:>12} |{data4[6]:>9} |{isof3:^29}|
| {data5[0]:<15}|{round(data5[1]/1000, 3):>21} | {data5[2]:<15}| {data5[3]:<15}| {data5[4]:<20}|{data5[5]:>12} |{data5[6]:>9} |{isof4:^29}|
| {data6[0]:<15}|{round(data6[1]/1000, 3):>21} | {data6[2]:<15}| {data6[3]:<15}| {data6[4]:<20}|{data6[5]:>12} |{data6[6]:>9} |{isof5:^29}|
""")

print("\tDone!\n")