master_pass = input("Enter the master password: ")


def add():
    global usrn, usrpass
    usrn = input("Enter your username: ")
    usrpass = input("Enter your user password: ")
    with open("pass_code.txt", "a") as f:
        f.write(usrn + " | " + usrpass + "\n")


def view():
    with open("pass_code.txt", "r") as f:
        for read in f.readlines():
            xy = read.rstrip()
            user, pwd = xy.split("|")
            print("User: ", user, ", Password: ", pwd)


while True:
    mode = input("Would you like to add or view an existing password (press q to quit): ")
    if mode == "add":
        add()
    elif mode == "view":
        view()
    elif mode == "q":
        break
    else:
        print("Invalid input\n")
        continue
