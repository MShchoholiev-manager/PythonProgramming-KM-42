print("Welcome to task 1!")
import csv
with open("Alex_G.csv", "w", newline="") as csvfile:
    fieldnames = ["Song", "Year"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Song": "Treehouse   ",
                     "Year": "2011"})
    writer.writerow({"Song": "Race        ",
                     "Year": "2010"})
    writer.writerow({"Song": "Sarah       ",
                     "Year": "2012"})
    writer.writerow({"Song": "Pretend     ",
                     "Year": "2023"})
    writer.writerow({"Song": "Things to Do",
                     "Year": "2010"})
    writer.writerow({"Song": "Let it Go   ",
                     "Year": "2010"})
print("There are some of my favourite songs by Alex G and the year of their release")
print("-------------------------------")
with open("Alex_G.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for heading in reader.fieldnames:
        print(heading, end="         ")
    print("\n-------------------------------")
    for row in reader:
        print(row["Song"], row["Year"])
