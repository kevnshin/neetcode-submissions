class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (2 * len(nums))
        for i in range(len(ans)):
            numsIndex = i % len(nums)
            ans[i] = nums[numsIndex]
        return ans        