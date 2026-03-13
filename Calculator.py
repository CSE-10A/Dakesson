 
print("Your Calculator!")
print("-----------------------------------")
 
# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
 
# Ask the user what operation they want
print("\nWhat do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
 
choice = input("\nEnter your choice (1/2/3/4): ")
 
# Do the math based on the choice
if choice == "1":
    result = num1 + num2
    print(f"\n{num1} + {num2} = {result}")
 
elif choice == "2":
    result = num1 - num2
    print(f"\n{num1} - {num2} = {result}")
 
elif choice == "3":
    result = num1 * num2
    print(f"\n{num1} x {num2} = {result}")
 
elif choice == "4":
    # Can't divide by zero!
    if num2 == 0:
        print("\nOops! You can't divide by zero.")
    else:
        result = num1 / num2
        print(f"\n{num1} / {num2} = {result}")
 
else:
    print("\nThat's not a valid choice. Please enter 1, 2, 3, or 4.")