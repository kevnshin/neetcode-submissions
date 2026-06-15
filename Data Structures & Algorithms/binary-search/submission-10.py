class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left:int = 0
        right:int = len(nums) - 1
        

        while left <= right:
            print("========START LOOP=====")
            print("left", left)
            print("right", right)
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            mid:int = math.ceil((right + left) / 2)
            if mid == left or mid == right:
                if nums[mid] == target:
                    return mid
                else:
                    break
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid
            else:
                return mid

            
            print("========END LOOP=====")
            print("mid", mid)
            print("left", left)
            print("right", right)

        return -1

            
        