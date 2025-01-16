from pprint import pprint
import random
import webbrowser
#Variables
thegame = False
devmode = False
combat = True
nocombat = False
successful = False
devx = ""
hitphrases = ["You landed a hit!", "You put the hurt on him!", "Hit landed B3!", "Landed a solid punch!"]
missphrases = ["You missed your target!", "A Swing and A Miss!", "You gotta be quicker than that!", "The punch landed nowhere near the guy"]
enemyhitphrases = ["Your enemy landed a hit!", "The enemy put the hurt on you!", "The enemy did a lotta damage!","Ow! That one hurt!"]
enemymissphrases = ["The enemy missed you", "The enemy swang and missed", "You dodged just in time!", "He almost hit you!"]
defendphrases = ["You blocked the hit and took no damage!", "Hit successfully blocked!", "Block: 100", "#Blocked"]
misseddefendphrases = ["You blocked but the enemy didn't swing!", "You blocked...But what for?", "You blocked, but he didn't swing so you just stand there awkwardly.", "Your block was pointless!"]
enemydefend = ["The enemy blocked your hit!", "Your hit was blocked", "You went for the punch but the enemy blocked at the right time!", "Hit? Blocked."]
endgame = False
torf = True

#Intro Sequence
pprint("Welcome to a totally average choose your own adventure game!")
pprint("What is your name?")
name = input()
if(name == "D"): #Dev Mode Activate
    print("Developer Mode Activated")
    devmode = True
    torf = False
    thegame = True
else:
    pprint("That's a fine name!")
    pprint("Are you ready for an adventure "+ name +"?")
while torf:
    yn = input()
    if(yn == "Yes" or yn == "yes"):
        print("Alright then! Start the Adventure!")
        torf = False
        thegame = True
    elif(yn == "No" or yn == "no"):
        print("Are you sure?")
        yn = ""
        yn = input()
        if(yn == "Yes" or yn == "yes"):
            print("Well fine then! But you'll regret it!")
            break
        elif(yn == "No" or yn == "no"):
            print("Well if you can't make up your damn mind, I'll do it for you! Start the adventure!")
            torf = False
            thegame = True
        else:
            print("You don't wanna play by the rules? Fine! NO ADVENTURE FOR YOU!")
            break
    else:
        print("I have no clue what that means but I'm gonna take that as a Yes... Start the Adventure!")
        torf = False
        thegame = True

