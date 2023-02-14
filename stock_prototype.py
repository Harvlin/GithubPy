def stock():

    while True:

        Stock = {
            "a": 10,
            "b": 10,
            "c": 10,
            "d": 10,
        }

        x = str(input("Add or eject item ? :"))

        if x == "add":
            y = str(input("What item do you want to Add ? :"))

            if y == "a":
                z = int(input("How many ?"))
                Stock["a"] += z
                print(Stock)
            elif y == "b":
                z = int(input("How many ?"))
                Stock["b"] += z
                print(Stock)
            elif y == "c":
                z = int(input("How many ?"))
                Stock["c"] += z
                print(Stock)
            elif y == "d":
                z = int(input("How many ?"))
                Stock["d"] += z
                print(Stock)


        elif x == "eject":
            y = str(input("What item do you want to eject ? :"))

            if y == "a":
                z = int(input("How many ?"))
                Stock["a"] -= z
                print(Stock)
            elif y == "b":
                z = int(input("How many ?"))
                Stock["b"] -= z
                print(Stock)
            elif y == "c":
                z = int(input("How many ?"))
                Stock["c"] -= z
                print(Stock)
            elif y == "d":
                z = int(input("How many ?"))
                Stock["d"] -= z
                print(Stock)

        x = str(input("Stop ?  (y/n):"))
        if x == "y":
            break

stock()