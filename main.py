from DB.connection import DAO
import functions


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

    if option == 1:
        try:
            assets = dao.ShowAssets()
            if len(assets)>0:
                function.showAssets(assets)
            else:
                print("No assets found")
        except:
            print("Error")
    elif option == 2:
        print("Buy Assets")
    elif option == 3:
        print("Update Assets")
    elif option == 4:
        print("Sell Assets")
    else:
        print("Wrong option")


PrincipalMenu()