import random  
from time import sleep


prob = random.random()
print prob
#add sleep(1) to every other line
print ("Hello, Welcome to this world") # Also add more in-depth into the story
sleep (2)
print ("In this world you will be given choices and the decisions will be yours to make ")
sleep(2)
print ("However, there is a catch.")
sleep(2)
print ("The success of your decision will be based on the probability of a dice roll")
sleep(2)
print ("On a 10 sided dice, if you role less than or equal to 4 than your choice will have bad consequences")
sleep(2)
print ("If your role is greater than or equal to 6, then your choice will have the best possible outcome")
sleep(2)
print ("If your role is exactly 5, then your choice will have neutral outcomes. Anything could happen")
sleep(2)
print ("So let's begin...")
sleep(2)
 #timer add later for about 10 seconds
print("You awaken to the sound of explosives and screams in the background. You are troubled with what you are hearing so you decide to turn on the tv to know what is happening")
print("*Type Power to turn on the TV")
Power=raw_input()
sleep (2)
print("The tv won't turn on")
sleep (2)
print("You hear a noise coming from outside")
sleep (2)
print("You decide, out of curiosity, to step outside")
sleep (2)
print("Type Open to open the door")
Open=raw_input()
sleep (2)
print("You have stepped out of your house after hearing a strange noise coming from outside.You step outside and the wind starts to move around you. Out of knowhere an alien has jumped right in front of you. You have three options") 
sleep (2)
print ("A) Run towards it and attack.")
sleep(1)
print("or")
sleep (1)
print ("B) Rush back inside. ")
sleep (2)
print ("SIDENOTE: Type in the exact letter")
d1a = raw_input("What choice will you make [A/B]") 

