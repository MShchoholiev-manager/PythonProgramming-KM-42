print("Welcome to task 1!")
while True:
 s1 = input("Enter some sentence! ").lower()
 if not s1.replace(" ", "").isalpha() == True:
  print("Sentence must contain only letters!")
 else: 
  break
 
while True:
 s2 = input("Enter some another sentence! ").lower()
 if not s2.replace(" ", "").isalpha() == True:
  print("Sentence must contain only letters!")
 else:
  break
 
s11 = set()
for i in s1:
 if i.isalpha():
  s11.add(i)

s21 = set()
for i in s2:
 if i.isalpha():
  s21.add(i)

if s21.issubset(s11):
 print("Yes, we can form second sentence from the first!")
else:
 print("No, we cant form second sentence from the first!")

print("Unique letters of the first sentence", s11)
print("Unique letters of the second sentence", s21)
print("Common letters of two sentences", (s11.intersection(s21)))







 