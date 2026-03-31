class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        
        for i in range(len(prices)-1):
            # Assume buy on i day 
            profit_temp = max(prices[i:]) - prices[i]
            if profit_temp > profit:
                profit = profit_temp
        
        return profit 


            