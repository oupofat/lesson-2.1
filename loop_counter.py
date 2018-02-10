'''Section 2: Loop Counter Pattern
Print the numbers between 1 to 10.
Print the numbers between 40 to 50.
Print the numbers between 1 to 10, but in reverse.
Print the even numbers from 2 to 20.
Ask the user for his name, say hello to him 10 times.
Ask the user for a number, print the numbers from 1 to that number.
Ask the user for a start number and an stop number. Print the numbers starting from the start number and ending at the stop number.'''

counter = 1
while counter <= 10:
    print(counter)
    counter = counter + 1

counter = 40
while counter <= 50:
    print(counter)
    counter = counter + 1
    
counter = 10
while counter >= 1:
    print(counter)
    counter = counter - 1
    
counter = 2
while counter <= 10:
    print(counter)
    counter = counter + 2 
    
counter = 1
user = input("whats your name")
while counter <= 10:
    print("hello")
    counter = counter +1
    
user = int(input("Pick a number?"))
counter = 1
while counter <=user:
    print(counter)
    counter = counter +1

start = int(input("Pick a number to start with?"))
end = int(input("Now pick a number to end with?"))
counter = start
while counter <=end:
    print(counter)
    counter = counter +1