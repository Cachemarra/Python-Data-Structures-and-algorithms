# WRITE MAX_PROFIT FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################
def max_profit(stock):
    max_profit = 0

    while len(stock) >= 1:
        price = stock.pop(0)

        for element in stock:
            profit = element - price
            if max_profit < profit:
                max_profit = profit
    return max_profit
            

prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""