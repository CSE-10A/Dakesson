# ask which direction they want to convert
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    # convert Celsius to Fahrenheit using the formula: f = (c * 9/5) + 32
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print(c, "°C is", round(f), "in Fahrenheit")

elif choice == "2":
    # convert Fahrenheit to Celsius using the formula: c = (f - 32) * 5/9
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print(f, "°F is", round(c), "in Celsius")

else:
    print("Invalid choice.")