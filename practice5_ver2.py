print("Welcome to task 5!")
while True:
    fruits = input("Enter some fruits separated by commas: ")
    if not fruits or fruits.isdigit():
        print("Try again! Enter at least one fruit, please.")
    else:
        fruits_list = fruits.split(",")
        for i in range(len(fruits_list)):
            fruits_list[i] = fruits_list[i].strip()
        if len(fruits_list) == 1:
            output = fruits_list[0]
        elif len(fruits_list) == 2:
            output = fruits_list[0] + " and " + fruits_list[1]
        else: 
            output = ", ".join(fruits_list[:-1]) + " and " + fruits_list[-1]

        print(output)
        break    