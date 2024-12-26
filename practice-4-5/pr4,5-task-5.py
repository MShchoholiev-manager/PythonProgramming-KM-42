while(True):
    try:
        list = input('Enter the items in the list: ').split()#create a list and separate the last item for the word "and"
        last_element = list.pop(-1)
    except IndexError:
        print('Enter at least one item')
        continue
    break
if len(list) == 0:
    print(last_element)#one element doesn't need a coma or "and"
else:#for more than one item, you need "and" or coma.
    string = ", ".join(list)
    string += ' and ' + last_element
    print(string)