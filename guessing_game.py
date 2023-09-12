import random

#Guessing game
guess_limit = 3
guess_count = 0
secret_number = random.randint(1, 20)
out_of_guesses = False

try:
    while guess_count < guess_limit:
        your_guess = int(input("Please guess any number less than 20: "))
        if (your_guess==secret_number):
            print ("Congratulations, you guessed right")
            break
        else:
            print("You lose, wrong input")
            guess_count += 1
except:
    pass
finally:
    print(f"The last secret number is: {secret_number}")
    