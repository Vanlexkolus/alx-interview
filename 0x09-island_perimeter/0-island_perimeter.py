#!/usr/bin/python3
"""
Island Perimeter:
    returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    perimeter = 0

    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    # Loop through the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add 4 for a land cell
                perimeter += 4

                # Check if there's a land cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # They share a border, reduce by 2

                # Check if there's a land cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # They share a border, reduce by 2

    return perimeter
