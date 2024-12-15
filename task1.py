import csv
with open('The_Neighbourhood.csv', 'w', newline='') as csvfile:
    fieldnames = ['Song', '              |  Year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'Song': 'Softcore',
                     '              |  Year': '          |  2018'})
    writer.writerow({'Song': 'Reflections',
                     '              |  Year': '       |  2018'})
    writer.writerow({'Song': 'A Little Death',
                     '              |  Year': '    |  2013'})
    writer.writerow({'Song': 'Leaving Tonight',
                     '              |  Year': '   |  2012'})
    writer.writerow({'Song': 'Flawless',
                     '              |  Year': '          |  2013'})
    writer.writerow({'Song': 'R.I.P 2 My Youth',
                     '              |  Year': '  |  2015'})
    writer.writerow({'Song': 'You Get Me so High',
                     '              |  Year': '|  2018'})
    writer.writerow({'Song': 'Compass',
                     '              |  Year': '           |  2018'})
    writer.writerow({'Song': 'Scary Love',
                     '              |  Year': '        |  2018'})
    writer.writerow({'Song': 'Cry Baby',
                     '              |  Year': '          |  2015'})

print('One of my favorite groups is The Neighbourhood, this file contain some of songs I like.\n------------------------------')    
with open('The_Neighbourhood.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    for row in reader:
        print(row['Song'], row['              |  Year'])
print('Done')