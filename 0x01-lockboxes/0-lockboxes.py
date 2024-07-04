#!/usr/bin/python3
"""
Module to determine if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    The can Unlock function
    """
    n = len(boxes)
    unlocked = set()
    stack = [0]

    while stack:
        current = stack.pop()
        if current not in unlocked:
            unlocked.add(current)
            for key in boxes[current]:
                if key < n:
                    stack.append(key)

    return len(unlocked) == n


# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
