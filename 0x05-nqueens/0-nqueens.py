#!/usr/bin/python3

"""N-queens problem module"""

import sys


def nqueens(n):
    """N-queens problem"""
    if not isinstance(n, int):
        print("N must be a number")
        return
    if n < 4:
        print("N must be at least 4")
        return
    board = [[0 for j in range(n)] for i in range(n)]
    if not solve_nqueens(board, 0, n):
        print("Solution does not exist")
        return
    return board


def solve_nqueens(board, col, n):
    """Solve N-queens problem"""
    if col == n:
        print_solution(board)
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1, n) or res
            board[i][col] = 0
    return res


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def print_solution(board):
    """Print the solution"""
    print("[", end="")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                print("[{}, {}]".format(i, j), end="")
                if i != len(board) - 1:
                    print(", ", end="")
    print("]")


if __name__ == "__main__":
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
    nqueens(n)
