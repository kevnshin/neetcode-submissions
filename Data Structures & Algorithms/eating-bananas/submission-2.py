class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperBound = max(piles)
        kRange = range(1, upperBound + 1)
        left = 0
        right = upperBound
        while left <= right:
            time = 0
            kIndex = (left + right) // 2
            for pile in piles:
                time += math.ceil(pile / kRange[kIndex])
            if time <= h:
                result = kRange[kIndex]
                right = kIndex - 1
            else:
                left = kIndex + 1
        return result
            