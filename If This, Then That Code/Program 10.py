# the secret number the user has to guess
secret_number = 7

# keep asking until they get it right
while True:
    # ask for a guess
    guess = int(input("Guess a number between 1 and 9: "))

    # check if the guess is correct
    if guess == secret_number:
        print("Well guessed!")
        break  # exit the loop since they got it right
    else:
        # tell them to try again
        print("Wrong guess, try again!")