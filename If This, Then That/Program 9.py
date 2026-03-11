# get the year from the user
year = int(input("Enter a year: "))

# check the leap year rules
if year % 400 == 0:
    # divisible by 400 = leap year
    print(True)
elif year % 100 == 0:
    # divisible by 100 but not 400 = NOT a leap year
    print(False)
elif year % 4 == 0:
    # divisible by 4 but not 100 = leap year
    print(True)
else:
    # not divisible by 4 at all = NOT a leap year
    print(False)