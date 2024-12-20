from factorial.factorial import fact
from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from logarithm.logarithm import log, ln, lg

def main():
    while True:
        print("\n==== Menu ====")
        print("1. Factorial")
        print("2. Square / Cube")
        print("3. Square Root / Cube Root")
        print("4. Logarithms")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        try:
            if choice == "1":
                n = int(input("Enter a natural number: "))
                print(f"Factorial of {n} is {fact(n)}")
                
            elif choice == "2":
                x = float(input("Enter a number: "))
                print(f"Square of {x} is {exp2(x)}")
                print(f"Cube of {x} is {exp3(x)}")
                
            elif choice == "3":
                x = float(input("Enter a positive number: "))
                print(f"Square root of {x} is {root2(x)}")
                print(f"Cube root of {x} is {root3(x)}")
                
            elif choice == "4":
                print("1. Logarithm (log_a(b))")
                print("2. Natural Logarithm (ln)")
                print("3. Common Logarithm (lg)")
                log_choice = input("Choose an option (1-3): ")

                if log_choice == "1":
                    a = float(input("Enter base (a > 0 and a != 1): "))
                    b = float(input("Enter number (b > 0): "))
                    print(f"log_{a}({b}) = {log(a, b)}")
                    
                elif log_choice == "2":
                    b = float(input("Enter number (b > 0): "))
                    print(f"ln({b}) = {ln(b)}")
                    
                elif log_choice == "3":
                    b = float(input("Enter number (b > 0): "))
                    print(f"lg({b}) = {lg(b)}")
                    
                else:
                    print("Invalid choice!")
                    
            elif choice == "5":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please select a valid option.")
                
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()