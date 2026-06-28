"""
Problem : 121. Best Time to Buy and Sell Stock

Link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Pattern : Arrays

Difficulty : Easy

Approach :
Track the minimum price seen so far.
Calculate the profit for each day and keep the maximum.

Time Complexity : O(n)
Space Complexity : O(1)

"""

def maxProfit(prices):
    profit = []
    min_price = prices[0]
    for i in range(len(prices)):
        if min_price > prices[i]:
            min_price = prices[i]
        profit.append(prices[i]-min_price) 
    return max(profit) 