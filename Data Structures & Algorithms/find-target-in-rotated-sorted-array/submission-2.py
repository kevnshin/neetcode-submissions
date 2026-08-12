class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # left side is sorted
            if nums[mid] >= nums[left]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
            # right side is sorted
            else: 
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            # if nums[left] > nums[mid]:
            #     if target < nums[left]:
            #         if target > nums[mid]:
            #             left = mid + 1
            #         else:
            #             right = mid - 1
            #     else:
            #         if target > nums[mid]:
            #             right = mid - 1
            #         else:
            #             left = mid + 1
            # else:
            #     if target < nums[left]:
            #         if target > nums[mid]:
            #             right = mid - 1
            #         else:
            #             left = mid + 1
            #     else:
            #         if target > nums[mid]:
            #             left = mid + 1
            #         else:
            #             right = mid - 1
                
        return -1

        