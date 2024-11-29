print('Welcome to lab 14 task 1.\n')
print('My favourite singer is Frank Ocean and here are some of his songs and their year of release:')
print('--------------------------------------------------------------------------------------------')
import csv
with open('frank_ocean.csv', 'w', newline='') as csvfile:
    fieldnames = ['Composition   |', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Composition   |': 'Dear April   ',
                     'Year': '2019'})
    writer.writerow({'Composition   |': 'Futura Free  ',
                     'Year': '2016'})
    writer.writerow({'Composition   |': 'White Ferrari',
                     'Year': '2016'})
    writer.writerow({'Composition   |': 'Ivy          ',
                     'Year': '2016'})
    writer.writerow({'Composition   |': 'Bad Religion ',
                     'Year': '2012'})
    writer.writerow({'Composition   |': 'Forrest Gump ',
                     'Year': '2012'})
    
with open('frank_ocean.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------')
    for row in reader:
        print(row['Composition   |'], "|", row['Year'])
