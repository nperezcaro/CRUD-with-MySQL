
def PrincipalMenu():
    print("------PRINCIPAL MENU---------")
    print("1 - Show Assets")
    print("2 - Buy Assets")
    print("3 - Update Assets")
    print("4 - Sell Assets")
    print("5 - Exit")
    print("------------------------------")
    option = int(input("Select an option: "))

    if option <1 or option>5:
        print("Option selected doesn't exist, please select a correct option.")
    elif option == 5:
        print("Thanks for using this system")
    else:
        executeOption(option)


def executeOption(option):
    print(option)


PrincipalMenu()