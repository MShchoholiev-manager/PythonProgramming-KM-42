import fileinput
import re

lst = list()

with fileinput.input(files=(f'yob{i}.txt' for i in range(1880, 2020))) as f:
    for line in f:
        lst.append((fileinput.filename(), line))
    
group_of_file = dict()

for filename, line in lst:
    if filename not in group_of_file:
        group_of_file[filename] = []
    group_of_file[filename].append(line)
    
popular_male_names = list()  
popular_female_names = list()  

restring = re.compile(r'^([^,]+),([MF]),(\d+)$')

for filename, lines in group_of_file.items():
    male_names = dict()
    female_names = dict()

    for line in lines:
        match = restring.match(line)
        if match:
            name = match.group(1)  
            gender = match.group(2)  

            if gender == 'M':
                male_names[name] = male_names.get(name, 0) + 1
            elif gender == 'F':
                female_names[name] = female_names.get(name, 0) + 1

    if male_names:
        popular_male_names.append(max(male_names, key=male_names.get))
    if female_names:
        popular_female_names.append(max(female_names, key=female_names.get))
        

def create_a_dict(lst):
    dict1 = {}
    
    for name in lst:
        if name not in dict1:
            dict1[name] = 0
            
        dict1[name] += 1
        
    return dict1

popular_male_names_dict = create_a_dict(popular_male_names)  
popular_female_names_dict = create_a_dict(popular_female_names)

def print_loop(dict1):
    for name, years in sorted(dict1.items(), key=lambda x: -x[1]):
        print(f"{name}: {years}")

print("'''")
print_loop(popular_male_names_dict)
print("'''")

print("\n'''")
print_loop(popular_female_names_dict)
print("'''")          