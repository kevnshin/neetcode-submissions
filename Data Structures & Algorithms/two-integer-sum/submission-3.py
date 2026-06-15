class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result: List[int] = []
        numberDict: dict[int, int] = {}
        indexList: List[int] = range(len(nums))
        for i in indexList:
            numberDict[nums[i]] = i

        for i in indexList:
            remainder: int = target - nums[i]
            if (remainder in numberDict) and (i is not numberDict[remainder]) :
                result.append(i)
                result.append(numberDict[remainder])
                break
        return result

        