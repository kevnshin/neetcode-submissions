class Solution:
    def isHappy(self, n: int) -> bool:
        foundCycle = False
        prevNums = set()
        number = n

        while not foundCycle:
            thousands = (number // 1000) % 10
            hundreds = (number // 100) % 10
            tens = (number // 10) % 10
            ones = number % 10
            print("thousands", thousands)
            print("hundreds", hundreds)
            print("tens", tens)
            print("ones", ones)

            sumOfSquares = thousands ** 2 + hundreds ** 2 + tens ** 2 + ones ** 2
            print("sumOfSquares", sumOfSquares)
            if sumOfSquares == 1:
                return True
            elif sumOfSquares in prevNums:
                return False
            else:
                prevNums.add(sumOfSquares)
            number = sumOfSquares
            


        