if d1a == ("A"):  #Add sleep(2) to the lines
    print("So you have chosen to run towards and attack it huh?")
    print ("May the dice be ever in your favor")
    print("Dice is rolling...")
    sleep(3)
    diceThrow = random.randrange(1,10)  
    print (diceThrow)
    if diceThrow >= 6:
        print("Good job")
        sleep (2)
        print("With what little you have left to lose, you charge at the unusual creature") #Add sleeps
        sleep (2)
        print("The alien in turn, charges at you as well")
        sleep (2)
        print("As you two start to approch each other, a sudden smoke screen appears from the ground")
        sleep (2)
        print("Both of you stop as you stare at each other, the creature fades into the smoke")
        sleep (2)
        print("As soon as that happens you feel a hand touching your arm as the hand starts to roughly pull you away from the smoke ")
        sleep (2)
        print("As You and the mysertious figure are hastily running away from the scene Do you...")
        sleep (2)
        print("A: Act hostile and violently towards the stranger ")
        sleep (2)
        print("B: Keep quiet and continue running with the stranger")
        print("SIDENOTE: Type in the exact letter")
        d2a = raw_input ("What do you choose? [A/B]") #Second decision from the first A good option
        if d2a == ("A"): #Part of Second decision from A good option
            print ("So you choose to act hostile huh? ok")
            print("Dice is rolling...")
            sleep(3)
            diceThrow = random.randrange(1,10)
            print (diceThrow)
            if diceThrow >= 6:
                print("You won")
                sleep (2)
                print("You pushed his arm away")
                sleep (2)
                print("You are afraid that you cannot trust this man")
                sleep (2)
                print("You ask him where are you being taken")
                sleep (2)
                print("He doesn't answer")
                sleep (2)
                print("You keep asking him questions and he still doesn't answer")
                sleep (2)
                print("You've had enough and start to get angry with him")
                sleep (2)
                print("Out of fear that he might be one of the aliens, you punch him")
                sleep (2)
                print("The man catches the punch and knocks you to the ground")
                sleep (2)
                print("He signaled you to stop talking as an alien started to walk around you guys about 50 feet away")
                sleep (2)
                print("The alien had finally walked past and you now decide to trust this man ")
                sleep (2)
                print("The man later talked about a refugee camp that he plans on taking you")
                sleep (2)
                print("You agree as you leave together towards the camp")
                sleep (2)
                print("You end up surviving. You win")
                
                
            if diceThrow <= 4:
                print("You lost")
                sleep (2)
                print("You act violent towards the mysterious man")
                sleep (2)
                print("You keep in mind that you cannot trust anyone, because they might be the enemy in disguise")
                sleep (2)
                print("You pick up a rock nearby and start threatening him with it")
                sleep (2)
                print("The man tries to signal you to lower your voice, but you don't pay attention")
                sleep (2)
                print("Instead you do the opposite and keep threatening him. ")
                sleep (2)
                print("The man decides to give up on you and run off")
                sleep (2)
                print("You take this as a win, but quickly realize that he was right")
                sleep (2)
                print("As an alien appears right behind you, you relize that you should've listened")
                sleep (2)
                print("You were eaten and lost the game")
        if d2a == ("B"): #Part of Second Decision in good A 
            print("So you choose to keep quiet and play it safe? Interesting.")
            print("Dice is rolling...")
            sleep(3)
            diceThrow = random.randrange(1,10)
            print (diceThrow)
            if diceThrow >= 6:
                print("You won")
                sleep (2)
                print("Because of your good survival skills you end up going with the mysterious man")
                sleep (2)
                print("Despite not knowing where you are going")
                sleep (2)
                print("You end up arriving at some sort of camp")
                sleep (2)
                print("This camp is filled with other people")
                sleep (2)
                print("This camp ended up being a camp where citizens are taken to be safe")
                sleep (2)
                print("You end up surviving and winning the game Good job")
                
                
                
            if diceThrow <= 4:
                print("You lost")
                sleep (2)
                print("You ended up going with a mysertious man even though he saved you")
                sleep (2)
                print("You are unsure of what he has planned but you go along with it anyway")
                sleep (2)
                print("This man ended up being dressed in a military uniform")
                sleep (2)
                print("You notice this and ask him") 
                sleep (2)
                print("Are you going to take me to a SafeSpace" )
                sleep (2)
                print("The military man doesn't answer")
                sleep (2)
                print("You observe his uniform again, and notice that its covered in blood.")
                sleep (2)
                print("Despite all blood the man seems in perfect condition")
                sleep (2)
                print("The man then started to shake")
                sleep (2)
                print("His body had begun to morph into something else")
                sleep (2)
                print("You notice this, and start to run away")
                sleep (2)
                print("But by then it was too late, and you were eaten")
                sleep (2)
                print("You lose")
            
                
            
            
            
    if diceThrow <= 4: #Part of Decision 1 bad A option
        print("Bad luck")
        sleep (2)
        print("You decide to attack the creature even though you have nothing on you")
        sleep (2)
        print("You should of thought of what you were doing before you have done it")
        sleep (2)
        print("You charge towards the creature, and prepare to punch it in the face")
        sleep (2)
        print("And you...")
        sleep (2)
        print("Succesully punch it")
        sleep (2)
        print("However, it did no damage")
        sleep (2)
        print("you assume that the creature let you punch it")
        sleep (2)
        print("It is the alien's turn now, as it thrusts you all the way back into your house")
        sleep (2)
        print("What do you do now?")
        sleep (2)
        print("A) Still attempt to fight it")
        sleep (2)
        print("B) Quickly seek shelter")
        sleep (2)
        print("SIDENOTE: Don't screw this up")
        d2a = raw_input ( )
        if d2a == ("A"):
            print("So you decide to fight it even when you already failed? ok")
            print("Dice is rolling...")
            sleep(3)
            diceThrow = random.randrange(1,10)
            print (diceThrow)
            if diceThrow >= 6:
                print("Good roll")
                print("You decide to fight it again")
                sleep (2)
                print("But this time you grab a kitchen knife")
                sleep (2)
                print("You charge towards it and prepare to strike")
                sleep (2)
                print("The alien does the same and decides to strike first")
                print("*Press Dodge to Dodge*")
                Dodge=raw_input()
                sleep (2)
                print("You successfully dodged the aliens attack, and now it's your turn ")
                print("*Press Attack to Attack*")
                Attack=raw_input()
                sleep (2)
                print("Congrats you have striked the aliens head ")
                sleep (2)
                print("The alien is now dead and you have beaten it")
                sleep (2)
                print("You head inside to congratulate your win")
                sleep (2)
                print("Good job on winning the game")
                
            if diceThrow <= 4:
                print("You lost")
                sleep (2)
                print("Because you have tried to attack it again, you have lost the game")
                sleep (2)
                print("The alien anticipated your attack as you were charging towards it with your kitchen knife, and grabbed you from behind and ate you")
                sleep (2)
                print("You have lost, Good Job")

            
        if d2a == ("B"):
            print("So you decide to hide? Good choice")
            print("Dice is rolling...")
            sleep(3)
            diceThrow = random.randrange(1,10)
            print (diceThrow)
            if diceThrow >= 6:
                print("Good roll")
                sleep (2)
                print("You decide to hide in one of the big kitchen cabniets.")
                sleep (2)
                print("The alien heads inside and starts looking around")
                sleep (2)
                print("You try your best to keep your breathing to a miminuim ")
                sleep (2)
                print("You hear the alien walk around the house")
                sleep (2)
                print("After 5 minutes, you decide to get out of the cabniet")
                sleep (2)
                print("After that You immediately run to your neighbors house, where hope to seek comfort and a safe area")
                sleep (2)
                print("Congrats you have survived, good job on beating the game")
                
                
                
            if diceThrow <= 4:
                print("You decided to hide")
                sleep (2)
                print("You decide to hide in the kitchen cabniet, where you hope to be safe")
                sleep (2)
                print("The alien enters the house where it starts walking around, searching the area")
                sleep (2)
                print("After 5 minutes of hiding, you hear the creature start to move out of the house")
                sleep (2)
                print("And you would've escaped if it weren't for your phone")
                sleep (2)
                print("Right when the alien was about to leave the house, your phone had begun to ring.")
                sleep (2)
                print("It was an emergancy broadcast alert")
                sleep (2)
                print("The alien hears this and stands right in front of the cabniet your hiding in")
                sleep (2)
                print("You were eaten and have lost the game.")
                

            
        
