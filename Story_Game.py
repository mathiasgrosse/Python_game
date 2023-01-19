
# This game will teach you how to go clubbing in Berlin

print("""
Is Saturday Morning and you had a great rest from the week. You are alone and you want to go clubbing for the first time in Berlin but had no idea how it works.
You need to decide where and when you want to go clubbing.. so let's get started! 
""")

#level 1

level1_done = False

while level1_done == False:
    print("Where do you want to go? (BERGHEIM/SYSIPHOS/HOPPETOSSE)")
    choice = input()
    if choice == "BERGHEIM":
        print("you waited 3 hours in the line and got rejected because you are not the vibe")
        print("What you do next?(GO HOME/GO OTHER CLUB/MAKE THE LINE AGAIN)")
        sub_choice = input()
        if sub_choice == "GO OTHER CLUB":
            print("That's the spirit champ. You are a true Berliner!")
        else:
            print("YOU ARE CRAZY MAN. TRY AN OTHER CLUB! WEEKEND'S JUST STARTED") 
    elif choice == "SYSIPHOS":
        print("Good idea man, entering during daylight is a lot easier.")
        print("You are in front of the Bouncer and almost made it in.")
        print("He asks you: Hey man have you been here before?")
        print("What do you answer?(YES/NO)")
        sub_choice = input()
        if sub_choice == "YES":
            print("He knows your lying man... you are out. Go to Hoppetosse instead, rent a Scooter for 3 euros you will be ther in no time..")
            level1_done = True
        else:
            print("Why you didn't lie? He didn't let you in. You were never gonna make it anyways. Go to Hoppetosse")
            level1_done = True
    elif choice == "HOPPETOSSE":
        print("Good choice man, Let's go!")
        level1_done = True
    else:
        print("Focus man that club doesn't exist")

#level 2

print("You made it to level 2, keep going!")
level2_done = False

while level2_done == False:
    print("You go to Hoppetosse, there is only an hour qeue and you are in. Music is great and you have been there for few hours, but you are a little tired and not feeling the vibe that much anymore. ")
    print("You end up meeting people and got invited to .. the toilets??.. they offer you some magic but never tried before.")
    print("What you do? (LEAVE TOILET/TAKE IT/BE CURIOSE)")
    choice = input()
    if choice == "LEAVE TOILET":
        print("Good choice man, you never know what's in there")
        print("You stayed for one more hour and left. It was ok for a first experience anyways, before leaving the club you are asked again, what do you say? (Y/N)")
        sub_choice = input()
        if sub_choice == "Y":
            print("What is wrong with you man, party animal!")
            print("You are not feeling well... and...")
            level2_done = True
        elif sub_choice == "N":
            print("Very wize man. I'm proud of you! take a rest there will be an other time :)")
            print("YOU WIN")
            exit()
    elif choice == "TAKE IT":
        print("It wasn't what you thought it was. You are feeling dehydrated and ...")
        level2_done = True
    elif choice == "BE CURIOSE":
        print("Good idea man. He showed you a whole menu of weird stuff and you got well informed and took a mature decision about it")
        print("YOU WIN")
        exit()
    else:
        print("U drunk? didn't get you. Try again.")

        
#level 3
print()
print("Welcome to level 3. level 3 is not good")

print("You are dead man..")
print("What kind of religion are you?")
print("(CHRISTIAN/MUSLIM/ATHEIST)")
choice = input()
if choice == "CHRISTIAN":
    print("Saint Petter is the bouncer in heaven. He didn't let you in cause you are not the vibe. HORRIBLE WEEKEND MATE... GAME OVER.")
    exit()
elif choice == "MUSLIM":
    print("Clubbing is Haram Habibi... GAME OVER")
    exit()
elif choice == "ATHEIST":
    print("This is heaven. There is nothing here because it doesn't exist. BYE!")
    exit()
else:
    print("I'm sorry no habla espaniol")







