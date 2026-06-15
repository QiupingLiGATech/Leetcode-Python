# 268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


## Thoughts and Approaches

Arithmetic Series Summation:  When you add all the terms in an arithmetic sequence together, it forms an arithmetic series. 
The sum of the first n terms is calculated using the formula: Sum=(a1+an)*n/2

## Python Code

```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSum=sum(nums) ## time complexity O(n)
        n=len(nums)
        
        Expected=(n+1)*(0+n)/2
        
        return int(Expected-numSum)
```

## Time Complexity
O(n)

## Space Complexity
O(1) 
