def showAssets(assets):
    print("\nAssets: \n")
    counter = 1
    for asset in assets:
        data = "{0}. Ticker: {1} | Quantity: {2}"
        print(data.format(counter, asset[0], asset[1]))
        counter += 1
    print(" ")


def askDataAssetBuy():
    Ticker = input("Insert the ticker: ")
    Quantity = int(input("Insert the quantity: "))

    asset = (Ticker, Quantity)
    return asset


def askDataAssetDelete(assets):
    showAssets(assets)
    TickerExists = False

    TickerDelete = input("Insert the ticker: ")
    for asset in assets:
        if asset[0] == TickerDelete:
            TickerExists = True
            break

    if not TickerExists:
        TickerDelete = ""

    return TickerDelete