class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if (prices[j]-prices[i])> profit:
                    profit = (prices[j]-prices[i])

        return profit
