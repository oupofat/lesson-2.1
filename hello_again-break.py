'''Do Another
Take a program you wrote for a previous assignment. Make it run repeatedly.

After each run of the program, ask the user if they want to run it again. If they typed "y", run the program again, if they typed anything else, exist the program and print "Good bye!"'''


while True:
    name = input("whats your name?")
    print ("hello there",name,".")
    answer = input("Do another? (y or n) ")
    if answer != "y":
            break
print("Good bye!")