def add(num1, num2):
    return num1 + num2
def min(num1, num2):
    return num1 - num2
def multi(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

while True:
    user_input = input("Enter the operation you want (+) (-) (:) (/) (q to quit): ")
    num1 = eval(input("Num 1: "))
    num2 = eval(input("Num 2: "))
    if user_input == "+":
        print(add(num1, num2))
    elif user_input == "-":
        print(min(num1, num2))
    elif user_input == "*":
        print(multi(num1, num2))
    elif user_input == "/":
        print(divide(num1, num2))
    elif user_input == "q":
        break
        
    else:
        print("Invalid")