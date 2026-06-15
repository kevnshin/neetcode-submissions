class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        high:int = len(numbers) - 1
        low:int = 0
        while low < high:
            sum:int = numbers[low] + numbers[high]

            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1

        return [-1, -1]