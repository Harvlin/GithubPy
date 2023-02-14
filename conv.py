x = str(input("Convert to kg or gram : "))
y = int(input("Enter the value : "))
if x == "kg":
    convert = y / 1000
    float(print(f"{convert} kg"))
elif x == "gram":
    convert = y * 1000
    float(print(f"{convert} gram"))