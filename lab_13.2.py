print('Welcome to lab 11 task 2.\n')

male_popular_names = {}
female_popular_names = {}

for year in range(1880, 2020):
    with open(f'yob{year}.txt', 'r', encoding='utf-8') as f:
        top_male_name = (None, 0)
        top_female_name = (None, 0)

        for line in f:
            name, gend, occurrences = line.strip().split(',')
            occurrences = int(occurrences)

            if gend == 'M' and occurrences > top_male_name[1]:
                top_male_name = (name, occurrences)
            elif gend == 'F' and occurrences > top_female_name[1]:
                top_female_name = (name, occurrences)

        if top_male_name[0]:
            male_popular_names[top_male_name[0]] = male_popular_names.get(top_male_name[0], 0) + 1

        if top_female_name[0]:
            female_popular_names[top_female_name[0]] = female_popular_names.get(top_female_name[0], 0) + 1

sorted_male_names = sorted(male_popular_names.items(), key=lambda x: -x[1])
sorted_female_names = sorted(female_popular_names.items(), key=lambda x: -x[1])

print('  Male names:')
for name, count in sorted_male_names:
    print(f'{name} {count}')

print('\n  Female names:')
for name, count in sorted_female_names:
    print(f'{name} {count}')

print('\nDone!')