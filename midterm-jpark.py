#!/usr/bin/env python3

print("Name: Quinn Kimball\n")

password_database = {"Username" : "dnedry", "Password" : "please"}

command_database = {"reboot" : "OK. I will reboot all park systems.",
                    "shutdown" : "OK. I will shut down all park systems.",
                    "done": "I hate all this hacker stuff."}

white_rabbit_object = 0
counter = 0
tries = 3

while white_rabbit_object == 0 and counter < 3:
    input_user = input("Username: ")
    input_password = input("Password: ")
        
    if input_user == password_database["Username"] and input_password == password_database["Password"]:
        white_rabbit_object = 1

        print("\nHi, Dennis. You're still the best hacker in Jurassic Park.")

        print(f"\nPlease enter one of the following commands: ")

        for key in command_database:
            print(f"{key}")
        command = input(":")

        if command == "reboot":
            print(command_database["reboot"])
        elif command == "shutdown":
            print(command_database["shutdown"])
        elif command == "done":
            print(command_database["done"])
        else:
            print("The Lysine Contingency has been put into effect.")

    else:
        counter += 1
        tries -= 1
        print(f"Username/password incorrect. You have {tries} tries left.")

    if counter == 3:
        print("\nYou didn't say the magic word!" * 25)