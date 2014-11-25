guessed == False
number = 
noOfTurns = 0

while guessed == False:
    noOfTurns = noOfTurns + 1
    guess = input(int("Please enter your guess number: "))
    if guess == True:
        guessed == True
    elif guess > number:
        print("The number you guessed is too high")
    else:
        print("The number you guessed is too low")
        
    guessed == True

print("You took {0} turns to guess the number".format(noOfTurns))
print("The number was {1}".format(number))
