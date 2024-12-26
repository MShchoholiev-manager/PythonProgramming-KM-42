first_phrase =set(str(input('Enter the first phrase: ')).lower())#create a set
second_phrase =set(str(input('Enter the second phrase: ')).lower())
exception=[' ']
modified_first_phrase={''}
modified_second_phrase={''}
for number in range(0,10):
    exception.append(str(number))
for element in list(first_phrase):#create a set without unnecessary elements
    if element not in exception :
        modified_first_phrase.add(element)
for element in list(second_phrase):
    if element not in exception:
        modified_second_phrase.add(element)
possibility = True#check whether it is possible to make the second phrase from the first
for element in modified_second_phrase:
    if element not in modified_first_phrase:
        possibility = False
        break
if possibility:
    print('It is possible to make the second phrase from the first')
else:
    print('It is impossible to make the second phrase from the first')