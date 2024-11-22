#-------------------------------------------------------------------------------------------------------
#СПИСКИ, ЩО ЗНАДОБЛЯТЬСЯ ЗГОДОМ

biggest_result_male = []
biggest_result_female = []
dict_fem = []
dict_male = []
female_name_set = set()
male_name_set = set()

#-------------------------------------------------------------------------------------------------------
#РОЗКРИТТЯ УСІХ ФАЙЛІВ / СТВОРЕННЯ МНОЖИНИ УСІХ ІМЕН 

for n in range(1880, 2020):
    dict_fem.clear()
    dict_male.clear()

    with open(f"yob{n}.txt") as file:
        for line in file:
            line = list(line.split(","))
            line = [n.strip() for n in line]

            if line[1] == "F":
                female_name_set.add(line[0])
                female_name = line[0]
                female_number = int(line[2])
                female = [female_number, female_name]
                dict_fem.append(female)

            if line[1] == "M":
                male_name_set.add(line[0])
                male_name = line[0]
                male_number = int(line[2])
                male = [male_number, male_name]
                dict_male.append(male)

    dict_fem.sort(reverse=True)
    dict_male.sort(reverse=True)

    biggest_result_female.append(dict_fem[0])
    biggest_result_male.append(dict_male[0])

#-------------------------------------------------------------------------------------------------------
#РОЗРАХУНОК ТА ВИВІД НАЙПОПУЛЯРНИШИХ ЖІНОЧИХ ІМЕН

print("\nНайпопулярніші жіночі імена в період з 1880 до 2019 року:")

biggest_names_female = []
result_list_female = []

female_name_list = list(female_name_set)

for elem in biggest_result_female:
    elem = elem[1]
    biggest_names_female.append(elem)

for name in female_name_list:
    y = biggest_names_female.count(name)
    if y > 1:
        result = [y, name]
        result_list_female.append(result)
        
result_list_female.sort(reverse=True)

for final_female_result in result_list_female:

    print(final_female_result[1], final_female_result[0])

#-------------------------------------------------------------------------------------------------------
#РОЗРАХУНОК ТА ВИВІД НАЙПОПУЛЯРНИШИХ ЧОЛОВІЧИХ ІМЕН

print("\nНайпопулярніші чоловічі імена в період з 1880 до 2019 року:")

biggest_names_male = []
result_list_male = []

male_name_list = list(male_name_set)

for elem in biggest_result_male:
    elem = elem[1]
    biggest_names_male.append(elem)

for name in male_name_list:
    y = biggest_names_male.count(name)

    if y > 1:
        result = [y, name]
        result_list_male.append(result)
        
result_list_male.sort(reverse=True)

for final_male_result in result_list_male:

    print(final_male_result[1], final_male_result[0])

#-------------------------------------------------------------------------------------------------------
