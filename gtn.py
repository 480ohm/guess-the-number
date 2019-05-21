rom random import randint

print("Guess the Number!\n")
print("The number will be anywhere from 1 to 100.\n")

number = randint(1,100)
num_of_guesses = 0

print(number)

while True:
    num_of_guesses += 1
    guess = input("Guess " + str(num_of_guesses) + ": ")
    try:
        if int(guess) == number:
            if num_of_guesses == 1:
                print("Congratulations! You guessed the number in 1 try!\n")
            else:
                print("Congratulations! You guessed the number in " +
                      num_of_guesses + " tries\n.")
            break
        elif int(guess) < number:
            print("Your guess is too low. Try again.\n")
        elif int(guess) > number:
            print("Your guess is too high. Try again.\n")
    except ValueError:
        print("That is not a valid guess. Please enter a whole number.\n")
