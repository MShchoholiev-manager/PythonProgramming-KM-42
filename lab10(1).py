print("Welcome to task 1!\n")  # Welcome message
salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]  # Original salary list

def funct():
    # Calculate new salaries by increasing each by 30%
    new_salary_list = list(map(lambda i: round(i * 1.3, 2), salary_list))
    # Calculate the difference between new and original salaries
    difference = list(map(lambda i, j: round(i - j, 2), new_salary_list, salary_list))
    print("Salary table: ")  # Print table header
    # Print original, new, and difference salaries
    result = list(map(lambda i, j, l: print(i, j, l), salary_list, new_salary_list, difference))

def apply(fun):
    return fun  # Apply the function

apply(funct())  # Execute the function

