def makeChange(coins, total):
    # If the total is 0, no coins are needed
    if total <= 0:
        return 0

    # Sort the coins in descending order to try larger coins first
    coins.sort(reverse=True)

    # Initialize the variable to keep track of the fewest coins needed
    num_coins = 0

    for coin in coins:
        # Use as many of the current coin as possible
        if total >= coin:
            num_coins += total // coin  # How many of this coin can be used
            total %= coin  # Remainder of the total after using this coin

        # If the total becomes 0, return the number of coins used
        if total == 0:
            return num_coins

    # If total is not 0 after looping through all coins, return -1 (impossible)
    return -1
