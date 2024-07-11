def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


# Main file for testing
if __name__ == "__main__":
    minOperations = __import__('0-minoperations').minOperations

    n = 4
    print("Min # of operations to reach {} char: {}".format(n,
                                                            minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n,
                                                            minOperations(n)))


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations


# Main file for testing
if __name__ == "__main__":
    minOperations = __import__('0-minoperations').minOperations

    n = 4
    print("Min # of operations to reach {} char: {}".format(n,
                                                            minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n,
                                                            minOperations(n)))
