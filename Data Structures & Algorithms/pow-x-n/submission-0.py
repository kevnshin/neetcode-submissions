class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n > 0:
            result = 1
            while n > 0:
                result *= x
                n -= 1
            return result
        if n < 0:
            resultDenom = 1
            while n < 0:
                resultDenom *= x
                n += 1
            return 1 / resultDenom
        