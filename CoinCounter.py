import os
# i am petux

coinadd = 1
coinamount = 0
coinsum = 0
coins = []

def CoinShow(coins):
    coins = [1]
    for i in range(1, len(coins)):
        print(f"{i + 1}) {coins[i]}")
    a = int(input("What would you like to remove?"))

def Menu():
    selectionprompt = int(input("Welcome to the menu. What would you like to do?\n1) Show coins\n2) Continue adding coins\n3) End\n"))
    if selectionprompt == 1: CoinShow(coins)
    elif selectionprompt == 2: CoinAddition()
    else: return


def CoinAddition(coinsum, coins):
    coins = []
    coinadd = 1
    coinamount = 0
    coinsum = 0
    while coinadd != 0:
        print(f"\nTo open the menu enter 0\n\nSum: {coinsum}\nLast coin: {coinadd}\nAmount of coins: {coinamount}")
        coinadd = float(input("Enter your coin: "))
        coins.append(coinadd)
        coinsum += coinadd
        coinamount += 1
        os.system('cls' if os.name == 'nt' else 'clear')
    return coinsum, coins

CoinAddition(coinsum, coins)
Menu()
print(f"\nConclusion\n\nSum: {coinsum}\nAmount of coins: {coinamount}")
