#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def already_exists(queens, n, y):
    """check that a queen does not already exist in that y value"""
    for x in range(n):
       if y == queens[x][1]:
            return True
    return False

def reject(queens, n, x, y):
    """determines whether or not to reject the solution"""
    if (already_exists(queens, n, y)):
        return False
    i = 0
    while(i < x):
        if abs(queens[i][1] - y) == abs(i - x):
            return False
        i += 1
    return True

def clear_a(queens, n, x):
    """clears the answers from the point of failure on"""
    for i in range(x, n):
        queens[i][1] = None

def nqueens(queens, n, x):
    """recursive backtracking function to find the solution"""
    for y in range(n):
        clear_a(queens, n, x)
        if reject(queens, n, x, y):
            queens[x][1] = y
            if (x == n - 1):  # accepts the solution
                print(queens)
            else:
                nqueens(queens, n, x + 1)  # moves on to next x value to continue

    # start the recursive process at x = 0
    

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = sys.argv[1]
    queens = []
    # initialize the answer list
    for i in range(n):
        queens.append([i, None])
    
    nqueens(queens, n, 0)
    

