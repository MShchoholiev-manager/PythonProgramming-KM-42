import zipfile

zip_path = 'C:/Users/User/Downloads/archive.zip'

# Створюємо словники для підрахунку кількості разів, коли ім'я ставало найпопулярнішим
male_names_count = {}
female_names_count = {}


with zipfile.ZipFile(zip_path, 'r') as archive:
    for year in range(1880, 2020):
        file_name = f'yob{year}.txt'  
        if file_name in archive.namelist():  
            with archive.open(file_name) as f:
                lines = f.readlines()  

                year_male_names = {}
                year_female_names = {}

                
                for line in lines:
                    
                    line = line.decode('utf-8').strip()  
                    
                    if len(line.split(',')) == 3:
                        name, sex, occurrences = line.split(',')
                        occurrences = int(occurrences)

                        if sex == 'M':
                            if name in year_male_names:
                                year_male_names[name] += occurrences
                            else:
                                year_male_names[name] = occurrences
                        else:
                            if name in year_female_names:
                                year_female_names[name] += occurrences
                            else:
                                year_female_names[name] = occurrences

                if year_male_names:
                    max_male_occurrences = max(year_male_names.values())
                    for name, count in year_male_names.items():
                        if count == max_male_occurrences:
                            if name in male_names_count:
                                male_names_count[name] += 1
                            else:
                                male_names_count[name] = 1

                if year_female_names:
                    max_female_occurrences = max(year_female_names.values())
                    for name, count in year_female_names.items():
                        if count == max_female_occurrences:
                            if name in female_names_count:
                                female_names_count[name] += 1
                            else:
                                female_names_count[name] = 1

sorted_male_names = sorted(male_names_count.items(), key=lambda x: x[1], reverse=True)
sorted_female_names = sorted(female_names_count.items(), key=lambda x: x[1], reverse=True)

print("Male names:")
for name, count in sorted_male_names:
    print(f"{name} {count}")

print("\nFemale names:")
for name, count in sorted_female_names:
    print(f"{name} {count}")


        

    
    
