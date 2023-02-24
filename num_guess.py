from numpy import random
x = random.randint(10)
i = int(input(">>"))

while True:
 if i > x:
    print("Too High")
    i = int(input(">>"))

 elif i < x:
    print("Too low")
    i = int(input(">>"))

 elif i == x :
     print("Correct")
     break