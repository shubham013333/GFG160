def max_profit_optimal(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

prices = [100, 180, 260, 310, 40, 535, 695]
ans = max_profit_optimal(prices) #Output -> 865
print(ans)
# Time Complexity: O(n)
# Space Complexity: O(1)

