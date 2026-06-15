class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        full_product:int = 1
        full_product_without_zeros:int = 1
        zero_counts:int = 0

        for num in nums:
            if num != 0:
                full_product *= num
                full_product_without_zeros *= num
            else:
                zero_counts += 1
                full_product = 0

        if zero_counts > 1:
            return [0] * len(nums)



        products:list = [full_product] * len(nums)

        for i, num in enumerate(nums):
            if nums[i] != 0:
                products[i] = full_product // nums[i]
            else:
                products[i] = full_product_without_zeros

            

        return products

        