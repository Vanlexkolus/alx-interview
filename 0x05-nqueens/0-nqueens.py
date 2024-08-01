#!/usr/bin/python3

"""
Thisnis the beginning
"""
import sys

"""
This is just a false comment
"""


def print_solutions(solutions):
    """
    Print each solution in the solutions list.

    Args:
        solutions(list of list): A list where
        each element is a list representing a solution.
    """
    for solution in solutions:
        print(solution)

def is_valid(board, row, col):
    """
    Check if placing a queen at(row, col) is valid.

    Args:
        board(list): Current state of the board
        where index represents the row and value
        represents the column of the queen.
        row(int): The row where the queen is to be placed.
        col(int): The column where the queen is to be placed.

    Returns:
        bool: True if placement is valid, False otherwise.
    """
    for i in range(row):
        # Check if the same column or diagonal conflicts
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True

def solve_nqueens(n):
    """
    Solve the N-Queens problem using backtracking.

    Args:
        n(int): The size of the chessboard
        (n x n) and the number of queens.

    Returns:
        list of list: A list of solutions, where each
        solution is a list of(row, col) positions.
    """
    def backtrack(row, board):
        """
        Backtracking function to find all solutions.

        Args:
            row(int): The current row to place a queen.
            board(list): Current state of the board.
        """
        if row == n:
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1  # Reset the board position for backtracking

    solutions = []
    board = [-1] * n  # Initialize board with -1 indicating no queens placed
    backtrack(0, board)
    return solutions

def main():
    """
    Main function to handle input, validate it,
    and solve the N-Queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
