print("Welcome to task 2!")
male = {}
female = {}
for year in range(1880,2020):
    with open(f"yob{year}.txt", "r") as files:
        m_max = (None, 0)
        f_max = (None, 0)
        for line in files:
            name,sex,number_of_occurrences = line.split(",")
            number_of_occurrences = int(number_of_occurrences)
            if sex == "F" and number_of_occurrences>f_max[1]:
                f_max = (name, number_of_occurrences)
            elif sex == "M" and number_of_occurrences>m_max[1]:
                m_max = (name, number_of_occurrences)

        if m_max[0]:
            if m_max[0] in male:
                male[m_max[0]]+=1
            else:
                male[m_max[0]] = 1
        if f_max[0]:
            if f_max[0] in female:
                female[f_max[0]]+=1
            else:
                female[f_max[0]] = 1
                
sorted_male = sorted(male.items(), key=lambda x: -x[1])
sorted_female = sorted(female.items(), key=lambda x: -x[1])
print()
print("Female names:\n")
for name, number_of_occurrences in sorted_female:
    print(f"{name} {number_of_occurrences}")
print("\nMale names: \n")
for name, number_of_occurrences in sorted_male:
    print(f"{name} {number_of_occurrences}")


