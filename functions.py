def showAssets(assets):
    print("\nAssets: \n")
    counter = 1
    for asset in assets:
        data = "{0}. Ticker: {1} | Quantity: {2}"
        print(data.format(counter, asset[0], asset[1]))
        counter += 1
    print(" ")