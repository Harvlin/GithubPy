import random
user_action = input("Enter your choice (rock), (paper), (scissor): ")
possible_action = ["rock", "paper", "scissor"]
Bot = random.choice(possible_action)
print(f"You chose {user_action},  Bot choose {Bot}")

while True:
    if user_action == Bot:
        print("It's a tie")

    elif user_action == "rock":
        if Bot == "scissor":
            print("You win")
        else:
            print("You lose")

    elif user_action == "paper":
        if Bot == "rock":
            print("You win")
        else:
            print("You lose")

    elif user_action == "scissor":
        if Bot == "paper":
            print("You win")
        else:
            print("You lose")

    i = input("Play again (y/n): ")
    if i == "n":
        break
