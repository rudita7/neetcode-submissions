class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        i = 0
        j = len(prices)-1
        profit = prices[j] - prices[i]
        res = max(res, profit)
        while i < j:
            if prices[i+1] < prices[i]:
                i +=1
            elif prices[j-1] > prices[j]:
                j -= 1
            elif prices[i+1] > prices[i] and prices[j-1] < prices[j]:
                for k in range(i+1, j):
                    profit = prices[k] - prices[i]
                    res = max(res, profit)
                i += 1   
            else:
                i += 1
            profit = prices[j] - prices[i]
            res = max(res, profit)
        return res   