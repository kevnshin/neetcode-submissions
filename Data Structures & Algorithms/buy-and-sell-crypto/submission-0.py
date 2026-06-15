class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest: int = 100000
        highest: int = 0
        currentHighestProfit: int = 0

        for price in prices:
            if price < lowest:
                lowest = price
                highest = 0
            elif price > highest:
                highest = price
                if highest - lowest > currentHighestProfit:
                    currentHighestProfit = highest - lowest
        return currentHighestProfit
