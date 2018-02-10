'''Stage 2
Extend to program to give hi-lo hints. If the guess is wrong and is larger than the secret number, print "Wrong! Too high. Try again: ". It it is wrong and less than the secret number, print "Wrong! Too low. Try again: ".'''

secret_number = 6
while True:
    guess = int(input("guess a number"))
    if guess < secret_number:
        print("Wrong! Too low. try again")
    elif guess > secret_number:
        print("Wrong! Too high. Try again.")    
    else:
        print("You win")
        break
        