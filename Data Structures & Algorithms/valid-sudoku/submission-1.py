class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.rowSets = [set() for _ in range(9)]
        self.colSets = [set() for _ in range(9)]
        self.boxSets = [set() for _ in range(9)]
        for rowNum, rowValues in enumerate(board):
            for colNum, cellValue in enumerate(rowValues):
                if not self.checkRow(rowNum, cellValue):
                    return False
                if not self.checkCol(colNum, cellValue):
                    return False
                if not self.checkBox(rowNum, colNum, cellValue):
                    return False
        return True
    
    def checkRow(self, rowNum:int, cell:str) -> bool:
        if cell == ".":
            return True
        if cell in self.rowSets[rowNum]:
            return False
        self.rowSets[rowNum].add(cell)
        return True

    def checkCol(self, colNum:int, cell:str) -> bool:
        if cell == ".":
            return True
        if cell in self.colSets[colNum]:
            return False
        self.colSets[colNum].add(cell)
        return True

    def checkBox(self, rowNum:int, colNum:int, cell:str) -> bool:
        if cell == ".":
            return True
        boxNum:int = self.mapCellToBox(rowNum, colNum)
        if cell in self.boxSets[boxNum]:
            return False
        self.boxSets[boxNum].add(cell)
        return True
    
    def mapCellToBox(self, row:int, col:int) -> int:

        if row >= 0 and row <= 2:
            if col >= 0 and col <= 2:
                return 0
            if col >= 3 and col <= 5:
                return 1
            if col >= 6 and col <= 8:
                return 2

        if row >= 3 and row <= 5:
            if col >= 0 and col <= 2:
                return 3
            if col >= 3 and col <= 5:
                return 4
            if col >= 6 and col <= 8:
                return 5

        if row >= 6 and row <= 8:
            if col >= 0 and col <= 2:
                return 6
            if col >= 3 and col <= 5:
                return 7
            if col >= 6 and col <= 8:
                return 8

# [
# ["5","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]




        