'''Guess A Number Game
You will write a guess-a-number game, where the player repeatedly guesses numbers between 1 to 10 until they guess your secret number. You will implement this game in these stages:

Stage 1
Create a secret variable and set its value to your secret number --- pick a number between 1 and 10. Use a while loop to repeatedly ask the player for a guess. If the guess matches the secret number, print "You win!", and end the loop. If the guess is wrong, print "Wrong! Try again: " and ask for another guess.'''

secret_number = 6
guess = int(input("guess a number"))
while guess != secret_number:
    print("wrong")
    guess = int(input("Pick again"))
print("You win")