#!/usr/bin/python3
"""
This is a prime game by alx interview
"""


def isWinner(x, nums):
    """
    This is the isWinner function
    """

    if x < 1 or not nums:
        return None

    # Step 1: Find the maximum number in nums to precompute primes
    max_n = max(nums)

    # Step 2: Sieve of Eratosthenes to find all primes up to max_n
    sieve = [True] * (max_n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, max_n + 1, i):
                sieve[multiple] = False

    # Step 3: Precompute the number of primes up to each number <= max_n
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if sieve[i] else 0)

    # Step 4: Simulate the rounds
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        # Determine the number of primes up to n
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Step 5: Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
