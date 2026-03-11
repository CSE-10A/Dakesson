# get the integer from the user
n = int(input("Enter an integer: "))

# check the conditions one by one
if n % 2 != 0:
    # odd number is always Weird
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    # even and between 2 and 5
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    # even and between 6 and 20
    print("Weird")
elif n % 2 == 0 and n > 20:
    # even and greater than 20
    print("Not Weird")