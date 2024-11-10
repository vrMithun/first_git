class Solution(object):
    def isValidSudoku(self, board):
        self.board=board
        for i in range(len(board)):
            for j in range(len(board)):
                if  board[i][j]==".":
                    pass
                elif not self.checkRow(i,board[i][j]) or not self.checkColumn(i,j,board[i][j]) or not self.checkBox(i,j):
                    return False
        return True            
    def checkRow(self,row,data):
        if self.count(self.board[row],data)>1:
            return False
        return True

    def checkColumn(self,row,column,data):
        for i in range(len(self.board)):
            if i!=row and self.board[i][column]==data:
                return False
        return True        
    def count(self,arr,data):
        count=0
        for i in range(len(arr)):
            if arr[i]==data:
                count=count+1
        return count    
    def checkBox(self,row,column):
        startRow=3*(row//3)
        endRow=startRow+3
        startColumn=3*(column//3)
        endColumn=startColumn+3
        for i in range(startRow,endRow):
            for j in range(startColumn,endColumn):
                if i!=row and j!=column:
                    if self.board[row][column]==self.board[i][j]:
                        return False
        return True                