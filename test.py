from time import sleep

print ("All names are in Old Norse")

sleep (2

)

print (" For inputs, DON'T TYPE SYMBOLS!, it will screw up the gaem!")

sleep (2

)



path = input ( )

if path == ("Ormbyrd"):
   
if path == ("Bjornbyrd"):
    print (" You are a Bearborn (Bjorn = bear, Byrð = born) ")
if path == ("Ulfbyrd"):
    print (" You are a Wolfborn (Ulf = wolf, Byrð = born) ")
if path == ("Uxibyrd"):
    print (" You are a Oxborn (Uxi = ox, Byrð = born) ")

sleep (1)
print ("Welcome to Scandinavia. What is your name?")
name = input ( )
sleep (3)
print ("Your name is")
print (name)
sleep (1)
print ("A stranger walks up to you")
print ("The stranger says")
print (" 'Hello adventurer. You don't come from around here do you?' ")
print ("Choose reply:")
print (" Reply 1:")
sleep (1)
print (" I was born in Scandinavia")
sleep (1)
print (" Reply 2:")
sleep (1)
print (" You're right")
sleep (1)
print (" TYPE NUMBER ONLY!")

firstEncounterReply = input ( )
if firstEncounterReply == ("1"):
    print ("You are born in Scandinavia")
    print ("     The stranger says")
    print (" Oh? I'm so sorry")
if firstEncounterReply == ("2"):
    print ("Which country were you born in?")
    print ("Germany,England,Scotland")
    birthLand = input ( )
    if birthLand == ("Germany"):
        print (" You are Gallic")
    if birthLand == ("England"):
        print (" You are Celtic")
    if birthLand == ("Scotland"):
        print (" You are a Scotsman")
    print ("The stranger says something")
    print (" I knew you were from somewhere else, I bet that I can tell!")
    print (" You're from")
    if birthLand == ("Germany"):
        print ("Gaul")
    if birthLand == ("England"):
        print ("Angleland")
    if birthLand == ("Scotland"):
        print ("North Angleland")

sleep (2)

print ("The stranger looks like a man")
print ("The stranger says \"my name is Calder (Harsh and cold waters)\" ")
print ("The stranger asks you a question")
print ("Are you a man or a woman? I'm sorry but my eyesight is poor, and I can't tell")
gender = input ( )
if gender == ("man"):
    print ("So you're male. Thank you for telling me")
if gender == ("woman"):
    print ("So you're female. Thank you for telling me")

sleep (1)
print ("The stranger hands you a teir 1 sword")
print ("Swords are the weakest weapon in their teir. A teir 1 axe is much more powerful than a teir 1 sword")
print ("The teir 1 sword has a damage multiplier of 0.1")
sleep (4)

print ("The combat system works as so. A dice is rolled (On the computer) and depending on what number you get, that is how much damage you do")
print ("A 2 deals 20 damage, at 1x damage multiplier, a 3 deals 30 at 1x, a 4 deals 40 at 1x and a 5 deals 50 at 1x. Dice with higher numbers can be unlocked")
print ("You can keep rolling UNTIL you roll a 1. (In a 12 sided dice, a 1, a 2,so the first sixth")
print ("A 1 forfeits your attack. You can attack at any time to avoid this number")
sleep (10)

print ("Your teir 1 sword will deal 1/10 of the total damge, because the damage multiplier is 0.1")
sleep (2)

print ("Calder shouts!")
print ("    BEHIND YOU!")
print (" A hveðrungr (monster) appeared!")
print (" The hveðrungr has 50 health!")
print ("Now is your turn to attack!")
print ("You have double the hveðrungr's health!")