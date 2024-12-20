with open('C:/Users/User/Downloads/gadsby.txt', 'r') as f:
    line = f.read()
    newline = line.upper()

    # Ігноруємо все, крім літер
    filtered_text = list(filter(str.isalpha, newline))

    # Порахуємо частоту кожної літери
    letter_counts = {letter: filtered_text.count(letter) for letter in set(filtered_text)}
    total_letters = len(filtered_text)


    for letter in filtered_text:
        letter_counts[letter] += 1

    # Розрахуємо відсотки для кожної літери
    letter_percentages = {
        letter: (count / total_letters) * 100 if total_letters > 0 else 0
        for letter, count in letter_counts.items()
    }
    for letter, count in letter_counts.items():
        letter_percentages[letter] = (count / total_letters) * 100

    # Сортуємо літери за відсотками, але "e" повинна бути в кінці
    sorted_letters = sorted(letter_percentages.items(), key=lambda item: (-item[1], item[0]))

    # Створюємо список з перших 5 та останніх 5 літер
    first_five = sorted_letters[:5]
    last_five = sorted_letters[-5:]

    # Виводимо результат
    for letter, percentage in first_five + last_five:
        print(f"{letter.upper()}: {percentage:.3f}%")
