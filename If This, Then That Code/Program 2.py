# get a number from the user
num = int(input("Enter a number: "))

# if the remainder when divided by 2 is 0, it's even
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")