#the main game, variable thegame allows it to repeat if game over
while thegame:
    successful = False
    torf2 = True
    sidewalk = False
    Shortcut = False
    #DevMode Option
    if(devmode == True):
        print("Sidewalk or shortcut")
        devx = input()
        if(devx == "Sidewalk"):
            torf2 = False
            print('Fight or Puzzle?')
            devx = input()
            if(devx == "Puzzle"):
                successful = True
                sidewalk = True
            elif(devx == "Fight"):
                sidewalk = True
        elif(devx == "Shortcut"):
            torf2 = False
            print("Puzzle or Fight")
            devx = input()
            if(devx == "Puzzle"):
                Shortcut = True
            elif(devx == "Fight"):
                Shortcut = True
    #Main Option
    if(torf == False and devmode == False):
        print("It's late at night and you're walking home from a party. As you walk home you get a text from your mother. She wants you home immedately, but you know you're about 30 minutes out. However a shortcut through the woods would cut that time in half, but those woods can be dangerous at night...")
        print("Do you continue on the sidewalk, or take the shortcut?")
        x = ""
        count = 0
        choices = ["Sidewalk", "Shortcut"]
        value = random.randint(0,1)
        while torf2:
            x = input()
            if x == "Sidewalk" or x == "sidewalk":
                sidewalk = True
                torf2 = False
            elif x == "Shortcut" or x == "shortcut":
                Shortcut = True
                torf2 = False
            else:
                if count == 3:
                    print("Look man, If you wanna play this game, you gotta play by the rules. So I'll give you one more try, Please type Sidewalk or Shortcut")
                    x = ""
                    count = count + 1
                elif count == 4:
                    print("Alright man you're really starting to piss me off. That's it, you're taking the "+choices[value]+"!")
                    if (choices[value] == "Sidewalk"):
                        sidewalk = True
                        torf2 = False
                    else:
                        Shortcut = True
                        torf2 = False
                else:
                    print("That is not a valid choice. Please type Shortcut or Sidewalk to choose a path")
                    x = ""
                    count = count + 1
    #Sidewalk Option
    if(sidewalk == True):
        if(devx == "Puzzle"):
            nocombat = True
        else:
            print("As you walk down the sidewalk, you feel a presence around you. You look behind you only to see nothing. You're starting to get a bit freaked out. Then all of a sudden, someone jumps out of the bushes!")
            print("Initiate The Battle Music!")
        if(nocombat == False):
            playerhealth = 3
            playerhitchance = random.randint(0,100)
            playerblockchances = 3
            enemyhealth = 3
            enemyhitchance = random.randint(0,100)
            enemyblockchances = 3
            attack = False
            defend = False
            combat = True
        
            while combat:
                attack = False
                defend = False
                enemyai = random.randint(0,1)
                text = random.randint(0,3)
                print("Do you want to attack or defend?")
                print("Player Health: ", playerhealth,"                             Enemy Health: ",enemyhealth)
                print("Block Chances: ", playerblockchances)
                print("Hit Percentage: ",playerhitchance,"%","                      Enemy Hit Percentage: ",enemyhitchance,"%")
                x = ""
                x = input()
                if(x == "Attack" or x == "attack"):
                    attack = True
                if(x == "Defend" or x == "defend"):
                    defend = True

                if(attack == True):
                    if(playerhitchance >= (100-playerhitchance)):
                        if(enemyai == 1 and enemyblockchances > 0):
                            print(enemydefend[text])
                            enemyblockchances = enemyblockchances - 1
                            playerhitchance = random.randint(40, 80)
                            enemyhitchance = random.randint(30, 60)
                            

                        elif(enemyai == 0 or (enemyai == 1 and enemyblockchances == 0)):
                            if((100-playerhitchance) <= (100-enemyhitchance)):
                                print(hitphrases[text])
                                enemyhealth = enemyhealth -1
                                if(playerblockchances == 0):
                                    playerhitchance = random.randint(40, 80)
                                    enemyhitchance = random.randint(30, 60)
                                else:
                                    playerhitchance = random.randint(20, 60)
                                    enemyhitchance = random.randint(40, 70)
                            elif((100-playerhitchance) > (100-enemyhitchance)):
                                print(missphrases[text])
                                if(playerblockchances == 0):
                                    playerhitchance = random.randint(45, 80)
                                    enemyhitchance = random.randint(25, 55)
                                else:
                                    playerhitchance = random.randint(40, 80)
                                    enemyhitchance = random.randint(30, 60)
                    elif(playerhitchance < (100-playerhitchance)):
                        if(playerhitchance >= enemyhitchance):
                            print(hitphrases[text])
                            enemyhealth = enemyhealth -1
                            playerhitchance = random.randint(40, 80)
                            enemyhitchance = random.randint(30, 60)
                        elif(playerhitchance < enemyhitchance):
                            print(enemyhitphrases[text])
                            playerhealth = playerhealth - 1
                            playerhitchance = random.randint(40, 80)
                            enemyhitchance = random.randint(40, 60)
                        
                if(defend == True):
                    if playerblockchances == 0:
                            print("You can't block anymore!")
                    elif(enemyai == 1 and enemyblockchances > 0):
                            print(misseddefendphrases[text])
                            enemyhitchance = random.randint(30, 70)
                            playerhitchance = random.randint(40, 60)
                    elif(enemyai == 0 or (enemyai == 1 and enemyblockchances == 0)):
                            print(defendphrases[text])
                            playerhitchance = random.randint(30, 70)
                            enemyhitchance = random.randint(30, 70)
                            playerblockchances = playerblockchances - 1

                if(enemyhealth == 0):
                        print("You knocked out your enemy!")
                        successful = True
                        combat = False
                elif(playerhealth == 0):
                        print("You were knocked out during the fight...")
                        print("Type continue to continue the story")
                        x = ""
                        x = input()
                        if(x == "Continue" or x == "continue"):
                            webbrowser.open("https://www.youtube.com/watch?v=_WZCvQ5J3pk", new=1)
                            combat = False
                            thegame = False
    if(successful == True):
            print("A bit shaken up, you quickly flee the scene. However, you unfortunately got lost in doing so. You look down at your phone for directions, but its dead. Now you must rely on only street signs to get home.")
            puzzle = True
            CorrectStreets = ["Ainsley Way", "North Street", "Spooner Street","Wenderson Street","Edison Drive","Rotunda Circle"]
            CorrectPrompts = ["You go down Ainsley Way and find another intersection!", "As you run down North Street things start looking familiar, and you approach another intersection", "As you run down Spooner Street you hear \"Hey Lois!\" as you approach another intersection.", 
            "As you run down Wenderson you see the homes of Wendy Wenderson I through IX. Before you can even realize how odd that is you approach another intersection", "As you run down Edison Street you see all the lights blacked out. Ironic. You approach another intersection."]
            IncorrectStreets = ["Derry Drive", "South Street", "Elm Street", "Grizzly Way", "Wuja Drive", "Box Square"]
            IncorrectPrompts = ["As you go down Derry Drive you fall in a sewer grate. As you stand up you see a red balloon pass by", "As you go down South Street you hear the italian mob planning a murder. You're shot on sight", "As you go down Elm Street you hear what sounds like nails on a chalkboard. You turn around to see Freddy Kruger. You're screwed.",
            "As you go down Grizzly Way, you encounter a grizzly bear. Before you make the realization that \"Oh that's why it's named that\" you're eaten by the bear", "As you walk down the street, you hear, \"Ah Good Morning "+name+"! Would you like to go to history club?\" There is no escape.","That ain't it cheif"]
            x = ""
            streetcount = 0
            correctcount = 0
            invalid = 0
            while puzzle:
                order = random.randint(0,100)
                print("Which street do you take?")
                if(order < 50):
                    print(CorrectStreets[streetcount] + " or " + IncorrectStreets[streetcount])
                elif(order >= 50):
                    print(IncorrectStreets[streetcount] + " or " + CorrectStreets[streetcount])
                x = input()
                if(correctcount == 5):
                    puzzle = False
                    endgame = True
                elif(x == CorrectStreets[streetcount] and correctcount < 5):
                    print(CorrectPrompts[streetcount])
                    correctcount = correctcount + 1
                    streetcount = streetcount + 1
                elif(x == IncorrectStreets[streetcount]):
                    print(IncorrectPrompts[streetcount])
                    puzzle = False
                    thegame = False
                    streetcount = 0
                else:
                    if(invalid == 3):
                        print("Oh for the love of god, just pick a street name man!")
                        invalid = invalid + 1
                    elif(invalid == 4):
                        print("Fine don't play by the rules. See if I care. I'm leaving. Type whatever you want")
                        x = ""
                        x = input()
                        if(x == "Stop"):
                            thegame = False
                        else:
                            print()
                    else:
                        print("That is not a valid street name!")
                        invalid = invalid + 1
                
    if(Shortcut == True):
        fighttime = False
        puzzle2 = True
        nopuzzle = False
        if(devx == "Fight"):
            nopuzzle = True
            fighttime = True
        elif(nopuzzle == False):
            count2 = 0
            riddles = ["\"Poor people have it. Rich people need it. If you eat it you die. What is it?\"", "\"Spelled forwards I’m what you do every day, spelled backward I’m something you hate. What am I?\"", "\"I have branches, but no fruit, trunk, or leaves. What am I?\"", "\"Until I am measured, I am not known. Yet how you miss me, When I have flown. What am I?\"", "\"What goes up but never comes down?\""]
            riddleanswers = ["Nothing", "Live", "A Bank", "Time", "Age"]
            riddlecorrectprompt = "The door opens and you are met with another. It says:"
            riddleincorrect = ["\"INCORRECT!\" the door says. The oxygen escapes from the room, you pass out in seconds", "\"INCORRECT!\" the door says. The room fills with a gas that makes you see your greatest evil. You go insane in 10 minutes.", "\"INCORRECT!\" the door says. As you look up, you see a giant money bag comming in hot. You're crushed by the money bag.", "\"INCORRECT!\" the door says. A clock appears on a wall, and the minute hands begins to move faster and faster. You age qucker and quicker and die of \"Old Age\"", "\"INCORRECT!\" the door says. Darts fly out of the walls and you're dead on the spot."]
            print("You take a turn into the woods to take the shortcut. You pass a cave and hear it calling to you. Your curiosity gets the better of you and you go in the cave")
            print("You walk down the cave for 2 minutes until you see a door. It asks you:")
            while puzzle2:
                print(riddles[count2])
                x = input()
                if(x == riddleanswers[count2]):
                    print(riddlecorrectprompt)
                    count2 = count2 + 1
                else:
                    print(riddleincorrect[count2])
                    puzzle2 = False
                    thegame = False

                if(count2 > 4):
                    puzzle2 = False
                    fighttime = True
        if(fighttime == True):
                print("As the last door opens you walk into a huge sanctum. There's a goulish looking person sitting on a throne, wearing a crown. The ghoul stands up, points his sword, and charges!")
                print("Initiate the battle music!")
                playerhealth = 3
                playerhitchance = random.randint(0,100)
                playerblockchances = 3
                enemyhealth = 3
                enemyhitchance = random.randint(0,100)
                enemyblockchances = 3
                attack = False
                defend = False
                combat = True
        
                while combat:
                    attack = False
                    defend = False
                    enemyai = random.randint(0,1)
                    text = random.randint(0,3)
                    print("Do you want to attack or defend?")
                    print("Player Health: ", playerhealth,"                             Enemy Health: ",enemyhealth)
                    print("Block Chances: ", playerblockchances)
                    print("Hit Percentage: ",playerhitchance,"%","                      Enemy Hit Percentage: ",enemyhitchance,"%")
                    x = ""
                    x = input()
                    if(x == "Attack" or x == "attack"):
                        attack = True
                    if(x == "Defend" or x == "defend"):
                        defend = True

                    if(attack == True):
                        if(playerhitchance >= (100-playerhitchance)):
                            if(enemyai == 1 and enemyblockchances > 0):
                                print(enemydefend[text])
                                enemyblockchances = enemyblockchances - 1
                                playerhitchance = random.randint(40, 80)
                                enemyhitchance = random.randint(30, 60)
                            

                            elif(enemyai == 0 or (enemyai == 1 and enemyblockchances == 0)):
                                if((100-playerhitchance) <= (100-enemyhitchance)):
                                    print(hitphrases[text])
                                    enemyhealth = enemyhealth -1
                                    if(playerblockchances == 0):
                                        playerhitchance = random.randint(40, 80)
                                        enemyhitchance = random.randint(30, 60)
                                    else:
                                        playerhitchance = random.randint(20, 60)
                                        enemyhitchance = random.randint(40, 70)
                                elif((100-playerhitchance) > (100-enemyhitchance)):
                                    print(missphrases[text])
                                    if(playerblockchances == 0):
                                        playerhitchance = random.randint(45, 80)
                                        enemyhitchance = random.randint(25, 55)
                                    else:
                                        playerhitchance = random.randint(40, 80)
                                        enemyhitchance = random.randint(30, 60)
                        elif(playerhitchance < (100-playerhitchance)):
                            if(playerhitchance >= enemyhitchance):
                                print(hitphrases[text])
                                enemyhealth = enemyhealth -1
                                playerhitchance = random.randint(40, 80)
                                enemyhitchance = random.randint(30, 60)
                            elif(playerhitchance < enemyhitchance):
                                print(enemyhitphrases[text])
                                playerhealth = playerhealth - 1
                                playerhitchance = random.randint(40, 80)
                                enemyhitchance = random.randint(40, 60)
                        
                    if(defend == True):
                        if playerblockchances == 0:
                            print("You can't block anymore!")
                        elif(enemyai == 1 and enemyblockchances > 0):
                            print(misseddefendphrases[text])
                            enemyhitchance = random.randint(30, 70)
                            playerhitchance = random.randint(40, 60)
                        elif(enemyai == 0 or (enemyai == 1 and enemyblockchances == 0)):
                            print(defendphrases[text])
                            playerhitchance = random.randint(30, 70)
                            enemyhitchance = random.randint(30, 70)
                            playerblockchances = playerblockchances - 1

                        

                    if(enemyhealth == 0):
                            print("You knocked out your enemy!")
                            print("A Hidden Door opens to your street, you go through it as quickly as possible")
                            endgame = True
                            combat = False
                    elif(playerhealth == 0):
                            print("You were knocked out during the fight...")
                            print("Type continue to continue the story")
                            x = ""
                            x = input()
                            if(x == "Continue" or x == "continue"):
                                webbrowser.open("https://www.youtube.com/watch?v=_WZCvQ5J3pk", new=1)
                                combat = False
                                thegame = False

    if(endgame == True):
        youwin = ["Congratulations! You Win!","Conglaturation! You're Winner!"]
        print("You make it safely home and slip into bed. You fall asleep quickly and wake up the next morning!")
        chance = random.randint(0,100)
        if(chance <=75):
            print(youwin[0])
            print("Thanks for playing!")
            
        elif(chance > 75):
            print(youwin[1])
            print("Thanks for playing!")
        if(devmode == False):
            print("Wanna Play again?")
            x = input()
            if(x == "Yes" or x == "yes"):
                thegame = True
            elif(x == "No" or x == "no"):
                print("Shutting Down...")
                thegame = False
        elif(devmode == True):
            print("Wanna Play again?")
            x = input()
            if(x == "Yes" or x == "yes"):
                print("Do you want to turn Developer Mode Off?")
                x = input()
                if(x == "Yes" or x == "yes"):
                    print("Enter a Name:")
                    name = input()
                    devmode = False
                    thegame = True
                    nocombat = False
                    successful = False
                    devx = ""
                else:
                    thegame = True
                    nocombat = False
                    successful = False
            elif(x == "No" or x == "no"):
                print("Shutting Down...")
                thegame = False



    elif(thegame == False and endgame == False):
        print("Game Over!")
        if(devmode == True):
            print("Try Again?")
            x = ""
            x = input()
            if(x == "Yes"):
                thegame = True
                nocombat = False
                successful = False
                devx = ""
            else:
                print("Shutting Down...")
        else:
            print("Do you wanna try again "+ name + "?")
            x = ""
            x = input()
            if(x == "Yes"):
                thegame = True

            else:
                print("Shutting Down...")
