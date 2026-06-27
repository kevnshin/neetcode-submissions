class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        response = 0
        for num in nums:
            response ^= num
        return response







        # bit mask way
        # mask = 0

        # for num in nums:
        #     bit = 1 << (num + 10000)
        #     if mask & bit:
        #         mask &= ~bit
        #     else:
        #         mask |= bit


        # return mask.bit_length() - 1 - 10000