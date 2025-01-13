class Solution(object):
    def isValidSudoku(self, board):
        self.board = board
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    pass
                elif not self.checkRow(i, board[i][j]) or not self.checkColumn(i, j, board[i][j]) or not self.checkBox(i, j):
                    return False
        return True            

    def checkRow(self, row, data):
        if self.count(self.board[row], data) > 1:
            return False
        return True

    def checkColumn(self, row, column, data):
        for i in range(len(self.board)):
            if i != row and self.board[i][column] == data:
                return False
        return True        

    def count(self, arr, data):
        count = 0
        for i in range(len(arr)):
            if arr[i] == data:
                count = count + 1
        return count    

    def checkBox(self, row, column):
        startRow = 3 * (row // 3)
        endRow = startRow + 3
        startColumn = 3 * (column // 3)
        endColumn = startColumn + 3
        for i in range(startRow, endRow):
            for j in range(startColumn, endColumn):
                if i != row and j != column:
                    if self.board[row][column] == self.board[i][j]:
                        return False
        return True

# Instantiate the solution
solution = Solution()

# Test cases

# Test case 1 (Valid Sudoku)
valid_sudoku = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    ["9", "8", ".", ".", ".", ".", ".", "6", "."],
    ["8", "4", ".", "6", ".", ".", "3", ".", "1"],
    ["4", "4", ".", ".", ".", ".", ".", ".", "9"],
    ["7", ".", ".", ".", ".", ".", ".", ".", "3"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "4"]
]
print("Test case 1 (Valid Sudoku):", solution.isValidSudoku(valid_sudoku))
# Expected: True

# Test case 2 (Invalid Sudoku - Row violation)
invalid_sudoku_row = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    ["9", "8", ".", ".", ".", ".", ".", "6", "."],
    ["8", "4", ".", "6", ".", ".", "3", ".", "1"],
    ["4", "4", ".", ".", ".", ".", ".", ".", "9"],
    ["7", ".", ".", ".", ".", ".", ".", ".", "3"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "4"]
]
print("Test case 2 (Invalid Sudoku - Row violation):", solution.isValidSudoku(invalid_sudoku_row))
# Expected: False

# Test case 3 (Invalid Sudoku - Column violation)
invalid_sudoku_column = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    ["9", "8", ".", ".", ".", ".", ".", "6", "."],
    ["8", "4", ".", "6", ".", ".", "3", ".", "1"],
    ["4", ".", ".", ".", ".", ".", ".", ".", "9"],
    ["7", ".", ".", ".", ".", ".", ".", ".", "3"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "4"]
]
print("Test case 3 (Invalid Sudoku - Column violation):", solution.isValidSudoku(invalid_sudoku_column))
# Expected: False

# Test case 4 (Invalid Sudoku - Box violation)
invalid_sudoku_box = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    ["9", "8", ".", ".", ".", ".", ".", "6", "."],
    ["8", "4", ".", "6", ".", ".", "3", ".", "1"],
    ["4", ".", ".", ".", ".", ".", ".", ".", "9"],
    ["7", ".", ".", ".", ".", ".", ".", ".", "3"],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "4"]
]
print("Test case 4 (Invalid Sudoku - Box violation):", solution.isValidSudoku(invalid_sudoku_box))
# Expected: False

# Test case 5 (Empty board - no numbers)
empty_board = [
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]
print("Test case 5 (Empty board - no numbers):", solution.isValidSudoku(empty_board))
# Expected: True (Empty spots, valid by default)

# Test case 6 (Board with one number, valid)
valid_one_number = [
    ["5", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]
print("Test case 6 (Board with one number, valid):", solution.isValidSudoku(valid_one_number))
# Expected: True (Board is valid with one number placed)

