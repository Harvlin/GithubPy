def add(num1, num2):
    return num1 + num2
def min(num1, num2):
    return num1 - num2
def multi(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

while True:
    user_input = input("Enter the operation you want (+) (-) (*) (/) (q to quit): ")
    num1 = eval(input("Num 1: "))
    num2 = eval(input("Num 2: "))
    match (user_input):
        case "+":
            print(add(num1, num2))
        case "-":
            print(min(num1, num2))
        case "*":
            print(multi(num1, num2))
        case "/":
            print(divide(num1, num2))
        case "q":
            break