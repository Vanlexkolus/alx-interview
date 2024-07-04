#!/usr/bin/python3

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set()
    stack = [0]  # Start with the first box

    while stack:
        current = stack.pop()
        if current not in unlocked:
            unlocked.add(current)
            for key in boxes[current]:
                if key < n:  # Ensure the key corresponds to a valid box
                    stack.append(key)

    return len(unlocked) == n


# Test cases
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
