from datetime import datetime
data = [
    ("Post code", "Cost, thousands USD", "Country", "City", "Street", "Build.", "App.", "Date"),
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, datetime(2010, 10, 10, 10)),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33)),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143)),
]
for line in data:
    (post_code, cost, country, city, street, build, app, dt) = line
    if isinstance(dt, datetime):  # Check if dt is an instance of datetime
        iso_format_time = dt.isoformat(timespec='microseconds') 
    if data.index(line) == 0:
        print(f'|{post_code:^11}|'#create a formatted table
              f'{cost:^21}|'
              f'{country:^11}|'
              f'{city:^12}|'
              f'{street:^20}|'
              f'{build:^8}|'
              f'{app:^6}|'
              f'{dt:^28}|\n'
              '|-----------+---------------------+-----------+------------+--------------------+--------+------+----------------------------|')
    else:
        print(f'| {post_code:<10}|'
              f'{(cost/1000):>20.3f} |'
              f' {country:<10}|'
              f' {city:<11}|'
              f' {street:<19}|'
              f'{build:>7} |'
              f'{app:>5} |'
              f'{iso_format_time:^28}|'
        )