from DB.connection import DAO


def PrincipalMenu():
    continue_ = True
    while(continue_):
        correctOption = False
        while(not correctOption):
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
                continue_ = False
                print("Thanks for using this system")
                break
            else:
                correctOption = True
                executeOption(option)


def executeOption(option):
    dao = DAO()


PrincipalMenu()