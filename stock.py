#importing libaries....
import pandas as pd

def stock_function():
      
    while bool(True):
            
        x = pd.read_csv("stock.csv")
        a = input("Add(a)  or  Eject(e): ")
        
        if a == "a":
            b = input("Item name: ")
            
            if b == "Ap":
                x.loc[int(input("List row: ")), "Ap"] += int(input("Quantity: ").title())
                pd.options.display.max_rows= 1000
                print(x.to_string())
            elif b == "Ba":
                  x.loc[int(input("List row: ")), "Ba"] += int(input("Quantity: ").title())
                  pd.options.display.max_rows= 1000
                  print(x.to_string())
            elif b == "Ch":
                  x.loc[int(input("List row: ")), "Ch"] += int(input("Quantity: ").title())
                  pd.options.display.max_rows= 1000
                  print(x.to_string())     
            elif b == "Ma":
                  x.loc[int(input("List row: ")), "Ma"] += int(input("Quantity: ").title())
                  pd.options.display.max_rows= 1000
                  print(x.to_string())      
                       
        elif a == "e":
            b = input("Item name: ")
            if b == "Ap":
                x.loc[int(input("List row: ")), "Ap"] -= int(input("Quantity: ").title())
                pd.options.display.max_rows= 1000
                print(x.to_string())         
            elif b == "Ba":
                  x.loc[int(input("List row: ")), "Ba"] -= int(input("Quantity: ").title())
                  pd.options.display.max_rows= 1000
                  print(x.to_string())
            elif b == "Ch":
                  x.loc[int(input("List row: ")), "Ch"] -= int(input("Quantity: ").title())
                  pd.options.display.max_rows= 1000
                  print(x.to_string())
            elif b == "Ma":
                  x.loc[int(input("List row: ")), "Ma"] -= int(input("Quantity: ").title())
                  pd.options.display.max_rows= 1000
                  print(x.to_string()) 
        i = input("Press Enter to Stop>")
        if i == "":
            break
stock_function()