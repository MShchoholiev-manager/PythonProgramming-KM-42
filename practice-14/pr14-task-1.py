import csv

with open('radiohead.csv', 'w+', newline='') as csvfile:
    fieldnames = ['Song', 'Year']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    songs_dict = {
        'Creep': '1993',
        'No Suprises': '1997',
        'Airbag': '1997',
        'Like Spinning Plates': '2000',
        'Pyramid Song': '2001',
        'A Wolf at the Door': '2003',
        '2+2=5': '2004',
        'Nude': '2007',
        'Harry Patch (In Memory Of)': '2009',
        'Daydreaming': '2016' 
    }
    
    for key, value in songs_dict.items():
        writer.writerow({
            'Song': f'{key}',
            'Year': f'{value}'
        })
    
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    print("radiohead.csv")
    print('-' * 34)
    print(f"|{reader.fieldnames[0]:<26}|{reader.fieldnames[1]:<5}|")
    print('-' * 34)    
        
    for row in reader:
        print(f'|{row['Song']:<26}|', f'{row['Year']:<4}|',)