from numpy import random
while True:
    possible_move = [1, 2, 3, 4, 5, 6]
    random_move = random.choice(possible_move)
    print(f"You got {random_move} \n")
    if random_move == 1:
        print("-----")
        print("     ")
        print("  0  ")
        print("     ")
        print("-----")
    elif random_move == 2:
        print("-----")
        print("  0  ")
        print("     ")
        print("  0  ")
        print("-----")
    elif random_move == 3:
        print("-----")
        print("   0 ")
        print("  0  ")
        print(" 0   ")
        print("-----")
    elif random_move == 4:
        print("-----")
        print("0   0")
        print("     ")
        print("0   0")
        print("-----")
    elif random_move == 5:
        print("-----")
        print("0   0")
        print("  0  ")
        print("0   0")
        print("-----")
    elif random_move == 6:
        print("-----")
        print("0   0")
        print("0   0")
        print("0   0")
        print("-----")
    x = str(input("\n Play again (y/n) ?  "))
    if x != "y":
        print("\n OK")
        break