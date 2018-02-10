'''tage 3
Instead of hard-coding your secret number to a fixed number, use a random number generator to pick one for you. To do this, you need make two changes:

Add the line: import random to the top of your program
Where you define your secret variable, instead of setting its value to a number, set its value to random.randint(1, 10) --- this will give you a random number between 1 and 10, inclusive.'''
import random
secret_number = random.randint(1,10)
while True:
    guess = int(input("guess a number"))
    if guess < secret_number:
        print("Wrong! Too low. try again")
    elif guess > secret_number:
        print("Wrong! Too high. Try again.")    
    else:
        print("You win")
        break
        