'''Bonus Challenge 2
When a game is finished --- they either won or ran out of guesses. Given them the option to play again.'''

import random
secret_number = random.randint(1,10)
number_of_guesses = 0
while True:
    number_of_guesses = number_of_guesses +1
    guess = int(input("guess a number"))
    if guess < secret_number:
        print("Wrong! Too low. try again")
    elif guess > secret_number:
        print("Wrong! Too high. Try again.")
    else:
        print("You win")
    if number_of_guesses >= 5:
        print("You used up all your guesses!")
        answer = input("play again?(y or no)")
        if answer == "n":
            break
            print("thanks for playing!")
        
 