class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        longestStreak = 0
        currentStreak = 0
        for num in numSet:
            if num - 1 not in numSet:
                currentNum = num
                currentStreak = 1
            
                while currentNum + 1 in numSet:
                    currentStreak += 1
                    currentNum += 1
            
            longestStreak = max(currentStreak, longestStreak)

        return longestStreak

        