#!/usr/bin/env python3

print("You enter a dark room with 3 doors. Do you go through door 1, 2 or 3?")

door = input("-> ")

# == Door Number 1 logic ======================================================
if door == "1":
    
    print("There's what appears to be a large dragon with it's back turned towards you.")
    print("What do you do?\n")

    print("1. Try to attack the dragon while they aren't ready.")
    print("2. Say hello and ask the dragon their name.")

    # == Dragon logic ===========================================================
    dragon = input("-> ")

    if dragon == "1":
        print("As you attempt to attack the dragon it turns around, dousing you with it's firey breath.")
        print("Game Over")
    elif dragon == "2":
        print("It turns out the dragon is friendly and offers to fly you home.")
        print("Good job!")
    else:
        print(f"Well, {dragon} wasn't an option.")
        print("The dragon hears your clumsy reaction and swallows you in one bite.")

# == Door Number 2 Logic ======================================================
elif door == "2":

    print("You are met with 3 more doors and a man holding a gooseneck microphone.")
    print("WELCOME to the price of life or death, we have all been waiting!")
    print("Pick a door number to win whatever appears in that room!\n")

    print("1. Left")
    print("2. Middle")
    print("3. Right")

    # == Price Logic =======================================================
    price = input("-> ")

    if price == "1" or price == "2" or price == "3":
        print("A large bear appears behind the door and eats your face off. Ouch!")
    else:
        print("As Bob Ross once said, 'We don't make mistake's, we have happy accidents.'.")
        print("You win a brand new toaster! Now you just need some bread!")

# == Door Number 3 Logic ======================================================
elif door == "3":
    
    print("You are at the entrance of a cave with a dark figure looming inside.")
    print("What do you do?\n")

    print("1. Draw your lightsaber.")
    print("2. Emit your flashlight.")
    print("3. Turn and go back through the door.")

    # == Cave Logic ===========================================================
    cave = input("-> ")

    if cave == "1":
        print("The dark figure brandishes a red lightsaber and strikes you down before you can take a step.")
        print("Game over.")
    elif cave == "2":
        print("Your flashlight blinds the dark figure who then trips and falls to their death.")
        print("Good job!")
    elif cave == "3":
        print("The door is now locked, you look down to see a red lightsaber thrusted through your stomach")
        print("Game over.")
    else:
        print("This game is like building Ikea furniture, you need to read the instructions.")
        print("The cave awaits your decision.")

else:
    print("You did not select a door?? Good Call :)")