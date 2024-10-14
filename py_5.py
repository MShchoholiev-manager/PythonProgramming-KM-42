print('Завдання 5: ')

things = [] #creates an empty list

while True: #the start of the loop
    thing = input("Enter the name of some objects (or type '0' to finish): ").strip() #asks to enter some objects
    
    if thing.lower() == '0': #checks if the user's input is equal to 0
        if things: #if there are any objects in list
            if len(things) > 1:
                print(', '.join(things[:-1]) + ' and ' + things[-1]) #print commas between every obj and add and before the last obj
            else:
                print(things[0]) #prints the obj if its the only one
        else:
            print("No objects entered.") #if no obj entered
        break #exit the loop
    
    if thing:
        things.append(thing)
    else:
        print("Try again! Enter at least one object.")
