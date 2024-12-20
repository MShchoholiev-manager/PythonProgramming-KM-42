import csv

with open('Kuzma_Skryabin.csv', 'w', newline='') as csvfile:
    fieldnames = ['song', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'song': 'Kolorova', 'year': 2009})
    writer.writerow({'song': 'Places of Happy People', 'year': 2012})
    writer.writerow({'song': 'Sleep Alone', 'year': 2003})
    writer.writerow({'song': 'Old Photos', 'year': 2005})
    writer.writerow({'song': 'Mom', 'year': 2012})

print('Kuzma_Skryabin.csv')
with open('Kuzma_Skryabin.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    for row in reader:
        print(row['song'], row['year'])