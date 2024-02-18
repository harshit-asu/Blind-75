"""

Problem: 121. Best Time to Buy and Sell Stock

URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def maxProfit(prices) -> int:
    # find diff between curr price and bought price (prev)
    # if diff is > maxP, update it
    # if it is < 0, it means that we can buy the stock for a less price
    # so update bought price (prev) to the curr price
    maxP = 0
    prev = 10**5
    for i in range(len(prices)):
        d = prices[i] - prev
        if d > maxP:
            maxP = d
        if d < 0:
            prev = prices[i]
    return maxP


# sample test cases
cases = [
    [7,1,5,3,6,4],
    [7,6,4,3,1]
]

for case in cases:
    print(case, ":", maxProfit(case))