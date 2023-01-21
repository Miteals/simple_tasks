from xml.etree.ElementTree import QName


dict = {}

print("Dictionairy, make you own definition!")
while(True):
    print("Pick 1 if you wanna make a new definition")
    print("Pick 2 if you wanna find definition")
    print("Pick 3 if you wanna list all definitions")
    print("Pick 4 if you wanna remove definition")
    print("Pick 5 to exit the program")

    choice = input('Pick whatever you like! ')
    if (choice == "1"):
        key = input("Name your definition!: ")
        defi = input("Write down your definition!: ")
        dict[key] = defi
        print('Definition has been added succefully')  
    elif (choice == "2"):
        find = input("Name of the definition to find: ")
        dict[find]
        print("Definition has been found!")
        print(dict[find])
    elif (choice == "3"):
        print(dict)
    elif (choice == "4"):
        remove = input("Which one do you want to remove?: ")
        dict.pop(remove)
    elif (choice == "5"):
        quit()
