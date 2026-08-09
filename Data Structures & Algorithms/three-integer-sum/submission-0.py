class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        resultSet:Set[List[int]] = set()
        sortedNums = sorted(nums)
        for i, num in enumerate(sortedNums):
            j = i + 1
            k = len(sortedNums) - 1

            target = -sortedNums[i]

            while j < k:
                if sortedNums[j] + sortedNums[k] < target:
                    j += 1
                elif sortedNums[j] + sortedNums[k] > target:
                    k -= 1
                else:
                    resultSet.add((num, sortedNums[j], sortedNums[k]))
                    k -= 1
            
        return [list(item) for item in resultSet]

        