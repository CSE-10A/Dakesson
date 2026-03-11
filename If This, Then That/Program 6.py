# take two numbers as input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# compare them and print the bigger one
if num1 > num2:
    print("The larger number is:", num1)
elif num2 > num1:
    print("The larger number is:", num2)
else:
    # if they're equal, just let the user know
    print("Both numbers are equal.")
