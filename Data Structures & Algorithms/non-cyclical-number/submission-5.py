class Solution:
    def isHappy(self, n: int) -> bool:
        foundCycle = False
        prevNums = set()
        number = n

        while not foundCycle:
            sumOfSquares = 0
            while number:
                digit = number % 10
                digitSquared = digit ** 2
                sumOfSquares += digitSquared
                number = number // 10

            if sumOfSquares == 1:
                return True
            elif sumOfSquares in prevNums:
                return False
            else:
                prevNums.add(sumOfSquares)
            number = sumOfSquares
            


        