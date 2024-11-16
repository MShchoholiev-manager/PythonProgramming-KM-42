print("Welcome to task 2!")
dictionary = {"A":"Newfoundland",
         "B":"Nova Scotia",
         "C":"Prince Edward Island",
         "E":"New Brunswick",
         "G":"Quebec", "H":"Quebec", "J":"Quebec",
         "K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario",
         "R":"Manitoba",
         "S":"Saskatchewan",
         "T":"Alberta",
         "V":"British Columbia",
         "X":"Nunavut or Northwest Territories",
         "Y":"Yukon"}

while True:
  index = input("Enter post index: ").upper()
  if len(index) == 3 and index[0].isalpha() and index[2].isalpha() and index[1].isdigit():
    first = index[0]
    second = index[1]
    if not first in dictionary:
      print("There is no any province that starts with this letter!")
    else:
      print("The province is", dictionary[first])
      if second == "0":
        print("Province is rural!")
        break
      else: 
        print("Province is urban!")
        break
  else:
   print("Post index must contain 3 symbols! Then the first and third one symbols must be letters and the second one must be digit!")


