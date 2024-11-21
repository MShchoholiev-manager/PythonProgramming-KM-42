from datetime import datetime

data = [
    ("Post code", "Cost, thousands USD", "Country", "City", "Street", "Build.", "App.", "Date"),
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, datetime(2010, 10, 10, 10)),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33)),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143)),
]
print(f'''|{data[0][0]:^11}|{data[0][1]:^21}|{data[0][2]:^11}|{data[0][3]:^12}|{data[0][4]:^21}|{data[0][5]:^8}|{data[0][6]:^6}|{data[0][7]:^28}|
|{"-"*11}+{"-"*21}+{"-"*11}+{"-"*12}+{"-"*21}+{"-"*8}+{"-"*6}+{"-"*28}|
| {data[1][0]:<10}|{round(data[1][1], 3):>20} | {data[1][2]:<10}| {data[1][3]:<11}| {data[1][4]:<20}|{data[1][5]:>7} |{data[1][6]:>5} |{data[1][7].strftime('%Y-%m-%dT%H:%M:%S.%f%z'):^28}|
| {data[2][0]:<10}|{round(data[2][1], 3):>20} | {data[2][2]:<10}| {data[2][3]:<11}| {data[2][4]:<20}|{data[2][5]:>7} |{data[2][6]:>5} |{data[2][7].strftime('%Y-%m-%dT%H:%M:%S.%f%z'):^28}|
| {data[3][0]:<10}|{round(data[3][1], 3):>20} | {data[3][2]:<10}| {data[3][3]:<11}| {data[3][4]:<20}|{data[3][5]:>7} |{data[3][6]:>5} |{data[3][7].strftime('%Y-%m-%dT%H:%M:%S.%f%z'):^28}|
| {data[4][0]:<10}|{round(data[4][1], 3):>20} | {data[4][2]:<10}| {data[4][3]:<11}| {data[4][4]:<20}|{data[4][5]:>7} |{data[4][6]:>5} |{data[4][7].strftime('%Y-%m-%dT%H:%M:%S.%f%z'):^28}|
| {data[5][0]:<10}|{round(data[5][1], 3):>20} | {data[5][2]:<10}| {data[5][3]:<11}| {data[5][4]:<20}|{data[5][5]:>7} |{data[5][6]:>5} |{data[5][7].strftime('%Y-%m-%dT%H:%M:%S.%f%z'):^28}|

      ''')