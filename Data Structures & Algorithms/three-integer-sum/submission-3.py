class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result:List[List[int]] = []
        sortedNums = sorted(nums)
        for i, num in enumerate(sortedNums):
            if i > 0 and num == sortedNums[i - 1]:
                continue
            if num > 0:
                break
            
            j = i + 1
            k = len(sortedNums) - 1

            target = -sortedNums[i]

            while j < k:
                if sortedNums[j] + sortedNums[k] < target:
                    j += 1
                    # while j < len(sortedNums) and sortedNums[j - 1] == sortedNums[j]:
                        # j += 1
                elif sortedNums[j] + sortedNums[k] > target:
                    k -= 1
                    # while k > 0 and sortedNums[k + 1] == sortedNums[k]:
                    # k -= 1
                else:
                    result.append((num, sortedNums[j], sortedNums[k]))
                    k -= 1
                    while k > 0 and sortedNums[k + 1] == sortedNums[k]:
                        k -= 1
            
        return result

        