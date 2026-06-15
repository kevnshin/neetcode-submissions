class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length:int = len(nums)
        products:List[int] = [1] * length
        running_product_forward:int = 1
        running_product_backward:int = 1

        for i, num in enumerate(nums):
            products[i] *= running_product_forward
            running_product_forward = running_product_forward * nums[i]

            backwards_idx:int = length - i - 1

            products[backwards_idx] *= running_product_backward
            running_product_backward *= nums[backwards_idx]
        return products

#         length:int = len(nums)
#         prefix_products:List[int] = [None] * length
#         postfix_products:List[int] = [None] * length
#         running_product_forward:int = 1
#         running_product_backward:int = 1

#         for i, num in enumerate(nums):
#             prefix_products[i] = running_product_forward * num
#             running_product_forward = prefix_products[i]

#             backwards_idx:int = length - i - 1
#             postfix_products[backwards_idx] = running_product_backward * nums[backwards_idx]
#             running_product_backward = postfix_products[backwards_idx]
        
#         products:List[int] = [None] * length
#         prefix_product:int = 1

#         # print("prefixes: ", prefix_products)
#         # print("postfixes: ", postfix_products)

#         for i in range(len(products)):
#             postfix_product:int = postfix_products[i + 1] if i < length - 1 else 1
#             products[i] = prefix_product * postfix_product
#             prefix_product = prefix_products[i]
#         return products