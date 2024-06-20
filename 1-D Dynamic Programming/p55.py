"""

Problem: 322. Coin Change

URL: https://leetcode.com/problems/coin-change/description/

Author: Harshit Allumolu <hallumol@asu.edu>

"""

def coinChange(coins, amount: int) -> int:
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0
    for a in range(1, amount+1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
    return dp[amount] if dp[amount] != float('inf') else -1

# sample test cases
cases = [
    {
        "coins": [1, 2, 5],
        "amount": 11
    },
    {
        "coins": [2],
        "amount": 3
    },
    {
        "coins": [1],
        "amount": 0
    }
]

for case in cases:
    print(case, ":", coinChange(case["coins"], case["amount"]))