if d1a == ("B"): # Part of Decision 1 B
    print ("So you have chosen to run back inside?")
    print ("May the dice be ever in your favor...")
    print("Dice is rolling...")
    sleep(3)
    diceThrow = random.randrange(1,10)
    print (diceThrow)
    if diceThrow >= 6:
        print("You won")
        print("You quickly decide to run back inside, to protect yourself")
        
    if diceThrow <= 4:
        print("Bad luck")
        sleep (2)
        print("You decide that the creature is too much to handle")
        sleep (2)
        print("you slowly turn around as you try to grab onto the handle of the door so you can escape")
        sleep (2)
        print("As you are turning you find that the creature started to move")
        sleep (2)
        print("You don't care as you prepare to bolt out of there")
        sleep (2)
        print("At the final second before you are about to fully turn around and leave, the creature morphs into someone familar")
        sleep (2)
        print("You stand there, paralyzed, as you stand away from your thought-to-be-dead-mother")
        sleep (2)
        print("A tear runs down your face ")
        sleep (2)
        print("She extends her arm to you, as if she's asking you to come with her")
        sleep (2)
        print("What will you do?")
        sleep (2)
        print("A: Come to your senses and enter the house")
        sleep (2)
        print("B: Accept her invitation ")
        d2a = raw_input () 
        if d2a == ("A"):
            print("So you decide to rudly leave your mother? ok")
            print("Dice is rolling...")
            sleep(3)
            diceThrow = random.randrange(1,10)
            print (diceThrow)
            if diceThrow >= 6:
                print("Good job you win")
                sleep (2)
                print("You are tranced from what you see in front of you")
                sleep (2)
                print("You want to believe it but deep down you know what happened years ago, resulting in the death of your parents")
                sleep (2)
                print("You quickly come back into your senses and grab the door handle behind you")
                sleep (2)
                print("Shutting the door behind you, you quickly get to your car and get out of there. You survived the game")
                sleep (2)
                print("Congratulations you win")
            if diceThrow <= 4:
                print("Bad Roll")
                sleep (2)
                print("As you quickly come back into your senses, and are about to enter the house quickly,")
                sleep (2)
                print("The alien realizes this and decides to quickly come charging at you")
                sleep (2)
                print("You are eaten and have lost the game")
                sleep (2)
                print("Or that would've happened...")
                sleep (2)
                print("If it weren't for the military")
                sleep (2)
                print("As the creature charges towards you and you are about to die, out of knowhere the military pops up")
                sleep (2)
                print("Half of the soldiers goes gun blazing on the alien, while the others are signaling you to come over")
                sleep(2)
                print("The alien, who is not to far from you, is being fired upon, while soldiers are signaling you to comeover. What do you do?")
                sleep(2)
                print("A) Run to the soldiers")
                sleep(2)
                print("or")
                sleep(2)
                print("B) Stay put, it's too risky")
                print("What do you do? [A/B]")
                d1a=raw_input()
                if d1a == ("A"):
                    print("So you choose to run?")
                    print("Dice is rolling...")
                    sleep(3)
                    diceThrow = random.randrange(1,10)
                    print (diceThrow)
                    if diceThrow >= 6:
                        print("Nice Roll")
                        sleep(2)
                        print("You run towards the soldiers in a desperate effort to escape from the creature")
                        sleep(2)
                        print("While you are running the alien trails behind you, in a desperate attempt to still eat you")
                        sleep(2)
                        print("While you are running you hear the soldiers to duck")
                        sleep(2)
                        print("*Press n to duck*")
                        duck=raw_input()
                        sleep(2)
                        print("While you are running you quickly get down to the ground, as the soldiers fire an rpg at an alein")
                        sleep(2)
                        print("The alien is down, and you run towards the soldiers as they grab you and get out of there")
                        sleep(2)
                        print("Congrats! You survived")
                        
                    if diceThrow <= 4:
                        print("Bad roll")
                        print("In a desperate attempt to save yourself, you run towards the soldiers")
                        sleep(2)
                        print("The alien realizes this and runs towards you in an attempt to eat you")
                        sleep(2)
                        print("The soldiers try their best to save you, but it's too late")
                        sleep(2)
                        print("You fall victim to another one of the aliens and you die")
                        sleep(2)
                        print("You have lost the game")
                if d1a == ("B"):
                    print("So you choose to stay put?")
                    print("Dice is rolling...")
                    sleep(3)
                    diceThrow = random.randrange(1,10)
                    print (diceThrow)
                    if diceThrow >= 6:
                        print("Good roll")
                        print("You decide that it's to risky to try and run in the battlefield")
                        sleep(2)
                        print("This results in you staying put")
                        sleep(2)
                        print("The alien takes this oppertunity to try and eat you, despite being injured from the bullets")
                        sleep(2)
                        print("You see that the alien is running towards you, and you decide to quickly run into the house")
                        sleep(2)
                        print("You run in the house, and quickly decide to hide in a kitchen cabniet")
                        sleep(2)
                        print("The alien desperatly attempts to try and find you, by destroying everything in sight")
                        sleep(2)
                        print("Right when the alien reaches the cabniet you are hiding in, you decide to quickly bolt out of there")
                        sleep(2)
                        print("*Type bolt to get out of there*")
                        bolt=raw_input()
                        sleep(2)
                        print("Right when the alien is about to destroy the cabneit you manage to escape, passing under the immense alien and back outside")
                        sleep(2)
                        print("You end up meeting up with the soldiers, as the soldiers take care of the alien by burning the house down")
                        sleep(2)
                        print('You win! Congrats')
                        
                    if diceThrow <= 4:
                        print("Bad roll")
                        print("You end up staying put because you do not want to get into the crossfire")
                        sleep(2)
                        print("The alien sees you staying still and charges at you")
                        sleep(2)
                        print("As the alien gets closer and closer, and you try to escape towards the inside of the house...")
                        sleep(2)
                        print("You end up getting stuck in the crossfire of the soldiers firing upon the alien, and you fall to the ground injured")
                        sleep(2)
                        print("Before you try and get back up, it is to late, as the alien is right above you...")
                        sleep(2)
                        print("The alien eats you and you lose the game.")

                
                
                
                
        if d2a == ("B"):
            print ("So you choose to accept the invitation? Ok")
            print("Dice is rolling...")
            sleep(3)
            diceThrow = random.randrange(1,10)
            print (diceThrow)
            if diceThrow >= 6:
                print("Good job")
                sleep (2)
                print("You come racing towards your thought-to-be-dead-mother ")
                sleep (2)
                print("As you approch her more and more you realize that the monster has started to change")
                sleep (2)
                print("It was morphing back into its orginal form, preparing to eat you")
                sleep (2)
                print("Luckilly you see this and quickly rush towards it so you can attack it")
                sleep (2)
                print("You successfully manage to strike the face of the creature while it was in its human form, knocking it down")
                sleep (2)
                print("Suddenly a man coming out of the shadows comes and finishes the alien off before it can recover")
                sleep (2)
                print("This man ends up being part of the military and he quickly takes you to a faw away but safe camp")
                sleep (2)
                print("Where you end up surviving. Good job. You win")
            if diceThrow <= 4:
                print("You lost")
                sleep (2)
                print("You stupidly accepted the invitation of the alien")
                sleep (2)
                print("You start rushing towards your mother")
                sleep (2)
                print("And as you finally reach her, you accept her invitation by shaking her hand")
                sleep (2)
                print("The mother starts changing forms suddenly")
                sleep (2)
                print("You don't realize this because of how starstruck you are of seeing your mother again")
                sleep (2)
                print("Before you realize the alien changing, it is too late")
                sleep (2)
                print("And you have died and lost the game")
                sleep (2)
                print("Good job")


            


