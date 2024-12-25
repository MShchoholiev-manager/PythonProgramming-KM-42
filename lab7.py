from datetime import datetime

data = [
    ("Post code", "Cost, thousands USD", "Country", "City", "Street", "Build.", "App.", "Date"),
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, datetime(2010, 10, 10, 10)),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33)),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143)),
]

data0 = data[0]
data1 = data[1]
data2 = data[2]
data3 = data[3]
data4 = data[4]
data5 = data[5]
sym = '-'

rounded_data1 = round(data1[1] / 1000, 3)
rounded_data2 = round(data2[1] / 1000, 3)
rounded_data3 = round(data3[1] / 1000, 3)
rounded_data4 = round(data4[1] / 1000, 3)
rounded_data5 = round(data5[1] / 1000, 3)


print(f"""|{data0[0]:^15}|{data0[1]:^25}|{data0[2]:^15}|{data0[3]:^12}|{data0[4]:^20}|{data0[5]:^10}|{data0[6]:^8}|{data0[7]:^29}|
|{sym * 15}+{sym * 25}+{sym * 15}+{sym * 12}+{sym * 20}+{sym * 10}+{sym * 8}+{sym * 29}|
| {data1[0]:<14}|{rounded_data1 :>24} | {data1[2]:<14}| {data1[3]:<11}| {data1[4]:<19}| {data1[5]:<9}|{data1[6]:>7} |  {datetime.isoformat(data1[7]):<27}|
| {data2[0]:<14}|{rounded_data2 :>24} | {data2[2]:<14}| {data2[3]:<11}| {data2[4]:<19}| {data2[5]:<9}|{data2[6]:>7} |  {datetime.isoformat(data2[7]):<27}|
| {data3[0]:<14}|{rounded_data3:>24} | {data3[2]:<14}| {data3[3]:<11}| {data3[4]:<19}| {data3[5]:<9}|{data3[6]:>7} |  {datetime.isoformat(data3[7]):<19}.000000 |
| {data4[0]:<14}|{rounded_data4:>24} | {data4[2]:<14}| {data4[3]:<11}| {data4[4]:<19}| {data4[5]:<9}|{data4[6]:>7} |  {datetime.isoformat(data4[7]):<19}.000000 |
| {data5[0]:<14}|{rounded_data5:>24} | {data5[2]:<14}| {data5[3]:<11}| {data5[4]:<19}| {data5[5]:<9}|{data5[6]:>7} |  {datetime.isoformat(data5[7]):<27}|
  """)