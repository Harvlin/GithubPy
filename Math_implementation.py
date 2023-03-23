while True:
    x = int(input("\n1. Circumference of rectangular prism\n"
                  "2. Circumferences of cube\n"
                  "3. Area of triangle\n"
                  "4. Area of circle\n"
                  "0. Exit Program\n"
                  "Enter your choice according to the number: "))
    
    if x == 1:
        l = int(input("Enter the length: "))
        w = int(input("Enter the width: "))
        h = int(input("Enter the height: "))
        print(">> ", 4*(l+w+h))
    elif x == 2:
        s = int(input("Enter the side length: "))
        print(">> : ", s*12)
    elif x == 3:
        b = int(input("Enter the base: "))
        h = int(input("Enter the height: "))
        print(">> : ", 0.5*b*h)
    elif x == 4: 
        r = int(input("Enter the radius: "))
        print(">> : ", 3.14*r*r)
    else:
        break