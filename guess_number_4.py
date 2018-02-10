'''Stage 4
Make it so that the player can only guess 5 times at most. If they guessed 5 times and still miss, print "You used up all your guesses!".

Hint: you'll need to introduce the loop counter pattern into your code by adding a loop counter, and repeating condition, and a incrementer statement.'''

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
        break
        