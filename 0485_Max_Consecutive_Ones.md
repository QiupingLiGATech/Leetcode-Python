# 485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

## Thoughts and Approach

Used count and maxCount to track the progress. 

## Python Code

```Python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxCount=0
        for x in nums:
            if x==1: ##keep a count of 1s
                count+=1
                maxCount=max(maxCount, count)
            else: ## reset the count to 0 if we encounter 0
                count=0
        return maxCount
```

## Time Complexity
O(N), where N is the number of elements in the array.

## Space Complexity
O(1) we did not use any extra space 
