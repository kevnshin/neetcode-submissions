class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowBits = [0] * 9
        colBits = [0] * 9
        boxBits = [0] * 9
        for rowNum, rowValues in enumerate(board):
            for colNum, cellValue in enumerate(rowValues):
                if cellValue == ".":
                    continue
                
                bit = 1 << (int(cellValue) - 1)
                if rowBits[rowNum] & bit:
                    return False
                if colBits[colNum] & bit:
                    return False
                boxNum = (rowNum // 3) * 3 + (colNum // 3)
                if boxBits[boxNum] & bit:
                    return False
                
                rowBits[rowNum] |= bit
                colBits[colNum] |= bit
                boxBits[boxNum] |= bit
                

        return True
