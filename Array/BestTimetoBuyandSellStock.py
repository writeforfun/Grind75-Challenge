'''
Title: 121. Best Time to Buy and Sell Stock
Level: Easy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Author: Yuan
Date: 2022/06/18
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_purchase = prices[0]
        for day2 in range(1, len(prices)):
            max_profit = max(max_profit, prices[day2] - min_purchase)
            min_purchase = min(min_purchase, prices[day2])
            
        return max_profit