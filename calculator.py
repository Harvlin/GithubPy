# importing...
import math

# defining function
def mathematics_function():

    # make a loop
    mathematics = True
    while mathematics:

        # taking user input information
        print("What operation do you want to do ? \n A.Add\n B.Subtract\n C.Multiply\n D.Divide\n E.Square\n F.Power")
        print("(Square operation work only for the first number input)")
        i = str(input(" >>".lower()))
        x = eval(input("Enter your First number:"))
        y = eval(input("Enter your Second number:"))

        # conditional
        if i == "a":
            print("The result is ", float(x + y))

        elif i == "b":
            print("The result is ", float(x - y))

        elif i == "c":
            print("The result is ", float(x * y))

        elif i == "d":
            print("The result is ", float(x / y))

        elif i == "e":
            print("The result is ", float(math.sqrt(x)))

        elif i == "f":
            print("The result is ", float(math.pow(x, y)))

        #Invalid input
        else:
            print("Invalid input")
            return

        # continue or break the loop
        j = str(input("Do you want to do another calculation ?\n>>"))
        if j != "yes":
            print("Ok, thanks")
            break

mathematics_function()