# 121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

## Thoughts and Approaches

The key point is to track the minimum prices so far, and therefore we are able to compute the max profit so far. 


## Python Code

```Python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ##choose a single day to buy one stock and choose a different day in the future to sell that stock 
        maxProfit=0
        minPrice=prices[0]
        n=len(prices)

        for i in range(1,n,1):
            if prices[i]<minPrice:
                minPrice=prices[i]
            maxProfit=max(maxProfit, prices[i]-minPrice)
        
        return maxProfit
```

## Time Complexity
O(n). Only a single pass is needed.

## Space Complexity
O(1) 
