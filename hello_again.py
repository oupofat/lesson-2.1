'''Hello Again?
Write a program to:

Ask the user for their name.
Say a greeting to them. (Phrase of your choice)
Repeat starting from #1, unless they typed "Nobody" as their name.
If they typed "Nobody" as their name, end the program saying nothing.'''

while True:
    name = input("whats your name?")
    print ("hello there",name,".")
    while name !="nobody":
        break