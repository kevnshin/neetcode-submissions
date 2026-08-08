class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h1 = 0
        h2 = len(heights) - 1
        maxArea = 0
        while h1 < h2:
            width = h2 - h1
            height = min(heights[h1], heights[h2])
            area = width * height
            maxArea = max(area, maxArea)
            if heights[h2] > heights[h1]:
                h1 += 1
            else:
                h2 -= 1
        return maxArea

        