# ask the user to type one character
char = input("Enter a single character: ")

# check if the character (lowercased just in case) is one of the vowels
if char.lower() in "aeiou":
    print(char, "is a vowel")
else:
    print(char, "is not a vowel")