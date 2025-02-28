from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check each row for duplicates
        for i in range(9):  # Iterate over each row
            s = set()  # Initialize a set to track seen numbers
            for j in range(9):  # Iterate over each column in the row
                item = board[i][j]  # Get the current cell value
                if item in s:  # If the number is already seen, return False
                    return False
                elif item != ".":  # If it's a valid number (not an empty cell)
                    s.add(item)  # Add it to the set

        # Check each column for duplicates
        for i in range(9):  # Iterate over each column
            s = set()  # Initialize a set to track seen numbers
            for j in range(9):  # Iterate over each row in the column
                item = board[j][i]  # Get the current cell value
                if item in s:  # If the number is already seen, return False
                    return False
                elif item != ".":  # If it's a valid number (not an empty cell)
                    s.add(item)  # Add it to the set

        # Check each 3x3 sub-grid for duplicates
        starts = [(0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]  # Top-left coordinates of each sub-grid
        for i, j in starts:  # Iterate over each sub-grid
            s = set()  # Initialize a set to track seen numbers in the sub-grid
            for row in range(i, i + 3):  # Iterate over the 3 rows of the sub-grid
                for col in range(j, j + 3):  # Iterate over the 3 columns of the sub-grid
                    item = board[row][col]  # Get the current cell value
                    if item in s:  # If the number is already seen, return False
                        return False
                    elif item != ".":  # If it's a valid number (not an empty cell)
                        s.add(item)  # Add it to the set
        
        return True  # If no duplicates are found, return True
