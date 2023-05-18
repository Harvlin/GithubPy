from cryptography.fernet import Fernet
def write_key():
      key = Fernet.generate_key()
      with open("key.key", "wb") as key_file:
            key_file.write(key)
def load_key():
      file = open("key.key", "rb")
      key = file.read()
      file.close()
      return key 
master_pass = input("Enter the master password: ")
key = load_key()
fer = Fernet(key)
def add():
      global usrn, usrpass 
      usrn = input("Enter your username: ")
      usrpass = input("Enter your user password: ")
      with open("pass_code.txt", "a") as f:
            f.write(usrn + " | " + fer.encrypt(usrpass.encode()).decode() + "\n")
            
def view():
      with open("pass_code.txt", "r") as f:
            for read in f.readlines():
                  xy = read.rstrip()
                  user, pwd = xy.split("|")
                  print("User: ", user , ", Password: ", fer.decrypt(pwd.encode()).decode())
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