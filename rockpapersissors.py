import random

prob = random.random()
print prob

print("Hello")

diceThrow = random.randrange(1,6)
print (diceThrow)
if diceThrow >= 4:
    print("You lost")
if diceThrow <= 3:
    print("You won")
    
    print("Dice is rolling...")
    sleep(3)
    diceThrow = random.randrange(1,10)
    print (diceThrow)
    if diceThrow >= 6:
        print("You won")
    if diceThrow <= 4:
        print("You lost")


    