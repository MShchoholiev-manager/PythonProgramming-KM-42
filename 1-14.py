import csv

with open('linkin_park.csv', 'w', newline='') as csvfile:
    fieldnames = ['song', 'year']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    

    writer.writerow({'year': 2003, 
                     'song': 'Numb'})  
    writer.writerow({'year': 2024, 
                     'song': 'Heavy Is the Crown'})
    writer.writerow({'year': 2001, 
                     'song': "In the End"})
    writer.writerow({'year': 2024, 
                     'song': 'Emptiness Machine'})
    writer.writerow({'year': 2007, 
                     'song': "What I've done"})
    writer.writerow({'year': 2003, 
                     'song': 'Faint'})
    writer.writerow({'year': 2012, 
                     'song': 'Burn it Down'})
    writer.writerow({'year': 2003, 
                     'song': 'Breaking the Habit'})
    writer.writerow({'year': 2000, 
                     'song': 'Papercut'})  
    writer.writerow({'year': 2000, 
                     'song': 'One Step Closer'})  



with open('linkin_park.csv', newline='') as csvfile:
    
    reader = csv.DictReader(csvfile)
    
    n = 0

    for heading in reader.fieldnames:
        print(heading, end=' ')
    print('\n------------------------------')
    
    for row in reader:
        n += 1
        print(f"{n}. {row['song']} ({row['year']})")   