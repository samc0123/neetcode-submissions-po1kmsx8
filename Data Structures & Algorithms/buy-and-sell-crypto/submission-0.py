class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_info = {}
        stock_info['purchase_price'] = float('inf')
        stock_info['profit'] = 0

        for price in prices:
            # See if you want to purchase stock 
            if price < stock_info['purchase_price']:
                stock_info['purchase_price'] = price
                continue # Bought the stock so go to next value 
            elif price - stock_info['purchase_price'] > stock_info['profit']:
                # Update your new profit
                stock_info['profit'] = price - stock_info['purchase_price']
            else:
                continue 
                # Keep going and hope you can find a better profit

        return stock_info['profit']