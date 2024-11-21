def max_profit_brute(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if prices[j] > prices[i]:
                max_profit = max(max_profit, prices[j] - prices[i] +
                 max_profit_brute(prices[j + 1:]))
    return max_profit

prices = [100, 180, 260, 310, 40, 535, 695]
ans = max_profit_brute(prices) #Output -> 865
print(ans)
# Time Complexity: O(n^2)
# Space Complexity: O(1)






