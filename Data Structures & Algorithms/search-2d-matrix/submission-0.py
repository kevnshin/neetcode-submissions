class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top:int = 0
        bottom:int = len(matrix) - 1
        left:int = 0
        right:int = len(matrix[0]) - 1

        while top <= bottom:
            mid_row:int = (top + bottom) // 2

            if target < matrix[mid_row][0]:
                bottom = mid_row - 1
            elif target > matrix[mid_row][-1]:
                top = mid_row + 1
            else: 
                return self.leftRightBinarySearch(matrix[mid_row], target)
            
        return False


    def leftRightBinarySearch(self, row: List[int], target: int) -> bool:
        left:int = 0
        right:int = len(row) - 1

        while left <= right:
            if row[left] == target:
                return True
            elif row[right] == target:
                return True
            
            mid:int = (left + right) // 2

            if row[mid] < target:
                left = mid + 1
            elif row[mid] > target:
                right = mid - 1
            else:
                return True
        return False

        

        