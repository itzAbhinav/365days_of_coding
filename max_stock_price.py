class Solution:
    
    def stockbuySell(self, prices):
        maxProfit = 0

        for i in range(len(prices)):
           
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)

        return maxProfit

sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print("Max Profit:", sol.stockbuySell(prices))