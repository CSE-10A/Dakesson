# create a varible and ask the user for a number 1 through 7
day_num = int(input("Enter a number (1-7): "))

# check which number they entered and print the matching day
if day_num == 1:
    print("Monday")
elif day_num == 2:
    print("Tuesday")
elif day_num == 3:
    print("Wednesday")
elif day_num == 4:
    print("Thursday")
elif day_num == 5:
    print("Friday")
elif day_num == 6:
    print("Saturday")
elif day_num == 7:
    print("Sunday")
else:
    # if they enter something outside 1-7, let them know
    print("Invalid input. Please enter a number between 1 and 7.")