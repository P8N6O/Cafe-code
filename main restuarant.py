print ("--Welcome to Punno Cafe--")

menu = int(input("lease type 1 toe show menu:"))

if (menu == 1):
    print("--Choose the menu---\n1.Espresso\n2.Cappucino\n3.Latte")
    coffee = int(input("select coffee:"))
    if coffee == 1:
        print("Choose the type of the coffee\n1.Hot 55 Baht\n2.Cold 60 Baht")
        type = int(input("Select type:"))
        if type == 1:
            print("you choose hot Espresso 55 Baht")
        elif type == 2:
            print("you choose cold Espresso 60 Baht")
        else :
            print("Error")
    elif coffee == 2:
        print("Choose the type of the coffee\n1.Hot 55 Baht\n2.Cold 60 Baht")
        type = int(input("Select type:"))
        if type == 1:
            print("you choose hot Cappucino 55 Baht")
        elif type == 2:
            print("you choose cold Cappucino 60 Baht")
        else :
            print("Error")
    elif coffee == 3:
        print("Choose the type of the coffee\n1.Hot 55 Baht\n2.Cold 60 Baht")
        type = int(input("Select type:"))
        if type == 1:
            print("you choose hot Latte 55 Baht")
        elif type == 2:
            print("you choose cold Latte 60 Baht")
        else :
            print("Error")
    else :
            print("Error")
else :
            print("Error")

money = int(input("Input your money:"))

if type == 1:
    print("you recieved the change of " ,(money-55),"Baht")
elif type == 2:
    print("you recieved the change of " ,(money-60),"Baht")
else :
    print("Error")
        
print("---Thank You---")
    





